<p align="right">
  <strong>Language:</strong>
  <a href="README.md"><b>简体中文</b></a> |
  <a href="README.en.md"><b>English</b></a> |
  <a href="README.ko.md"><b>한국어</b></a> |
  <a href="README.ja.md"><b>日本語</b></a>
</p>

# Iris (アイリス / 虹鏡) · グローバルバーチャルヒューマン写真全マトリクス オープンソースハンドブック

> **The Aperture of Optics, The Soul in the Iris.**  
> レンズに映る森羅万象、瞳に宿る魂。AIバーチャルヒューマン（デジタルヒューマン）のための産業級クロスモデル（ChatGPT Image 2.5 / Seedream 5.0 Pro / Gemini）写真＆ビジュアル全マトリクス制御システム。

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Web Studio](https://img.shields.io/badge/Web%20Studio-Live%20on%20GitHub%20Pages-0071e3.svg)](https://noahvisualsx.github.io/Iris/)
[![Model Support](https://img.shields.io/badge/Model-Seedream%205.0%20Pro%20%7C%20ChatGPT%20Image%202.5%20%7C%20Gemini%20Imagen%203-blue.svg)](#iv-3大モデルコンパイラ仕様)
[![Dataset: Korea](https://img.shields.io/badge/Korea%20Matrix-660%20Prompts%20Airtight%20Complete-success.svg)](韩国/README.md)
[![Korea: Filters](https://img.shields.io/badge/Korea-100%20Filters-blue.svg)](韩国/滤镜/README.md)
[![Korea: Poses](https://img.shields.io/badge/Korea-100%20Poses-purple.svg)](韩国/拍照姿势/README.md)
[![Korea: Outfits](https://img.shields.io/badge/Korea-100%20Outfits-orange.svg)](韩国/穿搭/README.md)
[![Korea: Hosiery](https://img.shields.io/badge/Korea-60%20Hosiery-pink.svg)](韩国/丝袜/README.md)
[![Korea: Styles](https://img.shields.io/badge/Korea-100%20Styles-green.svg)](韩国/风格/README.md)
[![Korea: Hair & Makeup](https://img.shields.io/badge/Korea-50%20Hair%20%26%20Makeup-red.svg)](韩国/发型与妆容/README.md)
[![Korea: Expressions](https://img.shields.io/badge/Korea-100%20Expressions-yellow.svg)](韩国/神态与微表情/README.md)
[![Korea: Props & Nails](https://img.shields.io/badge/Korea-50%20Props%20%26%20Nails-teal.svg)](韩国/道具与美甲/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#vii-コントリビューション--ロードマップ)

**AIバーチャルヒューマン（Digital Humans）生成のための産業級クロスモデル写真制御システム。**  
バーチャルヒューマン生成において長年の課題であった「フィルターを変えると顔が変わる、ポーズを変えると破綻する、モデルごとに品質が分裂する」というエンジニアリングの難問を根本から解決します。

[設計思想](#i-コアアーキテクチャ4次元デカップリング制御体系) • [5カ国マトリクス](#iii-5カ国全マトリクス視覚データベース) • [モデルコンパイラ](#iv-3大モデルコンパイラ仕様) • [ミキサー速見表](#v-ミキシングコンソール全マトリクス速見表) • [顔固定仕様](#ii-バーチャルヒューマン顔固定id-anchoringエンジニアリング仕様)

</div>

---

## 目次

- [I. コアアーキテクチャ：4次元デカップリング制御体系 (4D Decoupled Control)](#i-コアアーキテクチャ4次元デカップリング制御体系)
- [II. バーチャルヒューマン顔固定（ID Anchoring）エンジニアリング仕様](#ii-バーチャルヒューマン顔固定id-anchoringエンジニアリング仕様)
  - [1. 標準マスターシート仕様 (Master Sheet Standard)](#1-標準マスターシート仕様-master-sheet-standard)
  - [2. 汎用マスターシート用プロンプトコードブロック](#2-汎用マスターシート用プロンプトコードブロック)
- [III. 5カ国全マトリクス視覚データベース (The 5-Country Matrix)](#iii-5カ国全マトリクス視覚データベース)
  - [1. 韓国編 (Korea) —— クールトーン白肌、エフォートレスな抜け感、Y2K CCD粒子](#1-韓国編-korea--クールトーン白肌エフォートレスな抜け感y2k-ccd粒子)
  - [2. 日本編 (Japan) —— 木漏れ日の空気感、日常の断片、シティガール35mmフィルム](#2-日本編-japan--木漏れ日の空気感日常の断片シティガール35mmフィルム)
  - [3. 中国編 (China) —— 新中式クワイエットラグジュアリー、洗練された骨格美、夜間直光フラッシュ](#3-中国編-china--新中式クワイエットラグジュアリー洗練された骨格美夜間直光フラッシュ)
  - [4. 米国編 (USA) —— カリフォルニアの夕暮れゴールド、クリーンガール、ストリートの自由](#4-米国編-usa--カリフォルニアの夕暮れゴールドクリーンガールストリートの自由)
  - [5. フランス編 (France) —— レッセフェールの気だるい気品、パリジャングレー、ヌーヴェルヴァーグ16mm](#5-フランス編-france--レッセフェールの気だるい気品パリジャングレーヌーヴェルヴァーグ16mm)
- [IV. 3大モデルコンパイラ仕様 (Cross-Model Compilers)](#iv-3大モデルコンパイラ仕様)
  - [1. Seedream 5.0 Pro (Volcengine Ark / 豆包)](#1-seedream-50-pro-volcengine-ark--豆包)
  - [2. ChatGPT (Image 2.5)](#2-chatgpt-image-25)
  - [3. Gemini (Imagen 3)](#3-gemini-imagen-3)
- [V. ミキシングコンソール全マトリクス速見表 (The Mixing Matrix)](#v-ミキシングコンソール全マトリクス速見表)
- [VI. 自動バッチ画像生成スクリプト (Tooling)](#vi-自動バッチ画像生成スクリプト-tooling)
- [VII. コントリビューション & ロードマップ (Roadmap)](#vii-コントリビューション--ロードマップ)

---

## I. コアアーキテクチャ：4次元デカップリング制御体系

従来のAI画像生成における最大の課題は**プロンプトの絡み合い（Prompt Entanglement）**にありました。「CCDフラッシュ」や「オーバーサイズブレザー」といった要素をプロンプトに追加すると、生成モデルがキャラクターの顔立ちの骨格、年齢、さらには人種的特徴までも意図せず書き換えてしまうことが頻発していました。

Irisは、音楽制作のミキシングコンソールのように各物理的・美学的変数を完全に独立したレイヤーとして分離する**4次元デカップリング・エンジニアリングアーキテクチャ**を採用しています：

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: 人物アイデンティティアンカー (骨格、目鼻立ち、髪型、原図) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────┼──────────────────────────────┐
│ Layer 2: 光学シミュレーション   │ Layer 3: 人体工学ポーズ及び   │
│ 及びセンサーフィルター (色温度) │ カメラアングル・フレーミング │
└──────────────────────────────┼──────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────┐
│ Layer 4: コーディネート素材、物理テクスチャ及び小物・プロップ │
└──────────────────────────────┬──────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │ クロスモデルコンパイラ変換層│
                 └──────┬──────┬──────┬──────┘
                        │      │      │
                        ▼      ▼      ▼
                   Seedream  ChatGPT Gemini
```

---

## II. バーチャルヒューマン顔固定（ID Anchoring）エンジニアリング仕様

一貫したデジタルヒューマンを生成するためには、**「標準マスターシート生成 ＋ 特徴量アンカーリング」**ワークフローを厳密に遵守する必要があります：

### 1. 標準マスターシート仕様 (Master Sheet Standard)
* **アスペクト比**：厳密に `3:4`（鎖骨から頭頂部までを収め、顔の特徴抽出に最適）。
* **ライティング環境**：柔らかく均一なフラット無影光（スタジオディフューズ光。強い影や白飛びハイライトは厳禁）。
* **髪型・姿勢**：自然な黒髪ストレートを完全に両耳の後ろにかけ、額、眉骨、両耳の輪郭、フェイスラインを完全に露出。
* **背景・衣装**：18%ニュートラルグレーのシームレス背景。シンプルな白いコットンクルーネックTシャツを着用。

### 2. 汎用マスターシート用プロンプトコードブロック

```text
A front-facing master reference passport-grade portrait of a 22-year-old East Asian female. Features: balanced oval face contour, clear jawline, natural straight eyebrows, delicate inner double eyelids with subtle almond eye shape, straight well-proportioned nasal bridge, naturally relaxed lips with soft cupid's bow. Hair: natural sleek black straight hair tucked completely behind both ears, exposing forehead and ear contours. Neutral relaxed facial expression, mouth gently closed. Studio flat neutral diffused light, no harsh shadows, 18% neutral grey backdrop, wearing a plain white crewneck t-shirt. Ultra-photorealistic 8k, raw skin texture with pores and micro-texture, 3:4 aspect ratio.
```

---

## III. 5カ国全マトリクス視覚データベース

---

### 1. 韓国編 (Korea) —— クールトーン白肌、エフォートレスな抜け感、Y2K CCD粒子

#### A. ビジュアル遺伝子と美学
* **美学の核心**：無理のない抜け感（Effortless · 꾸안꾸）、クールトーンの澄んだ白玉陶器肌、低彩度ミニマリズム。
* **代表的なシーン**：ソウル聖水洞（ソンスドン）のコンクリートカフェ、深夜のアパートの白壁、漢南洞（ハンナムドン）セレクトショップの試着鏡前。

#### B. 4大コアフィルターと光学パラメーター
1. **Y2KコンパクトCCDフラッシュ (2000s Compact CCD Flash)**：
   * *センサー特性*：1/2.3インチ小型CCDセンサー、オンカメラの硬質な直光ミニフラッシュ。
   * *色温度とトーン*：5500K、額や鼻筋の局所的な光の反射、シャドウが即座に漆黒へと落ちるコントラスト、特有の繊細な高ISOデジタルノイズ。
2. **クールトーン白肌の自然窓光ディフューズ (Muted Daylight Porcelain)**：
   * *光学パラメーター*：50mm f/1.8、曇天の窓からの柔らかな自然光拡散。
   * *色温度とトーン*：6200K〜6500K、黄みを抑えたブルーグレー調で、肌の透明感と透き通るような血色感をキープ。
3. **iPhoneフロントカメラのノーマル無加工スナップ (Raw iPhone Front Camera)**：
   * *光学特性*：換算24mm相当の広角、美肌補正アルゴリズム直出ゼロ、後れ毛や輪郭の自然なエッジ感、室内の蛍光灯による微細粒子。
4. **弘大（ホンデ）フィルムポラロイド (Hongdae Polaroid Instant)**：
   * *光学特性*：ポラロイド専用レンズ、アンバーとシアンブルーの柔らかな光漏れ、周辺部の心地よい減光と白いヴィンテージフレームの質感。

#### C. 6大シグネチャーポーズと人体工学
1. **両手でスマホを構え下顔面を隠すミラーセルフィー**：スマホを鼻の高さで持ち、口元から輪郭を隠し、物憂げな涼しげな瞳だけをレンズの上に覗かせる。
2. **視線を落としてドローストリングや襟元を直す瞬間**：視線を30度落とし、フーディーの紐やトレンチコートの襟元をつまむ、日常の自然な仕草を捉える。
3. **片手でサイドの髪を耳にかけながら軽く見下ろす**：人差し指と中指で前髪やサイドの後れ毛をそっと耳にかけ、顔を15度傾けてアンニュイな距離感を演出。
4. **アイスアメリカーノを手渡す彼氏目線（POV）**：やや高めのアングルから見下ろす視点で、アイスカップを差し出す自然な日常のやりとり。
5. **コンクリート階段で膝を抱えてしゃがみこむ**：モダンな階段の上で両膝を揃えて丸くなり、腕で脛を抱え、頬を膝に預けるリラックスした姿勢。
6. **通路を早足で歩きながら振り返る瞬間**：身体は前進しながら顔だけを90度振り返り、毛先が微細なモーションブラーとともにふわりと広がる。

#### D. 4つのスタイリングと素材ライブラリ
* **クリーンフィット・ミニマルテーラリング**：オーバーサイズドロップショルダーのチャコールウールブレンドブレザー ＋ タイトな白のリブタンクトップ ＋ 落ち感のあるワイドスラックス。
* **聖水洞ゴープコアストリート**：マットな質感のGORE-TEXブラックシェルジャケット ＋ ウォッシュドグレーのパラシュートパンツ ＋ シルバーのスニーカー。
* **朝のボーイッシュラウンジウェア**：450gのヘビーオンスコットンフリースフーディー ＋ ヘザーグレーのニットショーツ ＋ 白ソックス。
* **シグネチャーアクセサリー**：ミニマルなチタンシルバーフープピアス、極細ブラックのレクタングル眼鏡、ハーフムーンバッグ、テイクアウトカップ。

#### E. 韓国編クロスモデルプロンプト

##### Seedream 5.0 Pro (Volcengine Ark / 豆包)
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

### 2. 日本編 (Japan) —— 木漏れ日の空気感、日常の断片、シティガール35mmフィルム

#### A. ビジュアル遺伝子と美学
* **美学の核心**：木漏れ日とそよ風の呼吸感、温もりのあるフィルム粒子、飾らない透明感。
* **代表的なシーン**：東京下町の住宅街の坂道、午後の駅の木製ベンチ、暖色の自販機の前、代官山の書店。

#### B. 4大コアフィルターと光学パラメーター
1. **富士フイルム クラシックネガ (Fujifilm Classic Neg)**：控えめな彩度、深みのある青緑色のシャドウと独特のマゼンタ・オリーブ色のロールオフ。5200K〜5600K。
2. **ヴィンテージカムコーダー・ドリームコア (Dreamcore Camcorder Glow)**：90年代のハンディカムDVレンズ、微細な色収差、光源周辺の柔らかなハレーション。
3. **朝の木漏れ日と自然光ディフューズ (Muted Morning Transparency)**：35mm f/1.4 開放、ブラインドや葉っぱの木漏れ日が頬に落ち、逆光に透ける髪のハイライト。
4. **使い捨てカメラ「写ルンです」直出 (QuickSnap Disposable Flash)**：プラスチックレンズ特有の周辺歪み、直光フラッシュによる血色感、味わい深いビネット。

#### C. 6大シグネチャーポーズと人体工学
1. **自販機の横で膝を抱えてしゃがむ**：両膝を揃えてしゃがみ、温かい缶飲料を両手で包み、見上げるような無邪気な視線。
2. **横断歩道の大股ウォーキングスナップ**：ストライドを大きく横切り、ふいにカメラを振り返り、風にスカートが揺れる一瞬。
3. **マグカップを両手で包み息を吹きかける**：両手でしっかりとカップを抱え、顎をざっくり編みのマフラーにうずめたピュアな眼差し。
4. **電車の窓ガラスに映る横顔と物思い**：車窓のガラスに頬を寄せ、流れゆく景色を見つめながらガラスの反射と二重露光の奥行きを作る。
5. **ヴィンテージ自転車を止めて片足立ち**：サドルに腰掛け片足を地面につき、片手で風に飛ばされそうなベレー帽を押さえる。
6. **本棚の隙間からのぞき見**：本棚の奥に身体を隠し、片手でハードカバーの本を持ちながら顔の半分だけのぞかせる仕草。

#### D. 4つのスタイリングと素材ライブラリ
* **Fudgeスタイル・ブリティッシュボーイッシュレイヤード**：ベージュのダブルブレストトレンチコート ＋ 深緑のケーブルニットベスト ＋ サックスブルーのオックスフォードシャツ ＋ チャコールのプリーツスカート。
* **シティガール・ミリタリーワーク**：ウォッシュドオリーブのM-65ジャケット ＋ エクリュのワイドパンツ ＋ スエードのジャーマントレーナー。
* **夏の透明感リネンワンピ**：ウォッシュドリネンのホワイトノースリーブワンピース ＋ サンドベージュの薄手カーディガン ＋ ストラップサンダル。
* **シグネチャーアクセサリー**：太編みウールマフラー、白ソックス＆ブラウンローファー、生成りキャンバストート、オーバーイヤーヘッドフォン。

#### E. 日本編クロスモデルプロンプト

##### Seedream 5.0 Pro (Volcengine Ark / 豆包)
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

### 3. 中国編 (China) —— 新中式クワイエットラグジュアリー、洗練された骨格美、夜間直光フラッシュ

#### A. ビジュアル遺伝子と美学
* **美学の核心**：際立つ骨格美、堂々とした凛とした佇まい、東洋の余白の美と現代のラグジュアリーが交錯する品格。
* **代表的なシーン**：蘇州庭園の青レンガと竹林の影、北京の胡同（フートン）の赤い門前、美術館のコンクリートアトリウム。

#### B. 4大コアフィルターと光学パラメーター
1. **新中式水墨トーン (Ink & Bamboo Muted Green)**：彩度を落とした墨緑色と冷たいグレーの竹影。白玉のようにしっとりとしたマットな肌質、クリアな骨格の明暗ライン。
2. **夜間ハードフラッシュ・ディーヴァレッド (Hard Flash Diva Red)**：強力な外付け直光フラッシュで背景を漆黒に沈め、白肌と真紅のリップの劇的なコントラストを生む。
3. **ウォン・カーウァイ風シネマティック (Hong Kong 90s Cinematic Nostalgia)**：コダック5219映画用フィルム、赤とアンバーの大胆な色彩の衝突、スローシャッターによる光の残像。
4. **美術館クールミニマル (Museum Cold Minimalist)**：85mm f/1.4 単焦点の極めてシャープな解像感、彫刻のように立体的な陰影。

#### C. 6大シグネチャーポーズと人体工学
1. **顎を軽く上げた3/4サイドプロファイル**：身体を斜めに構え、顎を10度そっと上げてシャープなフェイスラインとデコルテを美しく見せるアングル。
2. **翡翠のボタンをそっと撫でる指先**：片手を優雅に持ち上げ、襟元の伝統的なチャイナボタンを軽く触りながら、泰然自若とした眼差しを向ける。
3. **欄干に寄りかかり振り返る余白の美**：石造りの欄干に背をあずけ、上半身だけを振り返り、鼻先をかすめる黒髪とともにストーリー性のある瞳。
4. **コートの裾を翻して大股で歩く**：ロングコートを揺らしながら颯爽と歩み寄り、ポケットに手を入れた自信に満ちた佇まい。
5. **鏡台の前でリップを引く仕草**：アンティークの鏡に映り込む横顔と、唇のそばで静止するリップスティックの指先。
6. **格子戸の光と影のストライプ**：ブラインドやすだれ越しに差し込む強い光で、顔を光と闇の美しい幾何学に分割するドラマチックなカット。

#### D. 4つのスタイリングと素材ライブラリ
* **新中式ラグジュアリーシルク**：30匁の重厚なブラックシルクスタンドカラーベスト ＋ 落ち感のあるアセテートワイドパンツ。
* **ダブルフェイスカシミヤのロングコート**：漆黒のダブルフェイスカシミヤロングコート ＋ タートルネックニット ＋ センタープレススラックス。
* **ヴィンテージレッド・ベルベットチーパオ**：深紅のベルベットスリットチャイナドレス ＋ ブラックミンクショール。
* **シグネチャーアクセサリー**：天然氷種翡翠のスタッドピアス、バロック淡水パールネックレス、シルバーの竹節かんざし。

#### E. 中国編クロスモデルプロンプト

##### Seedream 5.0 Pro (Volcengine Ark / 豆包)
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

### 4. 米国編 (USA) —— カリフォルニアの夕暮れゴールド、クリーンガール、ストリートの自由

#### A. ビジュアル遺伝子と美学
* **美学の核心**：陽光を浴びたヘルシーな生命力、健康的なハニーグロウ肌、エネルギッシュなストリートのアスレチック感。
* **代表的なシーン**：LAベニスビーチのパームツリーアベニュー、NYソーホーの鋳鉄建築が並ぶストリート、カリフォルニア1号線のコンバーチブル。

#### B. 4大コアフィルターと光学パラメーター
1. **ゴールデンアワー・逆光フレア (Golden Hour Flare)**：水平線近くに沈む強烈な夕陽が髪の輪郭を黄金色に縁取り、温かなレンズフレアをまとう。
2. **コダック ゴールド 200 (Kodak Gold 200)**：暖かみのあるアンバー色調、リッチな赤と黄色の発色、きめ細やかなフィルム粒子。
3. **NYCミュートブルーストリート (NYC Muted Blue Street)**：高コントラスト、クールトーンのグレーブルーのシャドウ、マンハッタンのビル群の重厚感。
4. **パパラッチ直光フラッシュ (Paparazzi Direct Flash)**：深夜のストリートの一瞬を切り取る、鋭くコントラストの高い直光フラッシュ。

#### C. 6大シグネチャーポーズと人体工学
1. **横断歩道を渡りながらの笑顔**：両手を自然に振りながら大股で通りを渡り、弾けるような心からの笑顔を向ける瞬間。
2. **片手にコーヒーを持ち通話しながら歩く**：片手でスマホを耳にあて、もう片方に大容量タンブラーを持ち、通り過ぎるタクシーに目をやる姿。
3. **オープンカーのドアに寄りかかりサングラスをずらす**：車に寄りかかり、人差し指でサングラスのフチを少し下げて茶目っ気のある視線を送る。
4. **防波堤に座り海風で乱れた髪をかきあげる**：海沿いのコンクリートに腰を下ろし、風になびくウェーブヘアを片手で優しく押さえる。
5. **サイドミラーを覗き込みリップを塗り直す**：車のサイドミラーを覗き込み、ヌードカラーのリップグロスを丁寧に塗る真剣な表情。
6. **スケートボード滑走のダイナミックスナップ**：デッキに片足を乗せて前傾姿勢を保ち、風を切りながら駆け抜ける疾走感。

#### D. 4つのスタイリングと素材ライブラリ
* **クリーンガール・アスレジャー**：スレートグレーのシームレスリブボディスーツ ＋ オーバーサイズドオートミールカシミヤジップカーディガン ＋ 厚底スニーカー＆白ソックス。
* **カリフォルニア・バイカーシック**：ヴィンテージブラウンの重厚なレザージャケット ＋ 白のクロップドタンクトップ ＋ ローライズストレートデニム。
* **ウォール街カジュアルスーツ**：サンドベージュの麻混ダブルブレザー ＋ 白のワイドスラックス ＋ ストラップサンダル。
* **シグネチャーアクセサリー**：ボールドな太めゴールドフープピアス、黒の楕円形サングラス、大容量ステンレスタンブラー、キャンバストート。

#### E. 米国編クロスモデルプロンプト

##### Seedream 5.0 Pro (Volcengine Ark / 豆包)
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

### 5. フランス編 (France) —— レッセフェールの気だるい気品、パリジャングレー、ヌーヴェルヴァーグ16mm

#### A. ビジュアル遺伝子と美学
* **美学の核心**：気負わない自然体のエレガンス（Laissez-faire）、過度な装飾の否定、知的なニュアンス、寝起きのような無造作ヘア（Bedhead）。
* **代表的なシーン**：サンジェルマン大通りのカフェ「レ・ドゥ・マゴ」のテラス席、オスマン建築のバルコニー、セーヌ川沿いの古本屋（ブキニスト）。

#### B. 4大コアフィルターと光学パラメーター
1. **ヌーヴェルヴァーグ 16mm 映画フィルム (Nouvelle Vague 16mm)**：独特の粗いフィルム粒子、主張しすぎないカフェオレのような淡いグレーのグラデーション。
2. **パリジャングレーの柔らかい散乱光 (Parisian Muted Warm Grey)**：曇り空の柔らかな光、低コントラスト、肌をシルクのように包み込む繊細な陰影。
3. **窓辺のフェルメール調バックライト (Window Vermeer Backlight)**：50mm f/1.4、白いルーバー窓から差し込む静謐なサイドライト。
4. **カフェのガラスの二重の映り込み (Cafe Window Reflection)**：カフェの曇りガラス越しに撮影し、街の往来と物思いにふける人物が詩的に重なる構図。

#### C. 6大シグネチャーポーズと人体工学
1. **テラスの丸テーブルで頬杖をついてぼんやり眺める**：藤編みの椅子に座り片手で頬を支え、テーブルに置かれた古いペーパーバックを見やりながら通りを眺める。
2. **バルコニーのアイアン欄干に寄りかかり街を見渡す**：ラフな白シャツを着て手すりに寄りかかり、エスプレッソを手に風に前髪を揺らす。
3. **クリップを口にくわえて髪を無造作に束ねる**：両腕を上げて髪をまとめ、唇にべっ甲のヘアクリップをくわえた気だるげな瞬間。
4. **ペルシャ絨毯の上に座りアンティークソファに寄りかかる**：床に直接座り込み、使い込まれたベルベットソファに身体を預けるくつろぎのポーズ。
5. **セーヌ川沿いで古い古本のページをめくる**：緑色の本箱の横に立ち、カバーのない古本を両手でめくる静かで知的な時間。
6. **石畳を歩きながらふと振り返る**：石畳の道を歩きながら、レンズに向かってかすかな微笑みを投げかけるミステリアスな表情。

#### D. 4つのスタイリングと素材ライブラリ
* **クラシック・ブルトンボーダーニット**：ドロップショルダーのネイビー×ホワイトボーダーニット ＋ ハイウエストのクロップドフレアデニム ＋ 赤のバレエシューズ。
* **花柄の気だるいラップドレス**：深Vネックのシルクシフォン花柄カシュクールワンピース ＋ ざっくり編みのオートミールカーディガン。
* **左岸派インテリジェントテーラリング**：メンズ仕立てのヘリンボーンツイードジャケット ＋ 洗いざらしの白シャツ ＋ ヴィンテージレザーベルト。
* **シグネチャーアクセサリー**：手編みのカゴバッグ（ジェーン・バーキン風）、べっ甲クリップ、アンティークコインペンダント、無造作なカーテンバング。

#### E. フランス編クロスモデルプロンプト

##### Seedream 5.0 Pro (Volcengine Ark / 豆包)
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

## IV. 3大モデルコンパイラ仕様

各画像生成AIモデルはプロンプトの解釈メカニズムが根本から異なるため、それぞれのエンジンに適した構文変換が必要です：

| 項目 | Seedream 5.0 Pro (Volcengine / 豆包) | ChatGPT (Image 2.5) | Gemini (Imagen 3) |
|---|---|---|---|
| **コアメカニズム** | 自然な写真描写の物語性 ＋ マスター画像の一貫性 | 連貫した日常の描写 ＋ 具象的な物理的インタラクション | 光学幾何学 ＋ 撮影機材・センサーの物理仕様 |
| **顔固定の手法** | マスターシートを `--ref` / 画像プロンプトとして指定 | 固定のベース描写構文 ＋ シード値の固定 | コンテキスト画像 ＋ 厳密な顔立ち・骨格の描写 |
| **ライティング制御** | `オンカメラ直光`, `柔らかな窓光`, `低コントラスト` | 光源の向き、影の形状、反射ハイライトの描写 | 機材名、絞り値 `f/1.8`、ケルビン色温度値の指定 |
| **禁忌事項** | 抽象的な形容詞の乱用を避ける | 機械的なネガティブプロンプトの羅列を避ける | 3D・アニメ系のキーワードを避ける |

---

## V. ミキシングコンソール全マトリクス速見表

音楽プロデューサーがミキサーのフェーダーを調整するように、4大コアトラックのパラメーターを自由にクロスオーバーして組み合わせることができます：

| トラック | トラック 1: フィルター・光学 (Optics) | トラック 2: ポーズ・動作 (Pose) | トラック 3: 表情・視線 (Expression) | トラック 4: ファッション・素材 (Textile) |
|---|---|---|---|---|
| **A** | Y2KコンパクトCCDの強いフラッシュ | 両手でスマホを構え下顔面を隠す | 眠たげに少し細めた瞳、クールな佇まい | ミニマルなオーバーサイズウールブレザー |
| **B** | 富士フイルム クラシックネガ | 自販機の横で膝を抱え温かい缶を持つ | 澄んだ好奇心ある眼差し、微かな口角の笑み | トレンチコート ＋ ケーブルニットベスト |
| **C** | 夜のストリートの強いコントラスト | 3/4サイドプロファイルでボタンに触れる | 凛とした高貴な眼差し、圧倒的な気品 | モダンシルクチャイナベスト ＋ 翡翠ボタン |
| **D** | カリフォルニアの夕暮れ逆光フレア | 0.5x広角で大股で歩きながら笑う | 弾けるような心からのオープンな笑顔 | ヴィンテージライダース ＋ ローライズデニム |
| **E** | ヌーヴェルヴァーグ16mmフィルム粒子 | カフェのテラス席で頬杖をつく | 気ままでアンニュイな夢見るような眼差し | ブルトンボーダーニット ＋ バレエシューズ |

> **ミックス例**：`[A フィルター: CCDフラッシュ]` ＋ `[E ポーズ: カフェで頬杖]` ＋ `[C 表情: 凛とした気品]` ＋ `[D 衣装: ライダース]`  
> **仕上がり**：深夜のテラスバーでアンニュイに佇む、コントラストと存在感が際立つY2Kイットガールの写真が完成！

---

## VI. 自動バッチ画像生成スクリプト

本プロジェクトには、Volcengine Ark (Seedream 5.0 Pro) を利用したバッチ生成およびマスターシート固定テスト用スクリプトが同梱されています：

```bash
# 作業ディレクトリに移動
cd 仓库/Iris

# マスターシート ＋ 韓国クールトーン白肌フィルターのバッチテストを実行
python3 ../../bin/gen_image.py \
  "真实日常生活抓拍照片，一位20岁出头的年轻东亚女性，冷白皮，双手拿手机半遮脸对镜自拍，深灰西装，千禧CCD直闪，严格禁止二次元与3D塑料感，3:4" \
  --ratio 3:4 \
  --ref path/to/master_anchor.png
```

---

## VII. コントリビューション & ロードマップ

- [x] **v0.1**：5カ国（韓・日・中・米・仏）の主要ビジュアルアセットライブラリおよび3大モデルコンパイラ仕様を策定。
- [ ] **v0.2**：北欧ミニマリズム（Nordic）およびブリティッシュグランジ（British Grunge）モジュールを追加。
- [ ] **v0.3**：ミキシング設定に基づきプロンプトを自動生成するWebUIツールおよびCLIツールを公開。
- [ ] **v0.4**：100組の実際の人像ベンチマークテストおよびモデル比較検証図表を公開。

新しい国・地域の美学、往年のクラシックフィルムシミュレーション、ポーズやカメラワークのPRを心よりお待ちしています！

---

<div align="center">
Created with passion by <a href="https://github.com/noahvisualsx">@noahvisualsx</a> • Open for Open Source Community
</div>
