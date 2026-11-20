# setup.md — เตรียมความพร้อมเครื่องผู้ใช้

เอกสารนี้อธิบายวิธีเตรียมสภาพแวดล้อมเพื่อรันโปรเจกต์ **kb-ingest** ตั้งแต่ยังไม่มีอะไรติดตั้ง เหมาะสำหรับผู้ใช้ที่เพิ่ง clone/copy โปรเจกต์มาครั้งแรกบน **Windows**

> ตรวจสอบกับสภาพแวดล้อมปัจจุบัน: Windows, Python **3.13.14**, มี `PyYAML` + `pydantic` แล้ว
> **ยังไม่มี** ChromaDB / fastembed / PyMuPDF / Tesseract → ติดตั้งตามขั้นตอนด้านล่าง

---

## สิ่งที่จะได้เมื่อทำครบ

- Virtual environment แยกของโปรเจกต์ (`.venv/`)
- ติดตั้ง dependencies แบบแยกตาม "ชุดฟีเจอร์" (extras) ไม่โหลดของไม่จำเป็นตอนเริ่ม
- OCR ภาษาไทย + อังกฤษพร้อมใช้งาน (`tha+eng`)
- รัน smoke test ยืนยันว่า **FR-01/FR-02** ทำงานได้จริง

---

## Step 1 — ติดตั้ง Python

**ข้อกำหนด:** Python **3.11 ขึ้นไป** (แนะนำ **3.12** เพื่อความเข้ากันได้ดีที่สุดกับ dependency ทุกตัว)

ตรวจสอบของที่มีอยู่:

```powershell
python --version
```

- ถ้าเห็น `Python 3.13.14` → ใช้ได้ (โปรเจกต์นี้ทดสอบบน 3.13 แล้ว)
- ถ้าไม่มี หรือต่ำกว่า 3.11 → ติดตั้งใหม่:

```powershell
winget install Python.Python.3.12
```

หรือดาวน์โหลดติดตั้งจาก <https://www.python.org/downloads/> (เลือก **Add Python to PATH**)

> ถ้าเจอปัญหาติดตั้ง dependency บน 3.13 ให้สร้าง venv ด้วย 3.12 แทน:
> `py -3.12 -m venv .venv`

---

## Step 2 — สร้าง Virtual Environment

รันจากโฟลเดอร์ root ของโปรเจกต์ (ที่มี `pyproject.toml`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

ถ้า PowerShell แจ้งเรื่อง execution policy:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

ทางเลือกอื่น (CMD หรือ Git Bash):

```powershell
.\.venv\Scripts\activate.bat
```

เมื่อ activate สำเร็จ จะเห็น `(.venv)` นำหน้า prompt จากนั้นอัปเกรด pip:

```powershell
python -m pip install --upgrade pip
```

> ใช้ `python -m pip` เสมอ เพื่อให้แน่ใจว่าติดตั้งลงใน venv ที่ activate อยู่ (ไม่ใช่ Python ตัวอื่นในเครื่อง)

---

## Step 3 — ติดตั้ง Dependencies

โปรเจกต์ประกาศ dependencies เป็น **extras** ใน `pyproject.toml` — เลือกติดตั้งตามช่วงงานที่กำลังทำ

### 3.1 ติดตั้งขั้นต่ำ (Phase 0 — แค่โครงสร้าง + scan)

```powershell
python -m pip install -e ".[dev]"
```

ติดตั้ง: `PyYAML`, `pydantic`, `pytest`, `ruff`

### 3.2 ติดตั้งเต็ม (แนะนำก่อนเริ่ม Phase 1)

```powershell
python -m pip install -e ".[pdf,docx,csv,embed-local,store,api,ui,dev]"
```

### 3.3 ตาราง Extras

| Extra | แพ็กเกจหลัก | ใช้สำหรับ | Phase |
|---|---|---|---|
| (พื้นฐาน) | `PyYAML`, `pydantic` | config + models | 0 |
| `pdf` | `PyMuPDF`, `pytesseract`, `pillow` | ดึงข้อความ PDF + OCR | 1–2 |
| `docx` | `python-docx` | ดึงข้อความ Word | 1 |
| `csv` | `pandas` | อ่านตาราง CSV แบบแบ่งช่วง | 1 |
| `embed-local` | `fastembed` | Embedding บน CPU (default, ไม่ส่งข้อมูลออก) | 1 |
| `embed-api` | `openai` | Embedding ผ่าน API (**ต้องได้รับอนุมัติก่อน**) | หลังตัดสินใจข้อ 8 |
| `store` | `chromadb` | Vector database | 1 |
| `api` | `fastapi`, `uvicorn` | REST API | 3 |
| `ui` | `streamlit` | หน้าค้นหา | 3 |
| `dev` | `pytest`, `ruff` | ทดสอบ + lint | 0–4 |

> **ไม่ต้องติดตั้ง `embed-api` ตอนนี้** — ข้อ 8 (privacy) ยังไม่ตัดสินใจ และ config มี guard บังคับอยู่แล้ว

### 3.4 ตรวจสอบการติดตั้ง

```powershell
python -c "import yaml, pydantic; print('base ok')"
python -c "import chromadb; print('chromadb', chromadb.__version__)"
python -c "import fastembed, fitz, docx, pandas; print('extractors ok')"
```

ถ้าคำสั่งที่สอง/สามยังใช้ไม่ได้ แสดงว่ายังไม่ได้รันคำสั่งติดตั้งแบบเต็ม (3.2)

### 3.5 หมายเหตุเรื่องโมเดล Embedding

ครั้งแรกที่สร้าง `FastembedLocalProvider` ระบบจะ **ดาวน์โหลดโมเดล** `intfloat/multilingual-e5-small` จาก HuggingFace (ต้องมีอินเทอร์เน็ต) แล้ว cache ไว้ในเครื่อง

- อยู่ใน Phase 0 ยังไม่มีการเรียก embed → ยังไม่ต้องโหลดตอนนี้
- ถ้าเครื่องไม่มีอินเทอร์เน็ต ต้องเตรียมโมเดลล่วงหน้าแล้วตั้งค่า cache path (เช่น `FASTEMBED_CACHE_PATH`) — จะอธิบายเพิ่มตอน Phase 1

---

## Step 4 — ติดตั้ง Tesseract OCR (สำหรับ PDF ที่เป็นภาพสแกน)

**จำเป็นสำหรับ Phase 2** (ตอนนี้ยังไม่บังคับ แต่แนะนำติดตั้งล่วงหน้า)

### 4.1 ติดตั้งโปรแกรม

วิธีที่ง่ายที่สุด (PowerShell):

```powershell
winget install UB-Mannheim.TesseractOCR
```

หรือดาวน์โหลด installer จาก <https://github.com/UB-Mannheim/tesseract/wiki>

- ขณะติดตั้ง ให้เลือก **Additional language data → Thai** (หรือจะเพิ่มทีหลังก็ได้)
- ตำแหน่งติดตั้งเริ่มต้นคือ `C:\Program Files\Tesseract-OCR`

**ต้อง restart terminal** หลังติดตั้ง เพื่อให้ PATH มีผล

### 4.2 ตรวจสอบ

```powershell
tesseract --version
tesseract --list-langs
```

ผลที่คาด: ต้องเห็น `eng` และ `tha` ในรายการภาษา

### 4.3 ถ้าไม่มีภาษาไทย

โหลด `tha.traineddata` จาก <https://github.com/tesseract-ocr/tessdata> แล้ววางไว้ที่:

```
C:\Program Files\Tesseract-OCR\tessdata\tha.traineddata
```

จากนั้นรัน `tesseract --list-langs` อีกครั้ง

> **ทำไมต้องทำขั้นนี้:** ระบบตรวจ text layer ของ PDF ก่อน แล้วเรียก OCR เฉพาะหน้าที่ไม่มีข้อความ และใช้ `lang="tha+eng"` ตาม config — ถ้าไม่มี `tha` ผลภาษาไทยจะเพี้ยน

---

## Step 5 — ตั้งค่า `config.yaml`

เปิด `config.yaml` ที่ root ของโปรเจกต์ แล้วแก้จุดต่อไปนี้:

```yaml
source:
  root: "D:/docs"          # ← เปลี่ยนเป็นโฟลเดอร์เอกสารจริงของคุณ
  include: ["*.pdf", "*.docx", "*.csv"]

embedding:
  profile: "local"          # ← ห้ามเปลี่ยนเป็น "fast" จนกว่าจะได้รับอนุมัติ
  allow_external: false     # ← ปล่อย false ไว้ (guard จะบล็อกถ้าพยายามใช้ API)
```

**ข้อควรระวัง:**

- ใช้ **forward slash `/`** หรือ escaped backslash `\\` ใน path (เช่น `D:/docs` หรือ `D:\\docs`)
- โฟลเดอร์ใน `source.root` **ต้องมีอยู่จริง** — ถ้าไม่มี `scan_source()` จะ raise `FileNotFoundError`
- **ห้ามใส่ API key ลงใน `config.yaml`** — อ่านจาก environment variable ใน provider แทน
- ไฟล์ที่สร้างตอนรัน (`data/`, `logs/`) ถูก `.gitignore` ไว้แล้ว ไม่ต้อง commit

---

## Step 6 — รันครั้งแรก (Smoke Test)

> ⚠️ ตอนนี้ยัง **ไม่มี CLI** (`python -m kb.cli ...` จะมีใน Phase 3 ตาม FR-12)
> ใช้คำสั่งด้านล่างเพื่อยืนยันว่าโปรเจกต์พร้อมแล้ว

### 6.1 รันชุดทดสอบ (22 รายการ)

```powershell
python -c "import sys, unittest; sys.path.insert(0,'src'); suite=unittest.defaultTestLoader.discover('tests'); result=unittest.TextTestRunner(verbosity=2).run(suite); sys.exit(not result.wasSuccessful())"
```

ผลที่คาด: `Ran 22 tests ... OK`

(ถ้าติดตั้ง `dev` แล้วสามารถใช้ `python -m pytest -q` แทนได้)

### 6.2 รัน scan ไฟล์จริงครั้งแรก

```powershell
python -c "import sys; sys.path.insert(0,'src'); from kb.config import load_settings; from kb.manifest import Manifest; from kb.discovery import scan_source, detect_changes; s=load_settings(); m=Manifest(s.manifest.path); c=scan_source(s.source.root, s.source.include); r,missing=detect_changes(m,c); print('files:',len(c),'queued:',len(r),'deleted:',len(missing))"
```

ผลที่คาด:

- รอบแรก: `files: N queued: N deleted: 0` (N = จำนวนไฟล์ที่เจอ)
- รอบที่สอง (รันซ้ำคำสั่งเดิม): `files: N queued: 0 deleted: 0` → **ยืนยัน idempotency ตาม FR-02**

ไฟล์ `data/manifest.db` จะถูกสร้างขึ้นอัตโนมัติ (SQLite)

### 6.3 ตรวจสอบสถานะใน manifest (ทางเลือก)

```powershell
python -c "import sys; sys.path.insert(0,'src'); from kb.config import load_settings; from kb.manifest import Manifest; print(Manifest(load_settings().manifest.path).summary())"
```

ผลที่คาด: `{'pending': N}` — แปลว่.system queue ไฟล์ไว้รอ Phase 1 แล้ว

---

## Step 7 — Checklist ก่อนเริ่มพัฒนาต่อ

- [ ] `python --version` ≥ 3.11
- [ ] `(.venv)` ปรากฏใน prompt
- [ ] `python -m pip install -e ".[pdf,docx,csv,embed-local,store,api,ui,dev]"` สำเร็จ
- [ ] `import chromadb` และ `import fastembed` ผ่าน
- [ ] `tesseract --list-langs` เห็น `tha` และ `eng` (อย่างน้อยก่อน Phase 2)
- [ ] `config.yaml` ชี้ `source.root` ไปยังโฟลเดอร์ที่มีไฟล์จริง
- [ ] `embedding.profile = local` และ `allow_external = false`
- [ ] รันชุดทดสอบ 22 รายการผ่าน
- [ ] รัน scan รอบที่สองได้ `queued: 0`

---

## Troubleshooting

| อาการ | สาเหตุ | วิธีแก้ |
|---|---|---|
| `ModuleNotFoundError: No module named 'kb'` | ยังไม่ได้ติดตั้งแบบ editable หรือ venv ไม่ activate | รัน `python -m pip install -e ".[dev]"` หรือใช้ `sys.path.insert(0,'src')` |
| `Activate.ps1 cannot be loaded` | PowerShell execution policy | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` แล้ว activate ใหม่ |
| `FileNotFoundError: source root ไม่มีอยู่` | `source.root` ใน config ผิดหรือยังไม่มีโฟลเดอร์ | สร้างโฟลเดอร์หรือแก้ path ให้ถูกต้อง |
| `ConfigurationError: profile="fast" ต้องการ allow_external=true` | พยายามใช้ Embedding API โดยยังไม่ได้รับอนุมัติ | เปลี่ยนกลับเป็น `profile: local` (ข้อ 5 ของ `CLAUDE.md`) |
| `tesseract : not recognized` | ยังไม่ได้ restart terminal หลังติดตั้ง | ปิด/เปิด PowerShell ใหม่ แล้ว `tesseract --version` |
| `Error opening data file tha.traineddata` | ไม่มี language data ภาษาไทย | วาง `tha.traineddata` ใน `tessdata` ตาม Step 4.3 |
| ติดตั้ง `chromadb` ล้มเหลวบน Python 3.13 | บางเวอร์ชันยังไม่รองรับ | สร้าง venv ใหม่ด้วย `py -3.12 -m venv .venv` แล้วติดตั้งใหม่ |
| โหลดโมเดล fastembed ไม่ได้ (ออฟไลน์) | ต้องดาวน์โหลดจาก HuggingFace ครั้งแรก | ตั้งค่า cache path ล่วงหน้า หรือรันบนเครื่องที่มีอินเทอร์เน็ตครั้งหนึ่ง |

---

## หมายเหตุด้านความปลอดภัย

- **Default คือ local embedding** — ข้อมูลเอกสารไม่ออกนอกเครื่อง
- อย่าเปลี่ยน `allow_external: true` เว้นแต่ได้รับอนุมัติชัดเจน (ข้อ 8 ของ spec ยังเปิดอยู่)
- อย่า commit `.env`, API key, ข้อมูลจริง, `data/` หรือ `logs/` ลง git

---

## เอกสารที่เกี่ยวข้อง

- `CLAUDE.md` — กฎและข้อตัดสินใจ 14 ข้อ
- `docs/spec.md` — FR/NFR, data model, roadmap แบบแบ่ง phase
- `.claude/skills/rag-ingest-pipeline/SKILL.md` — ทักษะสำหรับ AI agent ที่พัฒนาระบบนี้
