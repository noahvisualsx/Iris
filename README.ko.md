<p align="right">
  <strong>Language:</strong>
  <a href="README.md"><b>简体中文</b></a> |
  <a href="README.en.md"><b>English</b></a> |
  <a href="README.ko.md"><b>한국어</b></a> |
  <a href="README.ja.md"><b>日本語</b></a>
</p>

# Iris (아이리스) · 글로벌 버추얼 휴먼 포토그래피 전 매트릭스 오픈소스 핸드북

> **The Aperture of Optics, The Soul in the Iris.**  
> 렌즈에 담긴 만상, 눈동자에 깃든 영혼. AI 버추얼 휴먼(가상 인간)을 위한 산업급 크로스 모델(ChatGPT Image 2.5 / Seedream 5.0 Pro / Gemini) 포토그래피 & 비주얼 전 매트릭스 제어 시스템.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Web Studio](https://img.shields.io/badge/Web%20Studio-Live%20on%20GitHub%20Pages-0071e3.svg)](https://noahvisualsx.github.io/Iris/)
[![Model Support](https://img.shields.io/badge/Model-Seedream%205.0%20Pro%20%7C%20ChatGPT%20Image%202.5%20%7C%20Gemini%20Imagen%203-blue.svg)](#iv-3대-ai-모델-컴파일러-규격)
[![Dataset: Korea](https://img.shields.io/badge/Korea%20Matrix-660%20Prompts%20Airtight%20Complete-success.svg)](韩国/README.md)
[![Korea: Filters](https://img.shields.io/badge/Korea-100%20Filters-blue.svg)](韩国/滤镜/README.md)
[![Korea: Poses](https://img.shields.io/badge/Korea-100%20Poses-purple.svg)](韩国/拍照姿势/README.md)
[![Korea: Outfits](https://img.shields.io/badge/Korea-100%20Outfits-orange.svg)](韩国/穿搭/README.md)
[![Korea: Hosiery](https://img.shields.io/badge/Korea-60%20Hosiery-pink.svg)](韩国/丝袜/README.md)
[![Korea: Styles](https://img.shields.io/badge/Korea-100%20Styles-green.svg)](韩国/风格/README.md)
[![Korea: Hair & Makeup](https://img.shields.io/badge/Korea-50%20Hair%20%26%20Makeup-red.svg)](韩国/发型与妆容/README.md)
[![Korea: Expressions](https://img.shields.io/badge/Korea-100%20Expressions-yellow.svg)](韩国/神态与微表情/README.md)
[![Korea: Props & Nails](https://img.shields.io/badge/Korea-50%20Props%20%26%20Nails-teal.svg)](韩国/道具与美甲/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#vii-기여하기--로드맵)

**AI 버추얼 휴먼(Digital Humans) 생성을 위한 산업급 크로스 모델 포토그래피 제어 시스템.**  
버추얼 휴먼 생성 시 발생하는 *"필터를 바꾸면 얼굴이 바뀌고, 포즈를 바꾸면 신체가 붕괴되며, 모델마다 결과물이 파편화되는"* 궁극의 엔지니어링 난제를 해결합니다.

[프로젝트 철학](#i-핵심-아키텍처-4차원-분리-제어-체계) • [5개국 매트릭스](#iii-5개국-전-매트릭스-시각-데이터베이스) • [모델 컴파일러](#iv-3대-ai-모델-컴파일러-규격) • [믹싱 매트릭스](#v-믹싱-콘솔-전-매트릭스-치트시트) • [페이스 락 규격](#ii-버추얼-휴먼-페이스-락-및-신원-보전-엔지니어링-규격)

</div>

---

## 목차

- [I. 핵심 아키텍처: 4차원 분리 제어 체계 (4D Decoupled Control)](#i-핵심-아키텍처-4차원-분리-제어-체계)
- [II. 버추얼 휴먼 페이스 락 및 신원 보전 엔지니어링 규격 (ID Anchoring)](#ii-버추얼-휴먼-페이스-락-및-신원-보전-엔지니어링-규격)
  - [1. 표준 마스터 시트 규격 (Master Sheet Standard)](#1-표준-마스터-시트-규격-master-sheet-standard)
  - [2. 범용 마스터 시트 프롬프트 코드 블록](#2-범용-마스터-시트-프롬프트-코드-블록)
- [III. 5개국 전 매트릭스 시각 데이터베이스 (The 5-Country Matrix)](#iii-5개국-전-매트릭스-시각-데이터베이스)
  - [1. 한국편 (Korea) —— 쿨톤 백옥 피부, 꾸안꾸 무드, Y2K CCD 노이즈](#1-한국편-korea--쿨톤-백옥-피부-꾸안꾸-무드-y2k-ccd-노이즈)
  - [2. 일본편 (Japan) —— 코모레비 감성, 일상의 조각, 시티걸 35mm 필름](#2-일본편-japan--코모레비-감성-일상의-조각-시티걸-35mm-필름)
  - [3. 중국편 (China) —— 신중식 콰이어트 럭셔리, 또렷한 골격미, 야간 직광 플래시](#3-중국편-china--신중식-콰이어트-럭셔리-또렷한-골격미-야간-직광-플래시)
  - [4. 미국편 (USA) —— 캘리포니아 골든아워, 클린걸, 자유분방한 스트리트](#4-미국편-usa--캘리포니아-골든아워-클린걸-자유분방한-스트리트)
  - [5. 프랑스편 (France) —— 레세페르의 무심한 우아함, 파리지앵 그레이, 누벨바그 16mm](#5-프랑스편-france--레세페르의-무심한-우아함-파리지앵-그레이-누벨바그-16mm)
- [IV. 3대 AI 모델 컴파일러 규격 (Cross-Model Compilers)](#iv-3대-ai-모델-컴파일러-규격)
  - [1. Seedream 5.0 Pro (화산엔진 / 더우바오)](#1-seedream-50-pro-화산엔진--더우바오)
  - [2. ChatGPT (Image 2.5)](#2-chatgpt-image-25)
  - [3. Gemini (Imagen 3)](#3-gemini-imagen-3)
- [V. 믹싱 콘솔 전 매트릭스 치트시트 (The Mixing Matrix)](#v-믹싱-콘솔-전-매트릭스-치트시트)
- [VI. 자동화 배치 생성 스크립트 (Tooling)](#vi-자동화-배치-생성-스크립트-tooling)
- [VII. 기여하기 & 로드맵 (Roadmap)](#vii-기여하기--로드맵)

---

## I. 핵심 아키텍처: 4차원 분리 제어 체계

기존 AI 생성 작업에서 가장 큰 문제는 **프롬프트 얽힘(Prompt Entanglement)**입니다. 프롬프트에 "CCD 플래시"나 "오버핏 블레이저" 같은 스타일 단어를 추가할 때, 파운데이션 모델이 캐릭터의 얼굴 골격, 나이, 심지어 인종적 정체성까지 임의로 바꿔버리기 일쑤였습니다.

Iris는 사운드 엔지니어링의 오디오 콘솔처럼 각 물리적/미학적 변수를 독립된 레이어로 분리하는 **4차원 분리 엔지니어링 아키텍처**를 적용했습니다:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: 인물 정체성 앵커 (골격, 이목구비, 헤어, 마스터 시트) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┼──────────────────────────────┐
│ Layer 2: 광학 시뮬레이션 및    │ Layer 3: 인체공학적 포즈 및   │
│ 센서 필터 (색온도, 렌즈 특성) │ 카메라 앵글/프레이밍          │
└──────────────────────────────┼──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Layer 4: 패션 소재, 물리적 텍스처 및 소품                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │ 크로스 모델 컴파일러 변환층  │
                 └──────┬──────┬──────┬──────┘
                        │      │      │
                        ▼      ▼      ▼
                   Seedream  ChatGPT Gemini
```

---

## II. 버추얼 휴먼 페이스 락 및 신원 보전 엔지니어링 규격

일관된 디지털 휴먼을 생성하려면 반드시 **"표준 마스터 시트 생성 + 특징 파라미터 앵커링"** 워크플로우를 준수해야 합니다:

### 1. 표준 마스터 시트 규격 (Master Sheet Standard)
* **화면 비율**: 엄격한 `3:4` (쇄골부터 정수리까지 포함하여 안면 특징 추출에 최적).
* **조명 환경**: 부드럽고 균일한 플랫 무영 조명 (스튜디오 디퓨즈 라이트, 강한 그림자 및 하이라이트 번짐 엄격 금지).
* **헤어 및 자세**: 자연스러운 흑발 생머리를 양쪽 귀 뒤로 넘겨 이마, 눈썹뼈, 귀 윤곽, 턱선을 완벽히 노출.
* **배경 및 착장**: 18% 뉴트럴 그레이 무봉제 배경, 심플한 화이트 크루넥 반팔 티셔츠 착용.

### 2. 범용 마스터 시트 프롬프트 코드 블록

```text
A front-facing master reference passport-grade portrait of a 22-year-old East Asian female. Features: balanced oval face contour, clear jawline, natural straight eyebrows, delicate inner double eyelids with subtle almond eye shape, straight well-proportioned nasal bridge, naturally relaxed lips with soft cupid's bow. Hair: natural sleek black straight hair tucked completely behind both ears, exposing forehead and ear contours. Neutral relaxed facial expression, mouth gently closed. Studio flat neutral diffused light, no harsh shadows, 18% neutral grey backdrop, wearing a plain white crewneck t-shirt. Ultra-photorealistic 8k, raw skin texture with pores and micro-texture, 3:4 aspect ratio.
```

---

## III. 5개국 전 매트릭스 시각 데이터베이스

---

### 1. 한국편 (Korea) —— 쿨톤 백옥 피부, 꾸안꾸 무드, Y2K CCD 노이즈

#### A. 비주얼 유전자 및 미학 철학
* **미학 핵심**: 부담 없는 편안함(꾸안꾸 · Effortless), 쿨톤 세미 매트 백옥 피부, 저채도 미니멀리즘.
* **대표적 공간**: 성수동 콘크리트 미니멀 카페, 심야 아파트 화이트 벽면, 한남동 편집숍 전신거울 앞.

#### B. 4대 핵심 필터 및 광학 파라미터
1. **2000년대 컴팩트 CCD 플래시 (2000s Compact CCD Flash)**:
   * *센서 특성*: 1/2.3인치 소형 CCD 센서, 온카메라 직광 미니 플래시.
   * *색온도 및 톤*: 5500K, 이마와 콧등의 국소 반사광, 짙은 블랙으로 급격히 떨어지는 그림자, 특유의 자글자글한 디지털 노이즈.
2. **쿨톤 백옥 피부 자연광 디퓨즈 (Muted Daylight Porcelain)**:
   * *광학 사양*: 50mm f/1.8, 흐린 날 창가 대면적 소프트 자연광.
   * *색온도 및 톤*: 6200K~6500K, 옐로우 채도를 정밀하게 낮춘 블루그레이 톤으로 투명한 피부 결 보존.
3. **아이폰 전면 기본 카메라 생카 (Raw iPhone Front Camera)**:
   * *광학 특성*: 환산 24mm 마이크로 광각, 뷰티 필터 없는 생얼 결, 머리카락과 림 라인의 선명함, 실내 형광등 미세 입자.
4. **홍대 감성 폴라로이드 (Hongdae Polaroid Instant)**:
   * *광학 특성*: 빈티지 인스턴트 렌즈 특유의 따스한 앰버와 시안 블루 빛샘, 부드러운 비네팅과 흰색 프레임 질감.

#### C. 6대 시그니처 포즈 및 인체공학
1. **두 손으로 폰 쥐고 하관 가린 거울 셀카**: 폰을 콧등 높이로 들어 하관을 자연스럽게 가리고 살짝 나른한 눈매만 노출.
2. **시선 내리며 후드 스트링/깃 정리하기**: 시선을 30도 아래로 내리고 후드 끈이나 재킷 칼라를 자연스럽게 매만지는 일상 찰나.
3. **한 손으로 옆머리 넘기며 살짝 내려다보기**: 검지와 중지로 잔머리를 귀 뒤로 살짝 넘기며 고개를 15도 기울여 쿨한 거리감 연출.
4. **아이스 아메리카노 건네는 1인칭 남친 시점 (POV)**: 약간 높은 각도에서 내려다보는 구도로 테이크아웃 잔을 건네는 일상적 인터랙션.
5. **계단에 웅크려 앉아 무릎 안기**: 콘크리트 계단에서 무릎을 모아 안고 뺨을 무릎에 살짝 기댄 편안한 자세.
6. **복도를 걸어가며 뒤돌아보기 (헤드턴)**: 앞으로 걸어가는 동세에서 고개만 90도 돌려 카메라를 응시, 흩날리는 모션 블러 머릿결.

#### D. 4가지 스타일링 및 텍스처 라이브러리
* **클린핏 미니멀 테일러링**: 오버사이즈 드롭숄더 챠콜 울 블레이저 + 화이트 슬림핏 골지 나시 + 유려하게 떨어지는 와이드 슬랙스.
* **성수동 고프코어 스트리트**: 매트 블랙 고어텍스 바람막이 쉘 재킷 + 워싱 그레이 파라슈트 팬츠 + 실버 러닝화.
* **이른 아침 내추럴 보이지 룩**: 450g 헤비웨이트 오트밀 후드티 + 루즈핏 헤더그레이 니트 쇼츠 + 화이트 크루 삭스.
* **시그니처 액세서리**: 미니멀 티타늄 링 귀걸이, 얇은 블랙 사각 긱시크 안경, 블랙 가죽 반달백, 테이크아웃 종이컵.

#### E. 한국편 크로스 모델 프롬프트

##### Seedream 5.0 Pro (화산엔진 / 더우바오)
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

### 2. 일본편 (Japan) —— 코모레비 감성, 일상의 조각, 시티걸 35mm 필름

#### A. 비주얼 유전자 및 미학 철학
* **미학 핵심**: 나뭇잎 사이로 비치는 햇살과 바람의 호흡(코모레비 · 木漏れ日), 따스한 필름 그레인, 인위적이지 않은 투명감.
* **대표적 공간**: 도쿄 시타마치 주택가 비탈길, 오후 한적한 기차역 나무 벤치, 따스한 불빛의 자판기 앞, 다이칸야마 서점.

#### B. 4대 핵심 필터 및 광학 파라미터
1. **후지필름 클래식 네거티브 (Fujifilm Classic Neg)**: 내향적인 채도, 깊은 청록빛 그림자와 특유의 마젠타-올리브 롤오프, 5200K~5600K.
2. **빈티지 캠코더 드림코어 (Dreamcore Camcorder Glow)**: 90년대 핸디캠 렌즈, 미세한 색수차와 광원 주변의 몽환적인 헤일레이션(Halation).
3. **아침 햇살 바람 디퓨즈 (Muted Morning Transparency)**: 35mm f/1.4 최대 개방, 나뭇잎 그림자가 뺨에 드리우고 역광으로 빛나는 머리카락 라인.
4. **일회용 필름 카메라 퀵스냅 (QuickSnap Disposable Flash)**: 플라스틱 단렌즈의 미세 왜곡, 직광 플래시의 붉은 생기, 감성적인 림 비네팅.

#### C. 6대 시그니처 포즈 및 인체공학
1. **자판기 옆 쪼그려 앉기**: 무릎을 가지런히 모으고 발꿈치를 살짝 든 채 따뜻한 캔 음료를 두 손으로 감싸 쥐고 올려다보는 시선.
2. **횡단보도 중간 성큼 걷기**: 보폭을 넓혀 길을 건너다 카메라 쪽으로 고개를 돌리며 바람에 스커트 자락이 휘날리는 찰나.
3. **머그컵 감싸 쥐고 입김 불기**: 두 손으로 머그잔을 꼭 쥐고 턱을 도톰한 머플러 속에 살짝 묻은 청순한 눈빛.
4. **전철 창문 반영과 사색**: 차창 유리에 뺨을 가까이 대고 창밖 풍경을 바라보며 창문 반영과 얼굴이 오버랩되는 이중 깊이감.
5. **빈티지 자전거 세우고 멈추기**: 자전거 안장에 앉아 한 발로 땅을 딛고 한 손은 바람에 날리는 베레모를 누르는 포즈.
6. **서가 틈새로 살짝 엿보기**: 서가 뒤에 살짝 숨어 한 손으로 양장본 책을 든 채 반쪽 얼굴만 드러낸 호기심 어린 시선.

#### D. 4가지 스타일링 및 텍스처 라이브러리
* **퍼지(Fudge) 매거진 보이시 레이어드**: 베이지 더블 맥코트(고밀도 면 트윌) + 딥그린 케이블 니트 베스트 + 스카이블루 옥스퍼드 셔츠 + 다크 차콜 플리츠 스커트.
* **시티걸 워크웨어 캐주얼**: 워싱 올리브 M-65 야상 재킷 + 에크루 컬러 헤비 와이드 팬츠 + 스웨이드 독일군 스니커즈.
* **여름날 투명한 린넨 룩**: 화이트 민소매 린넨 원피스 + 샌드베이지 얇은 가디건 + 스트랩 위빙 샌들.
* **시그니처 액세서리**: 굵은 짜임 울 머플러, 화이트 크루 삭스 & 브라운 로퍼, 워싱 캔버스 토트백, 헤드폰.

#### E. 일본편 크로스 모델 프롬프트

##### Seedream 5.0 Pro (화산엔진 / 더우바오)
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

### 3. 중국편 (China) —— 신중식 콰이어트 럭셔리, 또렷한 골격미, 야간 직광 플래시

#### A. 비주얼 유전자 및 미학 철학
* **미학 핵심**: 타고난 안면 골격미, 당당하고 여유로운 아우라, 동양적 여백의 미와 현대적 하이엔드 럭셔리의 충돌.
* **대표적 공간**: 쑤저우 정원의 대나무 그림자와 벽돌담, 베이징 후퉁의 붉은 대문 앞, 현대 미술관의 콘크리트 중정.

#### B. 4대 핵심 필터 및 광학 파라미터
1. **신중식 수묵 톤 (Ink & Bamboo Muted Green)**: 저채도의 묵록색과 차가운 그레이 대나무 음영. 백옥 같은 매트한 피부 결감과 명확한 안면 명암선.
2. **레드 포인트 야간 하드 플래시 (Hard Flash Diva Red)**: 강력한 직광 플래시로 배경을 칠흑으로 누르고 백옥 피부와 클래식 레드 립을 극적으로 대비.
3. **왕가위 감성 90년대 시네마틱 (Hong Kong 90s Cinematic Nostalgia)**: 코닥 5219 영화용 필름, 강렬한 레드-앰버 컬러 블록과 셔터 드래그 잔상.
4. **미술관 쿨 미니멀 (Museum Cold Minimalist)**: 85mm f/1.4 단렌즈의 극강의 선예도로 조각상 같은 음영 윤곽 구현.

#### C. 6대 시그니처 포즈 및 인체공학
1. **턱을 살짝 든 3/4 측면 앵글**: 몸을 비스듬히 돌리고 턱을 10도 살짝 들어 날렵한 턱선과 우아한 목선을 강조하는 앵글.
2. **매듭 단추를 매만지는 손가락 디테일**: 한 손을 우아하게 들어 깃의 옥 매듭 단추를 살짝 만지며 무심하게 응시하는 시선.
3. **난간에 기대어 뒤돌아보기**: 고풍스러운 석조 난간에 등을 대고 상체만 돌려 콧등을 스치는 머리칼과 함께 렌즈를 바라보기.
4. **펄럭이는 코트 자락과 당당한 걸음걸이**: 롱코트 자락을 휘날리며 성큼 걸어오는 여유롭고 당당한 포즈.
5. **경대 거울을 보며 립 바르기**: 앤틱 화장대 거울에 비친 단아한 옆모습과 입술 근처에 멈춘 립스틱 손끝.
6. **빛과 그림자의 빗살무늬 분할**: 블라인드나 창살 틈으로 들어오는 강한 빛으로 얼굴을 명과 암으로 분할하는 드라마틱 앵글.

#### D. 4가지 스타일링 및 텍스처 라이브러리
* **신중식 헤비 실크 베스트 룩**: 30모미 블랙 실크 슬리브리스 차이나카라 베스트 + 찰랑이는 블랙 아세테이트 와이드 팬츠.
* **캐시미어 롱코트 아우라**: 발목까지 오는 블랙 더블페이스 캐시미어 롱코트 + 블랙 터틀넥 니트 + 핀턱 슬랙스.
* **빈티지 레드 실크 벨벳 치파오**: 딥레드 벨벳 하이슬릿 치파오 + 밍크 숄.
* **시그니처 액세서리**: 천연 비취 스터드 귀걸이, 담수 진주 네크리스, 은제 대나무 비녀.

#### E. 중국편 크로스 모델 프롬프트

##### Seedream 5.0 Pro (화산엔진 / 더우바오)
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

### 4. 미국편 (USA) —— 캘리포니아 골든아워, 클린걸, 자유분방한 스트리트

#### A. 비주얼 유전자 및 미학 철학
* **미학 핵심**: 햇살을 머금은 건강한 생명력, 은은한 허니 글로우 스킨, 자신감 넘치는 애슬레틱 스트리트 무드.
* **대표적 공간**: LA 베니스 비치 야자수 거리, 뉴욕 소호(SoHo)의 주철 건축물 골목, 캘리포니아 1번 국도 컨버터블 위.

#### B. 4대 핵심 필터 및 광학 파라미터
1. **캘리포니아 선셋 골든아워 플레어 (Golden Hour Flare)**: 10도 이하로 내려앉은 강렬한 역광이 머리칼 테두리를 금빛으로 물들이며 자연스러운 렌즈 플레어 연출.
2. **코닥 골드 200 (Kodak Gold 200)**: 진하고 따스한 앰버 톤, 풍부한 레드와 옐로우의 발색, 조밀한 유기적 필름 그레인.
3. **뉴욕 시티 블루 스트리트 (NYC Muted Blue Street)**: 맨해튼의 마천루와 아스팔트를 담아내는 고대비 쿨톤 슬레이트 블루 음영.
4. **파파라치 야간 직광 플래시 (Paparazzi Direct Flash)**: 헐리우드 파파라치 스냅처럼 찰나를 얼어붙게 만드는 날카로운 콘트라스트.

#### C. 6대 시그니처 포즈 및 인체공학
1. **횡단보도를 가로지르며 활짝 웃기**: 양팔을 흔들며 성큼 걷다가 환하게 터뜨리는 싱그럽고 에너지 넘치는 웃음.
2. **한 손에 커피 들고 통화하며 걷기**: 한 손으로 전화를 받으며 다른 손에 텀블러를 들고 지나가는 택시를 쳐다보는 순간.
3. **오픈카 문에 기대어 선글라스 내리기**: 차 문에 기대어 검지로 선글라스 프레임을 살짝 내려 눈을 마주치는 매력적인 포즈.
4. **방파제 둑에 걸터앉아 머리 쓸어넘기기**: 바닷바람에 흩날리는 금갈색 웨이브를 한 손으로 쓸어넘기며 앉아있는 여유.
5. **사이드미러를 보며 립글로스 덧바르기**: 자동차 거울에 시선을 고정하고 자연스러운 누드톤 립글로스를 바르는 집중된 표정.
6. **스케이트보드 활주 모션 스냅**: 스케이트보드 위에 한 발을 얹고 바람을 가르며 달리는 역동적인 스냅.

#### D. 4가지 스타일링 및 텍스처 라이브러리
* **클린걸 애슬레저 룩**: 차콜 골지 바디슈트 + 오트밀 캐시미어 집업 가디건 + 레트로 청키 스니커즈 & 화이트 삭스.
* **캘리포니아 바이커 시크**: 빈티지 브라운 헤비 가죽 라이더 재킷 + 화이트 크롭 나시 + 로우라이즈 워싱 스트레이트 데님.
* **월스트리트 캐주얼 수트**: 샌드베이지 린넨 더블 블레이저 + 화이트 와이드 슬랙스 + 스트랩 샌들.
* **시그니처 액세서리**: 볼드한 청키 골드 링 귀걸이, 블랙 타원형 선글라스, 대용량 스탠리 텀블러, 캔버스 쇼퍼백.

#### E. 미국편 크로스 모델 프롬프트

##### Seedream 5.0 Pro (화산엔진 / 더우바오)
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

### 5. 프랑스편 (France) —— 레세페르의 무심한 우아함, 파리지앵 그레이, 누벨바그 16mm

#### A. 비주얼 유전자 및 미학 철학
* **미학 핵심**: 무심하고 자연스러운 우아함(Laissez-faire), 과도한 연출의 거부, 지적인 뉘앙스, 살짝 흐트러진 내추럴 헤어.
* **대표적 공간**: 생제르맹 데프레 레되마고 테라스, 하이실링 아파트의 발코니 난간, 센강 변의 오래된 녹색 고서점(부키니스트).

#### B. 4대 핵심 필터 및 광학 파라미터
1. **누벨바그 16mm 영화 필름 (Nouvelle Vague 16mm)**: 거칠고 서정적인 유기적 입자감, 채도를 뺀 카페오레 톤의 부드러운 전환.
2. **파리지앵 오버캐스트 그레이 (Parisian Muted Warm Grey)**: 파리 특유의 흐린 하늘이 만드는 부드러운 디퓨즈 조명과 풍부한 명암 디테일.
3. **창가 역광 베르메르 조명 (Window Vermeer Backlight)**: 50mm f/1.4, 하얀 목재 블라인드 사이로 새어드는 정적인 유화 톤 라이팅.
4. **카페 유리창 이중 반영 (Cafe Window Reflection)**: 살짝 김 서린 카페 창문을 투과하여 거리 풍경과 인물의 옆얼굴이 몽환적으로 겹쳐지는 구도.

#### C. 6대 시그니처 포즈 및 인체공학
1. **야외 비스트로 테이블에서 턱 괴고 멍때리기**: 등나무 의자에 비스듬히 앉아 턱을 괴고 낡은 페이퍼백을 펼쳐둔 채 행인을 바라보는 포즈.
2. **오스만 양식 발코니에 기대어 지붕 내려다보기**: 루즈핏 셔츠를 입고 조각된 난간에 기대어 에스프레소를 든 채 바람을 느끼는 모습.
3. **집게핀을 입에 물고 머리 말아 올리기**: 두 팔을 올려 머리를 모으고 입술 사이로 호피 무늬 집게핀을 살짝 문 나른한 찰나.
4. **러그에 앉아 오래된 소파에 기대기**: 페르시안 카펫 바닥에 편안하게 앉아 빛바랜 벨벳 소파에 등을 기댄 포즈.
5. **센강 변에서 낡은 고서 넘기기**: 녹색 서점 상자 옆에 서서 표지 없는 책을 두 손으로 넘기며 몰입하는 지적인 순간.
6. **돌길을 걷다 살짝 뒤돌아보기**: 자갈길을 걷다가 카메라를 살짝 응시하며 알 듯 모를 듯한 미소를 머금은 표정.

#### D. 4가지 스타일링 및 텍스처 라이브러리
* **클래식 브레통 스트라이프**: 루즈핏 네이비-화이트 스트라이프 니트 + 하이웨이스트 크롭 세미부츠컷 생지 데님 + 레드 플랫 발레슈즈.
* **나른한 플로럴 랩 드레스**: 딥 V넥 타이 프런트 실크 쉬폰 플로럴 원피스 + 오트밀 청키 가디건.
* **좌안 지식인 테일러링**: 매니시 컷 헤링본 트위드 재킷 + 단추를 두 개 푼 화이트 셔츠 + 빈티지 레더 벨트.
* **시그니처 액세서리**: 핸드메이드 라탄 바스켓 백(제인 버킨 스타일), 호피 무늬 집게핀, 앤틱 코인 목걸이, 자연스러운 시스루 사이드뱅.

#### E. 프랑스편 크로스 모델 프롬프트

##### Seedream 5.0 Pro (화산엔진 / 더우바오)
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

## IV. 3대 AI 모델 컴파일러 규격

각 생성형 AI 모델은 프롬프트를 해석하는 메커니즘이 근본적으로 다르므로 엔진별 맞춤 변환이 필수적입니다:

| 항목 | Seedream 5.0 Pro (화산엔진 / 더우바오) | ChatGPT (Image 2.5) | Gemini (Imagen 3) |
|---|---|---|---|
| **핵심 메커니즘** | 리얼 사진 내러티브 서술 + 마스터 시트 일관성 | 응집력 있는 상황 묘사 + 구체적 물리 인터랙션 | 광학 기하학 + 물리적 카메라 센서 파라미터 |
| **페이스 락** | 마스터 시트를 `--ref` / 이미지 프롬프트로 첨부 | 캐릭터 기저 문장 고정 + 시드값 고정 | 레퍼런스 이미지 컨텍스트 + 정밀 이목구비 묘사 |
| **조명 제어** | `온카메라 직광`, `소프트 창가광`, `로우 콘트라스트` | 광원 방향, 그림자 형태, 반사 하이라이트 기술 | 특정 하드웨어 기종, 조리개 `f/1.8`, 켈빈 색온도 |
| **금기 사항** | 추상적인 형용사 뭉텅이 남발 지양 | 기계적인 네거티브 프롬프트 나열 지양 | 3D/애니메이션 계열 키워드 지양 |

---

## V. 믹싱 콘솔 전 매트릭스 치트시트

음악 프로듀서가 믹서 콘솔의 페이더를 올리고 내리듯, 4대 핵심 트랙을 자유롭게 크로스오버하여 조합할 수 있습니다:

| 모듈 | 트랙 1: 필터 및 광학 (Optics) | 트랙 2: 포즈 및 동세 (Pose) | 트랙 3: 표정 및 시선 (Expression) | 트랙 4: 패션 및 소재 (Textile) |
|---|---|---|---|---|
| **A** | 2000년대 컴팩트 CCD 직광 플래시 | 두 손으로 폰 쥐고 하관 가린 거울 셀카 | 나른하게 살짝 감긴 눈, 무심한 쿨함 | 미니멀 오버사이즈 드롭숄더 블레이저 |
| **B** | 후지 클래식 네거티브 그린 톤 | 자판기 옆 쪼그려 앉아 온음료 쥐기 | 맑고 호기심 가득한 눈매, 엷은 미소 | 브리티시 맥코트 + 케이블 니트 베스트 |
| **C** | 야간 스트리트 고대비 하드 플래시 | 3/4 측면 턱을 들고 깃 단추 만지기 | 도도하고 범접할 수 없는 아우라 | 모던 실크 차이나카라 베스트 + 옥 단추 |
| **D** | 캘리포니아 선셋 골든아워 플레어 | 0.5x 광각으로 성큼 걸으며 웃기 | 활짝 터뜨리는 전염성 강한 웃음 | 빈티지 디스트레스드 라이더 + 로우 데님 |
| **E** | 누벨바그 16mm 거친 입자 필름 | 카페 야외 테이블에서 턱 괴고 사색 | 무심하고 나른한 뉘앙스의 몽환적 눈빛 | 브레통 스트라이프 니트 + 레드 발레슈즈 |

> **믹싱 예시**: `[A 필터: CCD 플래시]` + `[E 포즈: 비스트로 사색]` + `[C 표정: 도도한 아우라]` + `[D 착장: 가죽 라이더 재킷]`  
> **결과물**: 심야 야외 테라스 바에서 무심하게 사색에 잠긴, 반전 매력의 Y2K 힙스터 룩 완성!

---

## VI. 자동화 배치 생성 스크립트

본 프로젝트에는 Volcengine Ark (Seedream 5.0 Pro) 기반의 배치 생성 및 마스터 시트 일관성 테스트 스크립트가 내장되어 있습니다:

```bash
# 작업 디렉토리 진입
cd 仓库/Iris

# 마스터 시트 + 한국 쿨톤 백옥 피부 필터 배치 테스트 실행
python3 ../../bin/gen_image.py \
  "真实日常生活抓拍照片，一位20岁出头的年轻东亚女性，冷白皮，双手拿手机半遮脸对镜自拍，深灰西装，千禧CCD直闪，严格禁止二次元与3D塑料感，3:4" \
  --ratio 3:4 \
  --ref path/to/master_anchor.png
```

---

## VII. 기여하기 & 로드맵

- [x] **v0.1**: 5개국(한/일/중/미/프) 핵심 비주얼 자산 라이브러리 및 3대 모델 컴파일러 규격 완성.
- [ ] **v0.2**: 북유럽 미니멀리즘(Nordic) 및 브리티시 그런지(British Grunge) 비주얼 모듈 추가.
- [ ] **v0.3**: 믹싱 콘솔 설정을 기반으로 프롬프트를 자동 생성하는 인터랙티브 WebUI 툴 및 CLI 도구 공개.
- [ ] **v0.4**: 100세트의 실제 인물 벤치마크 테스트 및 모델별 비교 도표 공개.

새로운 국가별 미학, 빈티지 필름 시뮬레이션 및 포즈/카메라 앵글 기여를 언제든 환영합니다!

---

<div align="center">
Created with passion by <a href="https://github.com/noahvisualsx">@noahvisualsx</a> • Open for Open Source Community
</div>
