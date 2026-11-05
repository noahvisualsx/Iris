<p align="right">
  <strong>Language:</strong>
  <a href="README.md"><b>简体中文</b></a> |
  <a href="README.en.md"><b>English</b></a> |
  <a href="README.ko.md"><b>한국어</b></a> |
  <a href="README.ja.md"><b>日本語</b></a>
</p>

# Iris (虹镜) · 全球虚拟人摄影全矩阵开源手册

> **The Aperture of Optics, The Soul in the Iris.**  
> 镜摄万象，眼眸有光。专为 AI 虚拟人打造的工业级跨模型（ChatGPT Image 2.5 / Seedream 5.0 Pro / Gemini）摄影与视觉全矩阵控制系统。

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Web Studio](https://img.shields.io/badge/Web%20Studio-Live%20on%20GitHub%20Pages-0071e3.svg)](https://noahvisualsx.github.io/Iris/)
[![Model Support](https://img.shields.io/badge/Model-Seedream%205.0%20Pro%20%7C%20ChatGPT%20Image%202.5%20%7C%20Gemini%20Imagen%203-blue.svg)](#四-三大模型编译器规范)
[![Global Matrix](https://img.shields.io/badge/5--Country%20Matrix-3315%20Dual--Image%20Prompts-success.svg)](#三-五国全矩阵视觉数据库)
[![Korea](https://img.shields.io/badge/Korea%20(韩国)-675%20Presets-blue.svg)](韩国/README.md)
[![Japan](https://img.shields.io/badge/Japan%20(日本)-660%20Presets-purple.svg)](日本/README.md)
[![China](https://img.shields.io/badge/China%20(中国)-660%20Presets-red.svg)](中国/README.md)
[![USA](https://img.shields.io/badge/USA%20(美国)-660%20Presets-orange.svg)](美国/README.md)
[![France](https://img.shields.io/badge/France%20(法国)-660%20Presets-teal.svg)](法国/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#七-参与贡献与路线图)

**专为 AI 虚拟人（Digital Humans）打造的工业级跨模型摄影全矩阵控制系统。**  
解决虚拟人生成中「换滤镜就换脸、换姿态就崩坏、跨模型表现分裂」的终极工程难题。

[项目哲学](#核心架构四维解耦控制) • [五国矩阵](#五国全矩阵视觉数据库) • [模型编译器](#三大模型编译器规范) • [调音台速查表](#调音台全矩阵速查表) • [锁脸工程规范](#虚拟人锁脸与身份保真度工程规范)

</div>

---

## 目录

- [一、 核心架构：四维解耦控制体系 (4D Decoupled Control)](#一-核心架构四维解耦控制体系)
- [二、 虚拟人锁脸与身份保真度工程规范 (ID Anchoring)](#二-虚拟人锁脸与身份保真度工程规范)
- [三、 五国全矩阵视觉数据库 (The 5-Country Matrix)](#三-五国全矩阵视觉数据库)
  - [🇰🇷 1. 韩国篇 (Korea) · 675套全量矩阵数据库 📂](韩国/README.md)（[章节速览](#1-韩国篇-korea--冷白皮极简松弛千禧微粒)）
  - [🇯🇵 2. 日本篇 (Japan) · 660套全量矩阵数据库 📂](日本/README.md)（[章节速览](#2-日本篇-japan--空气感日常碎片city-girl-胶片)）
  - [🇨🇳 3. 中国篇 (China) · 660套全量矩阵数据库 📂](中国/README.md)（[章节速览](#3-中国篇-china--新中式静奢清冷骨相夜间直闪)）
  - [🇺🇸 4. 美国篇 (USA) · 660套全量矩阵数据库 📂](美国/README.md)（[章节速览](#4-美国篇-usa--加州落日金光clean-girl无拘街头)）
  - [🇫🇷 5. 法国篇 (France) · 660套全量矩阵数据库 📂](法国/README.md)（[章节速览](#5-法国篇-france--毫不费力的慵懒巴黎灰调新浪潮电影)）
- [四、 三大模型编译器规范 (Cross-Model Compilers)](#四-三大模型编译器规范)
  - [1. Seedream 5.0 Pro (火山方舟/豆包)](#1-seedream-50-pro-火山方舟豆包)
  - [2. ChatGPT (Image 2.5)](#2-chatgpt-gpt-4o--dall-e-3)
  - [3. Gemini (Imagen 3 / Nano Banana)](#3-gemini-imagen-3--nano-banana)
- [五、 调音台全矩阵速查表 (The Mixing Matrix)](#五-调音台全矩阵速查表)
- [六、 自动化批量跑图脚本 (Tooling)](#六-自动化批量跑图脚本)
- [七、 参与贡献与路线图 (Roadmap)](#七-参与贡献与路线图)

---

## 一、 核心架构：四维解耦控制体系

在传统生图实践中，最大的痛点在于**提示词纠缠（Prompt Entanglement）**：当你在提示词里加入「CCD 滤镜」或「法式风衣」时，大模型往往会同时篡改角色的脸型、年龄甚至人种。

本系统采用**四维解耦工程架构**，像专业调音台一样将每个变量独立分层：

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: 人物基底锚点 (Identity Anchor: 骨相、五官、发型、底图) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┼──────────────────────────────┐
│ Layer 2: 光学模拟与滤镜层      │ Layer 3: 动作人体工学与机位层   │
│ (Optical & Sensor Emulation) │ (Ergonomics, Pose & Framing) │
└──────────────────────────────┼──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Layer 4: 穿搭面料与物理材质 (Wardrobe, Fabric Physics & Props) │
└──────────────────────────────┬──────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │ 跨引擎编译器适配层          │
                 │ (Cross-Model Compilers)   │
                 └──────┬──────┬──────┬──────┘
                        │      │      │
                        ▼      ▼      ▼
                   Seedream  ChatGPT Gemini
```

---

## 二、 虚拟人锁脸与身份保真度工程规范

生成稳定人物必须遵循**「母图生成 + 特征参数锚定」**工作流：

### 1. 标准母图规范 (Master Sheet Standard)
* **画幅比例**：严格 `3:4`（保留锁骨至头顶，最适宜人像特征提取）。
* **灯光环境**：柔和纯白漫反射无影光（Flat Light），严禁强阴影、过曝高光。
* **发型姿态**：黑色原生直发梳至耳后，露出完整额头、眉骨、双耳与下颌线轮廓。
* **背景着装**：纯浅灰灰度 18% 无缝背景，穿着极简白色纯棉圆领 T 恤。

### 2. 标准母图通用提示词代码块

```text
A front-facing master reference passport-grade portrait of a 22-year-old East Asian female. Features: balanced oval face contour, clear jawline, natural straight eyebrows, delicate inner double eyelids with subtle almond eye shape, straight well-proportioned nasal bridge, naturally relaxed lips with soft cupid's bow. Hair: natural sleek black straight hair tucked completely behind both ears, exposing forehead and ear contours. Neutral relaxed facial expression, mouth gently closed. Studio flat neutral diffused light, no harsh shadows, 18% neutral grey backdrop, wearing a plain white crewneck t-shirt. Ultra-photorealistic 8k, raw skin texture with pores and micro-texture, 3:4 aspect ratio.
```

---

## 三、 五国全矩阵视觉数据库 (The 5-Country Matrix)

本系统已完整交付全球五大审美高地全量 **3,315 套跨模型摄影提示词全矩阵**（每国 8 大支柱、660 套无损双图架构预设，共计 6,600 张视觉标本与 13,200 组独立提示词代码块）。点击直达各分部完整数据库：

| 国家 / 地区 | 美学核心与视觉基因 | 预设规模 | 8大支柱结构 (各篇完整覆盖) | 全量数据库入口 |
| :--- | :--- | :--- | :--- | :--- |
| 🇰🇷 **韩国篇 (Korea)** | 冷白瓷肌 · 极简松弛 · 首尔圣水洞微粒 | **660 套** 双图预设 | 穿搭 100 / 滤镜 100 / 姿势 100 / 神态 100 / 风格 100 / 丝袜 60 / 妆发 50 / 美甲 50 | [📂 **进入韩国全矩阵数据库**](韩国/README.md) |
| 🇯🇵 **日本篇 (Japan)** | 空气呼吸感 · 日常碎片 · City Girl 胶片 | **660 套** 双图预设 | 穿搭 100 / 滤镜 100 / 姿势 100 / 神态 100 / 风格 100 / 丝袜 60 / 妆发 50 / 美甲 50 | [📂 **进入日本全矩阵数据库**](日本/README.md) |
| 🇨🇳 **中国篇 (China)** | 新中式静奢 · 清冷骨相 · 东方留白夜直闪 | **660 套** 双图预设 | 穿搭 100 / 滤镜 100 / 姿势 100 / 神态 100 / 风格 100 / 丝袜 60 / 妆发 50 / 美甲 50 | [📂 **进入中国全矩阵数据库**](中国/README.md) |
| 🇺🇸 **美国篇 (USA)** | 加州落日金光 · Clean Girl · 无拘街头 | **660 套** 双图预设 | 穿搭 100 / 滤镜 100 / 姿势 100 / 神态 100 / 风格 100 / 丝袜 60 / 妆发 50 / 美甲 50 | [📂 **进入美国全矩阵数据库**](美国/README.md) |
| 🇫🇷 **法国篇 (France)** | 毫不费力慵懒 · 巴黎灰调 · 新浪潮电影 | **660 套** 双图预设 | 穿搭 100 / 滤镜 100 / 姿势 100 / 神态 100 / 风格 100 / 丝袜 60 / 妆发 50 / 美甲 50 | [📂 **进入法国全矩阵数据库**](法国/README.md) |

---

### 1. 韩国篇 (Korea) —— 冷白皮、极简松弛、千禧微粒

> 📂 **全量数据库直达**：[👉 点击浏览《韩国篇 660 套全量摄影美学矩阵与双图代码库》(韩国/README.md)](韩国/README.md)  
> *涵盖穿搭(100)、滤镜(100)、神态与微表情(100)、拍照姿势(100)、风格(100)、丝袜(60)、发型与妆容(50)、道具与美甲(50)*

#### A. 视觉基因与哲学
* **审美核心**：无负担的松弛感（Effortless）、冷白微光瓷肌、低饱和极简主义。
* **场景氛围**：首尔圣水洞水泥灰咖啡馆、深夜公寓极简白墙、弘大买手店试衣镜前。

#### B. 4 大核心滤镜与光学参数
1. **千禧 CCD 闪光 (2000s Compact CCD Flash)**：
   * *感光元件*：1/2.3 英寸小型 CCD 传感器，低照度机顶硬直闪。
   * *色温与曲线*：5500K，高光局部轻微溢出反光，暗部迅速跌落至纯黑，细腻高 ISO 噪点。
2. **冷白皮窗光漫射 (Muted Daylight Porcelain)**：
   * *光学参数*：50mm f/1.8，多云天气大面积冷光漫反射。
   * *色温与曲线*：6200K~6500K，压低黄色饱和度，整体微蓝灰调，保留皮肤通透半透明感。
3. **前置手机原生自拍 (Raw iPhone Front Camera)**：
   * *光学特征*：等效 24mm 微广角，无美颜算法直出，发丝与皮肤边缘锐化恰到好处，室内日光灯微颗粒。
4. **弘大胶片拍立得 (Hongdae Polaroid Instant)**：
   * *光学特征*：拍立得专用镜头，暖黄与青蓝微漏光交织，边缘轻度暗角与白色复古边框质感。

#### C. 6 大招牌姿势与人体工学
1. **双臂微屈·手机半遮面对镜自拍**：双手握手机置于鼻梁高度，挡住下半张脸，仅露出微垂杏眼与利落眉骨。
2. **低头整理防风绳/衣领**：视线下移 30 度，双手正捏住连帽衫拉链或风衣领口，捕捉极具生活感的抓拍瞬间。
3. **单手撩发·侧首微俯视**：食指与中指轻轻将耳前碎发拨至耳后，头颅微侧 15 度，眼神带有一丝未睡醒的清冷疏离。
4. **咖啡外带·第一人称男友视角 (POV)**：镜头居高临下微俯视，虚拟人单手递出燕麦拿铁纸杯，另一只手自然垂在风衣口袋。
5. **盘腿下蹲·楼梯拐角随拍**：在现代混凝土台阶上双膝收拢微曲，双臂环抱小腿，面颊微靠膝盖。
6. **走廊疾行·回眸抓拍**：身体保持向前走姿态，头部回转 90 度，长发带微弱动态模糊飘散。

#### D. 4 套穿搭面料与配饰库
* **Clean Fit 极简廓形**：Oversized 落肩冷灰西装外套（精纺羊毛混纺）+ 紧身白色罗纹削肩背心 + 垂感拖地阔腿西裤（深灰/深藏青）。
* **圣水洞随性街头**：纯黑防风机能冲锋衣（GORE-TEX 哑光质感）+ 水洗灰工装降落伞裤 + 银色亚瑟士跑鞋。
* **清晨居家男友风**：重磅燕麦色落肩连帽卫衣（450g 纯棉毛圈布）+ 宽松浅灰针织运动短裤 + 白袜。
* **配饰标配**：细圈钛钢冷银耳环、极简细黑框平光镜、纯黑皮质月牙包、手拿冰美式纸杯。

#### E. 韩国风跨模型工业级提示词

##### Seedream 5.0 Pro (豆包/火山)
```text
真实日常生活抓拍照片，一位20岁出头的年轻东亚女性，清冷淡颜，冷白皮，头小脸小骨相优越，身形纤细修长。深黑柔顺长发微微凌乱，几缕细碎胎毛发丝随走动自然飘拂，清透伪素颜底妆，原生自然眉形与水润淡唇。右手握手机遮挡嘴唇对镜自拍，眼神微垂慵懒，头部微倾10度。身穿落肩炭灰色精纺羊毛西装外套，内搭纯白罗纹背心，佩戴极简细银耳环。身处首尔极简清水混凝土咖啡馆，机顶小型CCD闪光灯直射，柔和硬阴影，冷蓝灰调，千禧复古数码质感。浅景深自然虚化，保留真实布料纤维织物纹理、面料垂坠褶皱、真实皮肤毛孔与自然血色，轻微生活感动态微模糊与暗部噪点，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
A raw, candid mirror selfie capturing a 22-year-old Korean woman with a minimalist and effortless aesthetic. She has smooth, straight raven-black hair falling naturally over her shoulders and luminous porcelain-cool skin tone. She holds her smartphone with both hands to obscure the lower half of her face, with only her delicate almond eyes looking sleepy yet calm above the camera lens. She wears an oversized tailored charcoal-wool blazer over a fitted white ribbed cotton tank top, accessorized with subtle silver hoop earrings. The setting is a minimalist indoor space with raw concrete walls. Direct harsh mini-flash illumination creates crisp back shadows and specular micro-highlights on her forehead and nose bridge, accompanied by authentic fine digital sensor noise from an early 2000s compact camera. 3:4 vertical orientation.
```

##### Gemini (Imagen 3)
```text
Photorealistic 35mm candid portrait of a 22-year-old East Asian female with sleek minimalist styling. 
Framing & Pose: Medium close-up, eye-level mirror reflection. She holds her phone up to nose height, casually concealing her mouth and jawline, tilting her head slightly with a calm, aloof micro-expression.
Lighting & Color: On-axis compact flash firing in a dim, minimalist room. Cool-white color balance (approx 6000K), desaturated neutral grays, clean skin highlights with authentic micro-pores, deep fall-off shadows against a smooth plaster backdrop.
Wardrobe: Heavyweight charcoal-melange oversized jacket, crisp white ribbed undershirt, micro-fine titanium hoop earring. Shot on vintage CCD sensor profile, authentic ISO 400 grain, no beauty post-processing.
```

---

### 2. 日本篇 (Japan) —— 空气感、日常碎片、City Girl 胶片

> 📂 **全量数据库直达**：[👉 点击浏览《日本篇 660 套全量摄影美学矩阵与双图代码库》(日本/README.md)](日本/README.md)  
> *涵盖穿搭(100)、滤镜(100)、神态与微表情(100)、拍照姿势(100)、风格(100)、丝袜(60)、发型与妆容(50)、道具与美甲(50)*

#### A. 视觉基因与哲学
* **审美核心**：生活在别处的呼吸感（Komorebi）、胶片颗粒温润感、自然不做作的透明度。
* **场景氛围**：东京下町居民区坡道、午后电车站台木椅、亮着暖灯的饮料自动贩卖机旁、代官山书店。

#### B. 4 大核心滤镜与光学参数
1. **富士经典负片 (Fujifilm Classic Neg)**：
   * *感光特征*：色彩饱和偏内敛，绿调与青蓝调浓郁，阴影带有独特的洋红与橄榄绿交织。
   * *色温*：5200K~5600K，中等反差，高光柔化微泛白。
2. **古早 DV 梦核柔焦 (Dreamcore Camcorder Glow)**：
   * *光学参数*：早期 Handcam DV 镜头，轻微色散（Chromatic Aberration），高光溢出光晕（Halation），梦幻朦胧。
3. **晨光微风自然漫射 (Muted Morning Transparency)**：
   * *光学参数*：35mm f/1.4 全开光圈，树影或百叶窗斑驳光影打在面颊，发丝金黄透光。
4. **一次性胶卷相机直出 (QuickSnap Disposable Flash)**：
   * *光学特征*：塑料镜头微边缘畸变，强闪光下人像泛红润感，背景暗角浓郁。

#### C. 6 大招牌姿势与人体工学
1. **自动贩卖机旁·下蹲抱膝**：双膝完全并拢蹲下，脚跟踮起，双手紧握一罐热饮，仰头 30 度与镜头对视。
2. **斑马线中央·大步流星抓拍**：身体侧向迈大步横穿街道，头猛然回看镜头，发梢被风扬起，裙摆呈动态展开。
3. **双手捧杯·呵气取暖**：双手严严实实裹住马克杯，下巴微缩进粗针织围巾内，眼神清澈充满灵气。
4. **电车车窗倒影·若有所思**：侧脸贴近车窗玻璃，眼神投向远方流动的风景，车窗倒影与侧脸产生双重曝光层次。
5. **骑单车驻足·单脚撑地**：坐在复古复古脚踏车上，单手扶车把，另一只手扶住被风吹乱的贝雷帽。
6. **书架缝隙·偷看镜头**：身体隐蔽于层层书架之后，只探出半张脸，手扶着一本厚皮书。

#### D. 4 套穿搭面料与配饰库
* **Fudge 杂志英伦日系叠穿**：卡其色双排扣风衣（高密防泼水棉斜纹）+ 墨绿色绞花针织马甲 + 浅蓝牛津纺衬衫 + 炭黑百褶长伞裙。
* **City Girl 随性工装**：Oversized 水洗军绿 M-65 夹克 + 米白重磅直筒阔腿裤 + 麂皮德训鞋。
* **夏日透明感棉麻**：水洗亚麻白色无袖连衣裙 + 浅卡其防晒针织开衫 + 细带编织凉鞋。
* **配饰标配**：粗绞花纯羊毛大围巾、纯白厚棉袜配马思纯同款乐福鞋、大容量原色水洗帆布包、挂颈复古头戴式金属耳机。

#### E. 日本篇跨模型工业级提示词

##### Seedream 5.0 Pro (豆包/火山)
```text
真实日常生活抓拍照片，一位20岁出头的年轻日本女性，日系空气感，清澈眼神，黑色齐肩短发配微乱空气刘海，几缕发丝随风轻拂。下蹲在傍晚东京街头亮着暖白光的自动饮料贩卖机旁，双手捧着热饮罐，仰头看向镜头，嘴角微扬。身穿宽版复古卡其色风衣，内叠穿墨绿粗针毛线马甲与牛津纺浅蓝衬衫，下身炭黑百褶裙，白袜配深棕乐福鞋。东京街头黄昏暮色，富士Classic Neg胶片色彩质感，青绿阴影与温润中性肤色，柔和自然胶片颗粒。浅景深自然虚化，保留真实布料纤维纹理、面料垂坠褶皱与真实皮肤毛孔，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
A genuine lifestyle photograph in the signature Japanese Fudge magazine aesthetic. A 22-year-old Japanese woman with shoulder-length tousled raven hair and airy wispy bangs. She is crouching down comfortably next to a glowing retro street vending machine in Tokyo at dusk, warming both hands around a hot canned beverage and looking up at the camera with wide, curious, innocent eyes. She wears an oversized beige trench coat over a forest-green cable-knit vest, a soft blue collared shirt, dark accordion-pleated midi skirt, and vintage brown leather loafers with white crew socks. Retro over-ear metallic headphones rest around her neck. Fujifilm 35mm film simulation with characteristic rich greens and muted warm yellows, gentle halation around the machine's neon lights, unposed everyday authenticity, 3:4.
```

##### Gemini (Imagen 3)
```text
Photorealistic environmental portrait in authentic Japanese City-Girl documentary style.
Subject: 22-year-old East Asian girl with natural luminous complexion and delicate features.
Framing & Kinetic: Full-body environmental shot, slightly high perspective looking down as she crouches compactly against a weathered suburban building wall. Dynamic flyaway hair catching the wind.
Lighting & Color: Ambient twilight illuminated by diffuse neon tube glow from an adjacent vending machine. Fujifilm Classic Chrome color profile: gentle desaturated tones, lifted green-tinted shadows, soft contrast roll-off, authentic 35mm film grain structure.
Wardrobe: Layered classic menswear-inspired garments: loose khaki mac coat, knitted vest, tailored pleated skirt, raw canvas shoulder tote bag. 
```

---

### 3. 中国篇 (China) —— 新中式静奢、清冷骨相、夜间直闪

> 📂 **全量数据库直达**：[👉 点击浏览《中国篇 660 套全量摄影美学矩阵与双图代码库》(中国/README.md)](中国/README.md)  
> *涵盖穿搭(100)、滤镜(100)、神态与微表情(100)、拍照姿势(100)、风格(100)、丝袜(60)、发型与妆容(50)、道具与美甲(50)*

#### A. 视觉基因与哲学
* **审美核心**：骨相美、大女主从容气场、东方留白意境与现代千金奢感的碰撞。
* **场景氛围**：苏州园林青砖黛瓦竹影前、北京夜间胡同红门、当代美术馆冷灰挑高空间、外滩夜景露台。

#### B. 4 大核心滤镜与光学参数
1. **新中式水墨影调 (Ink & Bamboo Muted Green)**：
   * *感光特征*：低饱和、微偏墨绿与冷灰竹影调，人物肤色呈现如羊脂白玉般温润细腻的哑光质感。
   * *光线*：多云天或天井柔光，面部明暗交界线清晰，凸显立体骨骼结构。
2. **小红书爆款夜间直闪 (Hard Flash Diva Red)**：
   * *光学参数*：强力外置机顶硬闪光灯（GN 数值高），照射距离 1.2 米以内。
   * *反差*：纯黑背景（夜景被瞬间压黑），面部冷白瓷肌与正红唇色形成剧烈视觉冲击。
3. **王家卫式浓郁港风 (Hong Kong 90s Cinematic Nostalgia)**：
   * *光学参数*：柯达 5219 电影胶片，暖红暖黄大色块碰撞，慢门带来的轻度光影拖尾与高密度颗粒。
4. **当代美术馆冷光极简 (Museum Cold Minimalist)**：
   * *光学参数*：85mm f/1.4 人像定焦，极高锐度，面部毛孔细节毫发毕现，雕塑般阴影轮廓。

#### C. 6 大招牌姿势与人体工学
1. **微扬下颌·侧颜 3/4 绝杀**：身体侧对镜头，脸向侧后方转动 45 度并微抬下巴 10 度，极致展现清晰的下颌缘、颈部天鹅线与锁骨。
2. **指尖微抚·玉石互动**：单手优雅抬起，修长食指轻抚翡翠耳坠或旗袍盘扣，眼神淡然目空一切。
3. **倚靠凭栏·回眸留白**：背对镜头斜倚在古典石栏或现代栏杆上，仅上身回转，发丝飘过鼻尖，眼神充满故事感。
4. **阔步走动·大衣带风**：正面迎向镜头快步走来，风衣下摆扬起，单手插在西裤口袋，眼神笃定有力。
5. **对镜端坐·端详朱唇**：坐在中式梳妆台前，镜中倒映出精致侧脸，另一只手拿着口红或香水瓶悬停于唇边。
6. **半明半暗·阴影切面**：站在朱红大门或百叶隔栅旁，利用强光在面部投下精准的一半光影、一半幽暗。

#### D. 4 套穿搭面料与配饰库
* **新中式静奢真丝**：黑色重磅真丝（30 姆米素绉缎）改良立领斜襟盘扣马甲 + 垂坠醋酸香云纱阔腿裤。
* **清冷财阀大女主**：超长款极简黑色纯双面羊绒大衣（大翻领）+ 内搭黑色高领羊绒衫 + 拖地西装裤 + 尖头皮靴。
* **现代东方红丝绒**：复古深红丝绒改良修身旗袍（高开叉、暗纹提花）+ 黑色水貂绒短披肩。
* **配饰标配**：天然老坑冰种翡翠蛋面耳钉、巴洛克异形天然淡水珍珠项链、手工银质竹节发簪、复古金丝边无框平光镜。

#### E. 中国篇跨模型工业级提示词

##### Seedream 5.0 Pro (豆包/火山)
```text
真实高级人像摄影照片，一位20岁出头的年轻中国女性，清冷骨相大女主，平直自然眉骨，冷白瓷肌，哑光正红唇色。身体微侧，微扬下颌3/4侧脸回眸注视镜头，单手轻抚领口手工翡翠盘扣，眼神从容疏离。身穿黑色重磅真丝立领改良马甲，手工翡翠盘扣，垂感缎面黑色阔腿长裤，佩戴单只极简异形珍珠耳环。身处夜间现代中式庭院竹影下，机顶强力硬闪光灯直射，背景深黑幽邃，面部骨骼高光与雕塑感阴影，电影级高反差奢华质感。浅景深自然虚化，保留真实丝绸织物光泽、面料重力垂坠与真实皮肤细腻毛孔，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
A striking, high-fashion portrait capturing a 22-year-old Chinese woman with an aristocratic, sculptural facial bone structure. She has flawless porcelain-white skin with a velvet matte finish, defined jawline, and bold classic crimson lipstick. She turns her head 3/4 towards the viewer with a regal, aloof gaze, chin slightly elevated to showcase her elegant neck contour, with one manicured hand gracefully touching a traditional jade frog button on her collar. Outfit: modernized black mulberry silk sleeveless mandarin-collar tunic with understated floral jacquard weaving, fluid wide-leg silk trousers, accented by a single baroque freshwater pearl earring. Setting: nocturnal minimalist courtyard beside slender bamboo silhouettes. Harsh on-camera fashion flash casts crisp shadows behind her, highlighting cheekbone structure and creating a high-contrast luxury editorial look. 3:4.
```

##### Gemini (Imagen 3)
```text
Editorial studio-grade fashion portrait: Neo-Chinese Quiet Luxury aesthetic.
Subject: 22-year-old East Asian female with razor-sharp facial symmetry, calm aristocratic demeanor, swept-back architectural low bun.
Composition & Angle: 3/4 profile medium shot, slightly low angle emphasizing statuesque presence. 
Lighting: Direct high-powered ring flash contrasted with an obsidian ink-wash architectural environment. Deep chiaroscuro modeling on the cheekbones and nose bridge, specular glint on dark pupils and velvet lips.
Wardrobe & Textures: 30-momme heavy black silk faille jacket with handcrafted jade toggle closures, flowing tailored trousers. Minimalist Chinese jewelry in sterling silver and raw white nephrite jade. 85mm prime lens clarity.
```

---

### 4. 美国篇 (USA) —— 加州落日金光、Clean Girl、无拘街头

> 📂 **全量数据库直达**：[👉 点击浏览《美国篇 660 套全量摄影美学矩阵与双图代码库》(美国/README.md)](美国/README.md)  
> *涵盖穿搭(100)、滤镜(100)、神态与微表情(100)、拍照姿势(100)、风格(100)、丝袜(60)、发型与妆容(50)、道具与美甲(50)*

#### A. 视觉基因与哲学
* **审美核心**：生命力、自洽的自信（Unapologetic Confidence）、阳光水光肌、健康运动生活。
* **场景氛围**：加利福尼亚一号公路沿岸海滩、洛杉矶棕榈树街道、曼哈顿红砖公寓消防逃生梯、深夜复古美式 Diner 餐馆。

#### B. 4 大核心滤镜与光学参数
1. **加州落日黄金时刻 (California Golden Hour)**：
   * *感光特征*：3200K~4000K 极致暖金光线，大面积逆光耀斑（Lens Flare），空气中微尘反射出神圣金色光环。
   * *质感*：高饱和暖橙与天蓝互补，皮肤呈现充满活力的古铜小麦色或自然晒后水光。
2. **柯达皇家胶片 (Kodak Portra 400)**：
   * *光学特征*：人像摄影标杆，温暖自然的肤色过渡，柔和的高光卷边，细腻经典的有机胶片颗粒。
3. **0.5x 超广角自拍鱼眼 (0.5x Ultra-Wide Fisheye Distortion)**：
   * *光学参数*：等效 13mm~16mm 手机超广角镜头，自上而下俯视自拍，产生具有趣味张力的透视拉伸感。
4. **美式复古派对硬闪 (Flash Party Candid)**：
   * *光学特征*：直白暴力的硬闪光，人物瞳孔微反红光，抓拍大笑和狂欢瞬间，充满荷尔蒙与现场噪音感。

#### C. 6 大招牌姿势与人体工学
1. **0.5x 俯拍高举手臂自拍**：手机举至头顶 45 度俯视，身体后仰，一手拿冰咖啡一手举手机，展露毫不做作的开怀笑容。
2. **跨步横穿马路·回眸大笑**：走在阳光炙热的斑马线上，步幅极大，单手插在牛仔裤后口袋，猛然回头开朗大笑。
3. **引擎盖/路沿随意斜坐**：坐在复古敞篷野马跑车引擎盖或街角混凝土路牙子上，双腿自然伸展，身体微微前倾。
4. **单腿微屈·全身穿搭镜前秀 (OOTD)**：站在电梯或试衣间全身大镜前，重心落在后脚，前脚微踮起，展现紧致腿部线条。
5. **嚼泡泡糖/吃披萨生活抓拍**：坐在美式餐馆红色皮沙发里，手里抓着一片拉丝披萨或吹起粉色泡泡糖，眼神调皮狡黠。
6. **靠墙环胸·自信直视**：背靠在布鲁克林涂鸦红砖墙上，双臂环抱在胸前，眼神直视镜头，气场强大毫无躲闪。

#### D. 4 套穿搭面料与配饰库
* **Clean Girl 健美运动风**：石灰灰宽松 Oversized 连帽衫（加厚抓绒）+ 黑色紧身骑行短裤 + 纯白运动中筒袜 + 经典复古运动鞋。
* **90s 加州复古机车辣妹**：做旧深棕磨损牛皮机车夹克 + 纯白修身挂脖短上衣 + 低腰做旧水洗直筒破洞牛仔裤。
* **常春藤老钱预科风 (Hamptons Prep)**：米白绞花纯棉毛衣斜系在肩头 + 藏蓝 Polo 领连衣裙 + 网球小白鞋。
* **配饰标配**：夸张粗圆管金色大耳圈（Chunky Gold Hoops）、细金链多层叠戴、黑框窄长墨镜、大号金属保温水杯。

#### E. 美国篇跨模型工业级提示词

##### Seedream 5.0 Pro (豆包/火山)
```text
真实街头生活抓拍照片，一位20岁出头的年轻女性，健康水光小麦肤色，蓬松微卷深棕色长发，自信开朗露齿大笑。手持手机高角度0.5x广角自拍，身体微后仰，另一手拿着大杯冰拿铁，洋溢活力生活感。身穿做旧深棕牛皮机车夹克，短款白色紧身背心，宽松水洗低腰牛仔裤，佩戴粗金圈大耳环。身处加州洛杉矶午后落日黄金时刻，强烈的逆光金色光晕透过发丝，Kodak Portra 400胶片色彩，温暖高饱和。浅景深自然虚化，保留皮革纹理、真实皮肤质感与自然光斑，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
An energetic, spontaneous golden-hour street photograph captured in sunny Los Angeles. A 22-year-old woman with sun-kissed, naturally glowing skin and voluminous wind-blown wavy brunette hair. She is captured mid-laugh with an infectious open smile, holding an oversized iced latte in one hand while snapping a top-down wide-angle selfie. She is dressed in an effortless California cool outfit: an oversized distressed vintage brown leather bomber jacket over a cropped white ribbed camisole, low-rise baggy faded denim jeans, accessorized with chunky polished gold hoop earrings and layered dainty gold necklaces. Bathed in brilliant California golden hour sunlight, creating radiant amber backlight flares through her curls, shot on Kodak Portra 400 film stock with rich warm hues and lively organic grain. 3:4.
```

##### Gemini (Imagen 3)
```text
Authentic documentary snapshot, 90s West Coast aesthetic.
Subject: 22-year-old woman with glowing dewy complexion, athletic physique, radiating spontaneous joy and confidence.
Framing & Optics: High-angle wide-angle perspective (approx. 20mm focal length), capturing environmental context of sun-drenched Venice Beach palm trees. Slight optical perspective barrel distortion.
Lighting & Color: Low-angle late afternoon solar flare striking the camera sensor, creating luminous golden edge light around the subject's silhouette. Warm color temperature (3800K), rich Kodachrome-inspired reds and yellows, vibrant dynamic range.
Wardrobe: Heavyweight worn-in leather flight jacket, cropped white cotton tank, relaxed-fit stone-washed denim, chunky gold jewelry. 
```

---

### 5. 法国篇 (France) —— 毫不费力的慵懒、巴黎灰调、新浪潮电影

> 📂 **全量数据库直达**：[👉 点击浏览《法国篇 660 套全量摄影美学矩阵与双图代码库》(法国/README.md)](法国/README.md)  
> *涵盖穿搭(100)、滤镜(100)、神态与微表情(100)、拍照姿势(100)、风格(100)、丝袜(60)、发型与妆容(50)、道具与美甲(50)*

#### A. 视觉基因与哲学
* **审美核心**：漫不经心的优雅（Laissez-faire）、拒绝过度修饰、知识分子文艺气质、真实雀斑与凌乱。
* **场景氛围**：巴黎圣日耳曼大道户外双叟咖啡馆、奥斯曼建筑挑高公寓铁艺阳台、塞纳河畔二手旧书摊前。

#### B. 4 大核心滤镜与光学参数
1. **法国新浪潮 16mm 胶片 (Nouvelle Vague 16mm)**：
   * *感光特征*：具有标志性粗颗粒感，色彩不争不抢，带有淡淡的灰调与奶咖色过渡，叙事感极强。
2. **巴黎午后灰调漫射 (Parisian Muted Warm Grey)**：
   * *光线*：巴黎经典的阴郁多云漫射天光，反差极低，光线像丝绸一样包裹面部，阴影细节极其丰富细腻。
3. **窗边逆光油画质感 (Window Vermeer Backlight)**：
   * *光学参数*：50mm f/1.4，透过法式白色木质百叶窗透进来的侧光，呈现出类似维米尔油画般的静谧光感。
4. **街头咖啡馆玻璃双重倒影 (Cafe Window Reflection)**：
   * *光学特征*：隔着咖啡馆擦拭微糊的玻璃拍摄，街景倒影与室内人物面部重叠，诗意虚实交错。

#### C. 6 大招牌姿势与人体工学
1. **户外小圆桌·单手托腮放空**：慵懒坐在咖啡馆沿街绿色藤编椅上，单手托着腮帮，面前摊开一本发黄的平装书，视线漫不经心地望向过路行人。
2. **铁艺阳台·凭栏远眺巴黎屋顶**：身穿宽松衬衫靠在奥斯曼雕花栏杆上，手端一杯红酒或浓缩咖啡，微风吹乱法式法式刘海。
3. **随手挽发·咬住玳瑁发夹**：双臂抬起在脑后抓拢头发，嘴唇微张轻轻咬住一枚玳瑁色鲨鱼夹，眼神向下瞥。
4. **地毯斜坐·靠着复古旧沙发**：整个人陷在铺满波斯地毯的地板上，身体倚靠着磨损的旧天鹅绒沙发，双腿随意曲折。
5. **塞纳河畔·翻阅泛黄二手书**：侧身站在绿皮书箱旁，双手捧起一本无封皮旧书，微低头阅读，神态专注深沉。
6. **漫步回眸·微风吹乱刘海**：在石板路上信步走动，转头半侧脸看着镜头，嘴角挂着若有若无的一抹神秘微笑。

#### D. 4 套穿搭面料与配饰库
* **经典法式海魂条纹**：重磅落肩蓝白相间条纹长袖针织衫（Breton Stripe）+ 复古高腰九分微喇原色牛仔裤 + 红色平底芭蕾舞鞋。
* **茶歇碎花慵懒裙**：深 V 领绑带印花真丝雪纺茶歇裙（Rouje 风格）+ 宽松浅燕麦色粗针粗花呢开衫（随意解开最上面两颗扣）。
* **左岸文艺学者风**：男装剪裁粗花呢人字纹西装外套 + 纯白洗旧棉衬衫（微敞开领口露出锁骨）+ 棕色复古皮带。
* **配饰标配**：手工编织草编菜篮子（Jane Birkin 同款）、复古玳瑁发夹、做旧浮雕古币吊坠、随意抓乱的法式空气八字刘海（Bedhead）。

#### E. 法国篇跨模型工业级提示词

##### Seedream 5.0 Pro (豆包/火山)
```text
真实街头生活抓拍照片，一位20岁出头的年轻法国女性，法式松弛慵懒感，纯净微瑕裸妆，鼻梁带极淡自然雀斑，微乱深棕色法式八字刘海卷发随性垂落。闲散坐在巴黎街头咖啡馆室外藤编椅上，单手托腮，另一手轻放在翻开的书页上，神态慵懒从容，若有所思望向远方。身穿蓝白粗条纹针织海魂衫，九分复古微喇牛仔裤，红色芭蕾平底鞋，桌边一只手工编织草编篮。身处巴黎奥斯曼街道鹅卵石路面，柔和低反差阴天灰调漫射光，法国新浪潮16mm电影胶片质感，细腻胶片颗粒，温润油画色调。保留真实毛孔、发丝空气感与针织纹理，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
A poetic, effortless 35mm film photograph radiating quintessential Parisian chic. A 22-year-old woman with delightfully tousled brunette bedhead hair and delicate wispy curtain bangs, embracing a makeup-free look with faint natural freckles across her nose. She sits nonchalantly at a small round bistro table outside a vintage Parisian cafe, cheek resting on one hand, looking daydreamy and serene into the distance. Outfit: classic navy-and-white Breton striped knit sweater, vintage high-waisted flared jeans, cherry-red ballet flats, with a traditional wicker basket bag resting on the cobblestones beside her. Atmospheric lighting: soft, overcast Parisian grey daylight filtering through Haussmannian balconies, rendered with the grainy, poetic warmth of a 16mm French New Wave film reel. Unposed, nostalgic, effortlessly elegant, 3:4.
```

##### Gemini (Imagen 3)
```text
Cinematic 35mm candid portrait capturing French 'Laissez-faire' lifestyle philosophy.
Subject: 22-year-old European woman, natural understated beauty, authentic skin with subtle texture and soft natural blush, hair softly windswept.
Framing & Atmosphere: Medium environmental composition seated at an outdoor cafe terrace along Boulevard Saint-Germain. Soft background blur of cobblestone street and passing blurred pedestrians.
Lighting & Optics: Muted overcast daylight with low contrast ratios and delicate shadow gradations. 50mm vintage prime lens rendering, gentle optical vignetting, subtle chromatic aberration, warm-toned gray spectral balance.
Styling: Striped cotton sailor top, vintage faded denim, minimal gold medallion necklace, open paperback book. Intimate and unhurried documentary grain.
```

---

## 四、 三大模型编译器规范

不同大模型底层对提示词的解析原理有着本质区别，在实际调用时必须进行语法转译：

| 维度 | Seedream 5.0 Pro (火山/豆包) | ChatGPT (Image 2.5) | Gemini (Imagen 3) |
|---|---|---|---|
| **核心机制** | 纯正写实摄影自然叙事流 + 母图一致性 | 连贯叙事流 + 具象物理交互描写 | 光学几何学 + 摄影传感器参数 |
| **锁脸手段** | 上传标准母图作为 `--ref` 垫图 | 固化人物基底长句 + 固定种子 | 提供参考图上下文 + 严格五官描摹 |
| **光影控制** | `机顶直闪`, `柔和漫射`, `低对比` | 详细描写光源方向、阴影形状、反光点 | 指定灯光硬件、光圈 `f/1.8`、色温开尔文值 |
| **禁忌词** | 拒绝大段抽象形容词（如“绝美、惊艳”） | 避免机械死板的负向词堆砌 | 避免夸张动漫风词汇，易损失写实度 |

---

## 五、 调音台全矩阵速查表

像音乐制作人拉动混音台推子一样，你可以跨国界随意混搭以下 4 大轨道的参数：

| 模块 | 轨道 1：滤镜与光学 (Optics) | 轨道 2：拍照姿态 (Pose) | 轨道 3：微表情 (Expression) | 轨道 4：穿搭面料 (Textile) |
|---|---|---|---|---|
| **A** | 千禧复古小型 CCD 强闪光 | 双手握手机半遮面对镜自拍 | 慵懒微困、双眼半张微下垂 | 极简 Oversized 羊毛落肩西装 |
| **B** | 富士 Classic Neg 绿调胶卷 | 街头下蹲抱膝、双手握热饮 | 清澈好奇、嘴角极其微扬 | 英伦风衣 + 粗针织毛线马甲 |
| **C** | 小红书夜间街头高反差硬闪 | 3/4 侧脸微昂头抚弄领口 | 清冷孤傲、大女主目空一切 | 改良真丝立领对襟马甲 + 盘扣 |
| **D** | 加州一号公路落日黄金逆光 | 0.5x 广角俯拍、大跨步横行 | 开怀大笑、充满感染力 | 做旧牛皮机车夹克 + 破洞低腰牛 |
| **E** | 法国新浪潮 16mm 粗颗粒胶片 | 户外小圆桌单手托腮放空 | 漫不经心、若有所思、微迷离 | 蓝白海魂衫 + 红色玛丽珍鞋 |

> **混搭范例**：`[A 滤镜 CCD闪光]` + `[E 姿态 托腮放空]` + `[C 表情 清冷孤傲]` + `[D 穿搭 机车夹克]`  
> **成片效果**：极具反差张力的千禧辣妹在夜晚露天吧台放空的清冷大片！

---

## 六、 自动化批量跑图脚本

本项目已内置基于 Volcengine Ark (Seedream 5.0 Pro) 的批量生成与母图绑定测试脚本：

```bash
# 进入工作目录
cd 仓库/Iris

# 使用标准母图 + 韩国冷白皮滤镜批量测试
python3 ../../bin/gen_image.py \
  "真实日常生活抓拍照片，一位20岁出头的年轻东亚女性，冷白皮，双手拿手机半遮脸对镜自拍，深灰西装，千禧CCD直闪，严格禁止二次元与3D塑料感，3:4" \
  --ratio 3:4 \
  --ref path/to/master_anchor.png
```

---

## 七、 参与贡献与路线图

- [x] **v0.1**：完成五国全矩阵（韩/日/中/美/法）核心视觉资产库与三模型编译器规范。
- [ ] **v0.2**：补充北欧极简风 (Nordic)、英国摇滚叛逆风 (British Grunge) 视觉模块。
- [ ] **v0.3**：发布自动根据调音台配置生成跨模型提示词的 WebUI 工具 / CLI 工具。
- [ ] **v0.4**：上传 100 组真人测试基准与模型实测对照图谱。

欢迎提交 PR 补充更多国家审美、小众经典胶片模拟与动作机位！

---

<div align="center">
Created with passion by <a href="https://github.com/noahvisualsx">@noahvisualsx</a> • Open for Open Source Community
</div>
