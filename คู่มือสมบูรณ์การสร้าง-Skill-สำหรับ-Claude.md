# คู่มือสมบูรณ์การสร้าง Skill สำหรับ Claude
### (The Complete Guide to Building Skills for Claude — ฉบับแปลภาษาไทย)

---

## สารบัญ

1. [บทนำ](#บทนำ)
2. [บทที่ 1: หลักการพื้นฐาน](#บทที่-1-หลักการพื้นฐาน)
3. [บทที่ 2: การวางแผนและออกแบบ](#บทที่-2-การวางแผนและออกแบบ)
4. [บทที่ 3: การทดสอบและพัฒนาต่อเนื่อง](#บทที่-3-การทดสอบและพัฒนาต่อเนื่อง)
5. [บทที่ 4: การเผยแพร่และแบ่งปัน](#บทที่-4-การเผยแพร่และแบ่งปัน)
6. [บทที่ 5: รูปแบบและการแก้ปัญหา](#บทที่-5-รูปแบบและการแก้ปัญหา)
7. [บทที่ 6: แหล่งอ้างอิงและทรัพยากร](#บทที่-6-แหล่งอ้างอิงและทรัพยากร)
8. [ภาคผนวก A: Checklist ฉบับย่อ](#ภาคผนวก-a-checklist-ฉบับย่อ)
9. [ภาคผนวก B: YAML Frontmatter](#ภาคผนวก-b-yaml-frontmatter)
10. [ภาคผนวก C: ตัวอย่าง Skill ฉบับสมบูรณ์](#ภาคผนวก-c-ตัวอย่าง-skill-ฉบับสมบูรณ์)
11. [สรุปประเด็นสำคัญ (โดยผู้แปล)](#สรุปประเด็นสำคัญ-โดยผู้แปล)

---

## บทนำ

**Skill** คือชุดคำสั่ง (Instructions) ที่บรรจุอยู่ในรูปแบบโฟลเดอร์ธรรมดา ซึ่งทำหน้าที่สอน Claude ให้รู้จักจัดการงานหรือ Workflow เฉพาะด้าน Skill ถือเป็นหนึ่งในวิธีที่ทรงพลังที่สุดในการปรับแต่ง Claude ให้เหมาะกับความต้องการของคุณ แทนที่จะต้องอธิบายความชอบ กระบวนการ และความเชี่ยวชาญด้านสาขาให้ Claude ฟังซ้ำทุกครั้ง Skill ช่วยให้คุณสอนเพียงครั้งเดียวแล้วใช้ประโยชน์ได้ทุกครั้งที่ต้องการ

Skill เหมาะอย่างยิ่งกับงานที่มีรูปแบบซ้ำ เช่น การสร้าง Frontend Design จาก Spec, การวิจัยด้วยวิธีการที่สม่ำเสมอ, การสร้างเอกสารที่ปฏิบัติตาม Style Guide ของทีม หรือการประสานงาน Multi-step Process Skill ทำงานร่วมกับความสามารถในตัวของ Claude ได้ดี เช่น การรันโค้ดและการสร้างเอกสาร สำหรับผู้ที่สร้าง MCP Integration นั้น Skill เป็นอีกหนึ่ง Layer ที่ทรงพลัง ช่วยแปลงการเข้าถึง Tool ดิบๆ ให้กลายเป็น Workflow ที่เชื่อถือได้และได้รับการปรับให้เหมาะสม

**สิ่งที่คุณจะได้เรียนรู้:**
- ข้อกำหนดทางเทคนิคและแนวทางปฏิบัติที่ดีที่สุดสำหรับโครงสร้างของ Skill
- รูปแบบสำหรับ Standalone Skill และ MCP-enhanced Workflow
- รูปแบบที่พิสูจน์แล้วว่าได้ผลดีในกรณีการใช้งานต่างๆ
- วิธีการทดสอบ พัฒนาต่อเนื่อง และเผยแพร่ Skill

**สำหรับใคร:**
- นักพัฒนาที่ต้องการให้ Claude ทำตาม Workflow เฉพาะอย่างสม่ำเสมอ
- Power User ที่ต้องการให้ Claude ทำตามขั้นตอนที่กำหนด
- ทีมงานที่ต้องการสร้างมาตรฐานการทำงานของ Claude ทั่วทั้งองค์กร

**สองเส้นทางในการใช้คู่มือนี้:**
- สร้าง Skill แบบ Standalone? — มุ่งเน้นที่ *หลักการพื้นฐาน*, *การวางแผนและออกแบบ*, และหมวด 1–2
- ปรับปรุง MCP Integration? — ส่วน "Skills + MCP" และหมวด 3 เหมาะสำหรับคุณ

**เป้าหมาย:** เมื่ออ่านจบคุณจะสามารถสร้าง Skill ที่ใช้งานได้จริงในการนั่งทำงานครั้งเดียว คาดว่าใช้เวลา 15–30 นาทีในการสร้างและทดสอบ Skill แรกโดยใช้ `skill-creator`

---

## บทที่ 1: หลักการพื้นฐาน

### Skill คืออะไร?

Skill คือโฟลเดอร์ที่ประกอบด้วย:

- **`SKILL.md`** (จำเป็น): คำสั่งในรูปแบบ Markdown พร้อม YAML Frontmatter
- **`scripts/`** (ไม่บังคับ): โค้ดที่รันได้ เช่น Python, Bash เป็นต้น
- **`references/`** (ไม่บังคับ): เอกสารอ้างอิงที่โหลดเมื่อจำเป็น
- **`assets/`** (ไม่บังคับ): Template, Font, Icon ที่ใช้ในผลลัพธ์

---

### หลักการออกแบบหลัก

#### Progressive Disclosure (การเปิดเผยข้อมูลแบบลำดับขั้น)

Skill ใช้ระบบสามระดับ:

| ระดับ | เนื้อหา | การโหลด |
|-------|---------|---------|
| **ระดับที่ 1** — YAML Frontmatter | โหลดอยู่ใน System Prompt ของ Claude เสมอ บอกเพียงพอว่าควรใช้ Skill นี้เมื่อใด | โหลดตลอดเวลา |
| **ระดับที่ 2** — เนื้อหา SKILL.md | โหลดเมื่อ Claude เห็นว่า Skill นี้เกี่ยวข้องกับงานปัจจุบัน | โหลดเมื่อเกี่ยวข้อง |
| **ระดับที่ 3** — ไฟล์เชื่อมโยง (Linked Files) | ไฟล์เพิ่มเติมในโฟลเดอร์ Skill ที่ Claude สามารถค้นหาได้ตามต้องการ | โหลดเฉพาะเมื่อจำเป็น |

การเปิดเผยแบบลำดับขั้นนี้ช่วยลดการใช้ Token ในขณะที่ยังคงความเชี่ยวชาญเฉพาะทางไว้

#### Composability (การประกอบรวมกัน)

Claude สามารถโหลด Skill หลายตัวพร้อมกันได้ Skill ของคุณควรทำงานร่วมกับ Skill อื่นได้ดี ไม่ใช่สมมติว่าตัวเองเป็น Skill เดียวที่มีอยู่

#### Portability (ความสามารถในการพกพา)

Skill ทำงานได้เหมือนกันทั้งบน Claude.ai, Claude Code และ API สร้างครั้งเดียวแล้วใช้ได้ทุก Surface โดยไม่ต้องแก้ไข (โดยมีเงื่อนไขว่า Environment รองรับ Dependency ที่ Skill ต้องการ)

---

### สำหรับผู้สร้าง MCP: Skills + Connectors

> 💡 **สร้าง Standalone Skill โดยไม่มี MCP?** ข้ามไปที่การวางแผนและออกแบบได้เลย สามารถกลับมาอ่านส่วนนี้ทีหลัง

หากคุณมี MCP Server ที่ทำงานได้แล้ว คุณทำส่วนที่ยากที่สุดสำเร็จแล้ว Skill คือ Layer ความรู้ที่อยู่บน MCP — บันทึก Workflow และ Best Practices ที่คุณรู้แล้ว เพื่อให้ Claude นำไปใช้ได้อย่างสม่ำเสมอ

**อุปมา "ครัวมืออาชีพ":**

> MCP มอบครัวมืออาชีพให้: การเข้าถึงเครื่องมือ วัตถุดิบ และอุปกรณ์
>
> Skill มอบสูตรอาหาร: คำสั่งทีละขั้นตอนในการสร้างสิ่งที่มีคุณค่า
>
> ร่วมกัน พวกเขาช่วยให้ผู้ใช้ทำงานที่ซับซ้อนได้โดยไม่ต้องคิดทุกขั้นตอนเอง

| MCP (การเชื่อมต่อ) | Skill (ความรู้) |
|---|---|
| เชื่อม Claude กับบริการของคุณ | สอน Claude วิธีใช้บริการของคุณอย่างมีประสิทธิภาพ |
| มอบการเข้าถึงข้อมูลแบบ Real-time | บันทึก Workflow และ Best Practices |
| Claude "ทำอะไรได้" | Claude "ควรทำอย่างไร" |

**ผลลัพธ์ที่ต่างกัน:**

*โดยไม่มี Skill:*
- ผู้ใช้เชื่อม MCP แต่ไม่รู้จะทำอะไรต่อ
- เกิด Support Ticket ว่า "ทำ X กับ Integration นี้ได้อย่างไร"
- แต่ละบทสนทนาเริ่มใหม่ตั้งแต่ต้น
- ผลลัพธ์ไม่สม่ำเสมอเพราะ Prompt ต่างกัน

*เมื่อมี Skill:*
- Workflow ที่สร้างไว้ล่วงหน้าทำงานโดยอัตโนมัติเมื่อจำเป็น
- การใช้ Tool ที่สม่ำเสมอและเชื่อถือได้
- Best Practices ฝังอยู่ในทุกการทำงาน
- ลด Learning Curve ของ Integration ลงได้อย่างมาก

---

## บทที่ 2: การวางแผนและออกแบบ

### เริ่มด้วย Use Case

ก่อนเขียนโค้ดใดๆ ให้ระบุ Use Case ที่เป็นรูปธรรม 2–3 กรณีที่ Skill ควรรองรับ

**ตัวอย่าง Use Case ที่ดี:**

```
Use Case: การวางแผน Sprint ของโปรเจกต์
Trigger: ผู้ใช้พูดว่า "ช่วยฉันวางแผน Sprint นี้" หรือ "สร้าง Sprint Tasks"
ขั้นตอน:
  1. ดึงสถานะโปรเจกต์ปัจจุบันจาก Linear (ผ่าน MCP)
  2. วิเคราะห์ Velocity และ Capacity ของทีม
  3. แนะนำลำดับความสำคัญของงาน
  4. สร้าง Task ใน Linear พร้อม Label และ Estimate ที่เหมาะสม
ผลลัพธ์: Sprint ที่วางแผนครบพร้อม Task ที่สร้างแล้ว
```

**คำถามที่ควรถามตัวเอง:**
- ผู้ใช้ต้องการทำอะไร?
- งานนี้ต้องการ Workflow หลายขั้นตอนอะไรบ้าง?
- ต้องการ Tool ใด (Built-in หรือ MCP)?
- ควรฝัง Domain Knowledge หรือ Best Practices อะไรไว้?

---

### หมวดหมู่ Use Case ที่พบบ่อย

ที่ Anthropic พบ Use Case หลักสามหมวด:

#### หมวด 1: Document & Asset Creation (การสร้างเอกสารและทรัพยากร)

**ใช้สำหรับ:** การสร้างผลลัพธ์ที่มีคุณภาพและสม่ำเสมอ รวมถึงเอกสาร Presentation, App, Design, โค้ด ฯลฯ

**ตัวอย่างจริง:** `frontend-design` skill (ดูเพิ่มเติมใน `docx`, `pptx`, `xlsx`)

> "สร้าง Frontend Interface ที่โดดเด่นและมีคุณภาพระดับ Production ใช้เมื่อสร้าง Web Component, หน้าเว็บ, Artifact, Poster หรือ Application"

**เทคนิคหลัก:**
- ฝัง Style Guide และมาตรฐานของแบรนด์ไว้
- โครงสร้าง Template สำหรับผลลัพธ์ที่สม่ำเสมอ
- Checklist ตรวจสอบคุณภาพก่อนสรุปผล
- ไม่ต้องการ External Tool — ใช้ความสามารถในตัวของ Claude

#### หมวด 2: Workflow Automation (การอัตโนมัติ Workflow)

**ใช้สำหรับ:** กระบวนการหลายขั้นตอนที่ได้ประโยชน์จากวิธีการที่สม่ำเสมอ รวมถึงการประสานงานข้ามหลาย MCP Server

**ตัวอย่างจริง:** `skill-creator` skill

> "คู่มือแบบ Interactive สำหรับสร้าง Skill ใหม่ นำผู้ใช้ผ่านขั้นตอนการกำหนด Use Case, การสร้าง Frontmatter, การเขียนคำสั่ง และการตรวจสอบ"

**เทคนิคหลัก:**
- Workflow ทีละขั้นตอนพร้อม Validation Gate
- Template สำหรับโครงสร้างทั่วไป
- มีข้อเสนอแนะในตัวสำหรับการทบทวนและปรับปรุง
- Loop การปรับปรุงแบบวนซ้ำ

#### หมวด 3: MCP Enhancement (การยกระดับ MCP)

**ใช้สำหรับ:** คำแนะนำ Workflow เพื่อเพิ่มประสิทธิภาพการเข้าถึง Tool ของ MCP Server

**ตัวอย่างจริง:** `sentry-code-review` skill (จาก Sentry)

> "วิเคราะห์และแก้ไข Bug ที่ตรวจพบใน GitHub Pull Requests โดยอัตโนมัติ โดยใช้ข้อมูล Error Monitoring ของ Sentry ผ่าน MCP Server"

**เทคนิคหลัก:**
- ประสานงาน MCP Call หลายรายการตามลำดับ
- ฝัง Domain Expertise
- จัดการ Error ที่พบบ่อยใน MCP

---

### กำหนดเกณฑ์ความสำเร็จ

คุณจะรู้ได้อย่างไรว่า Skill ทำงานได้ดี? ต่อไปนี้คือเป้าหมายโดยประมาณ — เป็นเป้าหมายที่ควรมุ่งถึง ไม่ใช่เกณฑ์ที่แน่นอน

**ตัวชี้วัดเชิงปริมาณ:**

- Skill ถูก Trigger 90% ของ Query ที่เกี่ยวข้อง
  - *วิธีวัด:* รัน Test Query 10–20 รายการที่ควร Trigger Skill แล้วดูว่าโหลดอัตโนมัติกี่ครั้ง
- ทำ Workflow เสร็จใน X Tool Calls
  - *วิธีวัด:* เปรียบเทียบงานเดียวกันโดยมีและไม่มี Skill แล้วนับ Tool Call และ Token ทั้งหมด
- ไม่มี API Call ที่ล้มเหลว 0 ครั้งต่อ Workflow
  - *วิธีวัด:* ตรวจสอบ Log ของ MCP Server ระหว่างทดสอบ ติดตาม Retry Rate และ Error Code

**ตัวชี้วัดเชิงคุณภาพ:**

- ผู้ใช้ไม่ต้อง Prompt เพิ่มเติมเกี่ยวกับขั้นตอนถัดไป
  - *วิธีประเมิน:* ระหว่างทดสอบ จดบันทึกว่าต้องแก้ไข/ชี้แจงบ่อยแค่ไหน
- Workflow เสร็จสมบูรณ์โดยไม่ต้องให้ผู้ใช้แก้ไข
  - *วิธีประเมิน:* รัน Request เดิม 3–5 ครั้ง เปรียบเทียบผลลัพธ์ว่าสม่ำเสมอหรือไม่
- ผลลัพธ์สม่ำเสมอข้ามหลาย Session
  - *วิธีประเมิน:* ผู้ใช้ใหม่สามารถทำงานสำเร็จได้ในครั้งแรกโดยใช้คำแนะนำน้อยที่สุดหรือไม่?

---

### ข้อกำหนดทางเทคนิค

#### โครงสร้างไฟล์

```
your-skill-name/
├── SKILL.md                  # จำเป็น — ไฟล์ Skill หลัก
├── scripts/                  # ไม่บังคับ — โค้ดที่รันได้
│   ├── process_data.py
│   └── validate.sh
├── references/               # ไม่บังคับ — เอกสารอ้างอิง
│   ├── api-guide.md
│   └── examples/
└── assets/                   # ไม่บังคับ — Template ฯลฯ
    └── report-template.md
```

**กฎสำคัญ:**

- ชื่อไฟล์ต้องเป็น `SKILL.md` เท่านั้น (Case-sensitive) — ไม่รับ `SKILL.MD`, `skill.md`
- ชื่อโฟลเดอร์ Skill ต้องใช้ kebab-case เท่านั้น
  - ✅ `notion-project-setup`
  - ❌ `Notion Project Setup` (มีช่องว่าง)
  - ❌ `notion_project_setup` (มี underscore)
  - ❌ `NotionProjectSetup` (มีตัวพิมพ์ใหญ่)
- **ห้ามมี `README.md`** ภายในโฟลเดอร์ Skill — เอกสารทั้งหมดต้องอยู่ใน `SKILL.md` หรือ `references/`

---

### YAML Frontmatter: ส่วนที่สำคัญที่สุด

YAML Frontmatter คือสิ่งที่ Claude ใช้ตัดสินใจว่าจะโหลด Skill หรือไม่ ทำให้ถูกต้องตั้งแต่แรก

**รูปแบบขั้นต่ำที่ต้องการ:**

```yaml
---
name: your-skill-name
description: ทำอะไร ใช้เมื่อผู้ใช้ขอ [วลีเฉพาะเจาะจง]
---
```

**รายละเอียด Field:**

**`name` (จำเป็น):**
- ใช้ kebab-case เท่านั้น
- ไม่มีช่องว่างหรือตัวพิมพ์ใหญ่
- ควรตรงกับชื่อโฟลเดอร์

**`description` (จำเป็น):**
- ต้องมีทั้ง **สิ่งที่ Skill ทำ** และ **เงื่อนไขการ Trigger (เมื่อไรควรใช้)**
- ไม่เกิน 1,024 ตัวอักษร
- ห้ามใช้ XML Tag (`<` หรือ `>`)
- ควรรวมคำที่ผู้ใช้อาจพูดถึง
- ระบุประเภทไฟล์หากเกี่ยวข้อง

**`license` (ไม่บังคับ):** MIT, Apache-2.0 ฯลฯ หากเป็น Open Source

**`compatibility` (ไม่บังคับ):** 1–500 ตัวอักษร บ่งบอก Environment ที่ต้องการ เช่น Product ที่รองรับ, System Package ที่ต้องการ

**`metadata` (ไม่บังคับ):** Key-value ใดๆ แนะนำ: `author`, `version`, `mcp-server`

```yaml
metadata:
  author: ProjectHub
  version: 1.0.0
  mcp-server: projecthub
```

**ข้อจำกัดด้านความปลอดภัย:**

ห้ามในส่วน Frontmatter:
- XML Angle Brackets (`< >`) — เพราะ Frontmatter ปรากฏใน System Prompt ของ Claude เนื้อหาที่เป็นอันตรายอาจฝัง Instruction แปลกปลอมได้
- Skill ที่มี "claude" หรือ "anthropic" ในชื่อ (สงวนไว้)

---

### การเขียน Skill ที่มีประสิทธิภาพ

#### Description Field — หัวใจของการ Trigger

ตามบล็อกวิศวกรรมของ Anthropic: *"Metadata นี้ให้ข้อมูลเพียงพอให้ Claude รู้ว่าควรใช้ Skill นี้เมื่อใด โดยไม่ต้องโหลดทั้งหมดเข้า Context"*

**โครงสร้าง:** `[สิ่งที่ทำ] + [เมื่อไรควรใช้] + [ความสามารถหลัก]`

**ตัวอย่าง Description ที่ดี:**

```yaml
# ดี — เฉพาะเจาะจงและนำไปปฏิบัติได้
description: วิเคราะห์ไฟล์ Figma Design และสร้างเอกสาร Developer Handoff 
  ใช้เมื่อผู้ใช้อัปโหลดไฟล์ .fig, ขอ "design specs", "component documentation" 
  หรือ "design-to-code handoff"

# ดี — รวม Trigger Phrase ไว้
description: จัดการ Linear Project Workflow รวมถึงการวางแผน Sprint, 
  การสร้าง Task และการติดตามสถานะ ใช้เมื่อผู้ใช้พูดถึง "sprint", 
  "Linear tasks", "project planning" หรือขอ "สร้าง tickets"

# ดี — Value Proposition ที่ชัดเจน
description: End-to-end Customer Onboarding Workflow สำหรับ PayFlow 
  จัดการการสร้างบัญชี, ตั้งค่าการชำระเงิน และการจัดการ Subscription 
  ใช้เมื่อผู้ใช้พูดว่า "onboard new customer", "set up subscription" 
  หรือ "create PayFlow account"
```

**ตัวอย่าง Description ที่ไม่ดี:**

```yaml
# คลุมเครือเกินไป
description: ช่วยเรื่องโปรเจกต์

# ไม่มี Trigger
description: สร้างระบบเอกสารหลายหน้าที่ซับซ้อน

# เป็นเทคนิคเกินไป ไม่มี User Trigger
description: Implement โมเดล Project Entity ด้วย Hierarchical Relationship
```

---

#### การเขียน Instruction หลัก

หลัง Frontmatter ให้เขียน Instruction จริงๆ ใน Markdown

**โครงสร้างที่แนะนำ:**

```markdown
---
name: your-skill
description: [คำอธิบาย]
---

# ชื่อ Skill ของคุณ

## คำสั่ง

## ขั้นตอนที่ 1: [ขั้นตอนแรก]
คำอธิบายชัดเจนว่าเกิดอะไรขึ้น

```bash
python scripts/fetch_data.py --project-id PROJECT_ID
```
ผลลัพธ์ที่คาดหวัง: [อธิบายความสำเร็จ]

## ตัวอย่าง

**ตัวอย่างที่ 1:** [สถานการณ์ทั่วไป]
ผู้ใช้พูดว่า: "ตั้งค่า Marketing Campaign ใหม่"
การดำเนินการ:
1. ดึง Campaign ที่มีอยู่ผ่าน MCP
2. สร้าง Campaign ใหม่พร้อม Parameters ที่กำหนด
ผลลัพธ์: Campaign สร้างแล้วพร้อม Confirmation Link

## การแก้ไขปัญหา

Error: [ข้อความ Error ที่พบบ่อย]
สาเหตุ: [ทำไมถึงเกิดขึ้น]
วิธีแก้: [วิธีแก้ไข]
```

---

### Best Practices ในการเขียน Instruction

**เฉพาะเจาะจงและปฏิบัติได้:**

```markdown
✅ ดี:
รัน `python scripts/validate.py --input {filename}` เพื่อตรวจสอบรูปแบบข้อมูล
หาก Validate ล้มเหลว ปัญหาที่พบบ่อยได้แก่:
- Field ที่จำเป็นหายไป (เพิ่มลงใน CSV)
- รูปแบบวันที่ไม่ถูกต้อง (ใช้ YYYY-MM-DD)

❌ ไม่ดี:
ตรวจสอบข้อมูลก่อนดำเนินการต่อ
```

**อ้างอิง Bundled Resource อย่างชัดเจน:**

```markdown
ก่อนเขียน Query ให้อ่าน `references/api-patterns.md` สำหรับ:
- คำแนะนำ Rate Limiting
- รูปแบบ Pagination
- Error Code และการจัดการ
```

**ใช้ Progressive Disclosure:**
เก็บ SKILL.md ให้มุ่งเน้น Instruction หลัก ย้ายเอกสารที่ละเอียดไปไว้ใน `references/` แล้ว Link มา

**รวม Error Handling:**

```markdown
## ปัญหาที่พบบ่อย

### MCP Connection Failed
หากเห็น "Connection refused":
1. ตรวจสอบว่า MCP Server รันอยู่: ไปที่ Settings > Extensions
2. ยืนยันว่า API Key ถูกต้อง
3. ลอง Reconnect: Settings > Extensions > [Your Service] > Reconnect
```

---

## บทที่ 3: การทดสอบและพัฒนาต่อเนื่อง

### ระดับการทดสอบ

Skill สามารถทดสอบได้หลายระดับขึ้นอยู่กับความต้องการ:

| วิธีทดสอบ | คำอธิบาย | เหมาะกับ |
|-----------|----------|----------|
| **Manual Testing ใน Claude.ai** | รัน Query โดยตรงและสังเกตพฤติกรรม รวดเร็ว ไม่ต้องตั้งค่า | การพัฒนาเบื้องต้น |
| **Scripted Testing ใน Claude Code** | ทำให้ Test Case อัตโนมัติเพื่อตรวจสอบซ้ำๆ | ทีมขนาดเล็ก-กลาง |
| **Programmatic Testing ผ่าน Skills API** | สร้าง Evaluation Suite ที่รัน Test Set ที่กำหนดไว้อย่างเป็นระบบ | Enterprise / เผยแพร่สู่สาธารณะ |

> **Pro Tip:** พัฒนางานเดียวจนกว่า Claude จะทำสำเร็จก่อน แล้วจึงนำแนวทางที่ได้ผลมาสร้างเป็น Skill วิธีนี้ใช้ประโยชน์จาก In-context Learning ของ Claude และให้สัญญาณที่รวดเร็วกว่าการทดสอบแบบกว้างๆ

---

### แนวทางทดสอบที่แนะนำ

#### 1. Triggering Tests — ทดสอบการ Trigger

**เป้าหมาย:** มั่นใจว่า Skill โหลดในเวลาที่ถูกต้อง

**Test Case:**
- ✅ Trigger กับงานที่ชัดเจน
- ✅ Trigger กับ Request ที่กล่าวต่างออกไป
- ❌ ไม่ Trigger กับหัวข้อที่ไม่เกี่ยวข้อง

**ตัวอย่าง Test Suite:**

```
ควร Trigger:
- "ช่วยตั้งค่า ProjectHub Workspace ใหม่"
- "ฉันต้องสร้างโปรเจกต์ใน ProjectHub"
- "เริ่มต้น ProjectHub Project สำหรับ Q4 Planning"

ไม่ควร Trigger:
- "อากาศที่ San Francisco เป็นอย่างไร?"
- "ช่วยเขียนโค้ด Python"
- "สร้าง Spreadsheet" (ยกเว้น ProjectHub Skill จัดการ Sheet ด้วย)
```

#### 2. Functional Tests — ทดสอบฟังก์ชัน

**เป้าหมาย:** ยืนยันว่า Skill สร้างผลลัพธ์ที่ถูกต้อง

**Test Case:**
- ✅ ผลลัพธ์ที่ถูกต้องถูกสร้างขึ้น
- ✅ API Call สำเร็จ
- ✅ Error Handling ทำงาน
- ✅ Edge Case ได้รับการรองรับ

**ตัวอย่าง:**

```
ทดสอบ: สร้างโปรเจกต์พร้อม 5 Task
กำหนด: ชื่อโปรเจกต์ "Q4 Planning" และ 5 Task Description
เมื่อ: Skill รัน Workflow
แล้ว:
  - โปรเจกต์ถูกสร้างใน ProjectHub
  - 5 Task ถูกสร้างพร้อม Property ที่ถูกต้อง
  - Task ทั้งหมดเชื่อมกับโปรเจกต์
  - ไม่มี API Error
```

#### 3. Performance Comparison — เปรียบเทียบประสิทธิภาพ

**เป้าหมาย:** พิสูจน์ว่า Skill ช่วยปรับปรุงผลลัพธ์เทียบกับ Baseline

**ตัวอย่างการเปรียบเทียบ:**

| ตัวชี้วัด | ไม่มี Skill | มี Skill |
|-----------|------------|---------|
| การป้อน Instruction | ผู้ใช้ต้องป้อนทุกครั้ง | ทำงานอัตโนมัติ |
| จำนวนรอบโต้ตอบ | 15 รอบ | 2 คำถาม |
| API Call ที่ล้มเหลว | 3 ครั้ง (ต้อง Retry) | 0 ครั้ง |
| Token ที่ใช้ | 12,000 | 6,000 |

---

### การใช้ Skill-creator

`skill-creator` skill — มีให้ใน Claude.ai ผ่าน Plugin Directory หรือดาวน์โหลดสำหรับ Claude Code — สามารถช่วยสร้างและพัฒนา Skill ได้

**การสร้าง Skill:**
- สร้าง Skill จากคำอธิบายภาษาธรรมชาติ
- สร้าง `SKILL.md` ที่มีรูปแบบถูกต้องพร้อม Frontmatter
- แนะนำ Trigger Phrase และโครงสร้าง

**การตรวจสอบ Skill:**
- ระบุปัญหาที่พบบ่อย (Description คลุมเครือ, Trigger หายไป, ปัญหาโครงสร้าง)
- ระบุความเสี่ยงที่จะ Trigger มากหรือน้อยเกินไป
- แนะนำ Test Case ตามวัตถุประสงค์ที่ระบุ

**การปรับปรุงแบบ Iterative:**
- หลังใช้ Skill แล้วพบ Edge Case หรือความล้มเหลว ให้นำตัวอย่างกลับมาที่ `skill-creator`
- ตัวอย่าง: *"ใช้ปัญหาและวิธีแก้ที่พบในบทสนทนานี้เพื่อปรับปรุงวิธีที่ Skill จัดการ [Edge Case เฉพาะ]"*

**วิธีใช้:**
```
ใช้ skill-creator skill ช่วยฉันสร้าง Skill สำหรับ [Use Case ของคุณ]
```

> **หมายเหตุ:** `skill-creator` ช่วยออกแบบและปรับปรุง Skill แต่ไม่ได้รัน Automated Test Suite หรือสร้างผลการประเมินเชิงปริมาณ

---

### การพัฒนาจาก Feedback

Skill เป็นเอกสารที่มีชีวิต วางแผนการพัฒนาต่อเนื่องตาม:

**สัญญาณ Undertriggering (Trigger น้อยเกินไป):**
- Skill ไม่โหลดเมื่อควร
- ผู้ใช้ต้องเปิดใช้งานด้วยตนเอง
- มีคำถาม Support ว่าควรใช้เมื่อไร

*วิธีแก้:* เพิ่มรายละเอียดและความละเอียดอ่อนใน Description โดยเฉพาะคำศัพท์เทคนิค

**สัญญาณ Overtriggering (Trigger มากเกินไป):**
- Skill โหลดสำหรับ Query ที่ไม่เกี่ยวข้อง
- ผู้ใช้ปิดใช้งาน
- เกิดความสับสนเรื่องวัตถุประสงค์

*วิธีแก้:* เพิ่ม Negative Trigger ระบุให้เฉพาะเจาะจงมากขึ้น

**ปัญหาการรัน (Execution Issues):**
- ผลลัพธ์ไม่สม่ำเสมอ
- API Call ล้มเหลว
- ผู้ใช้ต้องแก้ไขผลลัพธ์

*วิธีแก้:* ปรับปรุง Instruction เพิ่ม Error Handling

---

## บทที่ 4: การเผยแพร่และแบ่งปัน

### รูปแบบการเผยแพร่ปัจจุบัน (มกราคม 2026)

**วิธีที่ผู้ใช้แต่ละคนได้รับ Skill:**
1. ดาวน์โหลดโฟลเดอร์ Skill
2. บีบอัดเป็น Zip (หากจำเป็น)
3. อัปโหลดไปที่ Claude.ai ผ่าน Settings > Capabilities > Skills
4. หรือวางไว้ในไดเรกทอรี Skills ของ Claude Code

**Skill ระดับองค์กร:**
- Admin สามารถ Deploy Skill ทั่วทั้ง Workspace ได้ (เปิดตัว 18 ธ.ค. 2568)
- อัปเดตอัตโนมัติ
- การจัดการแบบรวมศูนย์

### มาตรฐานเปิด

Anthropic เผยแพร่ Agent Skills เป็นมาตรฐานเปิด เหมือน MCP พวกเขาเชื่อว่า Skill ควรพกพาข้ามเครื่องมือและแพลตฟอร์มได้ Skill เดียวกันควรทำงานได้ไม่ว่าจะใช้ Claude หรือ AI Platform อื่น

---

### การใช้ Skill ผ่าน API

สำหรับการใช้งานแบบโปรแกรม เช่น การสร้าง Application, Agent หรือ Automated Workflow ที่ใช้ Skill:

**ความสามารถหลัก:**
- Endpoint `/v1/skills` สำหรับ List และจัดการ Skill
- เพิ่ม Skill ลงใน Messages API Request ผ่าน `container.skills` Parameter
- Version Control และการจัดการผ่าน Claude Console
- ทำงานกับ Claude Agent SDK สำหรับการสร้าง Custom Agent

**เมื่อไรควรใช้ API เทียบกับ Claude.ai:**

| Use Case | Surface ที่ดีที่สุด |
|----------|-------------------|
| ผู้ใช้ปลายทางโต้ตอบกับ Skill โดยตรง | Claude.ai / Claude Code |
| ทดสอบและพัฒนาแบบ Manual | Claude.ai / Claude Code |
| Workflow แบบ Ad-hoc รายบุคคล | Claude.ai / Claude Code |
| Application ที่ใช้ Skill แบบโปรแกรม | API |
| Production Deployment ขนาดใหญ่ | API |
| Automated Pipeline และระบบ Agent | API |

> **หมายเหตุ:** Skill ใน API ต้องใช้ Code Execution Tool Beta ซึ่งมอบ Environment ที่ปลอดภัยสำหรับการรัน Skill

---

### แนวทางที่แนะนำในปัจจุบัน

1. **Host บน GitHub** ด้วย Repo สาธารณะ, README ที่ชัดเจน และตัวอย่างการใช้งานพร้อม Screenshot
2. **เอกสารใน MCP Repo ของคุณ** — เชื่อมโยง Skill จากเอกสาร MCP, อธิบายคุณค่าของการใช้ทั้งสองอย่างร่วมกัน และมี Quick-start Guide

**ตัวอย่าง Instruction การติดตั้ง:**

```markdown
# การติดตั้ง Skill ของ [Your Service]

1. ดาวน์โหลด Skill:
   - Clone repo: `git clone https://github.com/yourcompany/skills`
   - หรือดาวน์โหลด ZIP จาก Releases

2. ติดตั้งใน Claude:
   - เปิด Claude.ai > Settings > Skills
   - คลิก "Upload skill"
   - เลือกโฟลเดอร์ Skill (บีบอัดแล้ว)

3. เปิดใช้งาน Skill:
   - Toggle เปิด Skill [Your Service]
   - ตรวจสอบว่า MCP Server เชื่อมต่ออยู่

4. ทดสอบ:
   - ถาม Claude: "ตั้งค่าโปรเจกต์ใหม่ใน [Your Service]"
```

---

### การนำเสนอ Skill ของคุณ

**มุ่งเน้นที่ผลลัพธ์ ไม่ใช่ Feature:**

```
✅ ดี:
"Skill ของ ProjectHub ช่วยให้ทีมตั้งค่า Project Workspace ที่สมบูรณ์ได้ 
ในไม่กี่วินาที — รวมถึง Page, Database และ Template — 
แทนที่จะต้องเสียเวลา 30 นาทีในการตั้งค่าด้วยตนเอง"

❌ ไม่ดี:
"Skill ของ ProjectHub คือโฟลเดอร์ที่มี YAML Frontmatter 
และ Instruction ใน Markdown ที่เรียก MCP Server Tools"
```

---

## บทที่ 5: รูปแบบและการแก้ปัญหา

รูปแบบเหล่านี้เกิดจาก Skill ที่สร้างโดยผู้ใช้กลุ่มแรกและทีมภายใน ไม่ใช่ Template ที่ต้องปฏิบัติตามอย่างเคร่งครัด แต่เป็นแนวทางที่พิสูจน์แล้วว่าได้ผลดี

### การเลือกแนวทาง: Problem-first vs. Tool-first

เหมือนร้าน Home Depot คุณอาจเดินเข้าไปด้วยปัญหา ("ต้องซ่อมตู้ครัว") แล้วพนักงานชี้ไปที่เครื่องมือที่ถูกต้อง หรือคุณอาจเลือก Drill ใหม่แล้วถามว่าจะใช้งานอย่างไร

Skill ทำงานแบบเดียวกัน:
- **Problem-first:** "ฉันต้องตั้งค่า Project Workspace" → Skill ประสานงาน MCP Call ที่ถูกต้องในลำดับที่ถูกต้อง
- **Tool-first:** "ฉันมี Notion MCP เชื่อมต่ออยู่" → Skill สอน Claude ถึง Workflow และ Best Practice ที่เหมาะสมที่สุด

---

### รูปแบบที่ 1: Sequential Workflow Orchestration

**ใช้เมื่อ:** ผู้ใช้ต้องการกระบวนการหลายขั้นตอนตามลำดับที่กำหนด

```markdown
# Workflow: Onboard New Customer

## ขั้นตอนที่ 1: สร้างบัญชี
เรียก MCP Tool: `create_customer`
Parameters: name, email, company

## ขั้นตอนที่ 2: ตั้งค่าการชำระเงิน
เรียก MCP Tool: `setup_payment_method`
รอ: การยืนยัน Payment Method

## ขั้นตอนที่ 3: สร้าง Subscription
เรียก MCP Tool: `create_subscription`
Parameters: plan_id, customer_id (จากขั้นตอนที่ 1)

## ขั้นตอนที่ 4: ส่ง Welcome Email
เรียก MCP Tool: `send_email`
Template: welcome_email_template
```

**เทคนิคหลัก:** การเรียงลำดับขั้นตอนที่ชัดเจน, การพึ่งพาระหว่างขั้นตอน, การตรวจสอบในแต่ละระยะ, คำสั่ง Rollback สำหรับความล้มเหลว

---

### รูปแบบที่ 2: Multi-MCP Coordination

**ใช้เมื่อ:** Workflow ครอบคลุมหลาย Service

**ตัวอย่าง: Design-to-Development Handoff**

```markdown
## Phase 1: Design Export (Figma MCP)
1. Export Design Asset จาก Figma
2. สร้าง Design Specification
3. สร้าง Asset Manifest

## Phase 2: Asset Storage (Drive MCP)
1. สร้างโฟลเดอร์โปรเจกต์ใน Drive
2. อัปโหลด Asset ทั้งหมด
3. สร้าง Shareable Link

## Phase 3: Task Creation (Linear MCP)
1. สร้าง Development Task
2. แนบ Asset Link กับ Task
3. มอบหมายให้ Engineering Team

## Phase 4: Notification (Slack MCP)
1. โพสต์สรุป Handoff ไปที่ #engineering
2. รวม Asset Link และ Task Reference
```

**เทคนิคหลัก:** การแยก Phase ที่ชัดเจน, การส่งข้อมูลระหว่าง MCP, การตรวจสอบก่อนไปขั้นตอนถัดไป, การจัดการ Error แบบรวมศูนย์

---

### รูปแบบที่ 3: Iterative Refinement

**ใช้เมื่อ:** คุณภาพของผลลัพธ์ดีขึ้นเมื่อวนซ้ำ

**ตัวอย่าง: การสร้างรายงาน**

```markdown
## Initial Draft
1. ดึงข้อมูลผ่าน MCP
2. สร้างรายงาน Draft แรก
3. บันทึกเป็นไฟล์ชั่วคราว

## Quality Check
1. รัน Validation Script: `scripts/check_report.py`
2. ระบุปัญหา:
   - Section ที่หายไป
   - รูปแบบที่ไม่สม่ำเสมอ
   - ข้อผิดพลาดในการตรวจสอบข้อมูล

## Refinement Loop
1. แก้ไขปัญหาแต่ละข้อ
2. Regenerate Section ที่ได้รับผลกระทบ
3. Re-validate
4. ทำซ้ำจนผ่านเกณฑ์คุณภาพ

## Finalization
1. ใช้รูปแบบสุดท้าย
2. สร้างสรุป
3. บันทึกเวอร์ชันสุดท้าย
```

**เทคนิคหลัก:** เกณฑ์คุณภาพที่ชัดเจน, การปรับปรุงแบบวนซ้ำ, Script ตรวจสอบ, รู้ว่าควรหยุด Iterate เมื่อไร

---

### รูปแบบที่ 4: Context-aware Tool Selection

**ใช้เมื่อ:** ผลลัพธ์เดียวกันต้องการ Tool ต่างกันขึ้นอยู่กับบริบท

```markdown
## Smart File Storage

### Decision Tree
1. ตรวจสอบประเภทและขนาดไฟล์
2. กำหนด Storage Location ที่ดีที่สุด:
   - ไฟล์ใหญ่ (>10MB): ใช้ Cloud Storage MCP
   - เอกสารสำหรับทำงานร่วมกัน: ใช้ Notion/Docs MCP
   - ไฟล์โค้ด: ใช้ GitHub MCP
   - ไฟล์ชั่วคราว: ใช้ Local Storage

### Execute Storage
ตามการตัดสินใจ:
- เรียก MCP Tool ที่เหมาะสม
- ใช้ Metadata เฉพาะ Service
- สร้าง Access Link

### แจ้งผู้ใช้
อธิบายว่าทำไมถึงเลือก Storage นั้น
```

**เทคนิคหลัก:** เกณฑ์การตัดสินใจที่ชัดเจน, ตัวเลือกสำรอง, ความโปร่งใสในการเลือก

---

### รูปแบบที่ 5: Domain-specific Intelligence

**ใช้เมื่อ:** Skill เพิ่มความรู้เฉพาะทางนอกเหนือจากการเข้าถึง Tool

**ตัวอย่าง: Financial Compliance**

```markdown
## Payment Processing with Compliance

### Before Processing (Compliance Check)
1. ดึงรายละเอียดธุรกรรมผ่าน MCP
2. ใช้กฎ Compliance:
   - ตรวจสอบรายชื่อ Sanctions
   - ยืนยันการอนุญาตตาม Jurisdiction
   - ประเมิน Risk Level
3. บันทึกการตัดสินใจด้าน Compliance

### Processing
หาก Compliance ผ่าน:
- เรียก Payment Processing MCP Tool
- ใช้การตรวจสอบ Fraud ที่เหมาะสม
- ดำเนินธุรกรรม
มิฉะนั้น:
- ทำเครื่องหมาย Flag เพื่อตรวจสอบ
- สร้าง Compliance Case

### Audit Trail
- บันทึกการตรวจสอบ Compliance ทั้งหมด
- บันทึกการตัดสินใจในการ Process
- สร้างรายงาน Audit
```

**เทคนิคหลัก:** ฝัง Domain Expertise, Compliance ก่อนดำเนินการ, เอกสารที่ครอบคลุม, การกำกับดูแลที่ชัดเจน

---

### การแก้ปัญหา

#### Skill อัปโหลดไม่ได้

**Error:** `"Could not find SKILL.md in uploaded folder"`
- สาเหตุ: ไฟล์ไม่ได้ชื่อ `SKILL.md` พอดี
- วิธีแก้: เปลี่ยนชื่อเป็น `SKILL.md` (Case-sensitive)

**Error:** `"Invalid frontmatter"`
- สาเหตุ: ปัญหารูปแบบ YAML

```yaml
# ผิด — ไม่มี Delimiter
name: my-skill
description: ทำบางอย่าง

# ผิด — ปิด Quote ไม่ครบ
name: my-skill
description: "ทำบางอย่าง

# ถูก
---
name: my-skill
description: ทำบางอย่าง
---
```

**Error:** `"Invalid skill name"`
- สาเหตุ: ชื่อมีช่องว่างหรือตัวพิมพ์ใหญ่

```yaml
# ผิด
name: My Cool Skill

# ถูก
name: my-cool-skill
```

---

#### Skill ไม่ Trigger

**อาการ:** Skill ไม่โหลดอัตโนมัติ

**วิธีแก้:** ปรับปรุง Description Field

Checklist:
- Description คลุมเครือเกินไปหรือไม่? (`"ช่วยเรื่องโปรเจกต์"` ไม่ได้ผล)
- มี Trigger Phrase ที่ผู้ใช้จะพูดจริงๆ หรือไม่?
- ระบุประเภทไฟล์ที่เกี่ยวข้องหรือไม่?

**Debug:** ถาม Claude ว่า `"คุณจะใช้ [skill name] skill เมื่อใด?"` แล้ว Claude จะอ้าง Description กลับมา ปรับตามสิ่งที่ขาดหายไป

---

#### Skill Trigger บ่อยเกินไป

**อาการ:** Skill โหลดสำหรับ Query ที่ไม่เกี่ยวข้อง

**วิธีแก้:**

1. เพิ่ม Negative Trigger:
```yaml
description: การวิเคราะห์ข้อมูลขั้นสูงสำหรับไฟล์ CSV ใช้สำหรับ Statistical Modeling, 
  Regression, Clustering ไม่ใช้สำหรับการสำรวจข้อมูลเบื้องต้น 
  (ใช้ data-viz skill แทน)
```

2. ระบุให้เฉพาะเจาะจงมากขึ้น:
```yaml
# กว้างเกินไป
description: ประมวลผลเอกสาร

# เฉพาะเจาะจงมากขึ้น
description: ประมวลผลเอกสาร PDF ทางกฎหมายสำหรับการตรวจสอบสัญญา
```

---

#### ปัญหา MCP Connection

**อาการ:** Skill โหลดแต่ MCP Call ล้มเหลว

**Checklist:**
1. ตรวจสอบว่า MCP Server เชื่อมต่ออยู่ (Settings > Extensions > ควรแสดง "Connected")
2. ตรวจสอบ Authentication — API Key ยังใช้ได้, มี Permission/Scope ที่ถูกต้อง
3. ทดสอบ MCP อิสระ — ถาม Claude เรียก MCP โดยตรงโดยไม่มี Skill
4. ยืนยันชื่อ Tool — ชื่อ Tool ใน Skill ตรงกับชื่อใน MCP Server Documentation (Case-sensitive)

---

#### Instruction ไม่ได้รับการปฏิบัติตาม

**อาการ:** Skill โหลดแต่ Claude ไม่ทำตาม Instruction

**สาเหตุที่พบบ่อย:**

1. **Instruction ยาวเกินไป** — ทำให้กระชับ ใช้ Bullet Point และรายการตัวเลข ย้ายเอกสารอ้างอิงไฟล์แยก

2. **Instruction ถูกฝังไว้** — วาง Instruction สำคัญที่ด้านบน ใช้ Header `## Important` หรือ `## Critical` ทำซ้ำจุดสำคัญถ้าจำเป็น

3. **ภาษาคลุมเครือ:**
```markdown
# ไม่ดี
ตรวจสอบให้มั่นใจว่าทุกอย่างถูกต้องก่อนดำเนินการ

# ดี
CRITICAL: ก่อนเรียก create_project ต้องตรวจสอบ:
- ชื่อโปรเจกต์ต้องไม่ว่างเปล่า
- มีสมาชิกทีมอย่างน้อยหนึ่งคน
- วันเริ่มต้นไม่อยู่ในอดีต
```

4. **Model "ขี้เกียจ"** — เพิ่มการกระตุ้นอย่างชัดเจน:
```markdown
## หมายเหตุด้านประสิทธิภาพ
- ใช้เวลาทำให้ถูกต้องอย่างครบถ้วน
- คุณภาพสำคัญกว่าความเร็ว
- ห้ามข้ามขั้นตอน Validation
```

> **เทคนิคขั้นสูง:** สำหรับการตรวจสอบที่สำคัญ พิจารณา Bundle Script ที่ทำการตรวจสอบแบบโปรแกรม แทนการพึ่งพา Language Instruction โค้ดมีความแน่นอน ภาษาตีความได้หลายแบบ

---

#### ปัญหา Large Context

**อาการ:** Skill ช้าหรือ Response คุณภาพลดลง

**สาเหตุ:** เนื้อหาใน Skill ใหญ่เกินไป, เปิด Skill หลายตัวพร้อมกัน, โหลดเนื้อหาทั้งหมดแทน Progressive Disclosure

**วิธีแก้:**
1. ย้ายเอกสารละเอียดไปไว้ใน `references/` แล้ว Link
2. เก็บ SKILL.md ไว้ต่ำกว่า 5,000 คำ
3. ประเมินว่ามี Skill เปิดพร้อมกันมากกว่า 20–50 ตัวหรือไม่ พิจารณาปิดตัวที่ไม่จำเป็น

---

## บทที่ 6: แหล่งอ้างอิงและทรัพยากร

### เอกสาร Anthropic

**แหล่งอ้างอิงหลัก:**
- Best Practices Guide
- Skills Documentation
- API Reference
- MCP Documentation

**บทความบล็อก:**
- Introducing Agent Skills
- Engineering Blog: Equipping Agents for the Real World
- Skills Explained
- How to Create Skills for Claude
- Building Skills for Claude Code
- Improving Frontend Design through Skills

---

### เครื่องมือและ Utility

**skill-creator skill:**
- ติดตั้งไว้ใน Claude.ai และมีให้ดาวน์โหลดสำหรับ Claude Code
- สร้าง Skill จาก Description
- ตรวจสอบและให้คำแนะนำ
- ใช้งาน: *"ช่วยฉันสร้าง Skill โดยใช้ skill-creator"*

**Validation:**
- `skill-creator` ประเมิน Skill ได้
- ถาม: *"ตรวจสอบ Skill นี้และแนะนำการปรับปรุง"*

---

### การรับ Support

**สำหรับคำถามทางเทคนิค:**
- Community Forums: Claude Developers Discord

**สำหรับรายงาน Bug:**
- GitHub Issues: `anthropics/skills/issues`
- ต้องรวม: ชื่อ Skill, ข้อความ Error, ขั้นตอนที่ทำซ้ำได้

**Repository ตัวอย่าง Skill สาธารณะ:**
- GitHub: `anthropics/skills` — มี Skill ที่สร้างโดย Anthropic ให้ปรับแต่งได้

---

## ภาคผนวก A: Checklist ฉบับย่อ

### ก่อนเริ่ม

- [ ] ระบุ Use Case รูปธรรม 2–3 กรณี
- [ ] ระบุ Tool ที่จะใช้ (Built-in หรือ MCP)
- [ ] ทบทวนคู่มือนี้และตัวอย่าง Skill
- [ ] วางแผนโครงสร้างโฟลเดอร์

### ระหว่างพัฒนา

- [ ] ตั้งชื่อโฟลเดอร์เป็น kebab-case
- [ ] ไฟล์ `SKILL.md` มีอยู่ (สะกดถูกต้อง)
- [ ] YAML Frontmatter มี `---` Delimiter
- [ ] `name` Field: kebab-case ไม่มีช่องว่าง ไม่มีตัวพิมพ์ใหญ่
- [ ] `description` รวมทั้ง "ทำอะไร" และ "เมื่อไร"
- [ ] ไม่มี XML Tag (`< >`) ที่ใดเลย
- [ ] Instruction ชัดเจนและนำไปปฏิบัติได้
- [ ] รวม Error Handling
- [ ] มีตัวอย่างให้
- [ ] อ้างอิงไฟล์ Reference อย่างชัดเจน

### ก่อนอัปโหลด

- [ ] ทดสอบ Trigger กับงานที่ชัดเจน
- [ ] ทดสอบ Trigger กับ Request ที่กล่าวต่างออกไป
- [ ] ยืนยันไม่ Trigger กับหัวข้อที่ไม่เกี่ยวข้อง
- [ ] Functional Test ผ่าน
- [ ] Tool Integration ทำงาน (ถ้ามี)
- [ ] บีบอัดเป็น .zip

### หลังอัปโหลด

- [ ] ทดสอบในบทสนทนาจริง
- [ ] ติดตาม Under/Over-triggering
- [ ] เก็บรวบรวม Feedback ผู้ใช้
- [ ] พัฒนา Description และ Instruction
- [ ] อัปเดต Version ใน Metadata

---

## ภาคผนวก B: YAML Frontmatter

### Field ที่จำเป็น

```yaml
---
name: skill-name-in-kebab-case
description: ทำอะไรและเมื่อไรควรใช้ รวม Trigger Phrase เฉพาะ
---
```

### Field ทั้งหมด (รวมไม่บังคับ)

```yaml
name: skill-name
description: [คำอธิบายที่จำเป็น]
license: MIT                          # ไม่บังคับ: License สำหรับ Open Source
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"  # ไม่บังคับ: จำกัดการเข้าถึง Tool
metadata:                             # ไม่บังคับ: Field กำหนดเอง
  author: Company Name
  version: 1.0.0
  mcp-server: server-name
  category: productivity
  tags: [project-management, automation]
  documentation: https://example.com/docs
  support: support@example.com
```

### หมายเหตุด้านความปลอดภัย

**อนุญาต:**
- YAML Type มาตรฐาน (String, Number, Boolean, List, Object)
- Field Metadata กำหนดเอง
- Description ยาวได้ถึง 1,024 ตัวอักษร

**ห้าม:**
- XML Angle Brackets (`< >`) — ข้อจำกัดด้านความปลอดภัย
- การรันโค้ดใน YAML (ใช้ Safe YAML Parsing)
- Skill ที่มี Prefix "claude" หรือ "anthropic" (สงวนไว้)

---

## ภาคผนวก C: ตัวอย่าง Skill ฉบับสมบูรณ์

Repository ต่อไปนี้มี Skill ที่พร้อมใช้งานจริง และแสดง Pattern ที่กล่าวถึงในคู่มือนี้:

- **Document Skills** — สำหรับสร้าง PDF, DOCX, PPTX, XLSX
- **Example Skills** — รูปแบบ Workflow ต่างๆ
- **Partner Skills Directory** — Skill จาก Partner เช่น Asana, Atlassian, Canva, Figma, Sentry, Zapier และอื่นๆ

Repository เหล่านี้อัปเดตสม่ำเสมอและมีตัวอย่างเพิ่มเติมนอกเหนือจากที่กล่าวถึงในคู่มือนี้ Clone มาปรับแต่งสำหรับ Use Case ของคุณและใช้เป็น Template ได้เลย

---

## สรุปประเด็นสำคัญ (โดยผู้แปล)

> ส่วนนี้เป็นการสรุปและวิเคราะห์เพิ่มเติมเพื่อเสริมความเข้าใจ

### แนวคิดหลักที่ควรจำ

**1. Skill ไม่ใช่แค่ Prompt ยาว** — Skill คือระบบที่มีโครงสร้าง 3 ระดับ (YAML → SKILL.md → References) ซึ่งออกแบบมาเพื่อประหยัด Token และโหลดเฉพาะสิ่งที่จำเป็น

**2. Description คือกุญแจสำคัญ** — ถ้า Skill ไม่ Trigger หรือ Trigger บ่อยเกินไป ให้แก้ที่ Description ก่อนเสมอ เพราะนี่คือสิ่งที่ Claude ใช้ตัดสินใจทั้งหมด

**3. เริ่มจากปัญหาเดียว** — อย่าพยายามสร้าง Skill ที่รอบคอบทุกอย่างตั้งแต่แรก ให้เริ่มจากงานเดียวที่ยากที่สุด แล้วค่อยๆ ขยายออกไป

**4. MCP + Skill = ชุดสมบูรณ์** — MCP คือ "เครื่องมือ" Skill คือ "ความรู้วิธีใช้" — ต้องการทั้งสองอย่างเพื่อผลลัพธ์ที่ดีที่สุด

**5. Code ดีกว่า Language สำหรับ Validation** — เมื่อต้องการตรวจสอบเงื่อนไขสำคัญ ควรใช้ Script มากกว่าการเขียนคำสั่งเป็นข้อความ เพราะโค้ดแน่นอน ภาษาตีความได้หลายแบบ

---

### ตาราง Quick Reference สำหรับการแก้ปัญหา

| ปัญหา | สาเหตุหลัก | วิธีแก้ |
|-------|-----------|---------|
| Skill ไม่ Trigger | Description คลุมเครือ/ขาด Trigger | เพิ่ม Trigger Phrase ที่ผู้ใช้จะพูด |
| Skill Trigger มากเกินไป | Description กว้างเกินไป | เพิ่ม Negative Trigger, ระบุเฉพาะเจาะจง |
| อัปโหลดไม่ได้ | ชื่อไฟล์/โฟลเดอร์ผิด | ตรวจสอบ SKILL.md และ kebab-case |
| ไม่ทำตาม Instruction | Instruction ยาว/คลุมเครือ | กระชับ, ใส่ Critical ที่หัว, ใช้โค้ด |
| MCP ล้มเหลว | Connection/Authentication | ตรวจสอบ Settings, API Key, Tool Name |
| Response ช้า | Context ใหญ่เกินไป | ย้าย Docs ไป references/, ลด Skill ที่เปิด |

---

### เส้นทางการเรียนรู้ที่แนะนำ

1. **เริ่มต้น:** อ่านบทที่ 1–2 สร้าง Skill แรกโดยใช้ `skill-creator`
2. **พัฒนา:** ใช้ Checklist ในภาคผนวก A ตรวจสอบ Skill ของคุณ
3. **ทดสอบ:** ทำตามแนวทางในบทที่ 3 โดยเริ่มจาก Manual Testing
4. **เผยแพร่:** Host บน GitHub ตามแนวทางบทที่ 4
5. **ปรับปรุง:** ใช้สัญญาณ Over/Under-triggering เพื่อพัฒนาต่อเนื่อง

---

### แหล่งอ้างอิงเพิ่มเติม

- [Anthropic Skills Documentation](https://docs.anthropic.com)
- [GitHub: anthropics/skills](https://github.com/anthropics/skills)
- [Claude Developers Discord](https://discord.gg/claude)
- [Claude Agent SDK](https://docs.anthropic.com/sdk)

---

*เอกสารนี้แปลจาก "The Complete Guide to Building Skills for Claude" โดย Anthropic*
*แปลและเรียบเรียงสำหรับ อาจารย์สามิตร — ฉบับภาษาไทย*
