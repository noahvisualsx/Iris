# 跨模型提示词编译器底层工程规范 (Cross-Model Compiler Specifications)

本项目覆盖的三大主流模型（**Seedream 5.0 Pro**、**ChatGPT Image 2.5**、**Gemini Imagen 3**）在注意力机制、文本编码器与概念绑定逻辑上存在显著差异。本文档定义了统一的转译中间格式（IR: Intermediate Representation）与编译规则。

---

## 一、 中间表示 (IR: Intermediate Representation)

在调用任何大模型前，一个完整的虚拟人摄影任务被抽象为如下 JSON 结构：

```json
{
  "subject": {
    "anchor_id": "master_anchor_01",
    "base_description": "22-year-old East Asian female, oval face, straight nose, almond eyes, sleek raven hair",
    "micro_expression": "sleepy, relaxed lips slightly parted"
  },
  "optics": {
    "camera_type": "vintage compact CCD",
    "focal_length": "35mm",
    "lighting": "direct harsh on-axis camera flash",
    "color_profile": "cool-white desaturated, 6000K",
    "artifacts": "subtle digital noise, crisp fall-off shadow"
  },
  "ergonomics": {
    "pose": "hands holding phone covering lower face, taking mirror selfie",
    "head_tilt": "10 degrees slight downward tilt",
    "eye_contact": "looking just above the phone lens into mirror"
  },
  "wardrobe": {
    "garment_outer": "oversized charcoal melange wool blazer",
    "garment_inner": "white ribbed cotton crewneck tank",
    "accessories": "minimalist silver hoop earrings"
  },
  "environment": {
    "location": "minimalist raw concrete indoor space"
  },
  "aspect_ratio": "3:4"
}
```

---

## 二、 各模型编译算法

### 1. Seedream 5.0 Pro (火山引擎/豆包)
* **编码器特征**：基于中文分词与 CLIP 模块化多模态对齐，对特定短语权重敏感。
* **编译规则**：
  1. 严格使用纯正写实摄影自然语言，彻底杜绝 `（参考垫图）` 等中括号机械标签或表单字段冒号（避免被大模型判定为 3D/CGI 提示词）。
  2. 采用行云流水的纪实摄影语流，通过具象的物理光影与面料动态自然串联各维度参数。
  3. 必须在末尾强约束尺寸：如 `3:4` 或 `9:16`。
  4. 注入正向真实感锚定词：`细腻皮肤毛孔, 自然微小噪点, 无美颜滤镜, 真实生动`。
  5. 负向提示词注入（API 参数或 Prompt 过滤）：`保留真实皮肤毛孔与微小肌理，严格禁止二次元、卡通、手绘、动漫与3D渲染塑料感`。

### 2. ChatGPT (Image 2.5)
* **编码器特征**：T5 / GPT 连贯自然语言理解能力极强，但会忽略机械堆砌的标签词（Tag Soup）。
* **编译规则**：
  1. 必须将所有 IR 节点整合成一段具有「电影导演分镜视角」的长句子。
  2. 使用具象物理交互动词（如 `casually tucking a strand of hair`, `finger pressing the edge of an open book`）。
  3. 详细描写光线从光源传播到受光面的物理交互（`direct flash casts a crisp shadow behind her, creating specular micro-highlights on the forehead`）。
  4. 声明具体的底片或摄影介质（如 `early 2000s compact digital camera CCD sensor`）。

### 3. Gemini (Imagen 3 / Nano Banana)
* **编码器特征**：空间几何理解与摄影学物理参数对齐度最高，色彩还原倾向纪实真实感。
* **编译规则**：
  1. 分段结构化声明：`Subject`, `Framing & Kinetics`, `Lighting & Color Balance`, `Wardrobe & Material`。
  2. 声明精准的镜头物理焦段与光圈数值（如 `35mm prime lens, f/1.8`）。
  3. 声明具体的开尔文色温数值（如 `approx 6000K cool-white daylight`）与传感器特性。
  4. 杜绝概念化美学词汇，全部用客观摄影现象代替（用 `micro-pores and fine flyaway hairs` 代替 `ultra-detailed`）。
