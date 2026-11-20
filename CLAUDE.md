# CLAUDE.md — กฎและแนวทางการพัฒนาโปรเจกต์

> ไฟล์นี้คือ "สัญญาการทำงาน" สำหรับ Claude (หรือ AI agent) ทุกครั้งที่เข้ามาในโปรเจกต์นี้
> **อ่าน `docs/spec.md` ควบคู่กันเสมอ** ถ้าเอกสารสองฉบับขัดกัน ให้หยุดและถามผู้ใช้ก่อนดำเนินการ

---

## 1. ภารกิจของโปรเจกต์

สร้างระบบจัดการไฟล์ขนาดใหญ่ (PDF, DOCX, CSV) ด้วย Python เพื่อ:

1. ดึงข้อความ (extract) และแบ่งเป็น chunks แบบ **structure-aware**
2. เก็บลง **ChromaDB** เพื่อใช้งานเป็น **Retrieval engine**
3. รองรับการต่อยอดเป็น **RAG** (retrieve → LLM) ในภายหลังโดยไม่ต้องเขียนใหม่ทั้งระบบ

**วิสัยทัศน์ (จากการสัมภาษณ์):** Internal Knowledge Base สำหรับค้นหา/ถามตอบเอกสารภายในองค์กร

---

## 2. ข้อตัดสินใจที่ห้ามเปลี่ยนโดยไม่ถามผู้ใช้

| # | เรื่อง | ค่าที่ตกลงไว้ |
|---|---|---|
| 1 | เป้าหมาย | Internal KB — ถามตอบจาก PDF/Word ภายในองค์กร |
| 2 | ภาษา | ผสมไทย-อังกฤษ → ต้องใช้ multilingual embedding |
| 3 | PDF | ผสม digital text + ภาพสแกน → ตรวจ text layer ก่อน OCR เฉพาะหน้าที่จำเป็น |
| 4 | ขนาด | 10k–100k ไฟล์ / 50–500 GB |
| 5 | ความถี่ | อัปเดตรายวัน (daily batch) |
| 6 | Metadata | Filter ขั้นต่ำ (`source`, `file_type`, `department`, `created_at`) **ไม่ทำ ACL** |
| 7 | Hardware | **CPU only — ไม่มี GPU** |
| 8 | Privacy | ยังไม่ตัดสินใจ → ต้องเป็น config-driven สลับ provider ได้ |
| 9 | CSV | ยังไม่ตัดสินใจ → ใช้ 3 ชั้น (summary / schema / row-groups) |
| 10 | Retrieval | Semantic search + citation พื้นฐาน (ไม่บังคับ hybrid/reranker) |
| 11 | LLM | **ยังไม่ทำ** — สร้าง retrieval engine ก่อน |
| 12 | Chunking | Structure-aware (หัวข้อ/ย่อหน้า/หน้า/ตาราง) |
| 13 | Interface | Library + API + UI เล็ก ๆ |
| 14 | Priority #1 | **ความเร็วในการ ingest** |

> ถ้ามีเหตุผลจะเปลี่ยนข้อใด ให้ถามผู้ใช้ก่อนเสมอ ห้ามตัดสินใจแทน

---

## 3. โครงสร้างโปรเจกต์ (ห้ามข้ามชั้น)

```
project/
├── src/kb/
│   ├── config.py            # โหลด config.yaml / env — จุดเดียวของการตั้งค่า
│   ├── models.py            # dataclass/pydantic: FileRecord, Chunk, SearchHit
│   ├── extraction/          # PDF / DOCX / CSV → RawDocument (ห้ามเรียก embedding)
│   │   ├── base.py
│   │   ├── pdf.py
│   │   ├── docx.py
│   │   ├── csv.py
│   │   └── ocr.py
│   ├── chunking/            # RawDocument → list[Chunk] (ห้ามเรียก store)
│   │   ├── base.py
│   │   ├── pdf_chunker.py
│   │   ├── docx_chunker.py
│   │   └── csv_chunker.py
│   ├── embedding/           # EmbeddingProvider interface + 2 implementation
│   │   ├── base.py
│   │   ├── fastembed_local.py
│   │   └── openai_api.py
│   ├── store/               # VectorStore interface + Chroma implementation
│   │   ├── base.py
│   │   └── chroma.py
│   ├── manifest.py          # sqlite: delta detection + checkpoint
│   ├── discovery.py         # FR-01/FR-02: scan folder + ตรวจ size/mtime ก่อน sha256
│   ├── pipeline.py          # ตัวประสานทุกชั้นเท่านั้น
│   ├── retrieval.py         # query → hits + citation
│   ├── cli.py
│   ├── api.py               # FastAPI
│   └── ui.py                # Streamlit
├── tests/
├── docs/
│   └── spec.md
├── .claude/skills/rag-ingest-pipeline/SKILL.md
├── config.yaml
├── pyproject.toml
└── CLAUDE.md
```

**กฎชั้น (layer rules):**
- `extraction` → ไม่เรียก `embedding` / `store` โดยตรง
- `chunking` → ไม่เรียก `store` โดยตรง
- เฉพาะ `pipeline.py` ที่ประสานทุกชั้นได้
- ทุก provider/store ต้องมี interface ก่อนเสมอ (เพราะ privacy ยังไม่ตัดสินใจ และ Chroma อาจต้องย้าย)

---

## 4. มาตรฐานโค้ด Python

- Python **3.11+**, ใช้ `pathlib` เสมอ (ห้าม `os.path` แบบต่อ string)
- **Type hints ทุก public function** + docstring สั้น ๆ (ไทยหรืออังกฤษก็ได้)
- ใช้ `dataclass` หรือ `pydantic` สำหรับโครงสร้างข้อมูล ห้ามส่ง dict ลอย ๆ ข้ามชั้น
- ใช้ `loguru` (หรือ `logging`) สำหรับ log — **ห้าม `print()` ใน library code** (CLI/UI เท่านั้นที่พิมพ์ได้)
- ห้าม hardcode path, chunk size, model name — อ่านจาก `config.yaml` ผ่าน `config.py`
- f-string เท่านั้น, line length ≤ 100, ใช้ `ruff`/`black` หากมี
- จัดการ error แบบเฉพาะเจาะจง (ห้าม `except Exception: pass`)
- ทุก public function ต้องมี unit test ที่เกี่ยวข้อง

---

## 5. กฎเรื่องข้อมูลและความเป็นส่วนตัว (สำคัญสุด)

- **Default = ข้อมูลห้ามออกนอกเครื่อง** → embedding profile ตั้งเป็น `local`
- การเปลี่ยนเป็น `openai` ต้องมี (1) config (2) หลักฐานอนุมัติจากผู้ใช้ มิฉะนั้นห้ามทำ
- เก็บ **relative path** ใน metadata เท่านั้น (ห้ามเก็บ absolute path ลง Chroma)
- **ห้าม log เนื้อหาเอกสาร** — log แค่ `doc_id`, ชื่อไฟล์, status, จำนวน chunk
- ไฟล์ที่ถูกลบจาก source → ต้องลบ chunks ที่เกี่ยวข้องออกจาก Chroma ด้วย
- ห้าม commit ไฟล์ข้อมูลจริง, API key, หรือ config ที่มี secret ลง git

---

## 6. กฎเรื่องความเร็ว (Priority #1)

1. ตรวจ `size + mtime` ก่อน → ค่อยคำนวณ `sha256` เฉพาะไฟล์ที่เปลี่ยน
2. **OCR เฉพาะหน้าที่ไม่มี text layer** (นี่คือจุดประหยัดเวลาที่สุด)
3. Extraction ใช้ `ProcessPoolExecutor` (CPU-bound, โดน GIL)
4. Embedding ใช้ batch; ถ้าเป็น API ให้ใช้ thread/async (I/O-bound)
5. ทุก chunk ต้องมี **deterministic ID** → upsert ได้ รันซ้ำไม่ duplicate
6. ทุก stage ต้อง checkpoint ได้ → รันต่อจากที่ค้างได้หลัง error

---

## 7. กฎเรื่อง Chunking

- ตัดตามโครงสร้างก่อน → ค่อยเสริมด้วย token split เฉพาะ section ที่ยาวเกิน
- ขนาดเป้าหมาย **600–1000 tokens**, overlap **80–120** (ใช้ tokenizer ของ embedding model ที่เลือก)
- Metadata ต้องมี `page`, `section` (หรือ `row_range` สำหรับ CSV) ทุก chunk
- CSV แบ่งเป็น 3 ส่วนเสมอ: ① summary ② schema ③ row-groups (~50 แถว/chunk)
- ห้ามตัดกลางตาราง หรือกลางหัวข้อโดยไม่จำเป็น

---

## 8. การทดสอบ

- Unit test ต่อ extractor / chunker / manifest
- Integration test ใช้ Chroma แบบ in-memory หรือ temp dir (ห้ามแตะ production DB)
- ต้องมี golden sample 4 ประเภท: PDF digital, PDF สแกน, DOCX, CSV
- **ทดสอบ idempotency:** รัน ingest สองรอบ → จำนวน chunk ต้องเท่าเดิม
- ทดสอบ delta: แก้ไฟล์ 1 ไฟล์ → มีเฉพาะไฟล์นั้นถูก re-embed

---

## 9. Git

- Conventional commit: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- ทุกครั้งที่แก้ `CLAUDE.md`, `docs/spec.md`, หรือ `SKILL.md` → commit ทันที
- ห้าม commit ข้อมูลจริง / secret / `.env`

---

## 10. วิธีทำงานเมื่อได้รับมอบหมาย

1. อ่าน `CLAUDE.md` → อ่าน `docs/spec.md`
2. ระบุว่างานนี้อยู่ phase ไหน (ดูตาราง phase ใน spec)
3. Implement ตามชั้น → รัน test → report สั้น ๆ ว่าอะไรเปลี่ยนและอะไรยังไม่ทำ
4. ถ้าต้องตัดสินใจใหม่ที่กระทบข้อ 2 → **ถามก่อน อย่าเดา**

---

## 11. ข้อควรระวังที่รู้ไว้ล่วงหน้า

- Chroma แบบ local (SQLite) อาจช้าลงถ้า chunk โตหลักล้าน → ต้องมี `VectorStore` abstraction เสมอ
- Tesseract ต้องติดตั้ง language data `tha+eng` มิฉะนั้น OCR ภาษาไทยจะเพี้ยน
- อย่าเลือกโมเดล PyTorch ใหญ่มาฮั้นบน CPU — ใช้ ONNX/quantized (fastembed) แทน
- ข้อมูลผสมไทย-อังกฤษ → อย่าใช้ embedding ที่รองรับแค่อังกฤษ
