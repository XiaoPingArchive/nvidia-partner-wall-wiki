import os
import sys
import json

sys.path.insert(0, "/Users/popoya/Movies/视频生产/诸神之墙")
from generate_directory import partner_rows

app_js_path = "/Users/popoya/Movies/视频生产/诸神之墙/app.js"
index_html_path = "/Users/popoya/Movies/视频生产/诸神之墙/index.html"
style_css_path = "/Users/popoya/Movies/视频生产/诸神之墙/style.css"
coords_json_path = "/Users/popoya/.gemini/antigravity/brain/e59e264a-01f9-4f52-a072-7e94556f345c/scratch/logo_coordinates_exact.json"

# Load exact coordinates
with open(coords_json_path, "r", encoding="utf-8") as f:
    coords = json.load(f)

# Pre-defined detailed data for the core companies, keyed by domain
core_data = {
    "lenovo.com": {
        "shortName": "Le",
        "tech": "端侧 AI 智能体分发与高性能服务器制造",
        "disassembly": "联想集团作为全球领先的个人电脑及企业级服务器制造商，正在与英伟达深度结合。在英伟达 AI 生态中，联想是端侧本地 AI 智能体（Agent）硬件分发与部署的关键合作伙伴。其搭载 RTX 系列芯片的高性能 AI PC 和数据中心混合云解决方案，共同推动了企业端侧计算的高效落地。",
        "money": "在数据中心与高性能计算领域，联想与英伟达合作紧密。随着企业对本地数据隐私与端侧智能体处理能力需求的爆发，联想的本地化 AI 部署和集成服务正在迎来长期的行业红利期。",
        "action": "“联想不仅是个人电脑巨头，更是英伟达在端侧 AI 智能体落地和普及的核心合作伙伴。”",
        "script": "【深度观察】联想集团作为全球个人电脑及企业级服务器制造商，是英伟达端侧 AI 落地和高性能 AI PC 普及的关键合作伙伴。通过在本地端侧部署 AI 智能体，联想与英伟达共同推动企业数据安全处理与端侧高效计算的深度结合。"
    },
    "mediatek.com": {
        "shortName": "MT",
        "tech": "NVIDIA-Arm 汽车与 PC SoC 联合研发 / 3nm 先进制程",
        "disassembly": "联发科与英伟达展开了深度的芯片级战略合作，将联发科的低功耗 SoC 设计能力与英伟达 Blackwell 架构的强劲 GPU 算力相结合，推出了下一代 ARM 架构的智能座舱芯片及个人电脑芯片，为端侧多模态推理开辟了新赛道。",
        "money": "两强联手将推动 ARM 架构本地 AI 应用生态（如轻量级 Agent 框架和边缘计算接口）的爆发，使端侧智能体能流畅运行于更省电的汽车与物联网平台。",
        "action": "“联发科低功耗设计与英伟达 Blackwell GPU 算力融合，正全面重塑智能出行与端侧计算的格局。”",
        "script": "【深度观察】联发科通过与英伟达强强联合，利用其领先的超低功耗 SoC 设计能力，融合英伟达 Blackwell 架构算力，共同推出了新一代 ARM 架构的智能座舱及个人电脑芯片，为端侧多模态推理开辟新赛道。"
    },
    "asus.com": {
        "shortName": "As",
        "tech": "高性能电竞硬件与端侧 AI 辅助工具",
        "disassembly": "华硕作为全球知名的个人电脑与电竞硬件巨头，在英伟达的高性能计算生态中扮演着关键硬件集成商的角色。除了提供搭载 RTX 系列显卡的顶级设备外，华硕还与英伟达联合调优本地端侧的多模态 AI 辅助应用（如 Project G-Assist），提升电竞与创作领域的交互体验。",
        "money": "高性能电竞硬件和创作工作站是端侧 AI 最早商业化的落地场景。高功耗端侧 GPU 配合本地 AI 辅助软件，将为极客与专业创作者提供极高附加值的解决方案。",
        "action": "“华硕与英伟达在高性能 PC 和本地多模态 AI 辅助程序方面的联调，极大拓宽了端侧算力边界。”",
        "script": "【深度观察】作为高性能 PC 和电竞硬件的代表厂商，华硕不仅提供一流的 RTX 级别硬核设备，还与英伟达深度调测本地多模态 AI 辅助程序，推动端侧本地算力在电竞及内容创作领域的创新应用。"
    },
    "msi.com": {
        "shortName": "Ms",
        "tech": "高密度算力工作站与紧凑型 GPU 一体机",
        "disassembly": "微星科技致力于开发基于英伟达高性能 RTX 平台的高密度紧凑型工作站与液冷服务器，为中小企业、AI 研发团队及工作室提供高保密性、高性价比的本地化工作流部署方案。",
        "money": "在对数据保密性要求极高的中小型企业市场，微星通过提供免去昂贵云端会员与 Token 消耗的本地化 AI 一体机，承接算力改装与系统集成，具有广阔的 B2B 市场空间。",
        "action": "“微星的高密度紧凑型 GPU 工作站，为需要高本地计算与数据安全的团队提供了极佳的一体化方案。”",
        "script": "【深度观察】微星通过研发高密度的紧凑型 GPU 工作站，为需要高保密性及高本地计算能力的小型工作室与研发团队，提供一体化的本地部署解决方案，协助客户完成高性价比的 AI 软硬件适配。"
    },
    "adobe.com": {
        "shortName": "Ad",
        "tech": "创意软件本地 AI 接口 / Firefly 端侧集成",
        "disassembly": "数字创意巨头 Adobe 与英伟达深度合作，将其 Firefly 系列生成式 AI 模型与 Creative Cloud 工作流原生集成。通过适配英伟达的端侧硬件加速，用户可在本地的创意软件中实现秒级图像生成，兼顾极高的数据安全与流程流畅度。",
        "money": "随着 Adobe 本地 AI Agent 接口的成熟，设计与自媒体领域的人均产出效率将获得倍数级提升，大幅降低创意设计的软硬件综合成本。",
        "action": "“Adobe 与英伟达的端侧加速合作，实现了在本地 Photoshop 等经典工具中秒级运行生成式 AI 模型。”",
        "script": "【深度观察】软件巨头 Adobe 将旗下的 Firefly 大模型及生成式 AI 工具原生适配至英伟达的端侧计算架构中，使用户可以在 Photoshop 等经典工具中实现高效的本地 AI 辅助创作，大幅提升创意设计的工作流效率。"
    },
    "autodesk.com": {
        "shortName": "Au",
        "tech": "三维工业设计 CAD 智能体 / 本地物理仿真渲染",
        "disassembly": "工业设计与三维建模软件巨头欧特克正在将生成式 AI 模块与本地 CAD 平台进行融合。借助英伟达的高性能本地计算架构，工程设计人员能够在本地瞬间完成结构规划、力学应力分析和高质量 3D 渲染，重塑了传统工业设计的工作模式。",
        "money": "利用本地算力进行实时仿真与优化，减少了物理调试与后期修改 of 成本，为制造和设计产业提供了强有力的增效路径。",
        "action": "“欧特克通过把生成式 AI 模块与本地 CAD 平台融合，协助工程人员实时完成工业设计的物理仿真与渲染。”",
        "script": "【深度观察】三维设计与工业工程软件巨头欧特克，通过将生成式 AI 模块与本地 CAD 平台融合，协助工程人员和设计师利用本地算力进行实时仿真、优化 and 渲染，全面重塑了传统工业设计的开发模式。"
    },
    "siemens.com": {
        "shortName": "Si",
        "tech": "Omniverse 工业数字孪生工厂 / 物理模拟集成",
        "disassembly": "工业巨头西门子与英伟达在数字孪生与工业元宇宙领域展开了深度协作。通过将西门子的工业软件（如 Teamcenter）与英伟达 Omniverse 平台链接，双方在虚拟世界中以 1:1 的高精度模拟真实的工业产线与生产设备，实现卓越的工业流程优化。",
        "money": "在建厂和设备调试前，通过高精度物理规律模拟进行数字化仿真，能为全球大型制造企业节省数百万的物理调试和后期改造费用，这代表着智能制造的产业趋势。",
        "action": "“西门子与 Omniverse 平台的对接，使企业可以在虚拟空间中以 1:1 精度提前运行并优化整条实体产线。”",
        "script": "【深度观察】全球工业巨头西门子与英伟达在数字孪生和工业元宇宙领域展开了深度协作。通过将工业软件与 Omniverse 链接，西门子为全球制造企业提供了高精度的虚拟工厂仿真，降低了物理调试与后期改造的成本。"
    },
    "foxconn.com": {
        "shortName": "Fx",
        "tech": "Isaac 智能机器人平台 / 物理仿真组装产线",
        "disassembly": "富士康正在其新一代电动车厂及服务器制造工厂中，全面引入英伟达的 Isaac 机器人开发平台和 Omniverse 仿真技术。在实体智能机器人部署到实际产线之前，先在虚拟的物理模拟中进行大规模强化学习训练，显著缩短了智能工厂的自动化部署周期。",
        "money": "依靠物理仿真和具身智能的自动化流水线，不仅极大提升了高密度智能设备的生产效率，也为全球制造业的自动化机器人技术集成开拓了新路径。",
        "action": "“依托英伟达 Isaac 平台，富士康实现了在虚拟物理世界中对智能机器人和机械臂的高效训练与落地部署。”",
        "script": "【深度观察】富士康已从传统制造服务商向智慧工厂解决方案商转型。依托英伟达 Isaac 智能机器人平台，富士康在虚拟世界中对机械臂及自动搬运车进行大规模模拟训练，实现了高精度具身智能设备的高效落地。"
    },
    "tsmc.com": {
        "shortName": "TS",
        "tech": "cuLitho 先进计算光刻软件库 / 先进制程代工",
        "disassembly": "台积电是全球最大的半导体代工制造服务商，也是英伟达高性能芯片能够规模化量产的供应链基石。同时，台积电引入了英伟达的 cuLitho 计算光刻加速软件库，将光刻过程的物理仿真计算速度提升了上百倍，极大地拓宽了先进制程的物理极限。",
        "money": "台积电在晶圆制造与先进封装（如 CoWoS）领域的领先实力，不仅为双方在 2 纳米及更先进工艺下的芯片量产铺平了道路，也决定了全球高性能 AI 算力芯片的供给天花板。",
        "action": "“台积电引入英伟达 cuLitho 计算库，使芯片光刻物理仿真速度提升百倍，推动了芯片先进制程的跨代量产。”",
        "script": "【深度观察】半导体晶圆制造旗舰台积电与英伟达在先进制程制造及计算光刻领域展开了长期而紧密的协作。cuLitho 计算库的引入，使得芯片光刻仿真速度提升百倍，为双方在 2 纳米及更先进工艺下的芯片量产铺平了道路。"
    }
}

# Define the 8 Easter eggs / funny logos
easter_eggs = {
    "hua_niang": {
        "id": "hua_niang",
        "name": "【美食花絮】花娘小馆 (Hua Niang)",
        "shortName": "花娘",
        "logo": "hua_niang.png",
        "tech": "台北知名川菜馆 / 科技高管非正式聚会点",
        "website": "https://www.google.com/maps/search/?api=1&query=台北花娘小馆",
        "description": "位于台北松山区的知名川菜馆。英伟达创始人黄仁勋在台北电脑展期间多次在此设宴款待全球科技高管，招牌菜‘苍蝇头’在业界广为人知。该店被列入合作伙伴背景板，展现了英伟达企业文化中亲和、日常的在地人文情怀。",
        "money": "台北出差与科技人聚会必去的美食打卡圣地。这也是观察台湾商界名流、科技大佬非正式社交的顶级窗口。",
        "action": "“科技的尽头也是人情味，老黄把最爱的苍蝇头馆子塞进发布会，证明吃货也能做大事！”",
        "script": "【美食花絮】在马斯克 xAI 旁边，是英伟达本次发布会中安插的美食彩蛋——花娘小馆。作为黄仁勋本人十分喜爱的川菜馆，这里是科技巨头们在商务讨论之余感受在地温情生活的一个切片，体现了科技与日常人文的融合。"
    },
    "wang_ji": {
        "id": "wang_ji",
        "name": "【美食花絮】王记府城肉粽 (Wang Ji)",
        "shortName": "王记",
        "logo": "wang_ji.png",
        "tech": "台北知名小吃 / 传统台式肉粽",
        "website": "https://www.google.com/maps/search/?api=1&query=台北王记府城肉粽",
        "description": "台北八德路历史悠久的传统台式肉粽店，主打南部粽。黄仁勋在访问台北期间曾多次光顾，展示了英伟达企业高管接地气的在地互动与人文特质。",
        "script": "【美食花絮】在 Weka 旁边，是赫赫有名的王记府城肉粽。老黄曾深夜来这里吃宵夜被粉丝野生捕获。万亿总裁也爱吃几十块的南部粽，这种接地气的作风正是英伟达能打动开发者和普通大众的品牌文化象征！"
    },
    "fu_ba_wang": {
        "id": "fu_ba_wang",
        "name": "【美食花絮】富霸王猪脚 (Fu Ba Wang)",
        "shortName": "富霸王",
        "logo": "fu_ba_wang.png",
        "tech": "台北人气餐饮 / 卤猪脚名店",
        "website": "https://www.google.com/maps/search/?api=1&query=台北富霸王猪脚",
        "description": "台北四平商圈的知名人气卤猪脚餐厅。黄仁勋在台北期间曾特意派人打包带走以作午餐，被媒体报道后广为流传，体现了极致单品在传统消费服务业中的商业魅力。",
        "script": "【美食花絮】在 Zerone 旁边，是著名的富霸王猪脚。老黄为了吃这口饭，宁愿派人专程去排队打包。这说明只要在一个细分领域把产品做到无可替代，连世界级的科技巨头也会成为忠实支持者！"
    },
    "fruit_lady": {
        "id": "fruit_lady",
        "name": "【美食花絮】阿婆水果摊 (Fruit Lady)",
        "shortName": "水果",
        "logo": "fruit_lady.png",
        "tech": "通化街切片水果 / 特邀年会嘉宾",
        "website": "https://www.google.com/maps/search/?api=1&query=台北通化街阿婆水果摊",
        "description": "台北通化夜市的一家切片水果摊，由一位阿婆经营。黄仁勋多次在此买水果并大力赞赏。英伟达甚至邀请这位阿婆参加了台北尾牙大年会，成为企业温情公关的典范故事。",
        "script": "【美食花絮】在 Visionbey 旁边，是台北通化夜市的阿婆水果摊。老黄不仅购买并夸赞她卖芒果，还邀请她作为尾牙年会的特邀嘉宾。这种人性化、接地气的品牌文化，极大地丰富了科技巨头的人文内涵。"
    },
    "zhuan_yao": {
        "id": "zhuan_yao",
        "name": "【美食花絮】砖窑古早味怀旧餐厅 (磚窯)",
        "shortName": "砖窑",
        "logo": "zhuan_yao.png",
        "tech": "怀旧餐厅 / 顶级科技高管包场举办‘兆元宴’现场",
        "website": "https://www.google.com/maps/search/?api=1&query=台北砖窑古早味怀旧餐厅",
        "description": "一间充满台式红砖怀旧与铁皮玩具收藏特色的古早味餐厅。黄仁勋在此包场举办晚宴，款待了台积电、广达、鸿海等全球 AI 供应链的顶级科技高管（被称为‘兆元宴’）。",
        "script": "【美食花絮】在 Zscaler 的右边，是压轴的美食彩蛋——砖窑古早味餐厅。这里是黄仁勋包场举办‘兆元宴’款待台积电、广达、鸿海等科技大佬的现场。许多全球 AI 供应链的核心协作意向，都是在这间充满复古怀旧气息的台菜餐厅里敲定的。"
    },
    "ai_you_de_gou": {
        "id": "ai_you_de_gou",
        "name": "【趣味彩蛋】爱优 of 狗 (Iyoudog)",
        "shortName": "优狗",
        "logo": "ai_you_de_gou.png",
        "tech": "涂鸦标志 / 极客趣味模因",
        "website": "https://www.google.com/search?q=爱优的狗+黄仁勋",
        "description": "位于 Beyond AI 旁边的滑稽手绘狗头，附有‘爱优的狗’字样。这代表英伟达在严谨、硬核的生态背板中，植入的一丝极客幽默感与趣味彩蛋。",
        "script": "【趣味花絮】在第二行的 Beyond AI 旁边，有个滑稽狗头标志，写着‘爱优的狗’。这代表英伟达在严谨的供应链背板中植入的极客幽默与非正式文化。"
    },
    "shengni": {
        "id": "shengni",
        "name": "【趣味彩蛋】SHENGNI",
        "shortName": "圣尼",
        "logo": "shengni.png",
        "tech": "趣味标志 / 在地中文符号",
        "website": "https://www.google.com/search?q=SHENGNI+黄仁勋",
        "description": "位于 BizLink 旁边的趣味中文标志，是黄仁勋在合作伙伴大屏幕中设计的一个生活气息与在地印记符号。",
        "script": "【趣味花絮】BizLink 旁边也有一个写着 SHENGNI 的中文标志。这也是老黄在发布会上秀科技肌肉的同时，给台湾在地大众留下的趣味符号。"
    },
    "cola": {
        "id": "cola",
        "name": "【趣味彩蛋】COLA (Compal/Cooler Master)",
        "shortName": "可乐",
        "logo": "cola.png",
        "tech": "拼合标志 / 在地谐音模因",
        "website": "https://www.google.com/search?q=COMPAL+Cooler+Master+NVIDIA",
        "description": "仁宝电脑（COMPAL）与散热巨头酷冷至尊（Cooler Master）在视觉上的合并简称，被极客圈谐音称为老黄的‘快乐可乐’，代表两大代工与硬件基石在英伟达产业链中的协同支持。",
        "script": "【趣味花絮】在仁宝 COMPAL 旁边，有一个写着 COLA 的标志。它实际上是仁宝与酷冷至尊 (Cooler Master) 在视觉上的合体，被戏称为快乐水，也象征着代工与散热两强在 AI 高热功耗时代的生态支撑。"
    }
}

y_centers = [96.6, 161.8, 226.1, 291.0, 357.8, 420.2, 484.8, 553.4, 621.5, 690.0, 753.8, 821.5, 881.1]

def generate_fallback_content(name, domain, desc, row_num):
    text = f"{name} {domain} {desc}".lower()
    
    # 默认分类与词条
    cat_tech = "英伟达同盟军"
    core_highlight = f"定位是 {desc}。"
    nvidia_synergy = "作为诸神之墙上的一员，通过硬件兼容或方案定制，帮助英伟达的算力渗透到更细分行业场景中。"
    viral_quote = f"“老黄朋友圈里的低调实力派，默默用英伟达算力跑通行业闭环。”"
    
    # 1. 底层芯片与供应链 (Semiconductor / Chip Infrastructure)
    if any(k in text for k in ["tsmc", "hynix", "micron", "samsung", "asic", "semiconductor", "chip", "hbm", "guc", "alchip", "synopsys", "cadence", "arm", "silicon", "lithography"]):
        cat_tech = "芯片基石 / 算力底层"
        core_highlight = f"专攻芯片级核心技术：{desc}。"
        nvidia_synergy = "老黄 GPU 帝国的基石。没有他们的先进制程、高带宽显存（HBM）或芯片IP，老黄的芯片根本无法大规模量产。"
        viral_quote = "“万亿算力大厦的硬核地基！别光盯着英伟达的显卡，没有他们托底，老黄的芯片根本走不出实验室！”"
        
    # 2. 服务器、算力装配与云服务 (Server / HPC / Cloud)
    elif any(k in text for k in ["server", "data center", "datacenter", "cloud", "compute", "gpu", "supermicro", "quanta", "wiwynn", "wistron", "foxconn", "gigabyte", "asus", "hpe", "dell", "lenovo", "qct", "aicipc", "rack"]):
        cat_tech = "算力装配 / 落地推手"
        core_highlight = f"主要提供算力落地支持：{desc}。"
        nvidia_synergy = "负责帮老黄在客户现场“安家落户”。他们负责把英伟达的芯片整合成整机柜和数据中心，是把算力卖给大厂的最后一公里白手套。"
        viral_quote = "“老黄出图纸，他们出工程！直接帮英伟达把服务器柜子插满客户数据中心的超级装配工。”"

    # 3. 机器人、自动驾驶与物理 AI (Robotics / Physical AI / Embodied)
    elif any(k in text for k in ["robot", "isaac", "automotive", "vehicle", "driving", "adas", "unitree", "agility", "figure", "agibot", "1x", "motion", "diden", "sensor"]):
        cat_tech = "具身智能 / 物理AI"
        core_highlight = f"主打物理AI方向：{desc}。"
        nvidia_synergy = "给英伟达的 AI 大脑“长身体”的具身智能先锋。通过英伟达的 Isaac 或 Jetson 平台训练机器人，共同探索物理世界的下一代搞钱风口。"
        viral_quote = "“给英伟达算力‘装上铁脚板’的未来玩家！让 AI 大脑控制钢筋铁骨，这才是下一代物理世界大杀器。”"

    # 4. 网络、流量调度与零信任安全 (Networking / Security)
    elif any(k in text for k in ["security", "network", "firewall", "zero trust", "palo alto", "zscaler", "fortinet", "checkpoint", "akamai", "cloudflare", "cisco", "link", "cable", "switch"]):
        cat_tech = "算力防线 / 安全保镖"
        core_highlight = f"专注网络与安全侧：{desc}。"
        nvidia_synergy = "算力帝国的安全盾牌。GPU 数据中心开得越猛，流量与防护需求就越大。他们专门提供数据防漏与零信任防线。"
        viral_quote = "“算力帝国的金牌保镖！GPU 跑得再快，数据被偷了也是白搭，他们就是帮老黄看门的最强数字哨兵。”"

    # 5. 科研、医学、高性能计算与学术机构 (Research / Edu / Medical)
    elif any(k in text for k in ["university", "college", "edu", "gov", "hospital", "medical", "research", "hpc", "nchc", "harvard", "stanford", "ntu", "nthu", "nycu", "sinica", "hospital"]):
        cat_tech = "科研大脑 / 行业探路者"
        core_highlight = f"专注学术与前沿应用：{desc}。"
        nvidia_synergy = "英伟达在学术与生命科学界的“最强智囊团”。通过高性能计算和智慧医疗，帮英伟达探索人类基因、疾病和前沿科学的极限应用。"
        viral_quote = "“科学家与万亿资本的梦幻联动！帮老黄把算力火种播撒在攻克绝症与超级计算的无人区里。”"

    # 6. 软件、算法大模型与 AI 平台 (Software / Models)
    elif any(k in text for k in ["model", "ai", "llm", "software", "platform", "simulation", "design", "omniverse", "adobe", "openai", "anthropic", "runway", "deephow", "apmic", "deepl"]):
        cat_tech = "模型先锋 / AI应用玩家"
        core_highlight = f"主打软件与 AI 平台：{desc}。"
        nvidia_synergy = "吃透 CUDA 和英伟达软件栈的实际应用派。不管是做 3D 物理仿真还是视频生成大模型，都在源源不断地为英伟达贡献应用生态壁垒。"
        viral_quote = "“老黄生态圈 of 狂热追随者！把英伟达的软件用到极致，在应用端疯狂掘金的生态大功臣。”"

    script = f"【深度观察】{name}（第 {row_num} 行）在英伟达计算生态中被定位为：{cat_tech}。其业务特征是：{core_highlight} {nvidia_synergy} 正如业界所言：{viral_quote}"
    return cat_tech, core_highlight, nvidia_synergy, viral_quote, script

# 1. Build companies list dynamically from partner_rows
companies_list = []
row_company_ids = {f"row-{i+1}": [] for i in range(13)}

for r_idx, row in enumerate(partner_rows):
    row_num = r_idx + 1
    cat_id = f"row-{row_num}"
    
    for c_idx, (name, domain, desc) in enumerate(row):
        c_id = domain.replace(".", "_").replace("-", "_")
        row_company_ids[cat_id].append(c_id)
        
        # Abbreviation
        short_name = name[:2]
        if len(name) > 2 and name[2].isupper():
            short_name = name[:3]
        
        # Look up coordinates in coords JSON:
        logo_filename = f"{domain}.png"
        if logo_filename in coords:
            x1 = coords[logo_filename]["x1"]
            x2 = coords[logo_filename]["x2"]
            y1 = coords[logo_filename]["y1"]
            y2 = coords[logo_filename]["y2"]
        else:
            # Fallback based on row centers
            y_c = y_centers[r_idx]
            y1 = int(y_c - 25)
            y2 = int(y_c + 25)
            x1 = 100
            x2 = 200
            print(f"Warning: Coordinates not found for {logo_filename}")
            
        # Fallback fields
        cat_tech, core_highlight, nvidia_synergy, viral_quote, fallback_script = generate_fallback_content(name, domain, desc, row_num)
        
        # Base company dict
        comp_dict = {
            "id": c_id,
            "name": name,
            "shortName": short_name,
            "category": cat_id,
            "logo": f"{domain}.png",
            "tech": cat_tech,
            "website": f"https://{domain}",
            "coords": {"x1": x1, "x2": x2, "y1": y1, "y2": y2},
            "disassembly": core_highlight,
            "money": nvidia_synergy,
            "action": viral_quote,
            "script": fallback_script
        }
        
        # If domain is in easter_eggs, overlay the properties
        if domain in easter_eggs:
            egg = easter_eggs[domain]
            comp_dict["id"] = egg.get("id", c_id)
            comp_dict["name"] = egg.get("name", name)
            comp_dict["shortName"] = egg.get("shortName", short_name)
            comp_dict["logo"] = egg.get("logo", f"{domain}.png")
            comp_dict["tech"] = egg.get("tech", cat_tech)
            comp_dict["website"] = egg.get("website", f"https://{domain}")
            comp_dict["disassembly"] = egg.get("disassembly", egg.get("description", ""))
            comp_dict["money"] = egg.get("money", "")
            comp_dict["action"] = egg.get("action", "")
            comp_dict["script"] = egg.get("script", "")
            
        # Overlay pre-defined core data if exists
        elif domain in core_data:
            core = core_data[domain]
            comp_dict["shortName"] = core["shortName"]
            comp_dict["tech"] = core["tech"]
            comp_dict["disassembly"] = core["disassembly"]
            comp_dict["money"] = core["money"]
            comp_dict["action"] = core["action"]
            comp_dict["script"] = core["script"]
            
        companies_list.append(comp_dict)

unmatched_json_path = "/Users/popoya/Movies/视频生产/诸神之墙/debug_unmatched/_unmatched_data.json"
if os.path.exists(unmatched_json_path):
    print(f"[INFO] Skipping injection of unmatched placeholders from {unmatched_json_path}")
    unmatched_data = None  # explicit no-op for clarity

# Generate a filler mesh for the Taiwan Map to ensure it dims completely
mesh_id_counter = 1
for mx in range(1380, 1630, 10):
    for my in range(250, 650, 10):
        # Check if this 10x10 box overlaps with ANY existing company
        overlaps = False
        for comp in companies_list:
            cx1 = comp["coords"]["x1"]
            cx2 = comp["coords"]["x2"]
            cy1 = comp["coords"]["y1"]
            cy2 = comp["coords"]["y2"]
            # Two rectangles overlap if they DO NOT satisfy the non-overlap conditions
            if not (mx + 10 <= cx1 or mx >= cx2 or my + 10 <= cy1 or my >= cy2):
                overlaps = True
                break
        
        if not overlaps:
            c_id = f"taiwan_mesh_{mesh_id_counter}"
            cat_id = "row-bg"
            comp_dict = {
                "id": c_id,
                "name": f"台湾地图背景 {mesh_id_counter}",
                "shortName": "",
                "category": cat_id,
                "logo": "",
                "tech": "背景",
                "website": "#",
                "coords": {"x1": mx, "x2": mx+10, "y1": my, "y2": my+10},
                "disassembly": "这是墙上的背景图案。",
                "money": "无",
                "action": "无",
                "script": ""
            }
            companies_list.append(comp_dict)
            mesh_id_counter += 1

# 2. Build script_phases dynamically for each row (for study panel navigation)
script_phases = {
    "all": {
        "title": "英伟达 AI 帝国生态全景导览",
        "scripts": [
            "【研读导言】本栏目旨在系统化剖析英伟达在 2026 年台北电脑展上展出的全球合作伙伴生态墙。整面墙包含了 13 行、共 285 家企业与核心机构，展现了英伟达从底层芯片制造、超级计算网络、云算力托管到具身智能机器人及大模型应用软件的庞大帝国版图。",
            "【使用指南】您可以通过左侧导航进行逐行深度研读，点击具体公司卡片可查看其详细业务特征、NVIDIA 计算生态定位及业界合作的深度洞察。"
        ]
    }
}

for i in range(13):
    row_num = i + 1
    cat_id = f"row-{row_num}"
    script_phases[cat_id] = {
        "title": f"第 {row_num} 行生态合作伙伴研读",
        "companies": row_company_ids[cat_id],
        "outro": f"以上为第 {row_num} 行合作伙伴的生态定位复盘。您可以继续选择其他行，或者使用搜索框快速检索特定领域的企业。"
    }

# 3. Read current app.js bottom part
with open(app_js_path, "r", encoding="utf-8") as f:
    orig_app = f.read()

# Locate "// 状态管理"
split_index = orig_app.find("// 状态管理")
if split_index == -1:
    print("Error: Could not find state management marker in app.js!")
    sys.exit(1)
app_bottom_logic = orig_app[split_index:]

# Custom replace in bottom logic to handle row-X category names beautifully
old_category_name_func = """function getCategoryName(cat) {
  switch(cat) {
    case "hardware": return "硬核硬件组 (RTX Spark)";
    case "software": return "生产力软件组 (OpenShell)";
    case "industrial": return "具身智能与工业孪生 (Omniverse)";
    default: return "英伟达生态伙伴";
  }
}"""

new_category_name_func = """function getCategoryName(cat) {
  if (cat && cat.startsWith("row-")) {
    return "第 " + cat.split("-")[1] + " 行合作伙伴";
  }
  switch(cat) {
    case "hardware": return "硬核硬件组 (RTX Spark)";
    case "software": return "生产力软件组 (OpenShell)";
    case "industrial": return "具身智能与工业孪生 (Omniverse)";
    default: return "英伟达生态伙伴";
  }
}"""

if old_category_name_func in app_bottom_logic:
    app_bottom_logic = app_bottom_logic.replace(old_category_name_func, new_category_name_func)

# Replace references to videoScriptPhases in the bottom logic
app_bottom_logic = app_bottom_logic.replace("videoScriptPhases", "studyScriptPhases")

# 4. Write new app.js
new_app_js = f"""// ==========================================================================
// NVIDIA 2026 Partner Matrix Interactive System Logic (FULL 13 ROWS EDITION)
// ==========================================================================

// 核心数据集 (285 合作伙伴 & 美食/趣味彩蛋)
const companies = {json.dumps(companies_list, indent=2, ensure_ascii=False)};

// 深度研习模式下的分行观察导览数据
const studyScriptPhases = {json.dumps(script_phases, indent=2, ensure_ascii=False)};

{app_bottom_logic}
"""

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(new_app_js)
print("Rewrote app.js successfully with all 285 companies and Easter eggs!")

# 5. Update index.html filter tabs to row-based tabs
with open(index_html_path, "r", encoding="utf-8") as f:
    html = f.read()

old_tabs_block = """      <div class="filter-tabs">
        <button class="tab-btn active" data-category="all">全部公司</button>
        <button class="tab-btn" data-category="hardware">硬核硬件组 (RTX Spark)</button>
        <button class="tab-btn" data-category="software">生产力软件组 (OpenShell)</button>
        <button class="tab-btn" data-category="industrial">具身智能与工业孪生 (Omniverse)</button>
      </div>"""

new_tabs_block = """      <div class="filter-tabs" style="overflow-x: auto; display: flex; gap: 8px; max-width: 100%; padding-bottom: 8px;">
        <button class="tab-btn active" data-category="all">全部公司</button>
        <button class="tab-btn" data-category="row-1">第 1 行</button>
        <button class="tab-btn" data-category="row-2">第 2 行</button>
        <button class="tab-btn" data-category="row-3">第 3 行</button>
        <button class="tab-btn" data-category="row-4">第 4 行</button>
        <button class="tab-btn" data-category="row-5">第 5 行</button>
        <button class="tab-btn" data-category="row-6">第 6 行</button>
        <button class="tab-btn" data-category="row-7">第 7 行</button>
        <button class="tab-btn" data-category="row-8">第 8 行</button>
        <button class="tab-btn" data-category="row-9">第 9 行</button>
        <button class="tab-btn" data-category="row-10">第 10 行</button>
        <button class="tab-btn" data-category="row-11">第 11 行</button>
        <button class="tab-btn" data-category="row-12">第 12 行</button>
        <button class="tab-btn" data-category="row-13">第 13 行</button>
      </div>"""

if old_tabs_block in html:
    html = html.replace(old_tabs_block, new_tabs_block)
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html successfully with row tabs!")
else:
    if "data-category=\"row-1\"" in html:
        print("index.html already has row tabs.")
    else:
        print("Warning: could not find old tabs block, index.html might need custom search and replace.")

# 6. Update style.css to support hover effect for row-based tags
with open(style_css_path, "r", encoding="utf-8") as f:
    css = f.read()

custom_css_row = """
.company-card[data-category^="row-"]:hover .tech-tag {
  color: var(--color-nvidia);
  background: rgba(118, 185, 0, 0.08);
}
"""

if '[data-category^="row-"]' not in css:
    css += custom_css_row
    with open(style_css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated style.css row styling successfully!")
else:
    print("style.css already has row styles.")
