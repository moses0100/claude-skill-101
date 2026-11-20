# Claude Skills 101 — with Cowork and Code - Day 3 Notes

**หลักสูตร: สร้าง AI Skills แรกของคุณใน 3 วัน (Cowork and Code)**
**วันที่ 3: Claude Code — Skills บน Terminal**
วันที่: 9 พฤษภาคม 2569 | เวลา 20:30–23:30 น.

---

## 🎯 วัตถุประสงค์การเรียนรู้ประจำวัน

เมื่อจบการอบรมผู้เรียนจะสามารถ:
1. ติดตั้งและใช้งาน Claude Code ผ่าน terminal ได้อย่างถูกต้อง
2. เรียกใช้ Skills สำเร็จรูป (docx, pdf, xlsx) ผ่าน Claude Code ได้
3. สร้าง SKILL.md ใหม่ตั้งแต่ศูนย์ผ่าน terminal ได้
4. ทดสอบและปรับปรุง Skill จนมีประสิทธิภาพสูงสุด
5. สร้าง Skill Composition — Skill ที่เรียก Skill อื่น ๆ ได้
6. แชร์และจัดการ Skill ผ่าน Git/GitHub ได้อย่างเป็นระบบ

---

## 📚 Part 1: รู้จักและติดตั้ง Claude Code (20:30–21:00)

### 1.1 Claude Code คืออะไร?

#### ภาพรวม

**Claude Code** คือ **Command-Line Tool (CLI)** สำหรับ **agentic coding** — เครื่องมือที่ให้คุณมอบหมายงานเขียนโค้ดให้ Claude ทำงานโดยตรงจาก terminal โดยไม่ต้องเปิดหน้าเว็บหรือแอปใด ๆ

```
┌──────────────────────────────────────────────┐
│  Terminal / VS Code Terminal                 │
│                                              │
│  $ claude                                    │
│  > สร้างเว็บไซต์ portfolio ด้วย Next.js      │
│                                              │
│  Claude: กำลังสร้างโปรเจกต์...              │
│  [✓] สร้างไฟล์ src/app/page.tsx              │
│  [✓] สร้างไฟล์ src/components/Header.tsx    │
│  [✓] สร้างไฟล์ src/styles/globals.css       │
│  [✓] ติดตั้ง dependencies                   │
│  [✓] เสร็จสมบูรณ์!                          │
│                                              │
└──────────────────────────────────────────────┘
```

#### Claude Code ทำอะไรได้?

| ความสามารถ          | รายละเอียด                             |
| ------------------- | -------------------------------------- |
| **เขียนโค้ด**       | สร้าง แก้ไข ไฟล์โค้ดทุกภาษา           |
| **อ่านไฟล์**        | อ่านและวิเคราะห์โค้ดที่มีอยู่          |
| **รัน Command**     | รัน npm, git, python, และคำสั่งอื่น ๆ  |
| **ค้นหาไฟล์**       | ค้นหาไฟล์และโค้ดในโปรเจกต์             |
| **Debug**           | วิเคราะห์ error และแก้ไข bug           |
| **ใช้ Skills**      | เรียกใช้ Skills จาก `.claude/skills/`  |
| **Git Operations**  | commit, push, pull, create branch      |

#### เปรียบเทียบ Claude Chat vs Cowork vs Code

| ฟีเจอร์             | Claude Chat   | Claude Cowork   | Claude Code      |
| ------------------- | ------------- | --------------- | ---------------- |
| **อินเทอร์เฟซ**     | เว็บ/แอป      | Desktop App GUI | Terminal (CLI)   |
| **กลุ่มเป้าหมาย**   | ทุกคน         | ผู้ใช้ทั่วไป    | นักพัฒนา         |
| **อ่าน/เขียนไฟล์**  | จำกัด         | ✅              | ✅               |
| **รัน Code**        | ❌            | ✅ (sandbox)    | ✅ (เต็มรูปแบบ)  |
| **Git Integration** | ❌            | ❌              | ✅               |
| **Skills**          | จำกัด         | ✅              | ✅               |
| **Connectors**      | ❌            | ✅              | ผ่าน MCP         |
| **เหมาะกับ**        | ถาม-ตอบทั่วไป | งานไฟล์/เอกสาร  | เขียนโค้ด/DevOps |

**💡 เคล็ดลับ:**

> Claude Code เหมือน "มีโปรแกรมเมอร์ผู้ช่วยนั่งอยู่ข้าง ๆ" — คุณบอกว่าต้องการอะไร แล้ว Claude จะเขียนโค้ด แก้ไข รัน ให้ทั้งหมด คุณแค่ตรวจสอบและอนุมัติ

---

### 1.2 การติดตั้งและตั้งค่าเบื้องต้น

#### ข้อกำหนดเบื้องต้น (Prerequisites)

| รายการ             | เวอร์ชัน      | วิธีตรวจสอบ          |
| ------------------ | ------------- | -------------------- |
| **Node.js**        | 18+           | `node -v`            |
| **npm**            | มากับ Node.js | `npm -v`             |
| **Claude Pro/Max** | subscription  | claude.ai/settings   |
| **Code Editor**    | แนะนำ VS Code | `code -v`            |

#### ขั้นตอนติดตั้ง Claude Code

**ขั้นตอนที่ 1: ตรวจสอบ Node.js**

```bash
node -v
# ควรได้ v18.x.x ขึ้นไป

npm -v
# ควรได้ v9.x.x ขึ้นไป
```

ถ้ายังไม่มี Node.js ดาวน์โหลดจาก https://nodejs.org (เลือก LTS version)

**ขั้นตอนที่ 2: ติดตั้ง Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

**ขั้นตอนที่ 3: ตรวจสอบการติดตั้ง**

```bash
claude --version
# ควรได้เลขเวอร์ชัน เช่น 1.x.x
```

**ขั้นตอนที่ 4: เริ่มใช้งาน**

```bash
# เปิด terminal (หรือ VS Code Terminal)
# cd ไปยังโฟลเดอร์โปรเจกต์
cd my-project

# เริ่มใช้ Claude Code
claude
```

**ขั้นตอนที่ 5: Login/Authentication**

เมื่อใช้ `claude` ครั้งแรก จะต้อง login ผ่าน browser:

```bash
claude
# → เปิด browser ให้ login ด้วยบัญชี Claude Pro/Max
# → เมื่อ login สำเร็จ กลับมาที่ terminal ใช้งานได้เลย
```

#### แก้ปัญหาที่พบบ่อย

| ปัญหา                         | วิธีแก้                                   |
| ----------------------------- | ----------------------------------------- |
| `command not found: claude`   | ตรวจสอบ PATH หรือติดตั้งใหม่ด้วย sudo    |
| `Permission denied`           | ใช้ `sudo npm install -g` (macOS/Linux)   |
| Node version เก่าเกินไป       | อัพเกรด Node.js เป็น 18+ ก่อน            |
| Login ไม่สำเร็จ               | ตรวจสอบ subscription Claude Pro/Max       |
| Timeout เมื่อ install         | ลองใช้ VPN หรือเปลี่ยน network           |

---

### 1.3 คำสั่งพื้นฐานของ Claude Code

#### Slash Commands ที่ใช้บ่อย

| คำสั่ง      | หน้าที่                         | ตัวอย่าง          |
| ----------- | ------------------------------- | ----------------- |
| `/help`     | แสดงคำสั่งทั้งหมดที่ใช้ได้       | `/help`           |
| `/clear`    | ล้างบทสนทนาทั้งหมด              | `/clear`          |
| `/compact`  | สรุปบทสนทนาให้สั้นลง (ประหยัด token) | `/compact`    |
| `/cost`     | แสดงค่าใช้จ่าย token ที่ใช้ไป   | `/cost`           |
| `/model`    | เปลี่ยนโมเดลที่ใช้              | `/model sonnet`   |

#### วิธีใช้งานพื้นฐาน — สั่งงานเป็นภาษาธรรมชาติ

**สร้างไฟล์ใหม่:**

```bash
claude
> สร้างไฟล์ hello.ts ที่ print "สวัสดี Claude Code"
```

**อ่านและวิเคราะห์โค้ด:**

```bash
> อ่านไฟล์ src/app/page.tsx แล้วอธิบายว่าทำอะไร
```

**แก้ไข Bug:**

```bash
> มี error ใน console:
> TypeError: Cannot read properties of undefined (reading 'map')
> ที่ไฟล์ src/components/List.tsx บรรทัด 25
> ช่วยหาและแก้ให้หน่อย
```

**รัน Commands:**

```bash
> รัน npm install แล้ว npm run dev ให้หน่อย
```

**Git Operations:**

```bash
> สร้าง branch ใหม่ชื่อ "feature/add-login" แล้ว commit การเปลี่ยนแปลงทั้งหมด
```

#### Workshop ย่อย: ลองคำสั่งพื้นฐาน

```
แบบฝึกหัด — ทำตามลำดับ:

1. เปิด terminal แล้วพิมพ์ "claude"
2. พิมพ์ "/help" เพื่อดูคำสั่งทั้งหมด
3. สั่ง: "สร้างไฟล์ greeting.ts ที่มีฟังก์ชัน greet(name: string)
         ที่ return 'สวัสดี [name]'"
4. สั่ง: "อ่านไฟล์ greeting.ts แล้วเพิ่ม export default"
5. สั่ง: "รัน tsc greeting.ts เพื่อ compile"
6. พิมพ์ "/cost" เพื่อดู token ที่ใช้ไป
7. พิมพ์ "/clear" เพื่อล้างบทสนทนา
```

---

> ☕ **พักเบรก 21:30–21:45**

---

## 📚 Part 2: Skills ใน Claude Code (21:00–21:30)

### 2.1 Skills ใน Claude Code ทำงานอย่างไร?

#### โครงสร้าง Skills ใน Claude Code

Skills ใน Claude Code จะถูกจัดเก็บในโฟลเดอร์ `.claude/skills/` ของโปรเจกต์:

```
📁 my-project/
├── CLAUDE.md                        ← กฎทั่วไปของโปรเจกต์
├── 📁 .claude/
│   └── 📁 skills/
│       ├── 📁 docx/
│       │   └── SKILL.md             ← Skill สร้างเอกสาร Word
│       ├── 📁 pptx/
│       │   ├── SKILL.md             ← Skill หลัก
│       │   ├── editing.md           ← คู่มือแก้ไข pptx
│       │   └── pptxgenjs.md         ← คู่มือสร้าง pptx ใหม่
│       ├── 📁 xlsx/
│       │   └── SKILL.md             ← Skill สร้างสเปรดชีต
│       └── 📁 pdf/
│           ├── SKILL.md             ← Skill หลัก
│           ├── FORMS.md             ← คู่มือ PDF Forms
│           └── REFERENCE.md         ← คู่มือเพิ่มเติม
└── 📁 src/
    └── ...
```

#### กลไกการทำงาน

```
ผู้ใช้พิมพ์คำสั่ง
        ↓
Claude Code ตรวจ trigger ใน description ของทุก Skill
        ↓
พบ Skill ที่ตรง → อ่าน SKILL.md
        ↓
ทำตาม instructions ใน SKILL.md
        ↓
สร้างผลลัพธ์และแสดงผล
```

**ตัวอย่างการทำงานจริง:**

```bash
> สร้างเอกสาร Word รายงานประจำเดือน

# Claude Code ทำงาน:
# 1. ตรวจพบ trigger "เอกสาร Word" → เรียก Skill "docx"
# 2. อ่าน .claude/skills/docx/SKILL.md
# 3. ทำตาม instructions: ใช้ mammoth/docx-js สร้างไฟล์ .docx
# 4. Validate ไฟล์ที่สร้าง
# 5. ส่งผลลัพธ์และบอกตำแหน่งไฟล์
```

#### Skill หนึ่งอาจมีหลายไฟล์

บาง Skill มีไฟล์ประกอบหลายไฟล์เพื่อแยกคู่มือ:

| ไฟล์           | หน้าที่                              |
| -------------- | ------------------------------------ |
| `SKILL.md`     | คู่มือหลัก — อ่านก่อนเสมอ            |
| `editing.md`   | คู่มือแก้ไขไฟล์ที่มีอยู่             |
| `pptxgenjs.md` | คู่มือสร้างไฟล์ใหม่ตั้งแต่ศูนย์      |
| `FORMS.md`     | คู่มือเฉพาะสำหรับ PDF Forms          |
| `REFERENCE.md` | เอกสารอ้างอิงเพิ่มเติม               |

SKILL.md หลักจะระบุว่าเมื่อไหร่ควรอ่านไฟล์ไหนเพิ่มเติม

---

### 2.2 ทดลองใช้ Skill สำเร็จรูปผ่าน Claude Code

#### Workshop: ใช้ Skills ผ่าน Terminal

**แบบฝึกหัด 1: สร้าง Word Document**

```bash
claude
> สร้างเอกสาร Word จดหมายขอบคุณลูกค้า บริษัท ABC
> ที่ซื้อสินค้ามูลค่า 50,000 บาท เมื่อวันที่ 1 พฤษภาคม 2569
> ใช้ภาษาทางการ มี letterhead และ signature block
```

**แบบฝึกหัด 2: สร้าง PDF ใบเสนอราคา**

```bash
> สร้าง PDF ใบเสนอราคาบริการออกแบบเว็บไซต์
> รายการ:
>   1) ออกแบบ UI/UX          30,000 บาท
>   2) พัฒนา Frontend        50,000 บาท
>   3) พัฒนา Backend         40,000 บาท
>   4) ทดสอบและ Deploy       10,000 บาท
> มี logo placeholder, วันที่, และ Terms & Conditions
```

**แบบฝึกหัด 3: สร้าง Excel รายรับ-รายจ่าย**

```bash
> สร้าง Excel ตารางบันทึกรายรับ-รายจ่ายประจำเดือน
> มีคอลัมน์: วันที่, รายการ, ประเภท (รับ/จ่าย), จำนวนเงิน, หมายเหตุ
> มีสูตรคำนวณยอดรวมรายรับ ยอดรวมรายจ่าย และยอดคงเหลือ
> มี conditional formatting สีเขียว=รายรับ สีแดง=รายจ่าย
```

---

### 2.3 เปรียบเทียบ Skill บน Cowork vs Code

| หัวข้อ               | Claude Cowork                    | Claude Code                |
| -------------------- | -------------------------------- | -------------------------- |
| **อินเทอร์เฟซ**      | GUI (คลิก, ลาก, วาง)            | CLI (พิมพ์คำสั่ง)          |
| **จุดแข็ง**          | ง่าย ใช้ได้ทันที ไม่ต้องตั้งค่า | ยืดหยุ่น ทำได้มากกว่า       |
| **Skill ที่เหมาะ**   | สร้างเอกสาร, Content Marketing  | สร้างโค้ด, DevOps, testing |
| **สร้าง Skill ใหม่** | บอก Claude ตรง ๆ ได้เลย         | สร้างไฟล์ SKILL.md เอง     |
| **ทดสอบ Skill**      | ทดลองใช้ในแชทได้ทันที           | ทดสอบผ่าน terminal          |
| **Git**              | ไม่รองรับ                       | รองรับเต็มรูปแบบ           |
| **Connectors**       | Gmail, Drive, Slack... (GUI)    | ผ่าน MCP Servers           |

**เมื่อไหร่ใช้อะไร?**

- **ใช้ Cowork** เมื่อ: งานเอกสาร, งาน non-technical, ต้องการ Connectors, เริ่มต้นง่าย
- **ใช้ Code** เมื่อ: งาน coding, ต้องการ Git, ต้องการ terminal access, งาน DevOps

**💡 เคล็ดลับ:**

> Skills ที่สร้างบน Cowork สามารถ copy ไปใช้บน Code ได้ทันที (เพราะเป็น SKILL.md เหมือนกัน) — ลองสร้างบน Cowork ก่อน (ง่ายกว่า) แล้วค่อย copy ไปใช้บน Code เมื่อต้องการความยืดหยุ่นมากขึ้น

---

## 📚 Part 3: สร้าง Skill แรกบน Claude Code (21:45–22:15)

### 3.1 วางแผน Skill — คิดก่อนเขียน

#### Framework การออกแบบ Skill (IPO-C)

ก่อนเขียน SKILL.md ต้องวางแผนให้ชัดก่อน:

```
┌─────────────────────────────────────┐
│  1. Problem — ปัญหาที่ต้องการแก้     │
│     "งานอะไรที่ฉันทำซ้ำ ๆ?"          │
├─────────────────────────────────────┤
│  2. Input — ข้อมูลที่ต้องใส่เข้าไป  │
│     "ต้องใส่อะไรบ้าง?"              │
├─────────────────────────────────────┤
│  3. Process — ขั้นตอนการทำงาน       │
│     "ทำอะไรบ้างเป็นลำดับ?"          │
├─────────────────────────────────────┤
│  4. Output — ผลลัพธ์ที่ต้องการ      │
│     "ต้องการอะไรออกมา?"             │
├─────────────────────────────────────┤
│  5. Constraints — ข้อจำกัด          │
│     "มีอะไรที่ห้ามทำ / ต้องระวัง?"  │
└─────────────────────────────────────┘
```

#### ตัวอย่างการวางแผน Skill: "code-review-checklist"

| หัวข้อ          | รายละเอียด                                                  |
| --------------- | ----------------------------------------------------------- |
| **Problem**     | ทำ Code Review ให้ทีมทุกวัน แต่มักลืมตรวจสอบบางจุด         |
| **Input**       | ไฟล์โค้ด หรือ code snippet ที่ต้องการ review                |
| **Process**     | ตรวจ naming → security → performance → readability → tests  |
| **Output**      | รายงาน review พร้อมคะแนนแต่ละด้าน และคำแนะนำ                |
| **Constraints** | ไม่แก้โค้ดเอง แค่วิเคราะห์และแนะนำเท่านั้น                 |

---

### 3.2 เขียน SKILL.md ใน Claude Code

#### วิธีที่ 1: ให้ Claude สร้างให้

```bash
claude
> สร้างโฟลเดอร์ .claude/skills/code-review/
> แล้วสร้าง SKILL.md สำหรับ Skill ที่ตรวจสอบโค้ดตาม checklist 5 ด้าน:
> naming, security, performance, readability, testing
> ให้คะแนน 1-5 แต่ละด้าน พร้อมคำแนะนำการปรับปรุง
```

#### วิธีที่ 2: เขียนเองผ่าน VS Code

สร้างไฟล์ `.claude/skills/code-review/SKILL.md` และเขียนเนื้อหา:

```markdown
---
name: code-review
description: >
  ตรวจสอบโค้ดตาม checklist มาตรฐาน พร้อมคะแนนและคำแนะนำ
  Use this skill when the user mentions "review โค้ด",
  "ตรวจโค้ด", "code review", "check code quality",
  "วิเคราะห์โค้ด"
---

# Code Review Checklist

## Overview

Skill นี้ช่วยตรวจสอบโค้ดอย่างเป็นระบบ ครอบคลุม 5 ด้านหลัก
เหมาะสำหรับ Developer และ Tech Lead ที่ต้องการ review อย่างสม่ำเสมอ

## Instructions

1. รับโค้ดหรือไฟล์โค้ดจากผู้ใช้
   - ถ้าไม่มีโค้ด → ถามว่า "กรุณาแปะโค้ดที่ต้องการ review ครับ"
2. ตรวจสอบ 5 ด้าน (ทีละด้าน):

### 2.1 Naming Convention (การตั้งชื่อ)
- ชื่อตัวแปร ฟังก์ชัน class ชัดเจน สื่อความหมายหรือไม่?
- ตรงตาม convention ของภาษา? (camelCase, PascalCase, snake_case)
- ไม่มีชื่อย่อที่กำกวม? (เช่น d, tmp, x)

### 2.2 Security (ความปลอดภัย)
- มีการ validate และ sanitize input หรือไม่?
- มีการป้องกัน SQL Injection / XSS / CSRF?
- ไม่มี hardcoded secrets, API keys, passwords?
- มีการจัดการ authentication/authorization ถูกต้อง?

### 2.3 Performance (ประสิทธิภาพ)
- มี N+1 query หรือ unnecessary loop?
- มีการ cache ข้อมูลที่ควร cache?
- มีการจัดการ memory อย่างเหมาะสม?
- มี async/await ที่ไม่จำเป็น?

### 2.4 Readability (อ่านง่าย)
- โค้ดอ่านเข้าใจง่ายโดยไม่ต้องอธิบาย?
- มี comment ที่จำเป็นและถูกต้อง?
- function ไม่ยาวเกินไป (แนะนำไม่เกิน 50 บรรทัด)?
- ไม่มี nested if/else ลึกเกินไป (แนะนำไม่เกิน 3 ชั้น)?

### 2.5 Testing (การทดสอบ)
- มี unit test สำหรับ business logic สำคัญ?
- มีการทดสอบ edge cases และ error cases?
- test ตั้งชื่อชัดเจน รู้ว่าทดสอบอะไร?

3. ให้คะแนนแต่ละด้าน 1-5 พร้อมเหตุผล
4. สรุปคะแนนรวมและคำแนะนำสำคัญ 3 ข้อ

## Output Format

## Code Review Report

### สรุปคะแนน

| ด้าน         | คะแนน (1-5) | สถานะ |
| ------------ | ----------- | ----- |
| Naming       | X/5         | ✅/⚠️/❌ |
| Security     | X/5         | ✅/⚠️/❌ |
| Performance  | X/5         | ✅/⚠️/❌ |
| Readability  | X/5         | ✅/⚠️/❌ |
| Testing      | X/5         | ✅/⚠️/❌ |
| **รวม**      | **X/25**    | |

### รายละเอียดปัญหา

[แยกตามด้าน พร้อมตัวอย่างโค้ดที่ควรปรับ]

### คำแนะนำสำคัญ 3 อันดับแรก

1. [ปัญหาที่สำคัญที่สุด]
2. [ปัญหาที่สำคัญรองลงมา]
3. [ปัญหาที่ควรปรับปรุง]

## Constraints
- ไม่แก้โค้ดให้โดยตรง — แนะนำและยกตัวอย่างเท่านั้น
- ถ้าโค้ดผ่านทุกด้าน ให้แสดงข้อดีด้วย ไม่ใช่แค่ปัญหา
- ถ้าโค้ดสั้นมาก (< 10 บรรทัด) แจ้งว่า review บางด้านไม่สามารถประเมินได้

## Examples

### ตัวอย่างที่ 1: โค้ด TypeScript ที่มีปัญหา
**Input:**
```typescript
const d = await db.query('SELECT * FROM users WHERE id=' + id)
const x = d[0]
if (x) {
  if (x.active) {
    if (x.role === 'admin') {
      return true
    }
  }
}
return false
```

**Output:**
## Code Review Report
...Security: 1/5 (SQL Injection risk)
...Naming: 1/5 (d, x ไม่สื่อความหมาย)
...Readability: 2/5 (nested if ลึกเกินไป)
```

---

### 3.3 ทดสอบ Skill ที่สร้าง

#### การทดสอบ 4 แบบ

**แบบที่ 1: Happy Path — Input ปกติ**

```bash
> review โค้ดนี้ให้หน่อย:
> function getUserData(userId) {
>   const user = users.find(u => u.id === userId)
>   return user
> }
```

**แบบที่ 2: Missing Input**

```bash
> review โค้ดให้หน่อย
# คาดหวัง: Skill ถามว่า "กรุณาแปะโค้ดที่ต้องการ review ครับ"
```

**แบบที่ 3: โค้ดภาษาอื่น**

```bash
> review โค้ด Python นี้:
> def get_user(id):
>     return db.execute(f"SELECT * FROM users WHERE id={id}")
# คาดหวัง: Skill ทำงานได้แม้โค้ดจะเป็น Python
```

**แบบที่ 4: โค้ดที่ดีมาก**

```bash
> review โค้ดนี้:
> const getUserById = async (userId: string): Promise<User | null> => {
>   if (!userId || typeof userId !== 'string') return null
>   return await User.findById(userId).lean()
> }
# คาดหวัง: Skill ให้คะแนนสูงและชื่นชมจุดดี
```

---

## 📚 Part 4: Skill ขั้นสูงและ Skill Composition (22:15–22:50)

### 4.1 สร้าง Skill จากงานจริง (Workshop)

#### โจทย์ Workshop

```
เลือกงาน Coding/Dev ที่ทำซ้ำบ่อยในงานของคุณ
แล้วสร้างเป็น Skill ภายใน 15 นาที

ตัวอย่างที่เลือกได้:
A) git-commit-message — สร้าง commit message มาตรฐาน
B) api-doc-generator — สร้าง API documentation จากโค้ด
C) test-case-writer — สร้าง unit test จาก function
D) bug-report-template — สร้าง bug report ที่สมบูรณ์
E) refactor-advisor — แนะนำวิธี refactor โค้ดที่ซับซ้อน
F) คิดเอง — งาน Dev ที่ทำซ้ำบ่อยในโปรเจกต์ของคุณ
```

#### ตัวอย่าง Skill: "git-commit-message"

```markdown
---
name: git-commit-message
description: >
  สร้าง git commit message ที่สมบูรณ์ตาม Conventional Commits
  Use this skill when the user mentions "เขียน commit message",
  "git commit", "commit ให้หน่อย", "สร้าง commit"
---

# Git Commit Message Generator

## Overview

Skill นี้สร้าง commit message ตาม Conventional Commits format
ที่ทีมสามารถเข้าใจและ generate changelog ได้อัตโนมัติ

## Instructions

1. รับข้อมูลจากผู้ใช้:
   - ไฟล์ที่เปลี่ยนแปลง (หรือ git diff)
   - คำอธิบายสั้น ๆ ว่าทำอะไร (ถ้ามี)
2. วิเคราะห์ประเภทของการเปลี่ยนแปลง:
   - feat: เพิ่มฟีเจอร์ใหม่
   - fix: แก้ bug
   - refactor: ปรับโครงสร้างโค้ดโดยไม่เปลี่ยน behavior
   - docs: แก้ไข documentation
   - test: เพิ่ม/แก้ไข test
   - chore: งานทั่วไป (config, build, etc.)
3. สร้าง commit message ในรูปแบบ:
   `type(scope): short description`
   
   และ body (ถ้าจำเป็น):
   `- อธิบายรายละเอียดที่ซับซ้อน`

## Output Format

Commit Message ที่แนะนำ:
```
feat(auth): add JWT refresh token support

- Implement refresh token endpoint at POST /auth/refresh
- Add token expiry validation middleware
- Update UserSession model with refreshToken field
```

คำอธิบาย: [อธิบายเหตุผลที่เลือก type และ scope นี้]

## Constraints
- Subject line ไม่เกิน 72 ตัวอักษร
- ใช้ imperative mood ("add" ไม่ใช่ "added" หรือ "adding")
- ไม่ลงท้าย subject ด้วย period (.)
- ถ้าเปลี่ยนแปลงหลายอย่าง แนะนำให้แยก commit
```

---

### 4.2 Skill Testing & Iteration

#### หลักการ: Test-Improve-Repeat

```
สร้าง Skill เวอร์ชัน 1
        ↓
ทดสอบ 4 แบบ (happy path, missing, edge, different lang)
        ↓
พบปัญหา? ─── ไม่ ──→ ✅ พร้อมใช้งาน
        ↓ ใช่
ระบุปัญหา → แก้ไข SKILL.md → ทดสอบซ้ำ
```

**Checklist การทดสอบ Skill:**

```
□ ทดสอบ happy path — ได้ผลที่คาดหวัง
□ ทดสอบ missing input — Skill ถามข้อมูลเพิ่ม
□ ทดสอบ edge case — Skill จัดการได้อย่างถูกต้อง
□ ทดสอบภาษาอื่น — ผลลัพธ์ตรงตามภาษาที่ใช้
□ ทดสอบ input ขนาดใหญ่ — Skill ไม่หยุดทำงาน
□ Output format ถูกต้องและสม่ำเสมอ
□ Trigger คำสั่ง trigger ได้ตรงเป้า
```

---

### 4.3 Skill Composition — ใช้ Skill เรียก Skill

#### แนวคิด Skill Composition

Skill Composition คือการสร้าง Skill ที่ทำงานร่วมกับ Skill อื่น เหมือน "Skill ผู้จัดการ" ที่สั่งงาน "Skill ลูกน้อง"

```
┌─────────────────────────────────────────┐
│  "project-kickoff" Skill (Master)        │
│                                         │
│  เมื่อเรียกใช้ จะสั่งให้:               │
│  1. Skill "git-commit-message"           │
│     → สร้าง initial commit              │
│  2. Skill "api-doc-generator"            │
│     → สร้าง README และ API Docs          │
│  3. Skill "code-review"                  │
│     → ตรวจสอบโค้ดเริ่มต้น               │
└─────────────────────────────────────────┘
```

#### ตัวอย่าง Skill Composition: "daily-dev-report"

```markdown
---
name: daily-dev-report
description: >
  สร้างรายงานสรุปการทำงานประจำวันสำหรับ Developer
  Use this skill when the user mentions "สรุปงานวันนี้",
  "daily report", "รายงานประจำวัน"
---

# Daily Developer Report

## Overview

Skill นี้รวบรวมข้อมูลจากหลายแหล่งเพื่อสร้างรายงานประจำวัน
โดยใช้ Skills อื่น ๆ ร่วมกัน

## Instructions

1. รวบรวมข้อมูลการทำงานวันนี้:
   - ถามผู้ใช้: "วันนี้ทำงานอะไรบ้าง? (ระบุสั้น ๆ)"
   - ดึง git log ของวันนี้ (ถ้าอยู่ใน git repository)
2. สร้างสรุปงาน:
   - งานที่เสร็จแล้ว (Done)
   - งานที่กำลังทำ (In Progress)
   - ปัญหาที่พบ (Blockers)
   - งานที่จะทำพรุ่งนี้ (Tomorrow)
3. Format เป็น standup update ที่พร้อม share ในทีม

## Output Format

## Daily Dev Report — [วันที่]

**Done ✅**
- [งานที่เสร็จ]

**In Progress 🔄**
- [งานที่กำลังทำ] (X% complete)

**Blockers ⛔**
- [ปัญหา / สิ่งที่ต้องการความช่วยเหลือ]

**Tomorrow 📋**
- [งานที่วางแผนทำพรุ่งนี้]
```

#### Workshop: สร้าง Skill Composition

```
โจทย์: สร้าง Skill ที่ทำงานร่วมกับ Skill อื่นอย่างน้อย 2 Skill

ตัวอย่าง:
- "onboarding-helper": ช่วยนักพัฒนาใหม่
  → เรียก Skill อธิบายโปรเจกต์ + Skill สร้าง checklist
- "release-prep": เตรียม release
  → เรียก Skill code-review + Skill สร้าง changelog + Skill สร้าง release notes
- "feature-complete": ทำ feature ให้สมบูรณ์
  → เรียก Skill เขียน test + Skill สร้าง docs + Skill commit message
```

---

## 📚 Part 5: แชร์ Skill + สรุปหลักสูตร + Q&A (22:50–23:30)

### 5.1 Skill Performance & Best Practices

#### กฎ 10 ข้อสำหรับ Skill ที่ดี

**กฎที่ 1: Description ต้องมี trigger ชัดเจน**

```yaml
# ❌ แบบที่ไม่ดี
description: "ช่วยเขียนโค้ด"

# ✅ แบบที่ดี
description: >
  ตรวจสอบโค้ดตาม checklist มาตรฐาน
  Use this skill when the user mentions "review โค้ด",
  "code review", "ตรวจโค้ด", "check code"
```

**กฎที่ 2: Instructions ต้องเป็นขั้นตอน ไม่กำกวม**

```markdown
# ❌ แบบที่ไม่ดี
## Instructions
ช่วยผู้ใช้เขียนโพสต์ที่ดี

# ✅ แบบที่ดี
## Instructions
1. ถามผู้ใช้เรื่องหัวข้อ แพลตฟอร์ม กลุ่มเป้าหมาย
2. สร้าง Hook ประโยคแรก
3. เขียนเนื้อหาตามความยาวที่เหมาะกับแพลตฟอร์ม
4. เพิ่ม CTA และ Hashtag
5. ให้ผู้ใช้ตรวจสอบก่อน confirm
```

**กฎที่ 3: มี Examples อย่างน้อย 2 ตัวอย่าง**

Examples ช่วยให้ Claude เข้าใจ pattern ที่ต้องการได้แม่นยำขึ้นมาก

**กฎที่ 4: Output Format ต้องชัดเจน**

ระบุ format ที่ต้องการอย่างละเอียด เช่น ตาราง, bullet points, หัวข้อ

**กฎที่ 5: Constraints ครอบคลุม edge cases**

ระบุสิ่งที่ห้ามทำ และสิ่งที่ต้องทำเมื่อพบสถานการณ์พิเศษ

**กฎที่ 6: Skill ควรทำงานเดียวให้ดี**

อย่าสร้าง Skill ที่ทำหลายอย่างในครั้งเดียว — แยกเป็น Skill เดี่ยว แล้วค่อยรวมด้วย Composition

**กฎที่ 7: ทดสอบด้วย input ที่หลากหลาย**

อย่าทดสอบแค่ happy path — ทดสอบ edge cases, missing info, ภาษาอื่น

**กฎที่ 8: Instructions ไม่ควรยาวเกินไป**

Skill ที่ instructions ยาวเกินไปจะทำงานช้าและผิดพลาดบ่อย — ตัดสิ่งที่ไม่จำเป็นออก

**กฎที่ 9: ชื่อ Skill ต้องสื่อความหมาย**

ใช้ kebab-case และชื่อที่บอกได้ทันทีว่า Skill ทำอะไร เช่น `daily-email-digest`, `code-review-checklist`

**กฎที่ 10: Version Control Skill เสมอ**

ใช้ Git commit ทุกครั้งที่แก้ไข SKILL.md เพื่อสามารถ rollback ได้

#### ตารางสรุป: ข้อผิดพลาดที่พบบ่อย

| ข้อผิดพลาด | ผลที่เกิด | วิธีแก้ |
|-----------|---------|--------|
| Description ไม่มี trigger | Skill ไม่ถูกเรียกใช้ | เพิ่มประโยค "Use this skill when..." |
| Instructions คลุมเครือ | ผลลัพธ์ไม่สม่ำเสมอ | เขียนเป็นขั้นตอนชัดเจน |
| ไม่มี Output Format | รูปแบบผลลัพธ์ต่างกันทุกครั้ง | เพิ่ม Output Format section |
| ไม่มี Examples | Claude เดาสิ่งที่ต้องการผิด | เพิ่มตัวอย่าง input/output อย่างน้อย 2 |
| Constraints ไม่ครบ | Skill ทำเกินหรือน้อยเกิน | เพิ่ม Constraints และ Edge Cases |

---

### 5.2 แชร์ Skill ให้ทีม

#### วิธีจัดการ Skill ด้วย Git — ขั้นตอนสมบูรณ์

**ขั้นตอนที่ 1: สร้าง Repository**

```bash
# สร้าง repo สำหรับ Skills ของทีม
mkdir team-claude-skills
cd team-claude-skills
git init

# สร้างโครงสร้าง
mkdir -p skills/code-review
mkdir -p skills/git-commit-message
mkdir -p skills/daily-dev-report
mkdir -p docs

# สร้าง README
echo "# Team Claude Skills Repository" > README.md
echo "รวม Skills สำหรับทีม Dev ของเรา" >> README.md
```

**ขั้นตอนที่ 2: เพิ่ม Skills เข้า Repository**

```bash
# copy Skills ที่สร้างไว้
cp -r .claude/skills/code-review/ ./skills/code-review/
cp -r .claude/skills/git-commit-message/ ./skills/git-commit-message/

# commit
git add .
git commit -m "feat: add code-review and git-commit-message skills"
```

**ขั้นตอนที่ 3: Push ขึ้น GitHub**

```bash
git remote add origin https://github.com/your-org/team-claude-skills.git
git branch -M main
git push -u origin main
```

**ขั้นตอนที่ 4: ทีมอื่น ๆ ใช้งาน**

```bash
# clone repository
git clone https://github.com/your-org/team-claude-skills.git

# copy Skills ไปใส่ในโปรเจกต์
cp -r team-claude-skills/skills/code-review/ my-project/.claude/skills/code-review/

# หรือ symlink เพื่อ sync อัตโนมัติ
ln -s /path/to/team-claude-skills/skills/ my-project/.claude/skills/
```

#### Versioning Skills

```bash
# Tag เวอร์ชัน Skill
git tag -a v1.0.0 -m "Stable version of code-review skill"
git push origin v1.0.0

# ถ้าต้อง rollback
git checkout v1.0.0 -- skills/code-review/SKILL.md
```

---

### 5.3 แหล่งหา Skill ที่น่าสนใจ

| แหล่ง | ลิงก์ | ประเภท |
|-------|-------|--------|
| **Plugin Marketplace** | Claude Desktop App → Settings → Plugins | Skills สำเร็จรูปจาก Anthropic |
| **GitHub Search** | `github.com/search?q=claude+SKILL.md` | Skills จาก Community |
| **Awesome Claude** | ค้นหา "awesome-claude" บน GitHub | รายการ Resources รวม |
| **Anthropic Docs** | docs.anthropic.com | เอกสารทางการ |
| **Reddit r/ClaudeAI** | reddit.com/r/ClaudeAI | Skills และ Tips |
| **Claude AI Thailand** | กลุ่ม Facebook | Skills ภาษาไทย |

---

### 5.4 สรุปหลักสูตร 3 วัน

#### ภาพรวมสิ่งที่เรียนรู้

**วันที่ 1 — พื้นฐาน Skills:**

| หัวข้อ | Key Takeaway |
|--------|--------------|
| Skills vs Prompt Engineering | Skills = สมองสำเร็จรูป ใช้ซ้ำได้ แชร์ได้ |
| CLAUDE.md | กำหนดบุคลิกและกฎทั่วไปของ Claude |
| Plugins vs Skills | Plugin = กล่องเครื่องมือ, Skill = เครื่องมือชิ้นเดียว |
| โครงสร้าง SKILL.md | Frontmatter + Instructions + Examples + Constraints |
| Iterate | ทดสอบ → ปรับ → ทดสอบซ้ำ — วนรอบจนสมบูรณ์ |

**วันที่ 2 — Claude Cowork + Connectors:**

| หัวข้อ | Key Takeaway |
|--------|--------------|
| Content Strategist AI | SKILL.md = DNA ขององค์กร ทำให้ Claude ตอบตรงแบรนด์ |
| Connectors | Claude เชื่อมต่อ Gmail, Drive, Slack ได้จริง |
| Schedule | ตั้งเวลาให้ AI ทำงานอัตโนมัติ |
| Dispatch | trigger-action เมื่อมีเหตุการณ์เกิดขึ้น |
| Error Handling | Skill ที่ดีต้องรับมือ edge cases ได้ |

**วันที่ 3 — Claude Code:**

| หัวข้อ | Key Takeaway |
|--------|--------------|
| Claude Code CLI | terminal-based AI coding assistant |
| Skills บน Code | SKILL.md เหมือนกัน แต่ power มากกว่า |
| Code Review Skill | ตรวจโค้ดอัตโนมัติ 5 ด้านพร้อมคะแนน |
| Skill Composition | Skill เรียก Skill — สร้าง workflow ซับซ้อนได้ |
| Git + Skills | Version control Skill เหมือนโค้ด |

#### Skill ที่ผู้เรียนสร้างตลอดหลักสูตร

```
วันที่ 1:
├── social-media-post (หรือ Skill ที่เลือก)
└── meeting-summary (หรือ Skill จากงานจริง)

วันที่ 2:
├── content-strategist-[ชื่อองค์กร]
├── daily-email-digest
└── [Skill จากงานจริงขององค์กร]

วันที่ 3:
├── code-review-checklist
├── git-commit-message
└── [Skill Composition]
```

#### Next Steps — ต่อยอดหลังจากหลักสูตร

1. **นำ Skills ไปใช้จริง** — เริ่มใช้ Skills ที่สร้างไว้ในงานประจำวันทันที
2. **ปรับปรุงต่อเนื่อง** — iterate ทุกครั้งที่พบปัญหาหรือต้องการปรับเปลี่ยน
3. **แชร์ให้ทีม** — สร้าง team repository สำหรับ Skills ของทีม
4. **สร้าง Plugin** — เมื่อมี Skills หลายตัวที่เกี่ยวข้อง ลองรวมเป็น Plugin
5. **ค้นหา Skills ใหม่** — ติดตาม Plugin Marketplace และ Community อย่างสม่ำเสมอ
6. **สอนคนอื่น** — ความรู้ Skills ที่ดีที่สุดคือความรู้ที่แชร์ให้คนอื่น

---

### 5.5 Q&A และมอบประกาศนียบัตร

#### คำถามที่มักถามบ่อย (FAQ)

**Q: Skills ที่สร้างบน Cowork ใช้บน Code ได้ไหม?**
A: ได้ครับ เพราะทั้งคู่ใช้ SKILL.md เหมือนกัน แค่ copy ไฟล์ไปวางในโฟลเดอร์ `.claude/skills/` ของโปรเจกต์

**Q: SKILL.md ยาวแค่ไหนถึงจะดี?**
A: ไม่มีตายตัว แต่โดยทั่วไป 50-200 บรรทัดเหมาะที่สุด — ยาวเกินไปทำให้ Claude ทำงานช้าและผิดพลาด สั้นเกินไปทำให้ผลลัพธ์ไม่สม่ำเสมอ

**Q: Skill ทำงานผิดพลาดบ่อย ควรทำอย่างไร?**
A: เพิ่ม Examples ให้มากขึ้น (อย่างน้อย 3 ตัวอย่าง) และเพิ่ม Edge Cases section เพื่อระบุกรณีพิเศษ

**Q: สามารถใช้ Skill หลายตัวพร้อมกันได้ไหม?**
A: ได้ครับ Claude จะเรียกทุก Skill ที่ตรงกับ trigger และทำงานร่วมกัน — แต่ถ้าอยากควบคุมลำดับ ให้ใช้ Skill Composition แทน

**Q: Plugin Marketplace มี Skills อะไรที่น่าสนใจบ้าง?**
A: ปัจจุบันมี Skills หลักหมวด: Productivity (docx, xlsx, pptx, pdf), Marketing (blog-post, ad-copy, brand-story), Developer Tools (code-review, documentation), และ Business (meeting-summary, email-digest)

---

# Best Practice: การทำงานกับ Claude Code
## ตั้งแต่ Create Project จนถึง Production

> **สำหรับ Stack:** Next.js 15+ (App Router) · Tailwind CSS · shadcn/ui · TypeScript  
> **เรียบเรียงจากแนวทาง:** Anthropic Official Docs, Community Best Practices 2025-2026

---

## สารบัญ

1. [ภาพรวมแนวคิดหลัก](#1-ภาพรวมแนวคิดหลัก)
2. [การเตรียมตัว: Global Configuration](#2-การเตรียมตัว-global-configuration)
3. [Phase 1: Planning — คิดก่อนโค้ด](#3-phase-1-planning--คิดก่อนโค้ด)
4. [Phase 2: Project Scaffolding](#4-phase-2-project-scaffolding)
5. [Phase 3: CLAUDE.md — หัวใจของทุกโปรเจ็กต์](#5-phase-3-claudemd--หัวใจของทุกโปรเจ็กต์)
6. [Phase 4: Skills, Commands & Hooks](#6-phase-4-skills-commands--hooks)
7. [Phase 5: Development Workflow](#7-phase-5-development-workflow)
8. [Phase 6: Testing & Quality Gates](#8-phase-6-testing--quality-gates)
9. [Phase 7: Production & Deployment](#9-phase-7-production--deployment)
10. [Reusable Template สำหรับทุกโปรเจ็กต์](#10-reusable-template-สำหรับทุกโปรเจ็กต์)
11. [คำถามที่พบบ่อย](#11-คำถามที่พบบ่อย)
12. [แหล่งอ้างอิง](#12-แหล่งอ้างอิง)

---

## 1. ภาพรวมแนวคิดหลัก

การทำงานกับ Claude Code อย่างมีประสิทธิภาพตั้งอยู่บนหลักการ 3 ข้อสำคัญ:

**1.1 Context Management คือสิ่งสำคัญที่สุด**

Claude Code มี Context Window ที่จำกัด เมื่อ context เต็ม ประสิทธิภาพจะลดลงอย่างมาก ผู้ใช้ที่ประสบความสำเร็จจะจัดการ context อย่างเคร่งครัดผ่าน CLAUDE.md, การใช้ `/clear` บ่อยๆ, และการแบ่งงานเป็นชิ้นเล็กๆ

**1.2 Planning ก่อน Implementation เสมอ**

ทุกโปรเจ็กต์ที่มีคุณภาพเริ่มจากการวางแผน ไม่ว่าจะเป็นแบบง่ายๆ ด้วย Plan Mode หรือแบบละเอียดด้วย Spec-driven approach ก็ตาม "Vibe coding" อาจใช้ได้กับ MVP แต่ Production-grade code ต้องมีโครงสร้างที่ชัดเจน

**1.3 Feedback Loop ที่แน่นหนา**

ให้ Claude Code มีวิธีตรวจสอบตัวเอง ผ่าน test commands, linter, type checking — ยิ่ง feedback loop แน่นเท่าไหร่ คุณภาพยิ่งสูง

---

## 2. การเตรียมตัว: Global Configuration

ก่อนเริ่มโปรเจ็กต์ใดๆ ควรตั้งค่า Global Configuration ไว้ก่อน เพื่อให้ทุกโปรเจ็กต์ใช้ค่าพื้นฐานเดียวกัน

### 2.1 ติดตั้ง Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2.2 สร้าง Shell Alias (ไม่จำเป็นแต่แนะนำ)

เพิ่มใน `~/.zshrc` หรือ `~/.bashrc`:

```bash
alias cc="claude"
alias ccp="claude -p"  # print mode สำหรับ scripting
```

### 2.3 Global User Memory — กฎที่ใช้ทุกโปรเจ็กต์

สร้างไฟล์ `~/.claude/CLAUDE.md` สำหรับ preference ส่วนตัว:

```markdown
# Global Preferences

## Code Style
- ใช้ TypeScript strict mode เสมอ
- ไม่ใส่ semicolon (;) ท้ายบรรทัด
- ใช้ ES modules (import/export) ไม่ใช่ CommonJS
- Destructure imports เมื่อเป็นไปได้
- ใช้ functional components กับ React hooks
- ใช้ single quotes สำหรับ string
- ใช้ 2 spaces สำหรับ indentation
- ตั้งชื่อ component เป็น PascalCase
- ตั้งชื่อไฟล์เป็น kebab-case

## Preferred Stack
- Framework: Next.js (App Router) + TypeScript
- Styling: Tailwind CSS
- UI Library: shadcn/ui
- Package Manager: pnpm
- State: Zustand (ถ้าจำเป็น)

## Communication
- ตอบเป็นภาษาไทยเมื่อ comment ในโค้ด
- Commit messages เป็นภาษาอังกฤษ
```

> **หมายเหตุ:** ไฟล์ Global นี้จะถูกอ่านทุกครั้งที่เริ่ม session ใหม่ แต่จะถูก override ด้วย project-level CLAUDE.md ได้

### 2.4 Global Skills (ทักษะที่ใช้ซ้ำข้ามโปรเจ็กต์)

สร้างโฟลเดอร์:

```
~/.claude/skills/
├── code-review/
│   └── SKILL.md
├── create-component/
│   └── SKILL.md
└── git-workflow/
    └── SKILL.md
```

---

## 3. Phase 1: Planning — คิดก่อนโค้ด

### 3.1 เริ่มด้วย Plan Mode

เมื่อเริ่มโปรเจ็กต์ใหม่ ให้เข้า Plan Mode ก่อนเขียนโค้ดเสมอ:

```
claude

> /plan สร้างระบบ E-commerce dashboard ที่มี:
> - หน้า login/register
> - Dashboard แสดง order summary
> - Product management CRUD
> - ใช้ Next.js App Router, Tailwind CSS, shadcn/ui
> - Database: PostgreSQL + Prisma
```

Claude จะสร้างแผนงานให้ก่อน โดยไม่เขียนโค้ดทันที

### 3.2 สำหรับโปรเจ็กต์ขนาดใหญ่: Spec-Driven Approach

สร้าง spec file ก่อน:

```
> เริ่มจากสัมภาษณ์ฉันเกี่ยวกับ requirements ของโปรเจ็กต์นี้
> ถามทีละคำถาม เพื่อสร้าง spec ที่สมบูรณ์
```

Claude จะทำหน้าที่เป็น Product Manager สัมภาษณ์ requirements แล้วสร้าง spec document ให้ จากนั้น:

```
> /clear
> ใช้ spec ที่สร้างไว้ใน docs/spec.md เป็นฐาน
> เริ่ม implement ตาม Phase 1
```

### 3.3 ควรสร้างโครงโปรเจ็กต์ขึ้นรอไว้หรือไม่?

**คำตอบ: ใช่ แนะนำอย่างยิ่ง** แต่ต้องทำอย่างถูกวิธี

สิ่งที่ควรเตรียมไว้ล่วงหน้า:
- **CLAUDE.md template** — ปรับให้เข้ากับ stack ที่ใช้
- **โครงสร้างโฟลเดอร์มาตรฐาน** — ไม่ต้องมีโค้ดจริง แค่ skeleton
- **.claude/ configuration** — settings, hooks, skills ที่ใช้ซ้ำ
- **Base scaffolding script** — ใช้สร้างโปรเจ็กต์ใหม่ได้ทันที

สิ่งที่ **ไม่ควร** เตรียมไว้:
- โค้ดสำเร็จรูปที่ specific เกินไป (ทำให้ Claude ยึดติดกับ pattern เดิม)
- Components ที่ยังไม่รู้ว่าจะใช้จริงหรือเปล่า

---

## 4. Phase 2: Project Scaffolding

### 4.1 สร้างโปรเจ็กต์ Next.js + Stack ที่ต้องการ

```bash
# สร้างโปรเจ็กต์ Next.js ใหม่
pnpm create next-app@latest my-project \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"

cd my-project

# ติดตั้ง shadcn/ui
pnpm dlx shadcn@latest init

# ติดตั้ง components ที่ใช้บ่อย
pnpm dlx shadcn@latest add button card input label
pnpm dlx shadcn@latest add dialog dropdown-menu table toast

# เปิด Claude Code
claude
```

### 4.2 Initialize ด้วย /init

```
> /init
```

Claude จะวิเคราะห์ codebase แล้วสร้าง `CLAUDE.md` เริ่มต้นให้ จากนั้นต้องปรับแต่งเอง (ดู Phase 3)

### 4.3 โครงสร้างโฟลเดอร์มาตรฐาน

```
my-project/
├── CLAUDE.md                    # ← หัวใจของโปรเจ็กต์
├── .claude/
│   ├── settings.json            # hooks & permissions
│   ├── skills/
│   │   ├── create-page/
│   │   │   └── SKILL.md
│   │   ├── create-component/
│   │   │   └── SKILL.md
│   │   └── api-route/
│   │       └── SKILL.md
│   └── agents/                  # (ถ้าต้องการ)
│       └── code-reviewer.md
├── src/
│   ├── app/                     # App Router pages
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── (auth)/
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   └── api/
│   │       └── [...]/route.ts
│   ├── components/
│   │   ├── ui/                  # shadcn/ui components
│   │   ├── layout/              # Layout components
│   │   └── features/            # Feature-specific components
│   ├── hooks/                   # Custom React hooks
│   ├── lib/                     # Utilities, API wrappers
│   │   ├── utils.ts
│   │   └── api.ts
│   ├── types/                   # TypeScript type definitions
│   └── styles/                  # Custom styles ถ้าจำเป็น
├── prisma/                      # Prisma schema (ถ้าใช้)
│   └── schema.prisma
├── public/
├── docs/                        # Specs, plans, ADRs
│   ├── spec.md
│   └── architecture.md
├── tests/
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## 5. Phase 3: CLAUDE.md — หัวใจของทุกโปรเจ็กต์

CLAUDE.md คือไฟล์ที่ Claude Code อ่านทุกครั้งที่เริ่ม session ใหม่ มันคือ "สมองถาวร" ของโปรเจ็กต์

### 5.1 หลักการสำคัญในการเขียน CLAUDE.md

- **ไม่เกิน 150-200 บรรทัด** — ยิ่งยาว ยิ่ง compliance ลดลง
- **เขียนเฉพาะสิ่งที่ Claude ทำผิดถ้าไม่มี** — ถ้า Claude ทำถูกอยู่แล้ว ไม่ต้องเขียน
- **อย่า embed เนื้อหาไฟล์ทั้งหมด** — ใช้ reference path แทน เช่น "ดูรายละเอียดที่ docs/api.md"
- **บอกทางเลือกเสมอ** — ไม่ใช่แค่ "ห้ามใช้ X" แต่ "ห้ามใช้ X, ให้ใช้ Y แทน"

### 5.2 CLAUDE.md Template สำหรับ Next.js + Tailwind + shadcn/ui

```markdown
# Project: [ชื่อโปรเจ็กต์]

## Quick Facts
- **Stack**: Next.js 15 (App Router), TypeScript, Tailwind CSS, shadcn/ui
- **Package Manager**: pnpm
- **Node**: v20+
- **Database**: PostgreSQL + Prisma (ถ้ามี)

## Commands
- `pnpm dev` — Start dev server
- `pnpm build` — Production build
- `pnpm lint` — ESLint
- `pnpm test` — Run tests
- `pnpm db:push` — Push Prisma schema
- `pnpm db:generate` — Generate Prisma client

## Directory Structure
- `src/app/` — App Router pages & layouts
- `src/components/ui/` — shadcn/ui components (อย่าแก้ไขตรงๆ)
- `src/components/features/` — Feature components
- `src/components/layout/` — Layout components
- `src/hooks/` — Custom React hooks
- `src/lib/` — Utilities & helpers
- `src/types/` — TypeScript types
- `prisma/` — Database schema & migrations

## Code Style
- TypeScript strict mode, ไม่ใช้ `any` (ใช้ `unknown` แทน)
- ไม่ใส่ semicolon (;)
- ใช้ single quotes
- ใช้ functional components + hooks เท่านั้น
- ใช้ `interface` แทน `type` สำหรับ object shapes
- ตั้งชื่อ component: PascalCase, ไฟล์: kebab-case
- ใช้ ES modules (import/export)

## UI & Styling Rules
- ใช้ shadcn/ui components เป็นหลัก สำหรับ form, card, dialog, table
- ใช้ Tailwind utility classes, ไม่เขียน custom CSS ยกเว้นจำเป็น
- ใช้ CSS variables สำหรับ theming (ดู globals.css)
- Responsive design: mobile-first (sm → md → lg → xl)
- ใช้ cn() helper จาก lib/utils สำหรับ conditional classes

## Architecture Patterns
- Server Components เป็น default, ใช้ "use client" เฉพาะเมื่อจำเป็น
- Data fetching ใน Server Components ผ่าน async/await
- Form handling ด้วย Server Actions หรือ React Hook Form
- Error boundaries ใน error.tsx ของแต่ละ route
- Loading states ใน loading.tsx

## API Routes
- ใช้ Route Handlers ใน app/api/
- Return NextResponse.json()
- Validate input ด้วย Zod
- Handle errors ด้วย try-catch

## Testing
- Unit tests ด้วย Vitest + React Testing Library
- Component ใหม่ต้องมี test file คู่กัน
- Test file อยู่ข้าง component: `button.test.tsx`

## Git
- Branch naming: feature/xxx, fix/xxx, refactor/xxx
- Commit messages เป็นภาษาอังกฤษ แบบ conventional commits
- ห้าม commit ไปยัง main branch โดยตรง

## Common Mistakes to Avoid
- ห้ามใช้ `<img>`, ใช้ `<Image>` จาก next/image แทน
- ห้ามใช้ `<a>`, ใช้ `<Link>` จาก next/link แทน
- ห้ามใช้ useEffect สำหรับ data fetching (ใช้ Server Components)
- ห้ามแก้ไขไฟล์ใน components/ui/ โดยตรง
- ห้ามเขียน inline styles
```

### 5.3 Nested CLAUDE.md — Context เฉพาะโฟลเดอร์

สามารถสร้าง CLAUDE.md ในโฟลเดอร์ย่อยได้ เช่น:

```
src/components/CLAUDE.md    → กฎสำหรับ components
src/app/api/CLAUDE.md       → กฎสำหรับ API routes
prisma/CLAUDE.md            → กฎสำหรับ database schema
```

Claude จะอ่านทั้ง root CLAUDE.md และ nested CLAUDE.md ที่เกี่ยวข้อง โดยให้ priority กับไฟล์ที่ specific กว่า

---

## 6. Phase 4: Skills, Commands & Hooks

### 6.1 Skills — สอน Claude ทักษะเฉพาะทาง

สร้างไฟล์ `.claude/skills/create-page/SKILL.md`:

```markdown
---
name: create-page
description: สร้างหน้าใหม่ใน Next.js App Router พร้อม layout
  และ loading states ตาม project conventions
---

# สร้างหน้าใหม่

เมื่อสร้างหน้าใหม่ใน App Router ให้ทำดังนี้:

1. สร้างโฟลเดอร์ใน `src/app/[route-name]/`
2. สร้างไฟล์ต่อไปนี้:

```
src/app/[route-name]/
├── page.tsx        # หน้าหลัก (Server Component)
├── loading.tsx     # Loading UI
├── error.tsx       # Error boundary
└── layout.tsx      # Layout (ถ้าจำเป็น)
```

3. page.tsx pattern:

```tsx
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: '[Page Title]',
  description: '[Description]'
}

export default async function PageName() {
  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">[Title]</h1>
      {/* content */}
    </div>
  )
}
```

4. error.tsx pattern:

```tsx
'use client'

export default function Error({
  error,
  reset
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <h2 className="text-xl font-semibold mb-4">เกิดข้อผิดพลาด</h2>
      <button onClick={reset}>ลองใหม่</button>
    </div>
  )
}
```
```

### 6.2 Custom Commands — ลัดขั้นตอนที่ทำบ่อย

สร้างไฟล์ `.claude/skills/new-feature/SKILL.md`:

```markdown
---
name: new-feature
description: เริ่ม feature ใหม่ด้วย branch, plan, และ scaffolding
disable-model-invocation: true
argument-hint: "[feature-name]"
---

# เริ่ม Feature ใหม่: $ARGUMENTS

1. สร้าง branch ใหม่:
   !git checkout -b feature/$ARGUMENTS

2. วางแผน implementation:
   - วิเคราะห์ requirements จากชื่อ feature
   - เสนอ 3-step plan พร้อม small diffs
   - ระบุไฟล์ที่ต้องสร้างหรือแก้ไข

3. รอ approval ก่อน implement

4. Implement ทีละ step:
   - เขียน tests ก่อน (TDD)
   - Implement code
   - Run tests + lint
   - Commit แต่ละ step

5. สร้าง PR description เมื่อเสร็จ
```

เรียกใช้ด้วย:

```
> /new-feature user-profile
```

### 6.3 Hooks — ป้องกันข้อผิดพลาดอัตโนมัติ

สร้างไฟล์ `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "[ \"$(git branch --show-current)\" != \"main\" ] || { echo '{\"block\": true, \"message\": \"ห้าม edit บน main branch\"}' >&2; exit 2; }",
            "timeout": 5
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "file=\"$CLAUDE_FILE\"; if echo \"$file\" | grep -qE '\\.(ts|tsx)$'; then pnpm exec prettier --write \"$file\" 2>/dev/null; fi",
            "timeout": 15
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "pnpm exec tsc --noEmit 2>&1 | tail -20",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Hooks ที่แนะนำ:
- **PreToolUse**: ป้องกัน edit บน main branch, ป้องกันลบไฟล์สำคัญ
- **PostToolUse**: Auto-format ด้วย Prettier หลังแก้ไข
- **Stop**: Run type-check เมื่อ Claude ทำงานเสร็จ
- **Notification (compact)**: Re-inject context หลัง compaction

---

## 7. Phase 5: Development Workflow

### 7.1 Workflow Loop ที่แนะนำ

```
1. เริ่ม session → Claude อ่าน CLAUDE.md อัตโนมัติ
2. /plan หรืออธิบาย feature ที่ต้องการ
3. Approve แผน
4. Claude implement → สร้าง diff ขนาดเล็ก (< 200 บรรทัด)
5. Review → ให้ feedback ที่เจาะจง
6. Run tests → แก้ไขถ้ามีปัญหา
7. Commit
8. /clear → เริ่ม task ต่อไปด้วย context สะอาด
```

### 7.2 เทคนิคสำคัญ

**ใช้ `/clear` บ่อยๆ**

ทุกครั้งที่เริ่มงานใหม่ ให้ clear context เดิมออก เพราะ history เก่าจะกิน token และทำให้ Claude สับสน

**ใช้ `/compact` เมื่อ session ยาว**

ถ้าทำงานยาวๆ ในเรื่องเดียวกัน ใช้ `/compact` แทน `/clear` เพื่อสรุป context เก่าและปลดปล่อย token

**ใช้ Checkpoints**

Claude Code สร้าง checkpoint ทุกครั้งที่แก้ไฟล์ ใช้ `Esc + Esc` หรือ `/rewind` เพื่อย้อนกลับถ้า approach ไม่ดี

**ให้ feedback ที่เจาะจง**

```
# ❌ คลุมเครือ
> แก้ให้ดีขึ้น

# ✅ เจาะจง
> Component นี้ re-render บ่อยเกินไป
> ย้าย state ลงไปที่ child component
> และใช้ React.memo สำหรับ list items
```

**ใช้ Parallel Sessions**

สำหรับงานที่เป็นอิสระจากกัน เปิด Claude Code หลาย session:

```bash
# Session 1: ทำ Feature A
git worktree add ../project-feature-a feature-a
cd ../project-feature-a && claude

# Session 2: ทำ Feature B
git worktree add ../project-feature-b feature-b
cd ../project-feature-b && claude
```

### 7.3 Prompting ที่มีประสิทธิภาพ

```
# ❌ Micromanaging
> เปิดไฟล์ src/app/page.tsx แล้วไปบรรทัดที่ 42 แล้วเปลี่ยน...

# ✅ ให้ Claude วางแผนเอง
> หน้า Dashboard โหลดช้า
> ตรวจสอบ performance issues แล้วเสนอวิธีแก้ไข

# ✅ ท้าทาย Claude
> grill ฉันเรื่อง changes เหล่านี้
> อย่าสร้าง PR จนกว่าฉันจะตอบคำถามได้ทั้งหมด

# ✅ ให้เริ่มใหม่อย่างดีกว่า
> รู้ทุกอย่างที่รู้ตอนนี้แล้ว
> ทิ้งวิธีนี้ แล้ว implement วิธีที่ elegant กว่า
```

---

## 8. Phase 6: Testing & Quality Gates

### 8.1 Test-First Approach

Claude Code จะให้ผลลัพธ์ดีกว่าเมื่อมี tests เป็นเกณฑ์วัด:

```
> สร้าง test สำหรับ UserProfile component ก่อน
> จากนั้น implement component ให้ tests ผ่าน
```

### 8.2 Quality Checklist ก่อนจบทุก Feature

```
> ก่อนจะ commit ให้ตรวจสอบ:
> 1. pnpm build ผ่านไหม
> 2. pnpm lint ผ่านไหม
> 3. pnpm test ผ่านไหม
> 4. TypeScript type-check ผ่านไหม
> 5. มี error boundary ไหม
> 6. Responsive design ทดสอบแล้วไหม
```

### 8.3 Code Review ด้วย Fresh Session

เปิด session ใหม่เพื่อ review โค้ดที่ Claude เขียน — session ใหม่จะไม่มี bias จากการเขียนโค้ดเอง:

```
> /clear
> Review code changes ใน branch feature/user-profile
> ตรวจสอบ security, performance, และ best practices
```

---

## 9. Phase 7: Production & Deployment

### 9.1 Pre-deployment Checklist

สร้าง skill สำหรับ deploy: `.claude/skills/deploy/SKILL.md`:

```markdown
---
name: deploy
description: Deploy application to production
disable-model-invocation: true
---

# Production Deploy Checklist

ก่อน deploy ตรวจสอบ:

1. **Build**: `pnpm build` ผ่านไม่มี error
2. **Tests**: `pnpm test` ผ่านทั้งหมด
3. **Type Safety**: `pnpm exec tsc --noEmit` ผ่าน
4. **Lint**: `pnpm lint` ไม่มี warning
5. **Environment Variables**: ตรวจสอบ .env.production
6. **Database Migrations**: ตรวจสอบว่า migration ล่าสุดถูก apply
7. **Security**:
   - ไม่มี secrets ใน codebase
   - API routes มี authentication
   - Input validation ครบ
8. **Performance**:
   - Images ใช้ next/image
   - Dynamic imports สำหรับ heavy components
   - Server Components เป็น default
```

### 9.2 CI/CD Integration

Claude Code สามารถใช้ใน CI/CD pipeline ได้:

```bash
# ใน GitHub Actions
claude -p "Review PR changes, ตรวจสอบ security และ performance issues"
claude -p "Generate PR description summarizing changes, risks, และ test coverage"
```

---

## 10. Reusable Template สำหรับทุกโปรเจ็กต์

### 10.1 Bootstrap Script

สร้าง script ที่ใช้สร้างโปรเจ็กต์ใหม่ได้ทันที:

```bash
#!/bin/bash
# create-nextjs-project.sh

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "Usage: ./create-nextjs-project.sh <project-name>"
  exit 1
fi

# สร้าง Next.js project
pnpm create next-app@latest "$PROJECT_NAME" \
  --typescript --tailwind --eslint --app --src-dir \
  --import-alias "@/*"

cd "$PROJECT_NAME"

# ติดตั้ง shadcn/ui
pnpm dlx shadcn@latest init -d

# ติดตั้ง base components
pnpm dlx shadcn@latest add button card input label \
  dialog dropdown-menu table toast separator \
  form select textarea

# ติดตั้ง dependencies ที่ใช้บ่อย
pnpm add zod
pnpm add -D vitest @testing-library/react @testing-library/jest-dom

# คัดลอก Claude Code config template
cp -r ~/templates/claude-code/.claude .claude/
cp ~/templates/claude-code/CLAUDE.md CLAUDE.md

# สร้างโครงสร้างโฟลเดอร์
mkdir -p src/components/{ui,layout,features}
mkdir -p src/hooks src/lib src/types
mkdir -p docs tests

# เปิด Claude Code
echo "โปรเจ็กต์ $PROJECT_NAME พร้อมแล้ว!"
echo "cd $PROJECT_NAME && claude"
```

### 10.2 Template Repository

แนวทางที่ดีที่สุดคือสร้าง GitHub Template Repository:

```
my-nextjs-template/
├── CLAUDE.md                    # ← template พร้อมใช้
├── .claude/
│   ├── settings.json
│   └── skills/
│       ├── create-page/SKILL.md
│       ├── create-component/SKILL.md
│       ├── api-route/SKILL.md
│       └── deploy/SKILL.md
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── loading.tsx
│   │   └── error.tsx
│   ├── components/
│   │   ├── ui/                  # shadcn base
│   │   └── layout/
│   │       └── header.tsx
│   ├── hooks/
│   ├── lib/
│   │   └── utils.ts
│   └── types/
├── docs/
├── tests/
└── ...config files
```

ใช้งาน:

```bash
# สร้างโปรเจ็กต์ใหม่จาก template
gh repo create my-new-project --template=my-nextjs-template --clone
cd my-new-project
claude
> /init   # ปรับ CLAUDE.md ให้เหมาะกับโปรเจ็กต์นี้
```

### 10.3 ทำให้ทุกโปรเจ็กต์ไปในทิศทางเดียวกัน

มี 3 ระดับในการควบคุมความสม่ำเสมอ:

| ระดับ | ไฟล์ | หน้าที่ |
|-------|------|---------|
| **Global** | `~/.claude/CLAUDE.md` | Code style, preferences ส่วนตัว |
| **Template** | Template repo | โครงสร้างโปรเจ็กต์, skills, hooks มาตรฐาน |
| **Project** | `./CLAUDE.md` | Context เฉพาะโปรเจ็กต์ |

---

## 11. คำถามที่พบบ่อย

**Q: ควรใช้ Opus หรือ Sonnet?**

Opus เหมาะกับงานซับซ้อน เช่น architecture decisions, debugging ยากๆ, code review ส่วน Sonnet เหมาะกับงานตรงไปตรงมา เช่น scaffolding, simple CRUD ค่า default คือ Opus จนถึง 50% usage แล้วจะสลับเป็น Sonnet

**Q: Claude Code กับ Claude.ai Chat ต่างกันอย่างไร?**

Claude Code ทำงานใน terminal ของคุณ อ่าน codebase ได้ แก้ไขไฟล์ได้ รัน commands ได้ มี context ของทั้งโปรเจ็กต์ ส่วน Claude.ai Chat เหมาะกับการถามคำถาม วางแผน เขียน spec

**Q: ต้อง commit ทุก change หรือไม่?**

แนะนำให้ commit บ่อยๆ เป็น small, atomic commits เพราะ Claude Code สร้าง checkpoints จากไฟล์ที่ edit เท่านั้น ไม่ครอบคลุมการเปลี่ยนแปลงจาก bash commands เช่น database migrations

**Q: ทำอย่างไรเมื่อ Claude ทำพลาดซ้ำ?**

เพิ่มข้อกำหนดใน CLAUDE.md ในส่วน "Common Mistakes to Avoid" — CLAUDE.md คือที่เก็บ "บทเรียนจากความผิดพลาด"

---

## 12. แหล่งอ้างอิง

| แหล่งข้อมูล | ลิงก์ |
|------------|------|
| Anthropic Official Best Practices | https://code.claude.com/docs/en/best-practices |
| Claude Code Skills Documentation | https://code.claude.com/docs/en/skills |
| claude-code-best-practice (84 tips) | https://github.com/shanraisshan/claude-code-best-practice |
| awesome-claude-md (400+ templates) | https://github.com/sx4im/awesome-claude-md |
| Claude Code Config Composer | https://github.com/Matt-Dionis/claude-code-configs |
| Claude Code Showcase (hooks/skills/agents) | https://github.com/ChrisWiles/claude-code-showcase |
| Claude Code Complete Guide 2026 | https://claude-world.com/articles/claude-code-complete-guide-2026/ |
| 50 Claude Code Tips | https://www.builder.io/blog/claude-code-tips-best-practices |
| Claude Code Setup 2026 (MCP, hooks, skills) | https://okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/ |
| Skills & Hooks Starter Kit | https://github.com/DavidROliverBA/Daves-Claude-Code-Skills |

---

## Workshop Hands-on Claude Code Desktop

### Objective

สร้าง Python CLI system สำหรับจัดการและประมวลผลไฟล์ขนาดใหญ่ (CSV, PDF, Word) โดยแบ่งข้อมูลเป็น chunks แล้วเก็บ vector embeddings ลงใน ChromaDB เพื่อใช้งานใน RAG pipeline สำหรับ Q&A, Document Search และ Summarization

#### Prompt สำหรับเริ่มต้นการสัมภาษณ์แนวทางการสร้างระบบจัดการไฟล์ด้วย Python: 

```
ฉันอยากทำระบบจัดการไฟล์ไฟล์ csv, pdf, word ขนาดใหญ่ ด้วยภาษา python เพื่อจัดการแบ่งข้อมูลเหล่านี้แล้วเก็บลง vector db เช่น ChromaDB เพื่อไว้ไปจัดทำ RAG ต่อไป แต่ยังคิดไอเดียไม่ออก คุณช่วยสัมภาษณ์สอบถามแนวทางต่างๆ กับฉันก่อนเริ่ม โดยค่อยๆ ถามฉันมาเป็นข้อ ๆ เช่น A, B, C, D แล้วให้ฉันเลือก
```

#### Prompt สำหรับสร้าง CLAUDE.md , SKILL.md และสร้าง spec.md ใน docs/ ด้วย:
```
ช่วยฉันเขียนพวก CLAUDE.md , SKILL.md และสร้าง spec.md ไว้ใน docs/ เพื่อเป็นแนวทางในการพัฒนาระบบจัดการไฟล์ขนาดใหญ่ด้วย Python ที่เราได้คุยกันไว้ใน session ก่อนหน้านี้ โดย CLAUDE.md จะเป็นกฎเกณฑ์และแนวทางการเขียนโค้ดของโปรเจ็กต์นี้ ส่วน SKILL.md จะเป็นทักษะเฉพาะที่ฉันอยากให้คุณมีเพื่อช่วยในการพัฒนา และ spec.md จะเป็นเอกสารสเปคที่อธิบายรายละเอียดของฟีเจอร์และการทำงานของระบบ
```

#### Prompt สำหรับให้ Claude สร้างโครงสร้างโปรเจ็กต์และเริ่มเขียนโค้ด:

```
ตอนนี้เรามี CLAUDE.md, SKILL.md และ spec.md แล้ว ช่วยฉันสร้างโครงสร้างโปรเจ็กต์ Python สำหรับระบบจัดการไฟล์ขนาดใหญ่ที่เราได้วางแผนไว้ และเริ่มเขียนโค้ดสำหรับฟีเจอร์แรกที่เราตกลงกันไว้ใน spec.md ได้เลย
```

#### Prompt สำหรับให้ Claude สร้าง test cases ด้วย pytest:

```
ตอนนี้เราเริ่มเขียนโค้ดสำหรับฟีเจอร์แรกของระบบจัดการไฟล์ขนาดใหญ่แล้ว ช่วยฉันสร้าง test cases ด้วย pytest เพื่อทดสอบฟีเจอร์นี้ให้ครอบคลุมทุกกรณีที่เราคิดไว้ใน spec.md และแนวทางที่กำหนดใน CLAUDE.md ด้วย
```

#### Prompt สำหรับให้ Claude สร้างสคริปต์สำหรับรันโปรเจ็กต์นี้:
```
ช่วยเขียนการเตรียมความพร้อมเครื่องผู้ใช้ก่อนรันโปรเจ็กต์นี้ด้วยครับ เขียนไว้ใน docs/setup.md โดยอธิบายขั้นตอนการติดตั้ง dependencies ต่างๆ เช่น Python, ChromaDB, และวิธีการรันโปรเจ็กต์นี้ครั้งแรก
```

#### คำสั่งดูปริมาณ token ที่ใช้ไปใน session นี้:
```
/usage
```

#### คำสั่งดู Conext Window ที่เหลืออยู่:
```
/context
```

#### คำสั่งดูค่าใช้จ่ายที่เกิดขึ้นใน session นี้:
```
ช่วยคำนวณออกมาเป็นค่าใช้จ่าย (เงินบาท) สำหรับการทำโปรเจ็กต์นี้
```

## Workshop Hands-on Claude Code Command Line Interface (CLI)

### Objective
เว็บแอปสุ่มแจกรางวัลแบบวงล้อหมุน ไม่มี backend ใช้ React + Tailwind CSS  โดยให้ Claude Code ช่วยเขียนโค้ดทั้งหมด ตั้งแต่การวางแผน การสร้างโครงโปรเจ็กต์ การเขียนโค้ด และการทดสอบ

#### เข้าใช้งาน Claude Code CLI:

```bash
# ติดตั้ง Claude Code CLI
npm install -g @anthropic-ai/claude-code

# สร้างโปรเจ็กต์ใหม่
mkdir prize-wheel-app
cd prize-wheel-app
claude
```

#### Prompt สำหรับเริ่มต้นการวางแผนและสร้างโครงโปรเจ็กต์:

```
ฉันอยากสร้างเว็บแอปสุ่มแจกรางวัลแบบวงล้อหมุน โดยใช้ React, Tailwind CSS โดยไม่มี backend ช่วยฉันวางแผนการพัฒนา โดยสัมภาษณ์ฉันเกี่ยวกับฟีเจอร์ที่ต้องการ และสร้างแผนงานให้ฉันก่อนเริ่มเขียนโค้ด
```

#### Prompt สำหรับให้ Claude สร้างไฟล์ CLAUDE.md และ SKILL.md สำหรับโปรเจ็กต์นี้:

```
ช่วยฉันเขียนพวก CLAUDE.md , SKILL.md และสร้าง spec.md ไว้ใน docs/ เพื่อเป็นแนวทางในการพัฒนาระบบสุ่มแจกรางวัลแบบวงล้อหมุนด้วย React และ Tailwind CSS ที่เราได้คุยกันไว้ใน session ก่อนหน้านี้ โดย CLAUDE.md จะเป็นกฎเกณฑ์และแนวทางการเขียนโค้ดของโปรเจ็กต์นี้ ส่วน SKILL.md จะเป็นทักษะเฉพาะที่ฉันอยากให้คุณมีเพื่อช่วยในการพัฒนา และ spec.md จะเป็นเอกสารสเปคที่อธิบายรายละเอียดของฟีเจอร์และการทำงานของระบบ
```

#### Prompt สำหรับให้ Claude สร้างโครงสร้างโปรเจ็กต์และเริ่มเขียนโค้ด:

```
ตอนนี้เรามี CLAUDE.md, SKILL.md และ spec.md แล้ว ช่วยฉันสร้างโครงสร้างโปรเจ็กต์ React สำหรับระบบสุ่มแจกรางวัลแบบวงล้อหมุนที่เราได้วางแผนไว้ และเริ่มเขียนโค้ดสำหรับฟีเจอร์แรกที่เราตกลงกันไว้ใน spec.md ได้เลย
```

#### Prompt สำหรับให้ Claude สร้าง test cases ด้วย React Testing Library:

```
ตอนนี้เราเริ่มเขียนโค้ดสำหรับฟีเจอร์แรกของระบบสุ่มแจกรางวัลแบบวงล้อหมุนแล้ว ช่วยฉันสร้าง test cases ด้วย React Testing Library เพื่อทดสอบฟีเจอร์นี้ให้ครอบคลุมทุกกรณีที่เราคิดไว้ใน spec.md และแนวทางที่กำหนดใน CLAUDE.md ด้วย
```

---

> 🎓 **ยินดีด้วย! คุณสำเร็จหลักสูตร Claude Skills 101**
>
> ตลอด 3 วันที่ผ่านมา คุณได้เรียนรู้ตั้งแต่พื้นฐานของ Skills
> ไปจนถึงการสร้าง Skill ขั้นสูงบนทั้ง Claude Cowork และ Claude Code
> ประกาศนียบัตรจะได้รับจากสถาบันไอทีจีเนียส
>
> **IT Genius Engineering Co., Ltd.**
> อาจารย์สามิตร โกยม | samitkoyom@gmail.com
