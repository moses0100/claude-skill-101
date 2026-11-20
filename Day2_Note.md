# Claude Skills 101 — with Cowork and Code - Day 2 Notes

**หลักสูตร: สร้าง AI Skills แรกของคุณใน 3 วัน (Cowork and Code)**
**วันที่ 2: Claude Cowork กับ Skills เต็มรูปแบบ**
วันที่: 2 พฤษภาคม 2569 | เวลา 20:30–23:30 น.

---

## 🎯 วัตถุประสงค์การเรียนรู้ประจำวัน

เมื่อจบการอบรมผู้เรียนจะสามารถ:

1. สร้าง Content Strategist AI ที่รู้จักแบรนด์ขององค์กรตัวเองได้ด้วย SKILL.md
2. เชื่อมต่อ Connectors (Gmail, Google Drive, Slack) เข้ากับ Skills บน Claude Cowork ได้
3. สร้าง Workflow อัตโนมัติโดยใช้ Schedule และ Dispatch ได้
4. แปลงงานที่ทำซ้ำในองค์กรตัวเองให้เป็น Skill ที่ใช้งานได้จริง
5. ปรับปรุง Skill ให้รับมือกับ edge cases และ error ได้อย่างฉลาด
6. แชร์ Skill ให้ทีม และค้นหา Skill จากแหล่งต่าง ๆ ได้

---

## 📚 Session 1: Content Strategist AI — Workshop Hands-on (20:30–21:30)

### 1.1 ปัญหา & แนวคิด: Claude ทั่วไป vs Claude รู้จักแบรนด์คุณ

#### ทำไม Claude ทั่วไปถึงไม่ตอบโจทย์ Content Marketing?

เมื่อคุณถาม Claude ทั่วไปว่า "ช่วยเขียนโพสต์ Facebook ให้หน่อย" — Claude จะตอบในแบบกลาง ๆ ที่ใช้ได้กับทุกองค์กร แต่ไม่ตรงกับใครเลย

**เปรียบเทียบผลลัพธ์จริง:**

| | ❌ Claude ทั่วไป | ✅ Claude + SKILL.md |
|---|---|---|
| **คำตอบตัวอย่าง** | "ควรสร้าง Content ที่มีคุณภาพและสม่ำเสมอ เพื่อสร้าง Engagement กับกลุ่มเป้าหมาย" | "สำหรับ CTO กลุ่มเป้าหมายของ TechVision แนะนำโพสต์ LinkedIn เรื่อง ROI ของ Cloud Migration พร้อมตัวเลขจริงจากลูกค้า" |
| **ผลลัพธ์** | ใช้ได้กับทุกองค์กร ไม่ตรงกับใครเลย | ตอบตรงแบรนด์ ตรง Audience ใช้ได้จริงทันที |

**แนวคิดหลัก:** SKILL.md คือ "DNA ขององค์กร" ที่เราสอนให้ Claude จดจำ — เมื่อ Claude รู้จักแบรนด์ กลุ่มเป้าหมาย Tone of Voice และแพลตฟอร์มของคุณแล้ว ทุกคำตอบจะตรงเป้าและพร้อมใช้งานจริง

---

### 1.2 โครงสร้าง SKILL.md สำหรับ Content Strategist AI

#### ส่วนประกอบที่ขาดไม่ได้

SKILL.md สำหรับ Content Marketing ต้องระบุ 5 ข้อนี้ให้ครบ:

```markdown
## 1. ข้อมูลองค์กร
- ชื่อและประเภทธุรกิจ
- ขนาดองค์กร และลูกค้าหลัก

## 2. กลุ่มเป้าหมาย (Target Audience)
- Persona: อายุ ตำแหน่ง อำนาจตัดสินใจ
- Pain Points ที่ต้องการแก้

## 3. Tone of Voice
- น้ำเสียง: ทางการ / กึ่งทางการ / สบาย ๆ
- สิ่งที่ต้องหลีกเลี่ยง
- สิ่งที่ต้องเน้น

## 4. แพลตฟอร์มหลัก
- ความถี่การโพสต์แต่ละแพลตฟอร์ม
- ประเภท Content ที่เหมาะ

## 5. หัวข้อที่ต้องการสื่อสาร
- Pillar Content หลัก
- หัวข้อที่ห้ามพูดถึง
```

#### ตัวอย่าง SKILL.md ฉบับเต็ม — บริษัท TechVision

```markdown
# SKILL.md — Content Strategist AI
# บริษัท TechVision จำกัด

## 1. ข้อมูลองค์กร
ชื่อ: บริษัท TechVision จำกัด
ประเภท: บริษัท IT Solutions ให้บริการ Cloud & Cybersecurity
ขนาด: พนักงาน 120 คน | ลูกค้าหลัก: องค์กรขนาดกลาง-ใหญ่

## 2. กลุ่มเป้าหมาย
- CTO / IT Manager ในองค์กรขนาดกลาง (200-2000 คน)
- อายุ 30-50 ปี มีอำนาจตัดสินใจซื้อ
- Pain Point: ระบบ Legacy, ความปลอดภัยข้อมูล, ค่าใช้จ่าย IT สูง

## 3. Tone of Voice
- น้ำเสียง: มืออาชีพ แต่เข้าใจง่าย ไม่ใช้ศัพท์เทคนิคมากเกินไป
- หลีกเลี่ยง: ภาษาเชิงขาย (pushy), คำสัญญาเกินจริง
- เน้น: ความน่าเชื่อถือ, ตัวเลข ROI, Case Study จริง

## 4. แพลตฟอร์มหลัก
- LinkedIn: บทความและ Thought Leadership (2 ครั้ง/สัปดาห์)
- Facebook: โพสต์บริษัทและข่าวสาร (3 ครั้ง/สัปดาห์)
- Line Official: แจ้งข่าวโปรโมชั่นและ Event (2 ครั้ง/เดือน)

## 5. หัวข้อที่ต้องการสื่อสาร
- Cloud Migration: ลดต้นทุน IT ด้วย Cloud
- Cybersecurity: ปกป้องข้อมูลองค์กรจากภัยคุกคาม
- Success Story: ลูกค้าที่ประสบความสำเร็จจากบริการของเรา
- Insight: บทความให้ความรู้ด้าน IT ฟรี
```

---

### 1.3 วิธี Save SKILL.md ใน Claude — 2 วิธีหลัก

#### วิธีที่ 1: Project Instructions (เหมาะสำหรับเริ่มต้น)

1. เปิด Claude.ai → คลิก **Projects** → สร้าง Project ใหม่ (เช่น "Content Marketing AI")
2. คลิก **"Set project instructions"** ที่หน้า Project
3. Copy เนื้อหา SKILL.md ทั้งหมด → Paste ลงในช่อง text box
4. Save → ทุก Chat ใหม่ใน Project นี้จะจำข้อมูลองค์กรทันที

**ข้อดี:** ง่าย ทำได้ทันที ไม่ต้องแยกไฟล์
**ข้อจำกัด:** ใช้ได้เฉพาะ Project นี้ ไม่สามารถ Share ได้

#### วิธีที่ 2: Claude Skills (แนะนำสำหรับใช้งานระยะยาว) ⭐

1. ไปที่ **Customize → Skills** (claude.ai/customize/skills)
2. คลิก **"Create skill"** หรือ **"Upload a skill"**
3. อัปโหลดไฟล์ `SKILL.md` หรือ copy เนื้อหาลงไป
4. บันทึก → เป็น **Personal Skill** ของคุณ ทุก Chat ใหม่ใช้ได้เลย

**ข้อดี:** ใช้ได้ทั่วทั้ง Claude, แก้ไขง่าย, Share ได้
**ข้อจำกัด:** ต้องติดตั้งครั้งแรก (แต่ครั้งเดียว)

**เปรียบเทียบ 2 วิธี:**

| | วิธี 1: Project Instructions | วิธี 2: Claude Skills |
|---|---|---|
| **ที่อยู่** | ใน Project นี้เท่านั้น | ทั่วทั้ง Claude ของคุณ |
| **ประเภท** | ข้อความ text ใน Project | ไฟล์ที่แท้จริง (SKILL.md) |
| **แก้ไข** | Edit ในหน้า Project | ไปที่ Customize > Skills |
| **Share** | ไม่สามารถ Share ได้ | สามารถ Share ให้คนอื่นได้ |
| **เหมาะสำหรับ** | Workshop, ลองใหม่, เชื่อมกับโปรเจกต์เฉพาะ | ใช้งานจริงทุกวัน ติดตั้งครั้งเดียว |

---

### 1.4 Prompt Templates สำหรับ Content Strategist AI

#### Prompt 0: ให้ Claude สัมภาษณ์และสร้าง SKILL.md ให้คุณ

วิธีที่ง่ายที่สุดสำหรับผู้เริ่มต้นคือบอก Claude ให้สัมภาษณ์คุณก่อน:

```
คุณคือ Content Strategist AI ของฉัน
กรุณาสัมภาษณ์ฉันเพื่อเข้าใจแบรนด์ขององค์กร
โดยถามทีละข้อ แบบมีตัวเลือก A B C D

ครอบคลุม 5 หัวข้อนี้:
1. ชื่อและประเภทองค์กร
2. กลุ่มเป้าหมายและ Pain Point
3. Tone of Voice ของแบรนด์
4. แพลตฟอร์มที่ใช้หลัก
5. หัวข้อที่ต้องการสื่อสาร

เมื่อถามครบแล้ว ให้เขียน SKILL.md
ไฟล์ต้องเริ่มต้นด้วย YAML frontmatter ที่ถูกต้อง
ในรูปแบบที่พร้อม Copy ไปใช้ได้เลย
```

**หมายเหตุ:** วิธีนี้เหมาะสำหรับผู้ที่ยังไม่แน่ใจว่าต้องใส่อะไรใน SKILL.md บอก Claude ให้ถามและสร้างให้เลย
**ข้อดี:** ง่ายมาก ไม่ต้องคิดเอง แค่ตอบคำถาม
**ข้อจำกัด:** อาจได้ข้อมูลที่ไม่ครบถ้วน ต้องตรวจสอบและแก้ไขหลังจากนั้น

**ข้อควรระวัง:** หาก Claude สร้าง SKILL.md ที่ไม่ถูกต้อง (เช่น ขาด YAML frontmatter) ให้บอกให้แก้ไขทันที:
```
"ขอให้แก้ไข SKILL.md ให้เริ่มต้นด้วย YAML frontmatter ที่ถูกต้องด้วยครับ เช่น:
---
name: content-strategist
description: >
  Content Strategist AI ที่รู้จักแบรนด์ของเรา
  Use this skill when the user mentions "เขียนโพสต์", "สร้าง Content Calendar", "วิเคราะห์ Content"
---
```

#### Prompt 1: เขียนโพสต์ Social Media

```
เขียนโพสต์ [Facebook / LinkedIn / Line]
สำหรับหัวข้อ: [ระบุหัวข้อหรือกิจกรรม]

ให้ตรงกับ:
- Tone of Voice ขององค์กรเรา
- กลุ่มเป้าหมายที่เราตั้งไว้
- ความยาวที่เหมาะกับแพลตฟอร์มนั้น

พร้อม:
- Hook ประโยคแรกที่ดึงดูดความสนใจ
- Call-to-Action ที่ชัดเจน
- Hashtag ที่เกี่ยวข้อง 5 อัน
```

#### Prompt 2: สร้าง Content Calendar รายเดือน

```
สร้าง Content Calendar สำหรับเดือน [ระบุเดือน]

แบ่งเป็น 4 สัปดาห์ แต่ละสัปดาห์มี 3 โพสต์
ในรูปแบบตาราง ระบุ:
- สัปดาห์ที่ / วันที่แนะนำ
- แพลตฟอร์ม (Facebook / LinkedIn / Line)
- หัวข้อโพสต์
- Format (รูปภาพ / วิดีโอ / Carousel / Article)
- เป้าหมายโพสต์ (Awareness / Engagement / Conversion)
```

#### Prompt 3: วิเคราะห์ Content ประจำเดือน

```
ช่วยวิเคราะห์ Content เดือนที่ผ่านมา:

ข้อมูลที่มี:
- โพสต์ที่ Engagement สูงสุด: [ระบุ]
- โพสต์ที่ Engagement ต่ำสุด: [ระบุ]
- แพลตฟอร์มที่ดีที่สุด: [ระบุ]
- หัวข้อที่ผู้ชมตอบสนองดี: [ระบุ]

วิเคราะห์และแนะนำ:
1. Pattern ของ Content ที่ได้ผลกับองค์กรเรา
2. หัวข้อที่ควรเพิ่มเดือนหน้า
3. รูปแบบที่ควรลดหรือปรับ
```

---

### 1.5 Workshop Hands-on: สร้าง Content AI ของตัวเอง (3 Steps)

**Step 1: สัมภาษณ์ตัวเอง (หรือใช้ Prompt 0)**

กรอก Template นี้สำหรับองค์กรของคุณ:

```
ชื่อองค์กร: _______________
ประเภทธุรกิจ: _______________
กลุ่มเป้าหมาย: _______________
Pain Point ของลูกค้า: _______________
Tone of Voice: _______________
แพลตฟอร์มหลัก: _______________
หัวข้อ Content หลัก: _______________
```

**Step 2: สร้าง SKILL.md**

นำข้อมูลจาก Step 1 มาสร้าง SKILL.md แล้ว Save ผ่านวิธีที่ 1 หรือ 2

**Step 3: ทดสอบ Prompt Templates**

```
ทดสอบ 1: เขียนโพสต์ Facebook เรื่อง [หัวข้อล่าสุดขององค์กร]
ทดสอบ 2: สร้าง Content Calendar เดือนนี้
ทดสอบ 3: วิเคราะห์โพสต์ที่ผ่านมา (ถ้ามีข้อมูล)
```

> ✅ **Checklist หลัง Session 1:**
> - [ ] SKILL.md ขององค์กรถูก Save ไว้ใน Claude แล้ว (วิธี 1 หรือ 2)
> - [ ] ทดสอบ Prompt 1 (เขียนโพสต์) และได้ผลลัพธ์ที่ตรงกับแบรนด์
> - [ ] ทดสอบ Prompt 2 (Content Calendar) และได้ตารางที่ใช้งานได้จริง

---

> ☕ **พักเบรก 21:30–21:45**

---

## 📚 Session 2: Claude Cowork Deep Dive — Connectors & Workflow (21:45–22:30)

### 2.1 Connectors คืออะไร? วิธีเชื่อมต่อ

#### ทำความเข้าใจ Connector

**Connector** คือ "สะพานเชื่อม" ระหว่าง Claude กับบริการภายนอก ทำให้ Claude อ่าน/เขียนข้อมูลจากแอปที่คุณใช้งานอยู่ได้จริง เปรียบเสมือน Claude มี "มือ" ที่เข้าถึงเครื่องมือต่าง ๆ ในชีวิตประจำวันของคุณ

**Connectors ที่ใช้ได้บน Claude Cowork:**

| Connector           | ทำอะไรได้                      | ตัวอย่างการใช้งานจริง                  |
| ------------------- | ------------------------------ | -------------------------------------- |
| **Gmail**           | อ่าน / ส่ง / ค้นหาอีเมล       | สรุปอีเมลที่ยังไม่ได้อ่านทุกเช้า      |
| **Google Drive**    | อ่าน / สร้าง / ค้นหาไฟล์      | ค้นหาเอกสารโปรเจกต์และสร้างรายงาน    |
| **Slack**           | อ่าน / ส่งข้อความ             | สรุปข้อความสำคัญใน channel ทีม        |
| **Figma**           | ดูดีไซน์ / component           | ดึงข้อมูลดีไซน์มาสร้างโค้ด HTML/CSS   |
| **Google Calendar** | ดูตาราง / เพิ่มนัดหมาย         | สรุปตารางวันนี้และสร้าง agenda         |

#### วิธีเชื่อมต่อ Connector

**ขั้นตอน:**

```
1. เปิด Claude Desktop App
2. ไปที่ Settings → Connectors
3. เลือก Connector ที่ต้องการ (เช่น Gmail)
4. คลิก "Connect" → Authorize ผ่านบัญชี Google
5. เมื่อเชื่อมต่อสำเร็จ Claude จะเข้าถึงบัญชีนั้นได้ทันที
```

**ข้อควรระวัง:**
- แต่ละ Connector ต้อง authorize แยกกัน
- Claude จะเข้าถึงเฉพาะข้อมูลที่คุณให้สิทธิ์ไว้
- สามารถ revoke สิทธิ์ได้ตลอดเวลาใน Settings

#### ความแตกต่างเมื่อมี Connector

**ก่อนมี Connector:**
```
คุณ: "สรุปอีเมลวันนี้ให้หน่อย"
Claude: "ช่วยวาง/paste เนื้อหาอีเมลมาให้ด้วยครับ"
```

**หลังมี Gmail Connector:**
```
คุณ: "สรุปอีเมลที่ยังไม่ได้อ่านวันนี้"
Claude: [ดึงอีเมลจาก Gmail จริง] → สรุปให้ทันที โดยไม่ต้อง paste
```

---

### 2.2 Skill + Connector Workshop

#### ตัวอย่างที่ 1: Skill + Gmail Connector — Daily Email Digest

สร้าง Skill ที่ดึงข้อมูลอีเมลจริงจาก Gmail มาสรุปให้ทุกวัน:

```markdown
---
name: daily-email-digest
description: >
  สรุปอีเมลที่ยังไม่ได้อ่านประจำวัน พร้อม action items
  Use this skill when the user mentions "สรุปอีเมล",
  "email วันนี้", "daily digest", "อีเมลที่ยังไม่ได้อ่าน"
---

# Daily Email Digest

## Overview

Skill นี้ดึงข้อมูลจาก Gmail Connector สรุปอีเมลที่ยังไม่ได้อ่านของวันนี้
จัดลำดับความสำคัญ และระบุ action items ที่ต้องตอบกลับ

## Instructions

1. ใช้ Gmail Connector ค้นหาอีเมลที่ยังไม่ได้อ่านของวันนี้
2. กรองอีเมลที่สำคัญออก (ไม่รวม spam, newsletter, auto-reply)
3. สรุปแต่ละฉบับเป็น 1-2 ประโยคสั้น ๆ
4. ระบุ action items ที่ต้องตอบกลับหรือดำเนินการ
5. จัดลำดับความสำคัญ: สูง / กลาง / ต่ำ
6. สร้างรายงานสรุปในรูปแบบที่อ่านง่าย

## Output Format

📧 Daily Email Digest — [วันที่]

รวม: X ฉบับที่ยังไม่อ่าน | ต้องดำเนินการ: Y ฉบับ

ความสำคัญสูง:
- [ชื่อผู้ส่ง]: [หัวข้อ] → Action: [...]

ความสำคัญกลาง:
- [ชื่อผู้ส่ง]: [หัวข้อ] → [สรุปสั้น]

ความสำคัญต่ำ / FYI:
- [รายการ...]

## Constraints
- ไม่เปิดเผยเนื้อหาส่วนตัวหรือข้อมูลความลับในรายงาน
- ถ้าไม่พบอีเมลใหม่ให้แจ้ง "ไม่มีอีเมลใหม่วันนี้"
- ไม่ reply หรือแก้ไขอีเมลโดยไม่ได้รับคำสั่ง
```

#### ตัวอย่างที่ 2: Skill + Google Drive — สร้างรายงานจากไฟล์ใน Drive

```markdown
---
name: drive-report-generator
description: >
  ค้นหาไฟล์ใน Google Drive และสร้างรายงานสรุป
  Use this skill when the user mentions "สรุปไฟล์ใน Drive",
  "รายงานจาก Drive", "ค้นหาเอกสาร Google Drive"
---

# Drive Report Generator

## Instructions

1. รับชื่อโฟลเดอร์หรือคีย์เวิร์ดจากผู้ใช้
2. ใช้ Google Drive Connector ค้นหาไฟล์ที่เกี่ยวข้อง
3. อ่านเนื้อหาไฟล์ที่ค้นพบ
4. วิเคราะห์และสรุปเนื้อหาสำคัญ
5. สร้างรายงานใหม่เป็นไฟล์ Word หรือ PDF
6. บันทึกรายงานกลับไปที่ Google Drive (ถ้าต้องการ)

## Constraints
- ถ้าไม่พบไฟล์ ให้แจ้งผู้ใช้และถามชื่อโฟลเดอร์อื่น
- ไม่ลบหรือแก้ไขไฟล์ต้นฉบับโดยไม่ได้รับอนุญาต
```

#### Workshop: สร้าง Skill ที่ใช้ Connector จริง

```
โจทย์: เลือก 1 Connector แล้วสร้าง Skill ที่ใช้ประโยชน์จริงในงานของคุณ

ตัวอย่างที่เลือกได้:
A) Gmail: สรุปอีเมลลูกค้าที่รอตอบกลับ
B) Google Drive: ค้นหาเอกสารโปรเจกต์ล่าสุดและสรุป
C) Slack: สรุป mentions และ DMs ที่ยังไม่ตอบ
D) Google Calendar: สร้าง agenda สำหรับการประชุมวันนี้
E) คิดเอง: Workflow ที่ทำซ้ำทุกวันในงานของคุณ
```

#### Workshop Hands-on สร้าง Skills ที่เชื่อม Google Drive ใน Claude Cowork

##### Step 1: สัมภาษณ์ตัวเองเพื่อเข้าใจความต้องการ

```
ฉันต้องการให้คุณเป็นผู้ช่วยสรุปและดึงข้อมูล slip และใบสำคัญจ่ายเงินต่างๆ 
จาก google drive ของฉัน อยากให้คุณ สัมภาษณ์ฉันเพื่อเข้าใจความต้องการทั้งหมดของฉัน
โดยถามทีละข้อ แบบมีตัวเลือก A B C D เพื่อเขียน SKILL.md ที่ถูกต้องและพร้อมใช้งานได้เลย
```

##### Step 2: ให้ Claude สร้าง SKILL.md ที่พร้อมใช้งานได้จริง
**หมายเหตุ:** หาก Claude สร้าง SKILL.md ที่ไม่ถูกต้อง (เช่น ขาด YAML frontmatter) ให้บอกให้แก้ไขทันที:
```
จากทุกอย่างที่เราคุยกันมา ช่วยเขียน SKILL.md ไฟล์ต้องเริ่มต้นด้วย YAML frontmatter ที่ถูกต้องด้วยครับ เช่น:
---
name: gdrive-slip-extractor
description: >
  ค้นหาไฟล์ใน Google Drive และสร้างรายงานสรุป
  Use this skill when the user mentions "สรุปไฟล์ใน Drive",
  "รายงานจาก Drive", "ค้นหาเอกสาร Google Drive"
---
```

##### Step 3: ทดสอบ Skill ที่สร้างขึ้น

```
/gdrive-slip-extractor สรุปสลิปจาก Folder "Finance/Slip"
```

---

### 2.3 Schedule & Dispatch — AI ทำงานอัตโนมัติ

#### Schedule: ตั้งนาฬิกาปลุกให้ AI ทำงาน

**Schedule** คือระบบที่ให้ Skill ทำงานตามเวลาที่กำหนด โดยไม่ต้องสั่งทุกครั้ง เหมือน cron job ของ AI

**ตัวอย่าง Use Cases จริง:**

| เวลา Schedule             | Skill ที่ทำงาน                    | ผลลัพธ์                           |
| ------------------------- | --------------------------------- | --------------------------------- |
| ทุกวัน 08:00 น.           | daily-email-digest                | รายงานอีเมลส่งเข้ากล่องขาเข้า    |
| ทุกวันจันทร์ 09:00 น.     | weekly-report                     | รายงานสรุปสัปดาห์ใหม่             |
| ทุกวันที่ 1 ของเดือน      | monthly-analytics-summary         | รายงาน Analytics ประจำเดือน       |
| ทุก 2 ชั่วโมง             | slack-mentions-checker            | ตรวจสอบ Slack mentions ที่ไม่ตอบ  |

**วิธีสร้าง Schedule บน Cowork:**

วิธีที่ 1 — บอก Claude ตรง ๆ:
```
"ตั้ง schedule ให้สรุปอีเมลทุกเช้า 8 โมง"
```

วิธีที่ 2 — ใช้ Skill "schedule":
```
สร้าง scheduled task:
- ทำงาน: ทุกวันจันทร์ เวลา 09:00 น.
- งาน: สร้าง weekly report จากไฟล์ใน Google Drive โฟลเดอร์ "Reports"
- ส่งผลลัพธ์: สรุปใน Slack channel #weekly-report
```

#### Dispatch: ตั้งกับดักให้ AI ทำงานเมื่อมีเหตุการณ์

**Dispatch** คือระบบ trigger-action — "เมื่อเกิดเหตุการณ์ X ให้ทำ Y อัตโนมัติ"

**ตัวอย่าง Dispatch ที่ใช้งานได้จริง:**

```
Dispatch Rule 1:
เมื่อ: ได้รับอีเมลจาก domain @client.com
ให้ทำ: สรุปเนื้อหา → ส่ง notification ใน Slack #urgent

Dispatch Rule 2:
เมื่อ: มีไฟล์ใหม่ใน Google Drive โฟลเดอร์ "Invoices"
ให้ทำ: อ่านใบแจ้งหนี้ → สรุปยอด → บันทึกลง Excel

Dispatch Rule 3:
เมื่อ: มี mention ใน Slack #support
ให้ทำ: ตรวจสอบ ticket และสร้าง draft reply
```

**วิธีสร้าง Dispatch:**

```
"ตั้ง dispatch rule: เมื่อได้รับอีเมลหัวข้อมี 'URGENT'
ให้สรุปเนื้อหาแล้วส่งแจ้งเตือนใน Slack channel #alerts"
```

**เปรียบเทียบ Schedule vs Dispatch:**

| | Schedule | Dispatch |
|---|---|---|
| **ทริกเกอร์** | เวลา (time-based) | เหตุการณ์ (event-based) |
| **เปรียบเทียบ** | นาฬิกาปลุก | กับดัก/เซ็นเซอร์ |
| **ตัวอย่าง** | ทุกเช้า 8 โมง สรุปอีเมล | เมื่อมีอีเมลจาก VIP client |
| **เหมาะกับ** | งานรายวัน/รายสัปดาห์ | งาน real-time ที่ต้องตอบสนองเร็ว |

**💡 เคล็ดลับ:**

> Schedule + Dispatch ใช้ร่วมกัน = AI Workflow ที่สมบูรณ์ ไม่ต้องสั่งงาน AI เองเลย งานบางอย่างเกิดขึ้นตามเวลา บางอย่างตอบสนองต่อเหตุการณ์จริง

---

## 📚 Session 3: Advanced Skills + แชร์ Skill + สรุปวันที่ 2 (22:30–23:30)

### 3.1 สร้าง Skill จากงานจริงของผู้เรียน

#### วิธีที่ 1: Turn into Skill (วิธีที่ง่ายที่สุด)

หลังจากทำงานร่วมกับ Claude แล้วได้ผลลัพธ์ที่พอใจ ให้บอก Claude ว่า:

```
"ช่วย turn สิ่งที่เราเพิ่งทำเป็น Skill ได้ไหม?"
```

Claude จะวิเคราะห์บทสนทนา และสร้าง SKILL.md ให้อัตโนมัติ

**ตัวอย่างสถานการณ์จริง:**

```
คุณ: "สรุปรายงานประชุมนี้เป็น bullet points ภาษาไทย
       แยก action items ออกมา พร้อมระบุผู้รับผิดชอบ"
Claude: [สรุปให้สำเร็จ]
คุณ: "ดีมาก! ช่วย turn สิ่งที่เราเพิ่งทำเป็น Skill ได้ไหม?"
Claude: [สร้าง Skill "meeting-summary" ให้อัตโนมัติ]
```

#### วิธีที่ 2: Workflow to Skill (วิเคราะห์ขั้นตอนเอง)

ใช้ Framework 5W1H วิเคราะห์งานก่อน แล้วแปลงเป็น Skill:

| คำถาม                          | ตัวอย่างคำตอบ                    |
| ------------------------------ | -------------------------------- |
| **What** — ทำอะไร?             | สรุปรายงานประชุมทีม              |
| **When** — ทำเมื่อไหร่?        | ทุกวันจันทร์หลังประชุม 10 โมง   |
| **Who** — ใครเป็นผู้ใช้?       | ตัวเอง + ทีมทั้งหมด              |
| **Where** — ทำบนแพลตฟอร์มไหน?  | Claude Cowork                    |
| **Why** — ทำไมต้องทำ?          | ประหยัดเวลา 20 นาที/ครั้ง        |
| **How** — ทำอย่างไร?           | อ่าน notes → สรุป → ระบุ action  |

**Workshop: แปลงงานจริงเป็น Skill**

```
โจทย์: เลือกงานที่คุณทำซ้ำมากกว่า 2 ครั้ง/สัปดาห์
       แล้วแปลงเป็น Skill ในเวลา 10 นาที

ตัวอย่างที่เลือกได้:
A) สรุปรายงานการประชุม
B) เขียนอีเมลตอบลูกค้าตามแบบฟอร์ม
C) สร้างใบเสนอราคา
D) วิเคราะห์ข้อมูลยอดขายประจำสัปดาห์
E) สร้างโพสต์โซเชียลมีเดียประจำวัน
F) คิดเอง — งานอะไรก็ได้ที่ทำซ้ำบ่อย
```

---

### 3.2 Skill ขั้นสูง: Error Handling & Edge Cases

#### ทำไม Skill ถึงต้องจัดการ Edge Case?

Skill เวอร์ชันแรกมักจะทำงานได้กับ "กรณีปกติ" แต่จะล้มเหลวเมื่อพบ:
- Input ไม่สมบูรณ์ (ขาดข้อมูลสำคัญ)
- Input ผิดรูปแบบที่คาดไว้
- ผู้ใช้ใช้ภาษาอื่น
- ข้อมูลที่ขัดแย้งกัน
- Connector ที่ดึงข้อมูลไม่ได้

#### เทคนิค 5 อย่างสำหรับ Skill ที่ฉลาดขึ้น

**เทคนิคที่ 1: ถามก่อนทำ — เมื่อ Input ไม่ครบ**

```markdown
## Instructions

1. ตรวจสอบว่าผู้ใช้ให้ข้อมูลครบหรือไม่:
   - ถ้าไม่มีหัวข้อ → ถามว่า "คุณต้องการโพสต์เรื่องอะไร?"
   - ถ้าไม่ระบุแพลตฟอร์ม → ถามว่า "โพสต์บน Facebook, Instagram หรือ Twitter?"
   - ถ้าไม่มีกลุ่มเป้าหมาย → ถามว่า "ต้องการสื่อสารกับใคร?"
2. เมื่อได้ข้อมูลครบแล้วจึงเริ่มสร้างโพสต์
```

**เทคนิคที่ 2: ตรวจสอบ Constraint — แจ้งเมื่อทำไม่ได้**

```markdown
## Instructions

หากผู้ใช้ขอสิ่งที่ขัดกับ Constraint ให้แจ้งอย่างสุภาพ:
- "ขอโทษครับ Twitter จำกัด 280 ตัวอักษร
  ผมสร้างโพสต์สั้นให้แทนได้ไหมครับ?"
- "เนื้อหานี้อาจขัดกับ Community Guidelines ของ Facebook
  ผมปรับให้ปลอดภัยขึ้นได้ครับ"
```

**เทคนิคที่ 3: Fallback — มีแผนสำรองเสมอ**

```markdown
## Instructions

ถ้า Connector ไม่สามารถดึงข้อมูลได้:
- แจ้งผู้ใช้ว่าเกิดอะไรขึ้น (เช่น "Gmail Connector ไม่ตอบสนอง")
- ขอให้ผู้ใช้วาง/paste ข้อมูลมาแทน
- ไม่หยุดทำงานโดยไม่แจ้ง
```

**เทคนิคที่ 4: ยืนยันก่อน Action สำคัญ**

```markdown
## Instructions

ก่อนส่งอีเมล / โพสต์ / แก้ไขไฟล์ ให้แสดงผลลัพธ์
ให้ผู้ใช้ตรวจสอบก่อนเสมอ:
"นี่คือโพสต์ที่สร้างไว้ — ต้องการแก้ไขอะไรก่อน Post ไหมครับ?"
```

**เทคนิคที่ 5: Edge Cases Section**

```markdown
## Edge Cases

- ถ้าผู้ใช้พิมพ์ภาษาอังกฤษ → ตอบเป็นภาษาอังกฤษ
- ถ้า Connector ว่างเปล่า → แจ้ง "ไม่พบข้อมูล กรุณาตรวจสอบ Connector"
- ถ้า Output ยาวเกินไป → แบ่งเป็นหลายส่วน พร้อมสรุปหัวข้อ
- ถ้าผู้ใช้เปลี่ยนใจกลางคัน → หยุดและถามว่าต้องการอะไรแทน
```

**ตารางการแก้ปัญหา Skill ที่พบบ่อย:**

| ปัญหาที่พบ           | สาเหตุ                         | วิธีแก้                                       |
| -------------------- | ------------------------------ | --------------------------------------------- |
| ผลลัพธ์ไม่ตรงรูปแบบ | ไม่มี Output Format ชัดเจน     | เพิ่ม Output Format section ใน SKILL.md        |
| ขาดข้อมูลสำคัญ       | ไม่มีขั้นตอน "ถามผู้ใช้"       | เพิ่มขั้นตอน validation ใน Instructions        |
| ทำเกินที่ต้องการ     | Constraints ไม่ชัดเจน          | เพิ่ม Constraints section                      |
| ผลลัพธ์ไม่สม่ำเสมอ   | Examples น้อยเกินไป            | เพิ่ม Examples ให้หลากหลาย 3-5 ตัวอย่าง       |
| ไม่รองรับ edge case  | ไม่ได้คิดถึงกรณีพิเศษ         | เพิ่ม Edge Cases section                       |
| Skill ทำงานผิดพลาด  | Trigger ไม่ชัดเจน              | ปรับ description และเพิ่มตัวอย่างคำ trigger    |

---

### 3.3 การแชร์ Skill และ Plugin Marketplace

#### วิธีแชร์ Skill ให้ทีม

**วิธีที่ 1: ส่งไฟล์โดยตรง**

```bash
# คัดลอกโฟลเดอร์ Skill
cp -r .claude/skills/my-skill/ ~/shared/

# หรือ zip แล้วส่ง
zip -r my-skill.zip .claude/skills/my-skill/
```

**วิธีที่ 2: ใช้ Git/GitHub** (แนะนำสำหรับทีม)

```bash
# สร้าง repository สำหรับ Skills ของทีม
git init team-claude-skills
cd team-claude-skills

# สร้างโครงสร้าง
mkdir -p skills/content-strategist
mkdir -p skills/email-digest
mkdir -p skills/meeting-summary

# เพิ่ม Skill เข้า repository
cp -r ~/.claude/skills/content-strategist/ ./skills/content-strategist/
git add .
git commit -m "Add content-strategist skill"
git push origin main

# ทีมคนอื่น clone แล้วใช้ได้เลย
# git clone https://github.com/your-org/team-claude-skills
```

**วิธีที่ 3: รวมเป็น Plugin แล้วเผยแพร่**

เมื่อมี Skills หลายตัวที่เกี่ยวข้องกัน สามารถรวมเป็น Plugin ได้:

```
โครงสร้าง Plugin:
📁 content-marketing-plugin/
├── plugin.json          ← ข้อมูลหลัก Plugin
├── 📁 skills/
│   ├── 📁 content-strategist/
│   │   └── SKILL.md
│   ├── 📁 social-media-post/
│   │   └── SKILL.md
│   └── 📁 content-calendar/
│       └── SKILL.md
└── README.md
```

#### การติดตั้ง Skill ที่ได้รับ

```bash
# บน Terminal
cp -r received-skill/ .claude/skills/received-skill/

# บน Cowork: ลาก SKILL.md วางใน Workspace ที่กำหนด
# แล้วบอก Claude: "ติดตั้ง Skill จากไฟล์ที่ฉันอัปโหลด"
```

#### แหล่งค้นหา Skill

| แหล่ง                       | วิธีเข้าถึง                              | ประเภท Skill               |
| --------------------------- | ---------------------------------------- | -------------------------- |
| **Plugin Marketplace**      | Claude Desktop App → Settings → Plugins  | Skills สำเร็จรูปหลากหลาย  |
| **GitHub**                  | ค้นหา "claude skill SKILL.md"            | Skills จากนักพัฒนาอิสระ    |
| **Claude Community**        | community.anthropic.com                  | Skills จากชุมชน            |
| **Reddit r/ClaudeAI**       | reddit.com/r/ClaudeAI                    | Skills และ Tips            |
| **กลุ่ม Facebook**          | Claude AI Thailand                       | Skills ภาษาไทย             |

---

### 3.4 สรุปวันที่ 2 + Preview วันที่ 3

#### สิ่งที่เรียนรู้วันนี้

| Session | หัวข้อหลัก | Key Takeaway |
|---------|-----------|--------------|
| Session 1 | Content Strategist AI | SKILL.md = DNA ขององค์กร ทำให้ Claude รู้จักแบรนด์และตอบตรงเป้า |
| Session 2 | Connectors & Workflow | Claude เชื่อมกับ Gmail/Drive/Slack ได้จริง + Schedule & Dispatch ทำงานแทนเรา |
| Session 3 | Advanced Skills | Error handling ทำให้ Skill ฉลาดขึ้น + แชร์ Skill ด้วย Git/GitHub |

#### ความสามารถที่ได้รับวันนี้

ตอนนี้ผู้เรียนสามารถ:

- ✅ สร้าง Content AI เฉพาะองค์กรด้วย SKILL.md ได้
- ✅ ใช้ Connector เชื่อม Claude กับ Gmail, Drive, Slack ได้
- ✅ ตั้ง Schedule ให้ AI ทำงานอัตโนมัติตามเวลา
- ✅ สร้าง Dispatch rule สำหรับ trigger-action workflow
- ✅ สร้าง Skill จากงานจริง และปรับปรุงให้รับมือ edge case ได้
- ✅ แชร์ Skill ให้ทีมผ่าน Git/GitHub และ Plugin Marketplace

#### Preview วันที่ 3 — Claude Code

วันที่ 3 เราจะก้าวออกจาก GUI มาสู่ **Terminal** — Claude Code คือ CLI tool ที่ให้นักพัฒนาทำงานกับ Claude ผ่าน terminal โดยตรง มีความสามารถที่เหนือกว่า Cowork ในด้านการเขียนโค้ด Git operations และการสร้าง Dev Tools

ความแตกต่างที่สำคัญ:

| | Claude Cowork | Claude Code |
|---|---|---|
| อินเทอร์เฟซ | GUI (คลิก ลาก วาง) | CLI (พิมพ์คำสั่ง) |
| เหมาะกับ | งานเอกสาร, non-technical | เขียนโค้ด, DevOps |
| Git | ไม่รองรับ | รองรับเต็มรูปแบบ |
| รัน Code | จำกัด (sandbox) | เต็มรูปแบบ |

---

> 📌 **การบ้านก่อนวันที่ 3 (9 พฤษภาคม 2569):**
>
> 1. ติดตั้ง Node.js 18+ จาก https://nodejs.org (เลือก LTS)
> 2. ติดตั้ง Claude Code: `npm install -g @anthropic-ai/claude-code`
> 3. ทดสอบพิมพ์ `claude --version` ใน terminal — ควรได้เลขเวอร์ชัน
> 4. ติดตั้ง VS Code จาก https://code.visualstudio.com (ถ้ายังไม่มี)
> 5. เตรียมโปรเจกต์โฟลเดอร์สักโฟลเดอร์หนึ่งสำหรับทดลองใช้งาน
