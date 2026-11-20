# spec.md — Specification: ระบบจัดการไฟล์ขนาดใหญ่สำหรับ RAG

| Field | Value |
|---|---|
| Version | 0.1.0 (Draft) |
| Status | ออกแบบเสร็จ / **ยังไม่เริ่มเขียนโค้ด** |
| Last updated | 2026-11-20 |
| แหล่งที่มา | ผลสัมภาษณ์ 14 ข้อใน session นี้ |
| เอกสารที่เกี่ยวข้อง | `CLAUDE.md`, `.claude/skills/rag-ingest-pipeline/SKILL.md`, `docs/setup.md` |

---

## 0. ประวัติการแก้ไข

| Version | วันที่ | รายการเปลี่ยน |
|---|---|---|
| 0.1.0 | 2026-11-20 | ร่างแรกจากผลสัมภาษณ์ 14 ข้อ |

---

## 1. วิสัยทัศน์และขอบเขต

### 1.1 วิสัยทัศน์

สร้าง **Internal Knowledge Base** ที่รับไฟล์ PDF, DOCX, CSV จำนวนมาก ดึงข้อความ แบ่งเป็น chunks แบบมีโครงสร้าง แล้วเก็บลง **ChromaDB** เพื่อให้ค้นหาและอ้างอิงแหล่งที่มาได้ โดยออกแบบให้ต่อยอดเป็น RAG (เพิ่ม LLM) ได้ในอนาคตโดยไม่ต้องเขียนระบบใหม่

### 1.2 In scope

- Batch ingestion รายวันจากโฟลเดอร์ files
- ตรวจจับไฟล์ใหม่/เปลี่ยน/ลบ แบบ incremental
- ดึงข้อความจาก PDF ทั้งแบบ digital text และแบบสแกน (OCR)
- ดึงข้อความจาก DOCX และ CSV
- Structure-aware chunking พร้อม metadata สำหรับ citation
- Embedding แบบสลับ provider ได้ (local / API)
- เก็บและค้นหาใน ChromaDB พร้อม metadata filter
- CLI, REST API, และ Streamlit UI แบบเล็ก ๆ
- Checkpoint / resume / idempotency

### 1.3 Out of scope (ยังไม่ทำใน phase นี้)

- LLM generation / คำตอบภาษาธรรมชาติ (phase ถัดไป)
- ระบบสิทธิ์ пользователь / ACL / login
- Hybrid search (BM25), cross-encoder reranker
- Distributed processing (Spark, Ray)
- Web crawler /การเชื่อมต่ออีเมล
- รองรับไฟล์ประเภทอื่น (PPT, Excel, images นอกเหนือจากหน้า PDF สแกน)

---

## 2. ผู้ใช้และสถานการณ์ใช้งาน

**Persona:** เจ้าหน้าที่/นักพัฒนาภายในองค์กร ที่ต้องค้นหาเอกสารประจำวัน

| ID | Use case | รายละเอียด |
|---|---|---|
| UC-01 | Ingest รายวัน | รัน batch ตอนกลางคืน ประมวลผลเฉพาะไฟล์ที่เปลี่ยน |
| UC-02 | ค้นหาเอกสาร | พิมพ์คำค้น รับ chunks ที่เกี่ยวข้องพร้อมบอกแหล่งที่มา |
| UC-03 | ตรวจสถานะ | ดูว่ามีไฟล์ไง fail / ค้าง / รอ ingest อยู่ |
| UC-04 | Reindex | บังคับสร้างใหม่เฉพาะบางไฟล์หรือทั้ง collection |
| UC-05 | ต่อยอด RAG | นำ search hits ไปเป็น context ให้ LLM ในอนาคต |

---

## 3. Requirements

### 3.1 Functional Requirements (FR)

| ID | ฟีเจอร์ | เกณฑ์ยอมรับ |
|---|---|---|
| FR-01 | Scan source folder | เก็บ relative path, size, mtime ลง manifest |
| FR-02 | Delta detection | เปรียบเทียบ size+mtime ก่อน → sha256 เฉพาะไฟล์เปลี่ยน |
| FR-03 | Extract PDF digital | ใช้ PyMuPDF ได้ข้อความ + หน้า + หัวข้อ + ตาราง |
| FR-04 | OCR fallback | ตรวจ text layer ก่อน; OCR เฉพาะหน้าที่ไม่มีข้อความ (tha+eng) |
| FR-05 | Extract DOCX | ใช้ python-docx แยก Heading 1/2/3 และ tables |
| FR-06 | Extract CSV | ผลิต 3 ส่วน: summary, schema, row-groups (~50 แถว/chunk) |
| FR-07 | Chunking | ตัดตามโครงสร้างก่อน; 600–1000 tokens; overlap 80–120 |
| FR-08 | Embedding provider | มี interface + 2 provider (local/API); สลับด้วย config |
| FR-09 | Vector store | ChromaDB ผ่าน `VectorStore` interface; upsert ด้วย ID เดterministic |
| FR-10 | Retrieval | ค้นหา semantic + metadata filter + คืน top-k พร้อม citation |
| FR-11 | Delete handling | ไฟล์หายจาก source → ลบ chunks ของ doc นั้นออกจาก Chroma |
| FR-12 | CLI | `ingest`, `status`, `search`, `reindex` |
| FR-13 | REST API | `/ingest`, `/search`, `/status` ด้วย FastAPI |
| FR-14 | Web UI | หน้า Streamlit ค้นหา + แสดงผล + citation |
| FR-15 | Checkpoint/resume | ขัดจังหวะแล้วรันต่อได้ ไม่ต้องเริ่มใหม่ทั้งรอบ |
| FR-16 | Multilingual | รองรับข้อความผสมไทย-อังกฤษได้ตามสมเหตุสมผล |

### 3.2 Non-Functional Requirements (NFR)

| ID | เรื่อง | เป้า |
|---|---|---|
| NFR-01 | Hardware | ทำงานบน CPU only ได้ (ไม่มี GPU) |
| NFR-02 | Scale | 10k–100k ไฟล์, 50–500 GB |
| NFR-03 | ความเร็ว | **Priority #1** — ingest เสร็จทันรอบรายวัน |
| NFR-04 | Idempotency | รัน ingest สองรอบ → จำนวน chunk ไม่เพิ่ม |
| NFR-05 | Privacy | Default ไม่ส่งข้อมูลออกนอกเครื่อง |
| NFR-06 | Observability | log/status บอกความคืบหน้าและ error ต่อไฟล์ได้ |
| NFR-07 | Maintainability | แยกชั้นชัดเจน เปลี่ยน provider/store ได้โดยไม่แก้โค้ดอื่น |
| NFR-08 | Testability | มี golden samples 4 ประเภท และทดสอบอัตโนมัติ |

---

## 4. Data Model

### 4.1 File manifest (SQLite — `manifest.db`)

| Column | Type | ความหมาย |
|---|---|---|
| `path_hash` | TEXT (PK) | `sha256(relative_path)[:16]` |
| `relative_path` | TEXT | path สัมพันธ์กับ source root |
| `size` | INTEGER | ขนาดไฟล์ (bytes) |
| `mtime` | REAL | modified time |
| `content_hash` | TEXT | sha256 ของเนื้อหา (คำนวณเมื่อ size/mtime เปลี่ยน) |
| `status` | TEXT | `pending`, `extracted`, `chunked`, `embedded`, `failed`, `deleted` |
| `chunk_count` | INTEGER | จำนวน chunk ที่สร้าง |
| `last_ingested_at` | TEXT | ISO timestamp |
| `error_message` | TEXT | error ล่าสุด (ถ้า fail) |

> ใช้ size+mtime เป็นตัวกรองระดับแรก; content_hash เป็นตัวตัดสินใจ final เพื่อไม่ re-embed โดยเปล่าประโยชน์

### 4.2 Chunk metadata ( Chroma `metadatas` )

| Field | Type | บังคับ | ความหมาย |
|---|---|---|---|
| `doc_id` | string | ✅ | `content_hash[:16]` |
| `source` | string | ✅ | relative path |
| `file_name` | string | ✅ | ชื่อไฟล์ |
| `file_type` | string | ✅ | `pdf`, `docx`, `csv` |
| `department` | string | ⬜ | แผนก (ถ้าทราบจากโฟลเดอร์) |
| `created_at` | string | ⬜ | ISO date จาก mtime |
| `ingested_at` | string | ✅ | ISO timestamp |
| `page` | int | PDF | หน้าที่มาจาก |
| `section` | string | PDF/DOCX | heading path เช่น `3.2 > 3.2.1` |
| `row_range` | string | CSV | เช่น `"12-61"` |
| `chunk_index` | int | ✅ | ลำดับ chunk ใน doc |
| `content_hash` | string | ✅ | sha256 ของไฟล์ต้นฉบับ |
| `is_scanned` | bool | PDF | หน้านั้นมาจาก OCR หรือไม่ |

> Chroma รองรับเฉพาะ scalar (str/int/float/bool) — ห้ามใส่ list/dict

### 4.3 Chunk ID scheme

```
chunk_id = f"{content_hash[:16]}_{chunk_index:04d}"
```

ผล: รันซ้ำ → upsert ทับของเดิม ไม่เกิด duplicate; เปลี่ยนเนื้อหา → hash ใหม่ → chunk ใหม่ ส่วนเก่าถูกลบผ่าน `delete_by_doc(doc_id เดิม)`

---

## 5. รายละเอียด Pipeline แต่ละ Stage

### 5.1 ภาพรวม

```
[A] Discovery  →  [B] Extraction  →  [C] Chunking  →  [D] Embedding  →  [E] Store  →  [F] Retrieval
     manifest       ProcessPool       structure       provider         Chroma        citation
```

### 5.2 Stage A — Discovery & Delta Detection

1. เดินโฟลเดอร์แบบ recursive เก็บ relative path
2. ถ้า path ใหม่ / size หรือ mtime เปลี่ยน → คำนวณ `sha256`
3. ถ้า `content_hash` เท่าเดิม → ข้าม (ไม่ extract ใหม่)
4. ถ้าไม่อยู่ใน source อีก → mark `deleted` → ลบ chunks ใน Chroma
5. เขียนสถานะ `pending` ลง manifest ก่อนส่งเข้ากระบวนการถัดไป

**เหตุผล:** ลด I/O และเลี่ยงการ embed ซ้ำ ซึ่งเป็นคอขวดอันดับต้นของข้อมูล 50–500 GB

### 5.3 Stage B — Extraction

#### PDF (`extraction/pdf.py`)
- ใช้ `PyMuPDF` (`fitz`) อ่านทีละหน้า
- **เช็ค text layer ก่อนเสมอ:** ถ้าหน้ามีข้อความพอ (threshold ตั้งได้ เช่น ≥ 50 ตัวอักษร) → ใช้เลย
- ถ้าไม่มีข้อความ → ส่งหน้านั้นให้ `ocr.py`
- `ocr.py`: เรนเดอร์หน้าเป็นภาพ → `pytesseract` with `lang="tha+eng"` → ใส่ `is_scanned=True`
- ตรวจจับตารางด้วย `page.find_tables()` → แปลงเป็น markdown/ข้อความบรรทัด
- รวบเป็น `RawDocument(pages=[RawPage(number, text, headings, tables)])`

#### DOCX (`extraction/docx.py`)
- ใช้ `python-docx`
- อ่าน paragraph พร้อม `style.name` เพื่อระบุ Heading 1/2/3
- อ่าน `doc.tables` → serialize เป็นบรรทัด `| col1 | col2 |`
- รวบเป็น `RawDocument(sections=[RawSection(heading_path, blocks)])`

#### CSV (`extraction/csv.py`)
- ใช้ `pandas.read_csv(..., chunksize=...)` เพื่อไม่โหลดทั้งไฟล์
- ผลิต 3 ส่วน:
  - **summary**: จำนวนแถว, ชื่อคอลัมน์, ช่วงวันที่ (ถ้ามีคอลัมน์วันที่)
  - **schema**: header + ตัวอย่าง 3–5 แถว
  - **row-groups**: ทุกกลุ่ม ~50 แถว เขียนเป็น `"แถว 12: วันที่=..., ยอด=..."`
- ใส่ `row_range` ใน metadata ทุก row-group chunk

**Parallelism:** ใช้ `ProcessPoolExecutor` สำหรับ Stage B (CPU-bound); ส่งกลับแค่ `RawDocument` ที่มีข้อความพร้อมแล้ว

### 5.4 Stage C — Chunking

| ประเภท | กฎหลัก |
|---|---|
| PDF | ตัดตาม heading และขอบหน้า; ห้ามตัดกลางตาราง; ถ้า section ยาว > 1000 tokens ค่อย split |
| DOCX | ตัดตาม heading path; ย่อหน้ายาว split ด้วย overlap |
| CSV | ใช้ chunk ที่ extractor ผลิตมาแล้ว แปลงเป็นข้อความ + `row_range` |

- ใช้ tokenizer ของ embedding model ที่เลือกในการนับ token (ไม่ใช้ tiktoken มั่ว เพราะภาษาไทย)
- เป้าหมาย 600–1000 tokens, overlap 80–120
- ทุก chunk ได้ `Chunk(text, doc_id, metadata, chunk_index)`

### 5.5 Stage D — Embedding

```
EmbeddingProvider (Protocol)
├── FastembedLocalProvider   # default — multilingual-e5-small, ONNX int8, ไม่ส่งข้อมูลออก
└── OpenAIProvider           # ใช้ได้เฉพาะเมื่อได้รับอนุมัติ — text-embedding-3-small
```

- `config.yaml` → `embedding.profile: local | fast`
- `embed(texts: list[str]) -> list[list[float]]` แบบ batch เสมอ
- ตรวจว่า dimension ตรงกับ config ก่อน upsert
- ถ้า API → retry แบบ exponential backoff + จำกัด concurrency

### 5.6 Stage E — Store (ChromaDB)

- PersistentClient ที่ `config.vectorstore.path`
- Collection เดียว เช่น `internal_kb` (แยกด้วย metadata filter ไม่ต้องแยก collection)
- `upsert(ids, documents, metadatas, embeddings)` ทุกครั้ง
- `delete_by_doc(doc_id)` → query ids ด้วย `where={"doc_id": ...}` แล้วลบ
- `search(vector, k, where)` → คืน `SearchHit(text, metadata, score)`

### 5.7 Stage F — Retrieval & Citation

1. embed คำค้นwith provider เดียวกับตอน ingest
2. `collection.query(query_embeddings=[vec], n_results=k, where=filter)`
3. จัดรูป citation:

```
{relative_path} • หน้า {page} • {section}
{relative_path} • แถว {row_range}
```

4. คืนเป็น `list[SearchHit]` (พร้อมนำไปใช้เป็น context ให้ LLM ในอนาคต)

---

## 6. Interfaces

### 6.1 CLI

```bash
python -m kb.cli ingest --source D:\docs
python -m kb.cli ingest --source D:\docs --resume
python -m kb.cli status
python -m kb.cli search "นโยบายการลา" --top-k 5 --department HR
python -m kb.cli reindex --path "docs/คู่มือ.pdf"
```

### 6.2 REST API (FastAPI)

| Method | Path | คำอธิบาย |
|---|---|---|
| `POST` | `/ingest` | เริ่ม batch ingestion (background task) |
| `GET` | `/status` | สถานะ manifest และจำนวน chunk ต่อไฟล์ |
| `POST` | `/search` | `{query, top_k, filters}` → hits + citation |
| `DELETE` | `/documents/{doc_id}` | ลบ chunks ของ doc (กรณีฉุกเฉิน) |

### 6.3 Streamlit UI

- ช่องค้นหา + เลือก `department` / `file_type`
- แสดงผลเป็นการ์ด: ข้อความ + citation + score
- แสดงสถานะ ingest ล่าสุดแบบกระชับ

---

## 7. Configuration (`config.yaml`)

```yaml
source:
  root: "D:/docs"
  include: ["*.pdf", "*.docx", "*.csv"]

manifest:
  path: "data/manifest.db"

extraction:
  ocr:
    enabled: true
    lang: "tha+eng"
    min_text_chars_per_page: 50
  workers: 4                 # ProcessPool size

chunking:
  min_tokens: 600
  max_tokens: 1000
  overlap: 100
  csv_row_group_size: 50

embedding:
  profile: "local"           # local | fast
  allow_external: false      # ต้องเป็น true พร้อมอนุมัติเท่านั้นจึงใช้ profile "fast" ได้
  local:
    model: "intfloat/multilingual-e5-small"
    backend: "onnx"
    quantize: true
  fast:
    model: "text-embedding-3-small"   # ใช้ได้หลังได้รับอนุมัติ
  batch_size: 64

vectorstore:
  backend: "chroma"
  path: "data/chroma"
  collection: "internal_kb"

retrieval:
  top_k: 5

logging:
  level: "INFO"
  path: "logs/ingest.log"
```

> **ห้าม** ใส่ API key ในไฟล์นี้ — อ่านจาก environment variable เสมอ

---

## 8. Error Handling & Recovery

| สถานการณ์ | การจัดการ |
|---|---|
| ไฟล์เสีย / อ่านไม่ได้ | mark `failed` + เก็บ `error_message` → ดำเนินการต่อไฟล์อื่น |
| OCR ล้มเหลวหน้าใดหน้าหนึ่ง | ใช้ข้อความว่าง + log warning + mark ว่าหน้านั้นไม่สมบูรณ์ |
| Embedding API timeout | retry 3 ครั้ง → ถ้ายัง fail mark `failed` และ checkpoint |
| Chroma upsert ล้มเหลว | ไม่ mark `embedded`; รอบหน้าจะ retry จาก checkpoint |
| กระบวนการถูกขัดจังหวะ | รอบถัดไปอ่าน manifest แล้วเริ่มจาก status ล่าสุด |
| ไฟล์หายจาก source | `delete_by_doc` + mark `deleted` |

---

## 9. Performance

### 9.1 กลยุทธ์ (เรียงตาม Impact)

1. **OCR เฉพาะหน้าที่จำเป็น** — ประหยัดเวลาสูงสุด
2. Delta detection ด้วย size+mtime ก่อน sha256
3. Parallel extraction ด้วย ProcessPool
4. Batch embedding + thread ถ้าใช้ API
5. Deterministic ID → upsert แทน delete+insert ทุกครั้ง

### 9.2 เป้าหมายและการวัด

| Metric | วิธีวัด |
|---|---|
| เวลา ingest ต่อ 1 GB | benchmark บน sample 10 ไฟล์ → คาดการณ์ทั้งรอบ |
| จำนวนหน้าที่ถูก OCR | ต้องน้อยกว่าจำนวนหน้าทั้งหมดมาก (เพราะส่วนใหญ่เป็น digital) |
| duplicate chunks | รันสองรอบแล้วนับเท่ากัน |
| recall @5 | ชุดคำถามทดสอบ 20 ข้อเทียบกับ ground truth (ทำใน Phase 4) |

---

## 10. Security & Privacy

- **Default:** embedding profile = `local` → ข้อมูลไม่ออกนอกเครื่อง
- เปลี่ยนเป็น `fast` (API) ได้ก็ต่อเมื่อผู้ใช้อนุมัติชัดเจน (ข้อ 8 ยังเปิดอยู่)
- `config.py` บังคับ guard อัตโนมัติ: ถ้า `profile=fast` แต่ `allow_external=false` → โหลด config ไม่ได้ (`ConfigurationError`)
- เก็บ relative path เท่านั้นใน metadata
- ห้าม log เนื้อหาเอกสาร; log แค่ doc_id / file_name / status
- ห้าม commit ข้อมูลจริง, `.env`, หรือ secret ลง git
- ไม่ทำ ACL — การควบคุมการเข้าถึงเป็นหน้าที่ของระบบอื่น (ตามข้อ 6)

---

## 11. แผนการส่งมอบ (Phases)

| Phase | สิ่งที่ส่ง | Exit criteria |
|---|---|---|
| **0** | โครงสร้างโปรเจกต์, config, interface 3 ตัว, manifest schema, **FR-01/FR-02 (scan + delta detection)** | import ผ่าน, config โหลดได้, sqlite สร้างตารางได้, รัน scan สองรอบแล้วไม่มีไฟล์ถูก queue ซ้ำ |
| **1** | Extractor (PDF digital/DOCX/CSV) + chunker + Chroma store + CLI | ingest ตัวอย่างเล็กได้, search คืนผล + citation |
| **2** | OCR fallback, ProcessPool, checkpoint/resume, delete handling | ทดสอบกับ PDF สแกนได้, รันสองรอบไม่ duplicate |
| **3** | FastAPI, Streamlit, metadata filter, error handling | API/UI ผ่าน smoke test |
| **4** | Benchmark, เลือก embedding profile, evaluate retrieval, เตรียมเชื่อม LLM | มีตัวเลขประสิทธิภาพ + ชุดคำถามทดสอบ |

---

## 12. Acceptance Criteria (ภาพรวม)

- [ ] รองรับ PDF digital, PDF สแกน, DOCX, CSV ตาม FR-03 ถึง FR-06
- [ ] รันรายวันซ้ำได้โดยไม่ duplicate (FR-09, NFR-04)
- [ ] ตรวจจับไฟล์เปลี่ยน/ลบได้ถูกต้อง (FR-02, FR-11)
- [ ] ค้นหาภาษาไทย/อังกฤษปนได้ (FR-16)
- [ ] Citation บอกไฟล์ + หน้า/หัวข้อ/แถวได้ (FR-10)
- [ ] ทำงานบน CPU only (NFR-01)
- [ ] ไม่ส่งข้อมูลออกนอกเครื่องโดย default (NFR-05)
- [ ] มี CLI + API + UI (FR-12 ถึง FR-14)
- [ ] มี tests และ golden samples ครบ (NFR-08)
- [ ] ยังไม่มี LLM generation / ACL / hybrid search (ตามข้อ 11 และ 1.3)

---

## 13. Open Decisions / สมมติฐานที่ยังต้องถามผู้ใช้

| # | เรื่อง | สถานะ | แนวทางชั่วคราว |
|---|---|---|---|
| 1 | อนุญาตส่งข้อมูลไป Embedding API หรือไม่ | **ยังไม่ตัดสินใจ** (ข้อ 8) | ใช้ local profile |
| 2 | CSV ต้องการถามเชิงสถิติ (text-to-SQL) หรือแค่ค้นหา | **ยังไม่ตัดสินใจ** (ข้อ 9) | ใช้ 3 ชั้นตาม FR-06 |
| 3 | โฟลเดอร์ source จริงอยู่ที่ไหน / โครงสร้างแยกแผนกยังไง | ยังไม่ระบุ | ใช้ `department` จากชื่อโฟลเดอร์ถ้าพบ |
| 4 | ขนาด chunk สุดท้ายที่เหมาะกับเอกสารจริง | ต้อง benchmark | 600–1000 tokens, overlap 100 |
| 5 | Chroma จะรองรับจำนวน chunk ได้เพียงพอหรือไม่ | ต้องทดสอบ Phase 4 | เตรียม `VectorStore` interface ไว้ย้าย |

> เมื่อข้อใดถูกล้าง ให้อัปเดตตารางนี้ + ไฟล์ `CLAUDE.md` แล้ว commit ทันที
