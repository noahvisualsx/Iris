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


COUNTRY_OUTFIT_POOLS = {
    "韩国": [
        "身穿剪裁利落的纯黑一字领修身针织长袖上衣，恰到好处地展露优美天鹅颈与精致锁骨线条，极简清冷高级",
        "身穿韩系学院风白色挺括尖领长袖衬衫，外搭饰有精致小金扣的深藏青细针织V领背心，知性灵动",
        "身穿象牙白软糯马海毛宽松V领针织开衫，内搭同色系极简真丝缎面内搭，温柔清透",
        "身穿浅燕麦色高支纯棉廓形西装外套，内搭纯白修身罗纹针织打底衫，利落干练的汉南洞Clean Fit美学",
        "身穿冰川蓝薄透天丝亚麻微宽松长袖衬衫，领口自然微敞露出精致锁骨与极细银质锁骨链，清冷氧气感十足",
        "身穿深炭灰修身高领软糯羊绒针织衫，极简流畅剪裁衬托出修长脖颈与巴掌小脸，高级智性美拉满",
    ],
    "日本": [
        "身穿米白色高支透气亚麻微宽松长袖衬衫，领口自然舒展露出优美锁骨线条，温柔日系透明感",
        "身穿浅燕麦色软糯小羊绒圆领针织开衫，内搭纯白棉质打底衫，干净清爽的代官山日常美学",
        "身穿深藏青极简V领羊毛针织马甲叠穿挺括白衬衫，知性清纯的日系画报质感",
        "身穿淡奶油色垂坠感真丝混纺雪纺长袖衬衫，剪裁轻盈灵动，衬托清透冷白肤色",
    ],
    "中国": [
        "身穿月白色30姆米重磅真丝素绉缎新中式立领衬衫，手工一字盘扣精致典雅，温润垂坠光泽衬托冷白瓷肌",
        "身穿玄黑色极简修身羊绒高领针织衫，利落剪裁凸显修长天鹅颈与清冷大女主骨相气场",
        "身穿浅香槟色重磅真丝V领垂坠感衬衫，外搭极简剪裁高级羊绒大衣，清贵从容",
        "身穿烟粉黛青交织的宋锦暗纹立领修身短衫，丝绸光泽细腻内敛，东方清冷智性美感",
    ],
    "美国": [
        "身穿剪裁利落的象牙白高支罗纹修身方领针织上衣，外搭炭灰色廓形羊毛西装外套，佩戴极简金色小圆环耳圈，曼哈顿老钱极简风",
        "身穿纯黑修身极简一字肩长袖针织衫，展露紧致优美的肩颈锁骨线条，搭配精致金属锁骨链，高街超模质感",
        "身穿燕麦色重磅羊绒开衫内搭纯白修身丝棉打底衫，松弛优雅的加州Clean Girl高级穿搭",
        "身穿复古水洗丹宁修身夹克内搭纯白高支棉修身短T恤，利落阳光的西海岸摩登穿搭",
    ],
    "法国": [
        "身穿经典法式海军蓝白细条纹纯棉海魂衫，一字领微露优美锁骨与修长脖颈，随性优雅的巴黎左岸风情",
        "身穿炭灰色软糯V领粗棒针羊绒衫，佩戴一串极细复古金色锁骨链，松弛高级的法式质感",
        "身穿象牙白重磅真丝法式方领茶歇衬衫，剪裁浪漫修身，衬托通透白皙肌肤",
        "身穿燕麦色经典人字纹羊毛西装外套，内搭纯白丝质V领内搭衫，知性慵懒的圣日耳曼画报感",
    ],
}

COUNTRY_HOSIERY_TOP_POOLS = {
    "韩国": "身穿剪裁利落的纯黑高定羊毛修身西装短裙套装，内搭白色真丝衬衫，上下身穿搭完整高雅",
    "日本": "身穿剪裁利落的深藏青修身羊毛西装短裙套装，内搭象牙白真丝垂坠衬衫，上下身穿搭完整谐调",
    "中国": "身穿玄黑色重磅真丝修身改良旗袍短裙外搭极简羊绒大衣，上下身穿搭矜贵完整",
    "美国": "身穿曼哈顿高街深黑修身羊毛西装外套短裙套装，上下身穿搭利落摩登",
    "法国": "身穿巴黎高定黑色修身吸烟装短裙配真丝内搭，上下身穿搭优雅完整",
}

COUNTRY_SCENE_POOLS = {
    "韩国": [
        "干净极简的首尔汉南洞暖调设计感书房窗边，背景柔和浅景深虚化且干净高级无杂物",
        "圣水洞极简清水混凝土与温润原木交织的静谧艺术空间，背景柔和浅景深虚化无杂物",
        "清潭洞极简米白画廊式室内柔光角落，背景干净高级无杂乱物",
        "延南洞静谧独立咖啡馆临窗原木长桌旁，背景柔和浅景深虚化",
    ],
    "日本": ["代官山静谧原木买手店落地窗旁，背景柔和浅景深虚化且干净无杂物"],
    "中国": ["现代极简东方美学艺术展厅静谧窗前，背景柔和虚化且干净留白"],
    "美国": ["曼哈顿SoHo极简挑高艺术公寓落地窗旁，背景柔和浅景深虚化"],
    "法国": ["巴黎左岸圣日耳曼大道静谧法式公寓落地窗前，背景柔和浅景深虚化"],
}

COUNTRY_MAKEUP_ANCHORS = {
    "韩国": "天生饱满水光卧蚕，灵动清澈双眸闪烁着天然单点眼神光（Catchlight），清透无瑕的冷白瓷肌伪素颜水光底妆，两颊淡淡晕染清透玫瑰粉腮红，浅棕自然眼线与根根分明纤长睫毛，水光亮泽的珊瑚裸粉玻璃唇（完整保留面部唇颊妆容的鲜润度）",
    "日本": "天生饱满卧蚕，澄澈双眸闪烁着灵动单点眼神光（Catchlight），清透日系伪素颜水光底妆，双颊泛着天然通透的杏粉血色感腮红，根根分明纤长睫毛与水润透亮的果实裸粉唇妆",
    "中国": "天生饱满卧蚕，清亮深邃双眸带灵动单点眼神光（Catchlight），无瑕清透的冷白瓷肌半哑光微水光底妆，两颊淡淡晕染柔美气色腮红，极细内眼线与温润高级的丝绒玫瑰豆沙红唇",
    "美国": "深邃明媚双眸闪烁着清澈单点眼神光（Catchlight），清透水光裸妆，根根分明立体野生眉与纤长睫毛，两颊自然微醺红晕与饱满水润的玫瑰裸色果冻唇",
    "法国": "深邃灵动双眸闪烁着清澈单点眼神光（Catchlight），法式清透水润裸妆，两颊淡淡自然血色红晕，根根分明纤长睫毛与优雅水润的浆果玫瑰唇妆",
}

PLACE_NOUN_RE = re.compile(
    r"街|路|道|巷|店|馆|室|厅|园|滩|岸|台|廊|吧|房|窗|桥|场|院|阁|亭|楼|车|梯|寺|社|宫|祠|林|山|湖|河|海|溪|池|泉|岛|谷|坡|坪|阶|椅|桌|沙发|吧台|床|柜|栏|墙|门|棚|厢|舱|甲板|胡同|弄堂|大堂|走廊"
)

OUTFIT_DETECT_RE = re.compile(
    r"身穿|穿着|身着|上装|外搭|内搭|衬衫|毛衣|针织|西装|外套|大衣|连衣裙|长衫|旗袍|风衣|卫衣|背心|T恤|夹克|礼服|开衫|海魂衫|羊绒衫|洋装|长袍|抹胸|吊带|汉服|马面裙|西服|长裙|短裙|套裙|短裤|长裤|牛仔裤|风帽"
)

MAKEUP_DETECT_RE = re.compile(r"底妆|唇|腮红|眼妆|卧蚕|裸妆|伪素颜")


def clean_toxic_phrases(text: str) -> str:
    if not text:
        return ""
    replacements = [
        # 1. 遮脸/拂面乱发 -> 修饰脸型的八字刘海与丰盈光泽层次长发
        ("黑色直发自然垂落披肩，几缕碎发凌乱拂面", "丰盈柔顺有光泽的深色长层次微卷发自然垂落肩头，两侧修长八字刘海沿下颌线柔美垂落修饰脸型，露出干净清晰的精致五官，面部无乱发遮挡"),
        ("黑色柔顺长发被微风吹拂，几缕细碎发丝随意飘拂遮过眼角", "丰盈柔顺有光泽的深色层次长发随微风在肩侧轻盈舒展，两侧修长八字刘海沿下颌线柔美修饰脸型，露出干净清晰的精致五官，面部无乱发遮挡眉眼"),
        ("黑色长发松散垂在肩颈两侧，发丝微乱蓬松", "丰盈柔顺的深色层次长发自然垂在肩颈两侧，两侧修长八字刘海沿下颌线柔美修饰脸型，露出清晰精致五官"),
        ("深黑柔顺长发微微凌乱，几缕细碎胎毛发丝随走动自然飘拂掠过脸颊", "深黑丰盈柔顺的层次长发自然垂落肩头，两侧修长八字刘海轻柔修饰脸型，露出干净精致五官"),
        ("黑色柔顺长发自然垂落肩头，几缕碎发散落", "丰盈柔顺的黑色层次长发自然垂落肩头，两侧修长八字刘海柔美修饰脸型，面部干净清透"),
        ("黑色长发微乱自然垂在耳后与锁骨间，几根胎毛碎发随意飘散", "丰盈柔顺的黑色层次长发自然挽于耳后垂落锁骨间，两侧修长八字刘海柔美修饰脸型，露出清晰精致的五官骨相"),
        ("黑色柔顺长发被微风吹动，几缕发丝轻贴脸颊", "丰盈柔顺的黑色层次长发自然垂落肩侧，两侧修长八字刘海柔美修饰脸型，面部干净清晰"),
        ("几缕碎发凌乱拂面", "两侧修长八字刘海柔美修饰脸型，面部干净无乱发遮挡"),
        ("几缕细碎发丝随意飘拂遮过眼角", "两侧修长八字刘海柔美修饰下颌线，露出清澈双眸无乱发遮眼"),
        ("发丝向前垂落遮住面庞", "发丝顺着肩侧自然垂落，露出精致清晰的面部侧颜轮廓"),
        ("微乱碎发遮住一侧眉峰", "修长刘海自然修饰额角与下颌线，露出精致眉眼"),
        ("法式八字刘海遮住半边眉毛", "法式八字空气刘海轻柔修饰额角与高颧骨"),
        # 2. 广角拉伸畸变、手持畸形自拍臂、油光、欠曝、抖动模糊、碎屑
        ("对镜自拍或手持自拍，复古青春期抓拍", "干净极简的暖调复古木质书房窗边，柔和复古千禧卡片机抓拍氛围"),
        ("微广角28mm等效轻微边缘拉伸，闪光灯中心偏亮，暗角微弱", "50mm黄金人像镜头无畸变视角，柔和直闪补光均匀照亮全脸，中心清透白皙，微弱复古暗角"),
        ("微广角28mm等效轻微边缘拉伸", "50mm黄金人像镜头无畸变视角"),
        ("超广角轻度边缘拉伸，头大身小可爱视角，长腿向画面边缘延伸", "高机位微俯拍35mm～50mm黄金人像无畸变视角，小头小巧巴掌脸与修长身形比例，画面充满青春活力"),
        ("28mm微广角在近距离直闪下赋予画面强烈的透视张力与动势", "35mm人文定焦镜头在柔和直闪下赋予画面生动的空间层次与动势"),
        ("28mm f/2.8广角镜头", "50mm f/1.4黄金人像定焦镜头"),
        ("Biogon 28mm广角镜头", "Planar 50mm f/1.4黄金人像镜头"),
        ("28mm广角镜头", "50mm黄金人像定焦镜头"),
        ("广角镜头带来开阔透视感", "标准人文镜头带来开阔空间感，五官端正无广角拉伸变形"),
        ("塑料镜头特有的轻微桶形畸变与暗角", "复古镜头特有的柔和暗角，五官端正无畸变"),
        ("廉价单片塑料透镜导致的边缘解像力下降与微弱放射状彗差", "复古胶片镜头特有的边缘柔和微光与细腻胶片颗粒"),
        ("0.6米极近距离闪光，五官扁平立体交织，边缘柔和晕光", "柔和近景直闪补光，五官立体精致，皮肤冷白通透，边缘柔和晕光"),
        ("一只手掌推向镜头挡住部分画面，露出调皮求饶的笑眼", "微侧身回眸望向镜头，露出一双灵动清澈的笑眼，神态俏皮自然"),
        ("发丝微小碎屑与鼻梁真实肌理清晰", "发丝柔顺丝滑光泽与高挺鼻梁细腻冷白肌理清晰"),
        ("空无一人的小巷路灯在头顶照射，下巴与胸前投下极深影子，戏剧性", "静谧首尔街巷暖黄路灯柔和洒落，配合正面漫射补光勾勒立体精致五官，电影氛围感"),
        ("底片受潮乳剂老化，暗部发灰泛微紫，反差降低如蒙薄纱", "复古胶片特有的柔和低饱和紫灰暗部与朦胧唯美空气感，面部保持冷白通透与红润唇色"),
        ("面颊真实高光油润感", "面颊透出清透水光瓷肌光泽"),
        ("曝光欠压半档，暗部彩色噪点（Chroma Noise）强烈，高光受限", "柔和复古直闪补光，面部曝光白皙通透，背景暗部带细腻复古胶片颗粒"),
        ("曝光欠压半档，暗部彩色噪点强烈，高光受限", "柔和复古直闪补光，面部曝光白皙通透，背景暗部带细腻复古胶片颗粒"),
        ("深夜卧室未开灯，手持快门轻度抖动", "静谧极简的暗调卧室暖光角落，柔和直闪均匀照亮冷白瓷肌"),
        ("额头与山根局部100%过曝纯白，皮肤如反光乳胶般通透", "额头与高挺山根泛着清透柔和的冷白水光高光，肌肤如冷白瓷般通透细腻"),
        ("机顶硬闪光直射，局部高光溢出", "复古机顶闪光灯柔和补光，冷白瓷肌通透白皙"),
        ("面部虽然轻微欠曝但依靠室内墙壁反光保留柔和细节", "面部由室内柔和漫反射补光均匀照亮，冷白瓷肌通透细腻"),
        ("面部虽然轻微欠曝但依靠室内墙壁反光保留了极其丰富温润的中间调细节", "面部由室内柔和漫反射补光均匀照亮，冷白瓷肌通透细腻且保留丰富温润的中间调细节"),
        ("面部虽然轻微欠曝但依然保留丰富通透的暗部层次与眼神光", "面部由柔和漫反射补光均匀照亮，冷白瓷肌通透细腻且保留清澈眼神光"),
        ("面部虽然轻微欠曝但依然保留丰富通透的暗部肌理", "面部由柔和漫反射补光均匀照亮，冷白瓷肌通透细腻"),
        ("轻微生活感动态微模糊与暗部噪点", "细密温润的胶片颗粒感与柔和浅景深虚化"),
        ("轻微生活动态微糊", "细密温润的胶片颗粒感与柔和浅景深虚化"),
        ("两指轻捏瓶颈倒酒，或者单手握着瓶身对准镜头举杯", "单手修长手指优雅轻握翠绿玻璃瓶身，姿态松弛自然"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def purify_fields(fields: dict, country: str, cat_id: str, title: str, num: int) -> dict:
    out = {}
    scene_pool = COUNTRY_SCENE_POOLS.get(country, COUNTRY_SCENE_POOLS["韩国"])
    fallback_scene = scene_pool[num % len(scene_pool)]
    title_prefix = title.split("·")[0].strip()

    for k, v in fields.items():
        val = clean_toxic_phrases(v)
        if k == "场景氛围" and val:
            val = re.sub(r"(对镜自拍或)?手持自拍|前置自拍|OOTD自拍|年轻活力自拍|美丽的自拍|自赏自拍|偷闲自拍", "柔光人像写真抓拍", val)
            val = val.replace("潮牌街头大片", "首尔现代工业风空间")
            if not PLACE_NOUN_RE.search(val) and "唯美氛围" not in val:
                if PLACE_NOUN_RE.search(title_prefix):
                    val = f"{title_prefix}干净高级的实景空间，呈现{val}的唯美氛围"
                else:
                    val = f"{fallback_scene}，呈现{val}的唯美氛围"
        out[k] = sanitize_prompt(val)
    return out


def purify_and_enrich_prompt(prompt: str, fields: dict, country: str, cat_id: str, title: str, num: int) -> str:
    if not prompt:
        return ""

    p = clean_toxic_phrases(prompt)
    # 先剥离末尾 3:4，确保所有新增句子插在正文内，最后统一收尾 3:4
    p = re.sub(r"[，,。.\s]*3:4[。.\s]*$", "", p).strip()

    scene_pool = COUNTRY_SCENE_POOLS.get(country, COUNTRY_SCENE_POOLS["韩国"])
    fallback_scene = scene_pool[num % len(scene_pool)]
    outfit_pool = COUNTRY_OUTFIT_POOLS.get(country, COUNTRY_OUTFIT_POOLS["韩国"])
    fallback_outfit = outfit_pool[num % len(outfit_pool)]
    makeup_anchor = COUNTRY_MAKEUP_ANCHORS.get(country, COUNTRY_MAKEUP_ANCHORS["韩国"])
    title_prefix = title.split("·")[0].strip()

    # 1. 修复法国 hair_makeup 的 "身处适合鹅蛋脸、菱形脸与方圆脸。巴黎左岸..." 语法病句
    p = re.sub(r"身处适合[^。]+?[。，,]\s*", "身处", p)

    # 2. 修复夜晚/烛光场景混入白天日光描述的冲突
    if re.search(r"深夜|夜市|夜生活|冬夜|寒夜|昏黄烛光|夜景", p):
        p = p.replace("，漫射日光清透温暖", "，柔和通透的夜间暖调环境补光均匀照亮面庞")
        p = p.replace("，午后柔和的巴黎阴天灰调漫射日光均匀笼罩", "，柔和暖调环境光均匀包裹面庞")

    # 3. 修复韩国 styles 缺失具体场景地标名称的问题
    if country == "韩国" and cat_id == "styles" and title not in p:
        p = p.replace("身处", f"身处首尔「{title}」实景空间（背景柔和浅景深虚化、干净高级）：", 1)

    # 4. 修复抽象 "身处..." 病句
    p = re.sub(r"(对镜自拍或)?手持自拍|前置自拍|OOTD自拍|年轻活力自拍|美丽的自拍|自赏自拍|偷闲自拍", "柔光人像写真抓拍", p)
    p = p.replace("身处潮牌街头大片", "身处首尔现代地下车库冷白灯管空间，呈现潮牌高街画报")
    p = p.replace("身处街头快步走动", "身处首尔繁华街头夜色斑马线旁，步伐轻盈舒展")

    def fix_shenchu(match):
        clause = match.group(1).strip()
        rest_of_p = p.replace(match.group(0), "")
        if not PLACE_NOUN_RE.search(clause):
            if PLACE_NOUN_RE.search(title_prefix):
                return f"身处{title_prefix}干净高级的实景空间（背景柔和虚化无杂物），呈现{clause}"
            elif PLACE_NOUN_RE.search(rest_of_p):
                return f"画面呈现{clause}的唯美氛围"
            else:
                return f"身处{fallback_scene}，呈现{clause}"
        return f"身处{clause}"

    p = re.sub(r"身处([^，。；]+)", fix_shenchu, p, count=1)

    # 5. 注入高颜值骨相、饱满卧蚕、单点眼神光与清透伪素颜水光彩妆锚点
    if not MAKEUP_DETECT_RE.search(p):
        if "身处" in p:
            p = p.replace("身处", f"{makeup_anchor}。身处", 1)
        elif "画面呈现" in p:
            p = p.replace("画面呈现", f"{makeup_anchor}。画面呈现", 1)
        else:
            sents = p.split("。")
            if len(sents) >= 2:
                sents.insert(2, makeup_anchor)
                p = "。".join(sents)
            else:
                p = f"{p}。{makeup_anchor}"
    elif country == "韩国" and "卧蚕" not in p:
        p = p.replace(
            "清冷淡颜，冷白皮",
            "清冷高颜值淡颜，精致小巧巴掌脸，立体优越鼻梁与清晰下颌线，白皙通透冷白瓷肌，天生饱满水光卧蚕，灵动双眸闪烁天然单点眼神光（Catchlight）",
            1,
        )

    # 6. 为缺失穿搭的单卡自动补齐高审美完整穿搭
    if not OUTFIT_DETECT_RE.search(p):
        chosen_outfit = COUNTRY_HOSIERY_TOP_POOLS.get(country, fallback_outfit) if cat_id == "hosiery" else fallback_outfit
        if "身处" in p:
            p = p.replace("身处", f"{chosen_outfit}。身处", 1)
        elif "画面呈现" in p:
            p = p.replace("画面呈现", f"{chosen_outfit}。画面呈现", 1)
        elif "眼神" in p:
            p = p.replace("眼神", f"{chosen_outfit}。眼神", 1)
        else:
            sents = p.split("。")
            if len(sents) >= 2:
                sents.insert(2, chosen_outfit)
                p = "。".join(sents)
            else:
                p = f"{p}。{chosen_outfit}"

    # 7. 补齐 50mm~85mm 黄金人像无畸变视角、全脸柔和均匀受光与防广角大鼻子/防乱发糊脸铁律，并以 3:4 结尾（完全幂等）
    if "严禁广角大鼻子拉伸变形" not in p:
        if "黄金人像" not in p and "50mm" not in p and "85mm" not in p and "35mm" not in p:
            framing = (
                "半身至全身竖幅人像构图，50mm～85mm黄金人像定焦镜头无畸变视角，全脸明亮柔和均匀受光，背景干净高级且柔和浅景深虚化"
                if cat_id in ("outfits", "hosiery")
                else "胸部以上中近景或半身竖幅人像构图，50mm黄金人像定焦镜头无畸变视角，全脸明亮柔和均匀受光，五官清晰立体无死黑阴影，背景干净高级且柔和浅景深虚化"
            )
            p = f"{p}，{framing}，严禁广角大鼻子拉伸变形、严禁畸形前伸手臂、严禁乱发遮挡眉眼，3:4"
        else:
            p = f"{p}，全脸明亮柔和均匀受光，严禁广角大鼻子拉伸变形、严禁畸形前伸手臂、严禁乱发遮挡眉眼，3:4"
    else:
        p = f"{p}，3:4"

    return sanitize_prompt(p)



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

                    num_int = int(m_header.group(1))
                    fields = purify_fields(normalize_fields(raw_fields), c_name, cat_id, title, num_int)
                    raw_prompt, product_prompt = extract_prompts(sec, c_name)
                    prompt = purify_and_enrich_prompt(raw_prompt, fields, c_name, cat_id, title, num_int)

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
