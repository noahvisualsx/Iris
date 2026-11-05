<p align="right">
  <strong>Language:</strong>
  <a href="README.md"><b>简体中文</b></a> |
  <a href="README.en.md"><b>English</b></a> |
  <a href="README.ko.md"><b>한국어</b></a> |
  <a href="README.ja.md"><b>日本語</b></a>
</p>

# Iris · Global Digital Human Photography Aesthetics Matrix Open-Source Handbook

> **The Aperture of Optics, The Soul in the Iris.**  
> Capturing all dimensions through the lens; breathing luminous soul into the eyes. An industrial-grade, cross-model (ChatGPT Image 2.5 / Seedream 5.0 Pro / Gemini Imagen 3) photography and visual control matrix system tailored for AI Digital Humans.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Web Studio](https://img.shields.io/badge/Web%20Studio-Live%20on%20GitHub%20Pages-0071e3.svg)](https://noahvisualsx.github.io/Iris/)
[![Model Support](https://img.shields.io/badge/Model-Seedream%205.0%20Pro%20%7C%20ChatGPT%20Image%202.5%20%7C%20Gemini%20Imagen%203-blue.svg)](#iv-cross-model-compiler-specifications)
[![Global Matrix](https://img.shields.io/badge/5--Country%20Matrix-3300%20Dual--Image%20Prompts-success.svg)](#iii-the-5-country-visual-matrix)
[![Korea](https://img.shields.io/badge/Korea%20(韩国)-660%20Presets-blue.svg)](韩国/README.md)
[![Japan](https://img.shields.io/badge/Japan%20(日本)-660%20Presets-purple.svg)](日本/README.md)
[![China](https://img.shields.io/badge/China%20(中国)-660%20Presets-red.svg)](中国/README.md)
[![USA](https://img.shields.io/badge/USA%20(美国)-660%20Presets-orange.svg)](美国/README.md)
[![France](https://img.shields.io/badge/France%20(法国)-660%20Presets-teal.svg)](法国/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#vii-contributing--roadmap)

**An industrial-grade cross-model photography control system tailored for AI Digital Humans.**  
Solving the ultimate engineering challenges in AI portraiture: *"changing filters changes the face, switching poses breaks anatomy, and performance fractures across different AI engines."*

[Philosophy](#i-core-architecture-4d-decoupled-control-system) • [5-Country Matrix](#iii-the-5-country-complete-visual-database) • [Model Compilers](#iv-cross-model-compiler-specifications) • [Studio Matrix](#v-mixing-matrix-cheat-sheet) • [ID Anchoring](#ii-virtual-human-id-anchoring--facial-fidelity-specification)

</div>

---

## Table of Contents

- [I. Core Architecture: 4D Decoupled Control System](#i-core-architecture-4d-decoupled-control-system)
- [II. Virtual Human ID Anchoring & Facial Fidelity Specification](#ii-virtual-human-id-anchoring--facial-fidelity-specification)
  - [1. Master Reference Sheet Standard](#1-master-reference-sheet-standard)
  - [2. Universal Master Sheet Prompt Block](#2-universal-master-sheet-prompt-block)
- [III. The 5-Country Complete Visual Database](#iii-the-5-country-complete-visual-database)
  - [🇰🇷 1. Korea Edition · 660 Presets Full Database 📂](韩国/README.md) ([Preview](#1-korea-edition--muted-porcelain-effortless-chic-y2k-ccd-grain))
  - [🇯🇵 2. Japan Edition · 660 Presets Full Database 📂](日本/README.md) ([Preview](#2-japan-edition--komorebi-airiness-everyday-life-fragments-city-girl-35mm))
  - [🇨🇳 3. China Edition · 660 Presets Full Database 📂](中国/README.md) ([Preview](#3-china-edition--neo-chinese-quiet-luxury-sculptural-bone-structure-direct-night-flash))
  - [🇺🇸 4. USA Edition · 660 Presets Full Database 📂](美国/README.md) ([Preview](#4-usa-edition--golden-hour-flare-clean-girl-uninhibited-street-energy))
  - [🇫🇷 5. France Edition · 660 Presets Full Database 📂](法国/README.md) ([Preview](#5-france-edition--laissez-faire-elegance-parisian-muted-grey-french-new-wave-16mm))
- [IV. Cross-Model Compiler Specifications](#iv-cross-model-compiler-specifications)
  - [1. Seedream 5.0 Pro (Volcengine Ark / Doubao)](#1-seedream-50-pro-volcengine-ark--doubao)
  - [2. ChatGPT (Image 2.5)](#2-chatgpt-image-25)
  - [3. Gemini (Imagen 3)](#3-gemini-imagen-3)
- [V. Mixing Matrix Cheat Sheet](#v-mixing-matrix-cheat-sheet)
- [VI. Automated Batch Generation Script (Tooling)](#vi-automated-batch-generation-script-tooling)
- [VII. Contributing & Roadmap](#vii-contributing--roadmap)

---

## I. Core Architecture: 4D Decoupled Control System

In traditional generative AI generation, the foremost pain point is **Prompt Entanglement**: whenever you introduce a camera aesthetic like "CCD flash" or styling like "oversized blazer," generative foundation models frequently alter the character's facial bone structure, apparent age, or ethnic identity.

Iris utilizes a **multi-dimensional decoupled engineering architecture**, layering each physical and stylistic variable independently, much like an audio mixing console:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: Identity Anchor (Bone structure, facial features, hair, master ref) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┼──────────────────────────────┐
│ Layer 2: Optical & Sensor    │ Layer 3: Ergonomics, Pose    │
│ Emulation (Filters, Kelvin)  │ & Camera Framing             │
└──────────────────────────────┼──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Layer 4: Wardrobe, Fabric Physics & Ambient Props           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │ Cross-Model Compiler Layer│
                 └──────┬──────┬──────┬──────┘
                        │      │      │
                        ▼      ▼      ▼
                   Seedream  ChatGPT Gemini
```

---

## II. Virtual Human ID Anchoring & Facial Fidelity Specification

Generating consistent digital humans requires strict adherence to the **"Master Reference Sheet + Feature Parameter Anchoring"** workflow:

### 1. Master Reference Sheet Standard
* **Aspect Ratio**: Strictly `3:4` (capturing from collarbone to top of the head, optimal for facial feature extraction).
* **Lighting Environment**: Studio neutral flat diffused light (no harsh shadows, no blown-out highlights).
* **Hair & Posture**: Natural straight black hair tucked completely behind both ears, exposing forehead, brow bones, ears, and jawline contours.
* **Backdrop & Wardrobe**: 18% neutral grey seamless backdrop, wearing a plain white crewneck t-shirt.

### 2. Universal Master Sheet Prompt Block

```text
A front-facing master reference passport-grade portrait of a 22-year-old East Asian female. Features: balanced oval face contour, clear jawline, natural straight eyebrows, delicate inner double eyelids with subtle almond eye shape, straight well-proportioned nasal bridge, naturally relaxed lips with soft cupid's bow. Hair: natural sleek black straight hair tucked completely behind both ears, exposing forehead and ear contours. Neutral relaxed facial expression, mouth gently closed. Studio flat neutral diffused light, no harsh shadows, 18% neutral grey backdrop, wearing a plain white crewneck t-shirt. Ultra-photorealistic 8k, raw skin texture with pores and micro-texture, 3:4 aspect ratio.
```

---

## III. The 5-Country Complete Visual Database

Iris has completely delivered **3,300 industrial-grade cross-model prompt presets** across the world's 5 major visual regions (8 pillars per country, 660 presets per country with dual-image architecture, totaling 6,600 reference specimens and 13,200 prompt code blocks). Click below to access each country's full database:

| Region | Aesthetic DNA & Philosophy | Preset Scale | 8-Pillar Structure | Full Database Direct Link |
| :--- | :--- | :--- | :--- | :--- |
| 🇰🇷 **Korea Edition** | Muted porcelain, effortless chic, Y2K CCD grain | **660 Presets** | 100 Outfits / 100 Filters / 100 Poses / 100 Expressions / 100 Styles / 60 Hosiery / 50 Hair & Makeup / 50 Props & Nails | [📂 **Enter Korea Matrix (韩国/README.md)**](韩国/README.md) |
| 🇯🇵 **Japan Edition** | Komorebi airiness, daily fragments, City Girl 35mm | **660 Presets** | 100 Outfits / 100 Filters / 100 Poses / 100 Expressions / 100 Styles / 60 Hosiery / 50 Hair & Makeup / 50 Props & Nails | [📂 **Enter Japan Matrix (日本/README.md)**](日本/README.md) |
| 🇨🇳 **China Edition** | Neo-Chinese quiet luxury, sculptural bone structure | **660 Presets** | 100 Outfits / 100 Filters / 100 Poses / 100 Expressions / 100 Styles / 60 Hosiery / 50 Hair & Makeup / 50 Props & Nails | [📂 **Enter China Matrix (中国/README.md)**](中国/README.md) |
| 🇺🇸 **USA Edition** | Golden hour flare, Clean Girl, street freedom | **660 Presets** | 100 Outfits / 100 Filters / 100 Poses / 100 Expressions / 100 Styles / 60 Hosiery / 50 Hair & Makeup / 50 Props & Nails | [📂 **Enter USA Matrix (美国/README.md)**](美国/README.md) |
| 🇫🇷 **France Edition** | Laissez-faire elegance, Parisian grey, New Wave 16mm | **660 Presets** | 100 Outfits / 100 Filters / 100 Poses / 100 Expressions / 100 Styles / 60 Hosiery / 50 Hair & Makeup / 50 Props & Nails | [📂 **Enter France Matrix (法国/README.md)**](法国/README.md) |

---

### 1. Korea Edition —— Muted Porcelain, Effortless Chic, Y2K CCD Grain

> 📂 **Full Database Direct Access**: [👉 Explore Complete Korea Matrix: 660 Dual-Image Presets (韩国/README.md)](韩国/README.md)  
> *Covers Outfits (100), Filters (100), Expressions (100), Poses (100), Styles (100), Hosiery (60), Hair & Makeup (50), Props & Nails (50)*

#### A. Visual DNA & Philosophy
* **Aesthetic Core**: Effortless relaxation, luminous porcelain-cool complexion, desaturated minimalism.
* **Atmospheric Settings**: Concrete minimalist cafes in Seongsu-dong, midnight apartments with stark white walls, fitting mirrors in Hannam-dong boutique stores.

#### B. 4 Core Filters & Optical Parameters
1. **2000s Compact CCD Flash**:
   * *Sensor Profile*: 1/2.3-inch CCD compact camera sensor, direct on-axis harsh mini-flash.
   * *Kelvin & Tone*: 5500K, localized specular highlights with rapid fall-off shadows into rich blacks, fine authentic digital noise.
2. **Muted Daylight Porcelain**:
   * *Optical Parameters*: 50mm f/1.8, overcast diffused cool daylight.
   * *Kelvin & Tone*: 6200K~6500K, desaturated yellow channels, gentle blue-gray tint preserving translucent skin radiance.
3. **Raw iPhone Front Camera**:
   * *Optics*: Equivalent 24mm micro wide-angle, zero beauty filtering, sharp natural hair and edge roll-off, ambient indoor fluorescent micro-grain.
4. **Hongdae Polaroid Instant**:
   * *Optics*: Vintage instant lens, subtle light leaks blending warm amber and cyan-blue, soft vignetting with signature white border texture.

#### C. 6 Signature Poses & Ergonomics
1. **Hands Holding Phone Obscuring Lower Face**: Holding smartphone at nose height, casually concealing lips and jawline while revealing sleepy, detached almond eyes.
2. **Looking Down Adjusting Windbreaker Collar**: Gaze cast downward 30 degrees, fingers casually adjusting hoodie drawstrings or trench lapels to catch a split-second candid moment.
3. **Tucking Flyaway Hair Behind Ear**: Index and middle fingers casually sweeping delicate baby hairs behind the ear, head tilted 15 degrees with cool detachment.
4. **First-Person POV Handing Iced Americano**: Looking slightly down from an elevated boyfriend POV as the subject hands over an iced drink cup, other hand in coat pocket.
5. **Crouching Compactly on Concrete Steps**: Knees gathered closely on architectural stairs, arms wrapping around shins, cheek gently resting against knees.
6. **Brisk Walk Corridor Head-Turn**: Body moving forward with momentum, head turning 90 degrees back toward the lens with dynamic motion blur across hair tips.

#### D. 4 Wardrobe Ensembles & Textile Physics
* **Clean Fit Minimalist Tailoring**: Oversized dropped-shoulder charcoal wool-blend blazer + tight white ribbed scoop-neck tank + fluid drape wide-leg trousers.
* **Seongsu-dong Utilitarian Gorpcore**: Matte GORE-TEX black shell jacket + washed ash-gray parachute pants + silver metallic runner sneakers.
* **Morning Boyish Loungewear**: Heavyweight 450gsm oatmeal cotton fleece hoodie + relaxed heather-gray knit shorts + white crew socks.
* **Signature Accessories**: Titanium micro hoop earrings, sleek black thin-frame rectangular glasses, moon bag, iced Americano paper cup.

#### E. Korea Cross-Model Production Prompts

##### Seedream 5.0 Pro (Volcengine Ark / Doubao)
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

### 2. Japan Edition —— Komorebi Airiness, Everyday Life Fragments, City Girl 35mm

> 📂 **Full Database Direct Access**: [👉 Explore Complete Japan Matrix: 660 Dual-Image Presets (日本/README.md)](日本/README.md)  
> *Covers Outfits (100), Filters (100), Expressions (100), Poses (100), Styles (100), Hosiery (60), Hair & Makeup (50), Props & Nails (50)*

#### A. Visual DNA & Philosophy
* **Aesthetic Core**: Ambient breathing room (*Komorebi*), warm film grain, unforced transparency and documentary presence.
* **Atmospheric Settings**: Sloping residential roads in Tokyo's shitamachi, afternoon wooden train station benches, brightly lit vending machines at twilight, Daikanyama bookstores.

#### B. 4 Core Filters & Optical Parameters
1. **Fujifilm Classic Neg**: Understated color saturation, deep rich emerald greens and muted blues, shadows with characteristic subtle magenta and olive-green roll-off. 5200K~5600K.
2. **Dreamcore Camcorder Glow**: Vintage handheld DV lens, delicate chromatic aberration, halation around high-contrast light sources, nostalgic soft atmospheric bloom.
3. **Muted Morning Transparency**: 35mm f/1.4 wide open, dapple light through foliage or blinds illuminating cheeks, golden backlit hair edges.
4. **QuickSnap Disposable Flash**: Plastic lens with slight spherical fall-off, direct flash creating warm flushed skin tones and deep vintage vignetting.

#### C. 6 Signature Poses & Ergonomics
1. **Crouching beside Vending Machine**: Knees tightly parallel, heels slightly raised, holding a warm canned drink with both hands and looking up into the lens.
2. **Crosswalk Stride Catch**: Striding laterally across a zebra crossing, turning head suddenly back toward the camera with hair swept in the breeze.
3. **Cupping Mug Warming Hands**: Wrapping both hands tightly around a ceramic mug, chin slightly tucked into a chunky knit scarf.
4. **Train Window Reflection**: Side profile close to train glass, gazing thoughtfully into the passing scenery with reflections creating double-exposure depth.
5. **Resting on Vintage Bicycle**: Foot planted on the ground, one hand on handlebar, the other adjusting a windblown beret.
6. **Peeking through Bookshelf Crevice**: Obscured behind rows of vintage paperbacks, revealing half her face while holding an open cloth-bound book.

#### D. 4 Wardrobe Ensembles & Textile Physics
* **Fudge Magazine British-Japanese Layering**: Beige double-breasted mac coat (high-density cotton twill) + deep moss-green cable-knit vest + light-blue Oxford shirt + dark pleated accordion skirt.
* **City Girl Utilitarian Workwear**: Washed olive-drab M-65 field jacket + heavyweight ecru wide-leg trousers + vintage suede German army trainers.
* **Summer Transparent Linen**: Washed white sleeveless linen dress + airy sand-beige knit cardigan + thin-strap woven sandals.
* **Signature Accessories**: Chunky cable-knit wool scarf, thick white cotton crew socks with brown leather penny loafers, raw canvas tote bag, metallic over-ear monitor headphones.

#### E. Japan Cross-Model Production Prompts

##### Seedream 5.0 Pro (Volcengine Ark / Doubao)
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

### 3. China Edition —— Neo-Chinese Quiet Luxury, Sculptural Bone Structure, Direct Night Flash

> 📂 **Full Database Direct Access**: [👉 Explore Complete China Matrix: 660 Dual-Image Presets (中国/README.md)](中国/README.md)  
> *Covers Outfits (100), Filters (100), Expressions (100), Poses (100), Styles (100), Hosiery (60), Hair & Makeup (50), Props & Nails (50)*

#### A. Visual DNA & Philosophy
* **Aesthetic Core**: Sculptural facial bone structure, aristocratic composure, Eastern negative space colliding with contemporary luxury.
* **Atmospheric Settings**: Bamboo shadows against gray brick courtyard walls in Suzhou, vermilion gates in Beijing hutongs at night, modernist art gallery atriums.

#### B. 4 Core Filters & Optical Parameters
1. **Ink & Bamboo Muted Green**: Desaturated, delicate ink-green and cool-gray bamboo undertones. Matte skin texture resembling mutton-fat white jade under overcast sky or courtyard skylight.
2. **Hard Flash Diva Red**: High-GN on-camera direct flash under 1.2 meters. Obsidian black night backdrop creating striking contrast against porcelain skin and bold crimson lips.
3. **Wong Kar-wai 90s Cinematic Nostalgia**: Kodak 5219 motion picture stock, deep crimson and amber blocks colliding, slight shutter drag light trails and dense organic grain.
4. **Museum Cold Minimalist**: 85mm f/1.4 prime lens, razor-sharp edge fidelity, sculptural shadow delineation across facial contours.

#### C. 6 Signature Poses & Ergonomics
1. **3/4 Profile Chin Slightly Lifted**: Body angled away, head turning 45 degrees toward the lens with chin elevated 10 degrees to accentuate jawline and neck contours.
2. **Fingertips Touching Jade Frog Button**: Hand raised gracefully with long fingers lightly resting on a traditional toggle, gaze distant and aristocratic.
3. **Leaning against Stone Balustrade Looking Back**: Leaning against a classical carved balustrade with back to the camera, upper body turned back with windblown hair across nose bridge.
4. **Striding Forward with Coat Billowing**: Walking briskly toward the lens, coat hem flowing with motion, one hand in trouser pocket, purposeful sovereign gaze.
5. **Seated before Vanity Mirror**: Side profile reflected in antique vanity mirror while holding lipstick or perfume vial hovering near lips.
6. **Chiaroscuro Silhouette**: Standing beside wooden louvered partitions, dividing face cleanly into light and deep geometric shadow.

#### D. 4 Wardrobe Ensembles & Textile Physics
* **Neo-Chinese Heavyweight Silk**: 30-momme crepe-satin sleeveless vest with handmade jade buttons + fluid black acetate wide-leg trousers.
* **Bespoke Double-Faced Cashmere**: Floor-length minimalist black pure cashmere coat + black turtleneck cashmere sweater + tailored trousers + pointed leather boots.
* **Vintage Crimson Silk Velvet Qipao**: High-slit dark crimson velvet qipao with subtle jacquard weave + black mink short shoulder cape.
* **Signature Accessories**: Natural icy jadeite stud earrings, baroque irregular freshwater pearl necklace, sterling silver bamboo hairpin, vintage gold-wire wireframe glasses.

#### E. China Cross-Model Production Prompts

##### Seedream 5.0 Pro (Volcengine Ark / Doubao)
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
Wardrobe & Textures: 30-momme heavy black silk faille jacket with handcrafted jade toggle closures, flowing tailored trousers. Minimalist Chinese jewelry in sterling silver and raw white nephrite jade. ISO 100 sharpness, raw textural skin mapping.
```

---

### 4. USA Edition —— Golden Hour Flare, Clean Girl, Uninhibited Street Energy

> 📂 **Full Database Direct Access**: [👉 Explore Complete USA Matrix: 660 Dual-Image Presets (美国/README.md)](美国/README.md)  
> *Covers Outfits (100), Filters (100), Expressions (100), Poses (100), Styles (100), Hosiery (60), Hair & Makeup (50), Props & Nails (50)*

#### A. Visual DNA & Philosophy
* **Aesthetic Core**: Sun-drenched vitality, honey-dewy radiant complexion, unapologetic athletic street confidence.
* **Atmospheric Settings**: Palm-lined avenues in Venice Beach, cast-iron facades in Soho NYC, convertible road trips along California Highway 1.

#### B. 4 Core Filters & Optical Parameters
1. **Golden Hour Flare**: Low-angle late afternoon sun under 10 degrees piercing the lens, casting radiant rim light along hair contours with creamy flare.
2. **Kodak Gold 200**: Warm nostalgic amber tones, golden highlights, saturated punchy reds and yellows with tight organic film grain.
3. **NYC Muted Blue Street**: High-contrast cool slate-blue shadows emphasizing the industrial steel and stone textures of Manhattan streets.
4. **Paparazzi Direct Flash**: High-speed direct on-axis flash freezing midnight street moments against dark city avenues.

#### C. 6 Signature Poses & Ergonomics
1. **Mid-Stride Zebra Crossing Laugh**: Striding across the avenue, arms swinging naturally, caught mid-laughter with vibrant authenticity.
2. **Walking Coffee Call**: Phone pressed to ear with one hand, large cold brew cup in the other, glancing toward oncoming yellow cabs.
3. **Leaning against Convertible Door**: Sunglasses hooked on index finger dipping over nose bridge, looking over frames with playful confidence.
4. **Cross-Legged on Beach Jetty**: Resting on concrete sea wall, one hand propping body, the other holding back sunlit honey waves in the ocean breeze.
5. **Mirror Lip Gloss Touch-Up**: Leaning into the car side-view mirror, eyes focused on applying sheer nude lip glaze.
6. **Skate Gliding Motion Capture**: Cruising on a skateboard with body leaning forward, hair streaming completely behind in the wind.

#### D. 4 Wardrobe Ensembles & Textile Physics
* **Clean Girl Elevated Athleisure**: Slate-gray seamless ribbed unitard + oversized oatmeal cashmere zip cardigan + chunky retro sneakers with white socks.
* **California Biker Chic**: Worn-in dark-brown distressed cowhide biker jacket + white cropped scoop tank + low-rise vintage straight denim + chunky belt.
* **Wall Street Casual Chic**: Sand-beige double-breasted linen blazer + high-waisted white wide-leg trousers + strappy leather sandals.
* **Signature Accessories**: Chunky gold hoop earrings, black oval sunglasses, stainless-steel insulated tumbler with straw, heavy canvas carryall tote.

#### E. USA Cross-Model Production Prompts

##### Seedream 5.0 Pro (Volcengine Ark / Doubao)
```text
真实街头生活抓拍照片，一位20岁出头的年轻美国女性，加州健康小麦肤色，清透水光肌，微乱蜂蜜浅棕色波浪长发随风扬起。自信大步横穿洛杉矶阳光街道斑马线，单手拿着一杯冰咖啡，侧头开怀大笑，神态充满活力感染力。身穿做旧棕色重磅牛皮机车夹克，内搭纯白罗纹短款背心，高腰复古水洗浅蓝直筒牛仔裤，佩戴夸张粗金圈耳环。身处加州午后刺眼落日黄金时刻，强烈金色逆光穿透发丝，镜头自然金色光晕，柯达Gold 200胶片浓郁暖调。保留真实毛孔、面料粗糙纹理与皮革磨损折痕，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感，3:4
```

##### ChatGPT (Image 2.5)
```text
An authentic 35mm candid street photograph capturing the effortlessly cool California Clean-Girl aesthetic. A 22-year-old woman with a glowing sun-kissed honey complexion and wind-tousled bronde beach waves. She strides confidently across a sunny Los Angeles crosswalk, holding an iced latte in one hand, looking over her shoulder with an infectious, genuine open-mouthed smile. She is wearing a distressed heavy brown leather moto jacket over a cropped white ribbed scoop-neck tank top and relaxed-fit vintage light-wash denim jeans, accessorized with thick chunky gold hoop earrings. Setting: golden hour along Venice Beach with warm low-angle sunlight backlighting her hair and creating authentic lens flare. Shot on Kodak Gold 200 film with rich warm tones, authentic film grain, visible fabric textures, and realistic skin micro-pores. 3:4.
```

##### Gemini (Imagen 3)
```text
Documentary fashion snapshot: Contemporary West Coast American lifestyle.
Subject: 22-year-old woman with sun-kissed dewy skin, effortless athletic poise, authentic facial micro-textures with faint sun freckles.
Framing & Dynamic: Full-length motion freeze, low 35mm focal perspective capturing an energetic stride across asphalt.
Lighting & Color: Low-angle late afternoon solar flare striking the camera sensor, creating luminous golden edge light around the subject's silhouette. Warm color temperature (3800K), rich Kodachrome-inspired reds and yellows, vibrant dynamic range.
Wardrobe: Heavyweight worn-in leather flight jacket, cropped white cotton tank, relaxed-fit stone-washed denim, chunky gold jewelry.
```

---

### 5. France Edition —— Laissez-faire Elegance, Parisian Muted Grey, French New Wave 16mm

> 📂 **Full Database Direct Access**: [👉 Explore Complete France Matrix: 660 Dual-Image Presets (法国/README.md)](法国/README.md)  
> *Covers Outfits (100), Filters (100), Expressions (100), Poses (100), Styles (100), Hosiery (60), Hair & Makeup (50), Props & Nails (50)*

#### A. Visual DNA & Philosophy
* **Aesthetic Core**: Laissez-faire casual elegance, rejection of artificial perfection, intellectual nuance, uncalculated bedhead.
* **Atmospheric Settings**: Outdoor wicker chairs at Les Deux Magots on Boulevard Saint-Germain, wrought-iron balconies overlooking zinc rooftops, vintage bouquinistes along the Seine.

#### B. 4 Core Filters & Optical Parameters
1. **Nouvelle Vague 16mm Film**: Organic coarse grain, gentle muted palette, subtle transitions through warm grey and café-au-lait hues.
2. **Parisian Muted Warm Grey**: Overcast soft Parisian diffused daylight, low contrast, enveloping facial contours like washed silk.
3. **Window Vermeer Backlight**: 50mm f/1.4, delicate lateral light through tall white shutters, Vermeer-like tranquil light balance.
4. **Cafe Window Reflection**: Shooting through imperfect café window glass with street traffic reflecting over the subject's contemplative gaze.

#### C. 6 Signature Poses & Ergonomics
1. **Outdoor Bistro Table Daydreaming**: Lounging on a rattan chair, cheek resting in one hand, open vintage paperback on the marble tabletop, gazing calmly into the street.
2. **Balcony Leaning over Haussmannian Rail**: Wearing an unbuttoned menswear shirt, leaning against carved railings with espresso in hand, breeze tousling curtain bangs.
3. **Twisting Hair with Tortoise Claw Clip**: Both arms raised behind head gathering hair, lips slightly parted holding a tortoiseshell clip.
4. **Seated on Persian Rug against Velvet Sofa**: Sinking onto a rug-covered wooden floor, resting back against a worn velvet sofa, legs curled naturally.
5. **Flipping through Yellowed Pages along Seine**: Standing beside emerald-green bookstalls, hands holding an unjacketed old volume with quiet concentration.
6. **Sidewalk Stroll Glancing Back**: Walking along cobblestones, turning head slightly toward the lens with an enigmatic half-smile.

#### D. 4 Wardrobe Ensembles & Textile Physics
* **Classic Breton Sailor Knit**: Heavyweight dropped-shoulder navy-and-white striped knit sweater + vintage high-waisted cropped flared denim + red ballet flats.
* **Laissez-faire Floral Tea Dress**: Deep V-neck tie-front silk chiffon floral wrap dress + slouchy oatmeal chunky knit cardigan with top buttons undone.
* **Left Bank Intellectual Tailoring**: Menswear-cut herringbone tweed blazer + washed white poplin shirt with open collar + vintage cognac leather belt.
* **Signature Accessories**: Woven wicker basket bag (Jane Birkin style), tortoiseshell hair clip, antique coin medallion pendant, effortless wispy curtain bangs (Bedhead).

#### E. France Cross-Model Production Prompts

##### Seedream 5.0 Pro (Volcengine Ark / Doubao)
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

## IV. Cross-Model Compiler Specifications

Generative models interpret prompt structures through fundamentally different attention mechanics, requiring targeted syntax translations:

| Dimension | Seedream 5.0 Pro (Volcengine / Doubao) | ChatGPT (Image 2.5) | Gemini (Imagen 3) |
|---|---|---|---|
| **Core Mechanism** | Raw photographic narrative flow + master reference consistency | Cohesive storytelling + tangible physical interaction details | Optical geometry + physical sensor parameters |
| **ID Anchoring** | Upload master sheet as `--ref` / image prompt | Hardcode identity anchor sentence + fixed seed | Provide contextual reference image + strict anatomical features |
| **Lighting Syntax** | `On-axis flash`, `soft diffused window light`, `low contrast` | Directional source descriptions, shadow geometry, specular reflections | Specific hardware, f-stops (`f/1.8`), Kelvin ratings |
| **Taboo Syntax** | Avoid abstract buzzwords ("breathtaking, masterpiece") | Avoid mechanical negative prompt dumping | Avoid anime/3D art terminology |

---

## V. Mixing Matrix Cheat Sheet

Like an audio engineer sliding faders on a studio console, you can freely mix and match across four primary tracks:

| Track | Track 1: Optics & Sensors | Track 2: Ergonomics & Pose | Track 3: Expressions & Gaze | Track 4: Wardrobe & Textile |
|---|---|---|---|---|
| **A** | 2000s Compact CCD Harsh Flash | Hands Holding Phone Obscuring Lower Face | Sleepy, eyes half-lidded and calm | Minimalist Oversized Dropped-Shoulder Blazer |
| **B** | Fujifilm Classic Neg Green Roll-off | Crouching by Street Machine, Warming Hands | Clear, curious, subtle corner-of-mouth smile | British Mac Coat + Cable-knit Vest |
| **C** | Night Street High-Contrast Hard Flash | 3/4 Profile Chin Elevated Touching Lapel | Regal, aloof, composed sovereign gaze | Modern Silk Mandarin Vest + Jade Button |
| **D** | California Golden Hour Solar Flare | 0.5x Wide-Angle Stride Laughing | Open laughter, vibrant contagious joy | Distressed Biker Leather + Low-Rise Denim |
| **E** | French New Wave 16mm Organic Grain | Outdoor Cafe Table Daydreaming | Laissez-faire, daydreamy, nostalgic | Breton Sailor Stripes + Red Ballet Flats |

> **Sample Recipe**: `[A Optics: CCD Flash]` + `[E Pose: Bistro Daydreaming]` + `[C Expression: Aloof Sovereign]` + `[D Wardrobe: Biker Leather]`  
> **Output Result**: A rebellious yet detached Y2K it-girl lounging at a midnight patio bar with cinematic contrast and high-fashion edge!

---

## VI. Automated Batch Generation Script (Tooling)

Iris includes an automated batch runner leveraging Volcengine Ark (Seedream 5.0 Pro):

```bash
# Navigate to Iris directory
cd 仓库/Iris

# Run test batch using master reference anchor and Korean porcelain aesthetics
python3 ../../bin/gen_image.py \
  "真实日常生活抓拍照片，一位20岁出头的年轻东亚女性，冷白皮，双手拿手机半遮脸对镜自拍，深灰西装，千禧CCD直闪，严格禁止二次元与3D塑料感，3:4" \
  --ratio 3:4 \
  --ref path/to/master_anchor.png
```

---

## VII. Contributing & Roadmap

- [x] **v0.1**: Core 5-country visual aesthetics matrix and three-engine compiler specifications.
- [ ] **v0.2**: Nordic Minimalism and British Grunge visual modules.
- [ ] **v0.3**: Interactive WebUI compiler tool and CLI utility.
- [ ] **v0.4**: 100 human-verified benchmark test sets and cross-model comparison charts.

PRs are warmly welcome for new cultural aesthetics, vintage film simulations, and kinetic camera setups!

---

<div align="center">
Created with passion by <a href="https://github.com/noahvisualsx">@noahvisualsx</a> • Open for Open Source Community
</div>
