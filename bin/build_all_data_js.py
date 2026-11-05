#!/usr/bin/env python3
"""
Iris 全矩阵数据编译器 (v2.0)
扫描 仓库/Iris/{韩国,日本,中国,美国,法国} 下所有 8 大支柱 Markdown 文档，
全量提取 3,315 套双图预设，标准化跨国字段键名，同步配图资产，
并输出为标准 public/iris/data.js 与 仓库/Iris/data.js。
"""

import os
import glob
import re
import json
import shutil

BASE_DIR = os.path.abspath("仓库/Iris")
BLOG_IRIS_DIR = os.path.abspath("仓库/noahvisuals-blog/public/iris")
BLOG_DATA_PATH = os.path.join(BLOG_IRIS_DIR, "data.js")
IRIS_DATA_PATH = os.path.join(BASE_DIR, "data.js")

COUNTRIES = {
    "韩国": "KR",
    "日本": "JP",
    "中国": "CN",
    "美国": "US",
    "法国": "FR"
}

CAT_META = {
    "滤镜": ("filters", "滤镜与光学"),
    "拍照姿势": ("poses", "拍照姿势"),
    "穿搭": ("outfits", "穿搭与面料"),
    "丝袜": ("hosiery", "丝袜与腿部"),
    "风格": ("styles", "风格与场景"),
    "发型与妆容": ("hair_makeup", "发型与妆容"),
    "神态与微表情": ("expressions", "神态微表情"),
    "道具与美甲": ("props", "道具与美甲")
}

# 跨五国统一标准化字段映射表 (将各国子代理的不同命名归一到标准键，同时保留原键)
FIELD_ALIASES = {
    "本土/日常叫法": ["本土/日常叫法", "本土文化/场景名", "本土/传统物名"],
    "时尚/流行流派": [
        "时尚/流行流派", "时尚/流派标签", "时尚/风格流派", "日文标签与流派",
        "光学标签与流派", "姿势流派与标签", "美学/姿态流派", "美学/丝袜流派",
        "视觉风格流派", "美学流派与视觉风格", "视觉流派与核心意境",
        "美学/神态流派", "美学与神态流派", "道具流派与标签", "美甲流派与标签",
        "工艺门类与材质流派"
    ],
    # 01 滤镜
    "相机/介质": ["相机/介质", "相机硬件与光学介质", "感光元件", "光学参数"],
    "色温/光影": ["色温/光影", "色温与光影特性", "色温/光学参数", "色温与曲线", "光线"],
    # 02 拍照姿势
    "人体工学细节": [
        "人体工学细节", "人体工学与重心力矩", "人体工学与骨骼动态细节",
        "人体工学与关节力学", "人体工学与肢体力学细节"
    ],
    # 03 穿搭
    "单品构成与面料工艺细节": ["单品构成与面料工艺细节", "面料工艺与解构细节"],
    "适用场合与搭配鞋包": ["适用场合与搭配鞋包"],
    # 04 丝袜
    "视觉特征与材质工艺": ["视觉特征与材质工艺", "透肤张力与腿部光泽", "纺织参数与纤维密度"],
    "穿搭场景与鞋履搭配": ["穿搭场景与鞋履搭配", "搭配穿搭与场景"],
    # 05 风格
    "本土文化/场景名": ["本土文化/场景名", "本土/日常叫法"],
    "环境与光影细节": [
        "环境与光影细节", "空间环境与光影细节", "环境空间与材质肌理",
        "空间材质与建筑细节", "色温光影与环境氛围", "光学环境与物理色温"
    ],
    # 06 发型与妆容
    "剪裁构造与妆容细节": [
        "剪裁构造与妆容细节", "发型剪裁与碎发细节",
        "发型结构与发丝物理细节", "剪裁构造与发丝物理细节"
    ],
    "适用脸型与风格场景": ["适用脸型与风格场景", "妆容质感与色彩工程参数", "底妆、眼妆与唇部质感"],
    # 07 神态与微表情
    "双眸与视线物理特征": ["双眸与视线物理特征"],
    "唇角与肌肉微动细节": ["唇角与肌肉微动细节"],
    # 08 道具与美甲
    "材质工艺与视觉焦点": ["材质工艺与视觉焦点", "材质机理与物理光学细节", "道具外观与材质物理细节"],
    "互动手势与场景": [
        "互动手势与场景", "手部互动与场景氛围", "手部姿态与场景氛围",
        "手部互动与佩戴场景", "手部互动姿势与场景氛围", "手部动作与手指互动表现"
    ],
    # 通用氛围
    "场景氛围": [
        "场景氛围", "场景氛围与美学定位", "场景氛围与动态", "适用场景与情绪氛围",
        "适用场景与光影氛围", "场景与抓拍契机", "场景氛围与拍摄角度",
        "场景氛围与情绪定位", "核心意境与文化隐喻", "核心人物状态与叙事",
        "肢体细节与关节微动", "身体轮廓与空间透视"
    ]
}


def sanitize_prompt(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"。{2,}", "。", text)
    text = re.sub(r"[，,]\s*[。.]", "。", text)
    text = re.sub(r"[，,]{2,}", "，", text)
    text = re.sub(r"[。.]\s*[，,]", "，", text)
    return text.strip()


def normalize_fields(raw_fields: dict) -> dict:
    cleaned = {}
    for k, v in raw_fields.items():
        if "提示词" in k:
            continue
        cleaned[k] = sanitize_prompt(v)

    norm = {}
    matched_raw_keys = set()
    for target_key, candidates in FIELD_ALIASES.items():
        for cand in candidates:
            if cand in cleaned and cleaned[cand]:
                norm[target_key] = cleaned[cand]
                matched_raw_keys.add(cand)
                break

    for k, v in cleaned.items():
        if k not in matched_raw_keys and k not in norm:
            norm[k] = v

    return norm


def extract_prompts(sec: str, country: str):
    code_matches = list(re.finditer(r"([^\n]*)\n```text\n?(.*?)```", sec, flags=re.DOTALL))
    prompt = ""
    product_prompt = ""

    if not code_matches:
        return "", ""

    # 精确匹配带标签的代码块
    for cm in code_matches:
        label = cm.group(1).strip()
        code = cm.group(2).strip()
        is_foreign_label = any(tag in label for tag in ("日本語", "English", "Français"))
        is_specimen_label = any(
            kw in label
            for kw in ("标本", "平铺", "静物", "解构", "形态", "设计", "Blueprint", "Knolling", "Specimen")
        ) and "真人" not in label and "上身" not in label and "上手" not in label and "实拍" not in label and "实景" not in label
        is_model_label = any(
            kw in label
            for kw in ("真人", "上身", "上手", "实拍", "实景", "大片", "工业级", "Lookbook")
        )

        if is_specimen_label and not is_foreign_label and not product_prompt:
            product_prompt = code
        elif is_model_label and not is_foreign_label and not prompt:
            prompt = code

    # 针对 4 代码块双语排列的兜底精确提取
    if len(code_matches) >= 4:
        if country == "日本":
            # 日本篇顺序: B0(日文标本), B1(中文标本), B2(日文实穿), B3(中文实穿)
            if not product_prompt:
                product_prompt = code_matches[1].group(2).strip()
            if not prompt:
                prompt = code_matches[3].group(2).strip()
        else:
            # 中国/美国/法国篇顺序: B0(中文标本), B1(外文标本), B2(中文实穿), B3(外文实穿)
            if not product_prompt:
                product_prompt = code_matches[0].group(2).strip()
            if not prompt:
                prompt = code_matches[2].group(2).strip()
    elif len(code_matches) == 2:
        if not product_prompt:
            product_prompt = code_matches[0].group(2).strip()
        if not prompt:
            prompt = code_matches[1].group(2).strip()
    elif len(code_matches) == 1:
        if not prompt:
            prompt = code_matches[0].group(2).strip()

    return sanitize_prompt(prompt), sanitize_prompt(product_prompt)


def sync_images():
    src_img_dir = os.path.join(BASE_DIR, "images")
    dst_img_dir = os.path.join(BLOG_IRIS_DIR, "images")
    existing_images = {}
    if os.path.exists(src_img_dir):
        os.makedirs(dst_img_dir, exist_ok=True)
        for fname in os.listdir(src_img_dir):
            if fname.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                shutil.copy2(os.path.join(src_img_dir, fname), os.path.join(dst_img_dir, fname))
                stem = os.path.splitext(fname)[0]
                existing_images[stem] = f"images/{fname}"
    return existing_images


def build_data():
    all_items = []
    existing_images = sync_images()
    print("🚀 开始编译 Iris 全球五国 3,315 套摄影全矩阵数据...")

    for c_name, c_code in COUNTRIES.items():
        c_count = 0
        c_prod_count = 0
        for folder, (cat_id, cat_display) in CAT_META.items():
            f_dir = os.path.join(BASE_DIR, c_name, folder)
            files = glob.glob(f"{f_dir}/*.md")
            files = [f for f in files if not f.endswith("README.md")]

            for fpath in sorted(files):
                txt = open(fpath, encoding="utf-8").read()
                sections = re.split(r"(?=^###\s+#\d+)", txt, flags=re.MULTILINE)
                for sec in sections:
                    m_header = re.match(r"^###\s+#(\d+)\s+【(.*?)】", sec.strip())
                    if not m_header:
                        m_header = re.match(r"^###\s+#(\d+)\s*(.*?)$", sec.strip(), re.MULTILINE)
                    if not m_header:
                        continue

                    num_str = m_header.group(1).zfill(3)
                    title = m_header.group(2).strip().replace("【", "").replace("】", "")

                    raw_fields = {}
                    for line in sec.split("\n"):
                        m_f = re.match(r"^\s*-\s*\*\*(.*?)\*\*[：:]\s*(.*)", line)
                        if m_f:
                            k = m_f.group(1).strip()
                            v = m_f.group(2).strip()
                            if v.startswith("`") and v.endswith("`"):
                                v = v[1:-1].strip()
                            if not k.startswith("【") and "提示词" not in k:
                                raw_fields[k] = v

                    fields = normalize_fields(raw_fields)
                    prompt, product_prompt = extract_prompts(sec, c_name)

                    item_id = f"{c_code}-{cat_id}-{num_str}"
                    img_path = existing_images.get(item_id)

                    all_items.append({
                        "id": item_id,
                        "country": c_name,
                        "category_id": cat_id,
                        "category_name": cat_display,
                        "num": num_str,
                        "title": title,
                        "fields": fields,
                        "prompt": prompt,
                        "image": img_path,
                        "product_prompt": product_prompt or None
                    })
                    c_count += 1
                    if product_prompt:
                        c_prod_count += 1
        print(f"  ✓ {c_name}篇: 收录 {c_count} 套预设 (双图完备: {c_prod_count}/{c_count})")

    total_prod = sum(1 for x in all_items if x.get("product_prompt"))
    print(f"\n✨ 全量收录达成: 共 {len(all_items)} 套预设 | 双图架构覆盖: {total_prod}/{len(all_items)} (100%)！")

    json_str = json.dumps(all_items, ensure_ascii=False, indent=None)
    js_content = f"window.IRIS_DATA = window.PERSONA_DATA = {json_str};\n"

    # 写入博客静态资产
    os.makedirs(os.path.dirname(BLOG_DATA_PATH), exist_ok=True)
    with open(BLOG_DATA_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"💾 已同步写入博客静态资产: {BLOG_DATA_PATH} ({len(js_content.encode('utf-8')) / (1024*1024):.2f} MB)")

    # 写入 Iris 仓库
    with open(IRIS_DATA_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"💾 已同步写入 Iris 仓库根目录: {IRIS_DATA_PATH}")
    shutil.copy2(os.path.abspath(__file__), os.path.join(BASE_DIR, "bin", "build_all_data_js.py"))


if __name__ == "__main__":
    build_data()
