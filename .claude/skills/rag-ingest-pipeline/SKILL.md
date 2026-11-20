---
name: rag-ingest-pipeline
description: ออกแบบ พัฒนา และตรวจสอบระบบ ingest ไฟล์ขนาดใหญ่ PDF DOCX CSV ลง ChromaDB เพื่อทำ Retrieval และ RAG ด้วย Python ใช้เมื่อผู้ใช้ขอสร้างหรือแก้ pipeline, chunking, embedding, OCR, manifest, delta ingestion, retrieval, citation, หรือพูดถึงคำว่า RAG, ingest, Chroma, vector db, chunk, embedding, OCR ในการพัฒนาโปรเจกต์นี้
metadata:
  author: project-owner
  version: 0.1.0
---

# RAG Ingest Pipeline Skill

ทักษะนี้ฝัง "ความจำของโปรเจกต์" ที่ได้จากการสัมภาษณ์ 14 ข้อ เพื่อให้ Claude ทำงานกับระบบนี้ได้สม่ำเสมอทุก session โดยไม่ต้องอธิบายซ้ำ

---

## เมื่อไรควรใช้ Skill นี้

ใช้เมื่องานเกี่ยวข้องกับอย่างใดอย่างหนึ่งต่อไปนี้:

- เพิ่ม/แก้ extractor ของ PDF, DOCX, CSV
- ปรับกฎการแบ่ง chunk หรือ metadata ที่แนบไปกับ chunk
- เปลี่ยน/เพิ่ม embedding provider (local หรือ API)
- แก้ระบบตรวจจับไฟล์เปลี่ยน, checkpoint, resume, หรือ idempotency
- ปรับ Chroma collection, การ upsert, การลบ chunk, หรือ metadata filter
- ปรับการค้นหา/การอ้างอิงแหล่งที่มา (citation)
- เพิ่ม CLI, FastAPI, หรือ Streamlit
- ถูกขอให้ "ตรวจสอบว่าระบบยังตรงตามที่ตกลงกันอยู่ไหม"

**ไม่ใช้** กับงานทั่วไปที่ไม่เกี่ยวข้อง เช่น เขียนรายงานอากาศ หรือสร้างสเปรดชีตไม่เกี่ยวข้อง

---

## ก่อนเริ่มเสมอ (ห้ามข้าม)

1. อ่าน `CLAUDE.md` ที่ project root — มีกฎและข้อตัดสินใจที่ห้ามฝ่าฝืน
2. อ่าน `docs/spec.md` — มี FR/NFR, data model, และรายละเอียดแต่ละ stage
3. ตรวจสอบว่ากำลังทำงานใน phase ไหน (ตาราง phase อยู่ใน spec ข้อ 11)
4. ถ้าไม่แน่ใจว่า phase ไหน → ถามผู้ใช้ อย่าเดา

---

## แผนที่ระบบ (ให้จำภาพนี้เวลาออกแบบ)

```
scan folder → delta detect → extract → chunk → embed → Chroma upsert → retrieve + citation
                  ↑              ↑        ↑        ↑
              manifest.py    extraction/ chunking/ embedding/
                            (ProcessPool)        (config-driven)
```

ชั้นต้องแยกกัน: extraction ไม่เรียก embedding, chunking ไม่เรียก store, มี `pipeline.py` เป็นคนประสาน

---

## Workflow มาตรฐาน

### Step 1 — จำแนกประเภทงาน

| ผู้ใช้พูดว่า | ไปที่ |
|---|---|
| "รองรับ PDF สแกนเพิ่ม" | Extraction + OCR rules |
| "ผลค้นหาไม่ตรง" | Chunking → Embedding → Retrieval (ตามลำดับ) |
| "rันรายวันแล้วช้ามาก" | Delta detection + OCR trigger + ProcessPool |
| "รันซ้ำแล้วเจอดูplicate" | Deterministic ID + upsert + manifest |
| "อยากเปลี่ยนเป็นใช้ API" | **หยุด → ถามอนุมัติก่อน** → ค่อยแก้ config |
| "เพิ่มปุ่มค้นหาใน UI" | `ui.py` + `retrieval.py` |

### Step 2 — ใช้ Decision Rules (ด้านล่าง) ก่อนเขียนโค้ด

### Step 3 — Implement ตามชั้น

1. แก้ interface ก่อน (ถ้าจำเป็น)
2. แก้ implementation
3. แก้/เพิ่ม config
4. แก้/เพิ่ม test
5. อัปเดต `docs/spec.md` ถ้าพฤติกรรมเปลี่ยน

### Step 4 — ตรวจสอบก่อนส่งงาน (Definition of Done)

- [ ] ไม่มีข้อมูลถูกส่งออกAPI โดยไม่ได้รับอนุมัติ
- [ ] ทุก chunk มี metadata บังคับ (`doc_id`, `source`, `file_type`, `chunk_index`, `page`/`section`/`row_range`)
- [ ] ID เป็น deterministic และใช้ upsert
- [ ] มี test ครอบและ `pytest` ผ่าน
- [ ] ไม่มี `print()` ใน library code
- [ ] ไม่มีการ hardcode path / model name / chunk size
- [ ] อัปเดต spec ถ้ามีพฤติกรรมเปลี่ยน

---

## Decision Rules (หัวใจของ Skill)

### Embedding provider — เรื่อง privacy ยังไม่ตัดสินใจ

```
ถ้าไม่มีคำอนุมัติใช้ API จากผู้ใช้ (ชัดเจน)
   → ใช้ profile "local" เสมอ: fastembed + multilingual-e5-small (ONNX int8)
   → เหตุผล: ข้อมูลภายในห้ามออกนอกเครื่อง, CPU only, แต่ยังเร็วพอสำหรับ batch กลางคืน

ถ้าผู้ใช้อนุมัติใช้ API แล้ว
   → เปลี่ยนแค่ config.yaml เป็น profile "fast" (OpenAI text-embedding-3-small)
   → ห้ามแก้โค้ดของชั้นอื่น
```

**ห้ามเดาเอาเองว่าอนุมัติแล้ว** — ถ้าไม่แน่ใจให้ถาม

### OCR — เรื่องความเร็ว (Priority #1)

```
ดึง text layer ด้วย PyMuPDF ก่อน
   ├── ข้อความเพียงพอ (เช่น >= 50 ตัวอักษร/หน้า) → ใช้ข้อความเลย ข้าม OCR
   └── ไม่มีข้อความ → OCR เฉพาะหน้านั้น (Tesseract tha+eng)
```

ห้าม OCR ทั้งไฟล์โดยไม่ตรวจเช็ค text layer

### CSV — ยังไม่ตัดสินใจ รอคำแนะนำ

```
1 chunk: summary   → จำนวนแถว, ช่วงวันที่, คำอธิบายคอลัมน์
1 chunk: schema    → header + ตัวอย่าง 3–5 แถว
N chunk: row-groups → ~50 แถว/chunk เขียนเป็นประโยค "แถว 12: วันที่=..., ยอด=..."
metadata: row_range="12-61"
```

### Chunking

```
structure-aware ก่อน (หัวข้อ/ย่อหน้า/หน้า/ตาราง)
→ เฉพาะ section ที่ยาวเกิน 1000 tokens ค่อย split ด้วย overlap 80–120
→ ใช้ tokenizer ของ embedding model ที่เลือกในการนับ token
```

### Vector store

```
ใช้ ChromaDB ตามที่ตกลง
แต่ต้องผ่าน VectorStore interface เสมอ
→ เผื่อวันหนึ่งต้องย้าย Qdrant/Milvus เพราะ chunk หลักล้าน
```

### Retrieval

```
semantic search + top-k + metadata filter
citation = "relative_path • หน้า X • section Y" หรือ "row_range"
ห้ามเพิ่ม hybrid/reranker/LLM โดยลำพัง — ยังไม่ได้ตกลง
```

---

## โค้ดแพทเทิร์นที่ต้องใช้

```python
# embedding/base.py
class EmbeddingProvider(Protocol):
    @property
    def dimension(self) -> int: ...
    def embed(self, texts: list[str]) -> list[list[float]]: ...

# extraction/base.py
class Extractor(Protocol):
    def extract(self, path: Path) -> RawDocument: ...

# store/base.py
class VectorStore(Protocol):
    def upsert(self, chunks: list[Chunk]) -> None: ...
    def delete_by_doc(self, doc_id: str) -> None: ...
    def search(self, vector: list[float], k: int, where: dict | None) -> list[SearchHit]: ...
```

`Chunk` ต้องมี field บังคับ: `doc_id`, `text`, `metadata`, `chunk_index`

---

## ปัญหาที่พบบ่อย

| อาการ | สาเหตุ | วิธีแก้ |
|---|---|---|
| OCR ภาษาไทยเพี้ยน | ไม่มี language data `tha+eng` | ติดตั้ง `tesseract-ocr-tha` แล้วตั้ง `lang="tha+eng"` |
| OCR ช้ามาก | OCR ทั้งไฟล์โดยไม่ตรวจ text layer | ตรวจ text layer ก่อนตาม Decision Rules |
| Chroma chunk ซ้ำซ้อน | ID ไม่ deterministic | ใช้ `{content_hash[:16]}_{chunk_index:04d}` + upsert |
| ไฟล์ลบแล้วแต่ค้นยังเจอ | ไม่ได้ลบ chunk | เรียก `delete_by_doc` ตอน manifest เจอไฟล์หาย |
| embedding ภาษาไทยแย่ | ใช้โมเดลอังกฤษล้วน | เปลี่ยนเป็นโมเดล multilingual ตาม config |
| จำนวน chunk โตแล้ว Chroma ช้า | SQLite backend ถึงขีด | แจ้งผู้ใช้ + เตรียมย้ายผ่าน `VectorStore` interface |
| ProcessPool ค้าง/ใช้ memory เยอะ | ส่ง object ใหญ่กลับข้าม process | ส่งแค่ path + คืน RawDocument เล็ก ๆ |

---

## ตัวอย่างการทำงาน

**ผู้ใช้:** "ช่วยเพิ่มรองรับสแกนใน PDF บางไฟล์ที่ยังค้นไม่เจอ"

**การดำเนินการ:**
1. อ่าน CLAUDE.md + spec.md → ยืนยันว่าเป็น Phase 2
2. ตรวจ `extraction/pdf.py`: มีการเช็ค text layer ยัง?
3. ถ้ายัง → เพิ่ม `has_text_layer()` + เรียก `ocr.py` เฉพาะหน้าที่ไม่มี
4. เพิ่ม metadata `is_scanned=True` เฉพาะหน้านั้น
5. เพิ่ม test ด้วย golden sample PDF สแกน
6. รัน pytest → report ว่าอะไรเปลี่ยน

**ผู้ใช้:** "ลองเปลี่ยนไปใช้ OpenAI embedding สิ"

**การดำเนินการ:**
1. **หยุด** — ถามว่า "ได้รับอนุมัติให้ส่งข้อมูลภายในออกนอกเครื่องแล้วหรือยัง?" (ข้อ 8 ยังไม่ตัดสินใจ)
2. ถ้าใช่ → แก้แค่ `config.yaml` profile = `fast` + อธิบายความเสี่ยงสั้น ๆ
3. ถ้าไม่ → อธิบายว่าทำไม่ได้ตามข้อ 5 ของ CLAUDE.md

---

## ข้อห้ามเด็ดขาด

- ห้ามส่งข้อมูลออกนอกเครื่องโดยไม่ได้รับอนุมัติชัดเจน
- ห้ามเปลี่ยน Priority #1 (ความเร็ว ingest) หรือข้อตัดสินใจ 14 ข้อโดยไม่ถาม
- ห้ามเพิ่ม LLM generation, ACL, hybrid search, reranker โดยลำพัง (ยัง out of scope)
- ห้ามลบโค้ดของ provider เดิมทิ้ง — ต้องสลับได้ผ่าน config เสมอ
- ห้าม log เนื้อหาเอกสาร

---

## อ้างอิง

- `CLAUDE.md` — กฎและข้อตัดสินใจของโปรเจกต์
- `docs/spec.md` — สเปคฟีเจอร์ FR/NFR, data model, และ phase plan
