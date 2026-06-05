import os

# 13 行完整的数据映射 (已按屏幕物理坐标从左到右排序)
partner_rows = [
    # Row 1 (Total: 21)
    [
        ('1X', '1x.tech', 'OpenAI投资的人形机器人先驱'),
        ('AAEON', 'aaeon.com', '研扬科技，全球先进工业电脑与边缘计算平台制造商'),
        ('ABB Robotics', 'abb.com', '全球工业机器人四大家族之一，工业自动化巨头'),
        ('Academia Sinica', 'sinica.edu.tw', '台湾学术研究机构（中央研究院）'),
        ('Accton', 'accton.com', '智邦科技，全球云数据中心交换机代工龙头'),
        ('Accuracrazy', 'accuracrazy.com', '高精度AI视觉或系统方案商'),
        ('Acer', 'acer.com', '宏碁，知名个人电脑与硬件品牌'),
        ('ADLINK', 'adlinktech.com', '凌华科技，工业电脑与边缘计算专家'),
        ('Adobe', 'adobe.com', '创意与设计软件巨头，推出本地AI Agent'),
        ('Advanced Intelligence', 'advancedintelligence.com', '前沿智能硬件/软件方案商'),
        ('Advantech', 'advantech.com', '研华科技，全球工业电脑与边缘物联网龙头'),
        ('Aetina', 'aetina.com', '安提国际，边缘AI硬件与GPU加速方案商'),
        ('AFARI', 'afari.io', '边缘AI与智能连接技术'),
        ('Agibot', 'agibot.com', '智元机器人，国内具身智能明星企业'),
        ('Agile Robots', 'agile-robots.com', '思灵机器人，智能机器人独角兽'),
        ('Agility', 'agilityrobotics.com', '知名双足机器人Digit研发商'),
        ('Aible', 'aible.com', '企业级AI分析与自动化部署'),
        ('AIC', 'aicipc.com', '营邦企业，服务器机壳与系统设计商'),
        ('Ailytics', 'ailytics.ai', 'AI视频安全监控解决方案'),
        ('AIM', 'aim.com', '前沿计算方案商'),
        ('Aivres', 'aivres.com', '下一代云数据中心服务器供应商'),
    ],
    # Row 2 (Total: 24)
    [
        ('Akamai', 'akamai.com', '全球CDN与边缘安全巨头'),
        ('Anivance', 'anivance.com', '生物技术与AI计算'),
        ('Alchip', 'alchip.com', '世芯电子，高阶ASIC芯片设计龙头'),
        ('Alibaba Cloud', 'alibabacloud.com', '阿里云，中国最大云服务提供商'),
        ('Alsemy', 'alsemy.com', '半导体设计与AI方案商'),
        ('Anthropic', 'anthropic.com', '大模型独角兽，Claude母公司'),
        ('Arm', 'arm.com', '半导体芯片架构巨头，移动与端侧AI基石'),
        ('APMIC', 'apmic.com', '大语言模型及企业知识库引擎'),
        ('Armis', 'armis.com', '物联网资产管理与网络安全龙头'),
        ('ASRock', 'asrock.com', '华擎科技，知名主板及显卡硬件品牌'),
        ('ASRock Rack', 'asrockrack.com', '华擎科技旗下AI服务器品牌'),
        ('Astera Labs', 'asteralabs.com', '高带宽连接芯片设计新贵，AI独角兽'),
        ('ASUS', 'asus.com', '华硕电脑，个人PC与ROG电竞显卡巨头'),
        ('Atos', 'atos.net', '欧洲IT服务与超级计算机巨头'),
        ('Autobrains', 'autobrains.ai', '自动驾驶与ADAS车用视觉芯片与防撞算法开发商'),
        ('AVerMedia', 'avermedia.com', '圆刚科技，视频采集卡与边缘AI设备商'),
        ('AWS', 'amazon.com', '亚马逊云科技，全球云计算老大'),
        ('Axiomtek', 'axiomtek.com', '艾讯科技，工业物联网与嵌入式电脑'),
        ('【趣味彩蛋】爱优的狗 (Iyoudog)', 'ai_you_de_gou', '老黄的趣味涂鸦 / 滑稽狗头'),
        ('Beyond AI', 'beyondai.com', '智能多媒体与AI算法提供商'),
        ('【趣味彩蛋】SHENGNI', 'shengni', '趣味标志 / 在地中文文字'),
        ('BizLink', 'bizlinktech.com', '贸联，全球高性能连接线缆巨头'),
        ('Black Forest Labs', 'blackforestlabs.ai', 'Flux开源图像模型母公司'),
        ('BYD', 'byd.com', '比亚迪，新能源车与代工巨头'),
    ],
    # Row 3 (Total: 22)
    [
        ('ByteDance', 'bytedance.com', '字节跳动，全球短视频与算法巨头'),
        ('Cadasu', 'cadasu.com', '智能工业方案商'),
        ('Cadence', 'cadence.com', 'EDA芯片设计软件巨头'),
        ('Canonical', 'canonical.com', 'Ubuntu Linux发行版母公司'),
        ('Carnegie Mellon University', 'cmu.edu', '卡耐基梅隆大学，顶尖计算机与机器人高校'),
        ('Cathay Financial Holding', 'cathayholdings.com', '国泰金控，台湾最大金融控股集团，AI智能理财与智慧金融基石'),
        ('Centific', 'centific.com', '全球数字化平台与数据标注商'),
        ('Chang Gung Hospital', 'cgmh.org.tw', '长庚纪念医院，台湾智慧医疗示范院所'),
        ('Check Point', 'checkpoint.com', '全球网络安全巨头'),
        ('Chenbro', 'chenbro.com', '勤诚兴业，全球服务器机壳制造龙头'),
        ('Chunghwa Telecom', 'cht.com.tw', '中华电信，台湾最大电信运营商'),
        ('Cisco', 'cisco.com', '思科，网络硬件设备巨头'),
        ('Clevo', 'clevo.com.tw', '蓝天电脑，知名笔记本代工大厂'),
        ('Cloudflare', 'cloudflare.com', '全球CDN与边缘安全网络'),
        ('Cloudian', 'cloudian.com', '企业级混合云对象存储'),
        ('Codetrace', 'codetrace.com', '智能代码与开发工具'),
        ('Compal', 'compal.com', '仁宝电脑，全球最大的笔记本代工厂之一'),
        ('【趣味彩蛋】COLA', 'cola', 'COMPAL与coolermaster的趣味拼合标志'),
        ('Cooler Master', 'coolermaster.com', '酷冷至尊，全球电脑散热、均热板与水冷排解决方案巨头'),
        ('CoreWeave', 'coreweave.com', '英伟达投资的GPU算力云新星'),
        ('CrowdStrike', 'crowdstrike.com', '全球终端安全与杀毒巨头'),
        ('Crusoe', 'crusoeenergy.com', '绿色能源/清洁电力AI算力云'),
    ],
    # Row 4 (Total: 25)
    [
        ('Danfoss', 'danfoss.com', '丹佛斯，工业精密散热与变频器'),
        ('Dassault Systèmes', '3ds.com', '达索系统，全球领先的 3D 体验与 PLM 工业设计软件巨头'),
        ('DCAI', 'dcai', '数据中心与AI算力系统'),
        ('D-Link', 'dlink.com', '友讯科技，全球知名的网络设备商'),
        ('DDN', 'ddn.com', 'DataDirect Networks，高性能大模型海量存储'),
        ('DeepL', 'deepl.com', '全球领先的AI翻译与多语言大模型平台'),
        ('DeepHow', 'deephow.com', '面向工业技能培训的AI视频工作流'),
        ('DeepRad.AI', 'deeprad.ai', '医疗影像AI智能诊断'),
        ('Dell Technologies', 'dell.com', '戴尔科技，传统PC与服务器巨头'),
        ('Delta', 'deltaww.com', '台达电，全球电源与工业散热龙头'),
        ('Diden Robotics', 'didenrobotics.com', '具身智能机器人手臂及方案商'),
        ('E.SUN Bank', 'esunbank.com', '玉山银行，台湾智慧金融试点银行'),
        ('Edom Technology', 'edomtech.com', '益登科技，亚太领先的半导体器件代理商与技术通路商'),
        ('Eotylab', 'eotylab.com', '智能计算及软件'),
        ('Emerald AI', 'emeraldai.com', '企业AI智能应用与业务工作流管理'),
        ('ETH Zürich', 'ethz.ch', '苏黎世联邦理工学院，顶尖科技名校'),
        ('EverFocus', 'everfocus.com.tw', '慧友电子，车载监控与智能出行'),
        ('Everpure', 'everpure.com', '工业及民用滤水与系统环境'),
        ('Feng Chia University', 'fcu.edu.tw', '逢甲大学，知名科技与工程高校'),
        ('Figure', 'figure.ai', '顶尖人形机器人独角兽'),
        ('Firmus', 'firmus.co', '液冷超算数据中心服务商'),
        ('F5 Networks', 'f5.com', '全球领先的超大规模应用安全与多云流量调度交付巨头'),
        ('Flex', 'flex.com', '伟创力，全球大型电子制造与组装商'),
        ('Findings Tech', 'findingstech.com', '智能网络与数据分析'),
        ('Flexcompute', 'flexcompute.com', '超算物理仿真计算系统'),
    ],
    # Row 5 (Total: 22)
    [
        ('Fortinet', 'fortinet.com', '飞塔，全球防火墙与安全巨巨头'),
        ('Fortune AI', 'fortuneai.com', '企业AI系统集成'),
        ('Foxconn', 'foxconn.com', '富士康/鸿海，全球代工之王，AI服务器主力'),
        ('Foxlink', 'foxlink.com', '正崴精密，全球领先的精密连接器、线缆与核心组件制造商'),
        ('FSP', 'fsp-group.com', '全汉电源，高功率电源供应器专家'),
        ('Fujitsu', 'fujitsu.com', '富士通，日本最大的IT服务商'),
        ('G2C+', 'g2cplus.com', '台湾半导体封测及自动化设备联盟'),
        ('Futurenesia', 'futurenesia', '前沿智能硬件与系统集成'),
        ('Gartner', 'gartner.com', '全球权威信息技术咨询公司'),
        ('Giga Computing', 'gigacomputing.com', '技钢科技，技嘉旗下AI服务器品牌'),
        ('Gigabyte', 'gigabyte.com', '技嘉科技，显卡、主板及高性能计算'),
        ('GMI', 'gmit.com', '吉佳通，亚太区硬件与半导体代理分销商'),
        ('Goldman Sachs', 'goldmansachs.com', '高盛集团，全球顶级投行'),
        ('Google Cloud', 'cloud.google.com', '谷歌云，全球三大公有云之一'),
        ('Greneta', 'greneta.com', '前沿智能系统'),
        ('GUC', 'guc-asic.com', '创意电子，台积电旗下ASIC定制芯片设计大厂'),
        ('Harvard University', 'harvard.edu', '哈佛大学，全球顶尖名校'),
        ('Hesai', 'hesai.com', '禾赛科技，全球激光雷达龙头'),
        ('Hitachi Vantara', 'hitachivantara.com', '日立旗下海量数据存储与混合云'),
        ('Holon', 'holonsolutions.com', '智能建筑与能源管理'),
        ('HP', 'hp.com', '惠普，全球领先的个人电脑与数位打印硬件品牌'),
        ('HPE', 'hpe.com', '慧与科技，大型服务器与超级计算机供应商'),
    ],
    # Row 6 (Total: 20)
    [
        ('Humain', 'humain.ai', 'AI虚拟人与3D数字资产自动生成'),
        ('Hydra', 'hydra.com', '高带宽存储网络方案'),
        ('Hyve Solutions', 'hyvesolutions.com', '超大型数据中心定制化服务器设计商'),
        ('IBM', 'ibm.com', '蓝色巨人，提供企业混合云与红帽Linux生态'),
        ('Inno3D', 'inno3d.com', '映众，知名游戏显卡品牌'),
        ('Intel', 'intel.com', '英特尔，CPU巨头，AI加速计算重要参与者'),
        ('Inventec', 'inventec.com', '英业达，知名服务器与笔记本ODM厂商'),
        ('In Win', 'inwin.com', '迎广科技，全球领先的专业电脑机箱、服务器机壳与系统液冷机架制造商'),
        ('Jabil', 'jabil.com', '捷普，全球电子组装与结构件巨头'),
        ('J-Mex', 'j-mex.com', '捷迈，专业六轴运动传感器'),
        ('IREN', 'iren.com', 'Iris Energy, 绿色能源驱动的超大型AI数据中心算力托管提供商'),
        ('Jentech', 'jentech.com.tw', '健策精密，半导体均热片与散热老大'),
        ('JPC', 'jpceec.com', '佳必琪，高速连接线缆与光收发模块'),
        ('I-Shou University', 'isu.edu.tw', '义守大学，知名科技院校'),
        ('Kenmec', 'kenmec.com', '广运机械，自动化物流与服务器液冷散热'),
        ('KYEC', 'kyec.com.tw', '京元电子，全球大型半导体封装测试厂'),
        ('Lablup', 'lablup.com', '容器化大模型部署与调度平台'),
        ('Lambda', 'lambdalabs.com', '专注GPU算力租用的云平台'),
        ('Lanner', 'lanner.com', '立端科技，全球网络安全与车载边缘电脑'),
        ('Leadtek', 'leadtek.com', '丽台科技，专业显卡与AI算力工作站'),
    ],
    # Row 7 (Total: 19)
    [
        ('Lenovo', 'lenovo.com', '联想集团，全球第一大PC厂商，本地AI白手套'),
        ('MetAI', 'metai.com', '工业元宇宙协同设计'),
        ('Lightricks', 'lightricks.com', 'AI修图与视频编辑独角兽'),
        ('Linker Vision', 'linkervision.com', 'Linker Vision, 工业多模态大模型与连续视觉AI安全检测方案商'),
        ('LiteOn', 'liteon.com', '光宝科技，服务器高效电源与液冷机构龙头'),
        ('LTX', 'ltx.ai', '智能金融与企业级生成式AI工作流平台'),
        ('Lucid', 'lucidmotors.com', '豪华智能电动车品牌'),
        ('Luminary', 'luminary.cloud', '光子与红外图像AI计算'),
        ('MacKay Hospital', 'mmh.org.tw', '马偕纪念医院，知名智慧医疗示范机构'),
        ('Macnica', 'macnica.co.jp', '日本第一大半导体与AI方案分销商'),
        ('Marvell', 'marvell.com', '美满电子，高速光通信与以太网芯片老大'),
        ('Maxsun', 'maxsun.com.cn', '铭瑄，高性价比显卡与主板硬件'),
        ('MediaTek', 'mediatek.com', '联发科，天玑SoC与车载系统芯片霸主'),
        ('Meta', 'meta.com', '开源大模型Llama的发布者'),
        ('Micron', 'micron.com', '美光科技，内存与高性能HBM3E供应商'),
        ('Microsoft', 'microsoft.com', '微软，AI应用与Copilot端侧系统'),
        ('Fu Jen University', 'fju.edu.tw', '辅仁大学，知名智慧医疗/工程高校'),
        ('MinIO', 'min.io', '超高速开源分布式对象存储'),
        ('MOHW', 'mohw.gov.tw', '卫生福利部，推动台湾智慧医疗与健康数据治理'),
    ],
    # Row 8 (Total: 20)
    [
        ('Mirantis', 'mirantis.com', '企业级云和Kubernetes容器服务商'),
        ('CSAI', 'csai', '智能系统与企业计算技术'),
        ('MiTAC', 'mitac.com', '神达电脑，工业控制与服务器制造'),
        ('Mitsubishi', 'mitsubishielectric.com', '三菱电机，精密工业自动化与机械臂'),
        ('Morale AI', 'morale.ai', '心理与人机交互AI'),
        ('MSI', 'msi.com', '微星科技，电竞笔记本及AI渲染工作站'),
        ('N.Light', 'nlight.net', '恩耐激光，高功率半导体激光器'),
        ('Nasdaq', 'nasdaq.com', '纳斯达克，全球科技交易所'),
        ('NCHC', 'nchc.org.tw', '国家高速网络与计算中心，台湾高性能学术计算与超算核心'),
        ('National Central Uni', 'ncu.edu.tw', '国立中央大学，台湾主要科研院校'),
        ('MODA', 'moda.gov.tw', '数位发展部，推动数位转型、网络安全与数据治理'),
        ('NCKU', 'ncku.edu.tw', '国立成功大学（重复排布）'),
        ('NYCU', 'nycu.edu.tw', '国立阳明交通大学，台湾半导体黄埔军校'),
        ('NSYSU', 'nsysu.edu.tw', '国立中山大学，知名科技研究大学'),
        ('NTPU', 'ntpu.edu.tw', '国立台北大学，知名智慧商科与法律研究高校'),
        ('NTUT', 'ntut.edu.tw', '国立台北科技大学，台湾顶尖的技术与工程大学'),
        ('NTNU', 'ntnu.edu.tw', '国立台湾师范大学，科技与跨学科教育名校'),
        ('NTU', 'ntu.edu.tw', '国立台湾大学，全台综合实力第一名校'),
        ('NTUST', 'ntust.edu.tw', '国立台湾科技大学，核心技职与工程名校'),
        ('NTHU', 'nthu.edu.tw', '国立清华大学，顶尖学术与半导体院校'),
    ],
    # Row 9 (Total: 25)
    [
        ('Naver Cloud', 'navercloud.com', '韩国最大的云服务与中文大模型开发商'),
        ('Nebius', 'nebius.com', '欧洲高性能AI算力平台'),
        ('Neousys Technology', 'neousys-tech.com', '宸曜科技，宽温防震工业电脑与车载边缘计算系统专家'),
        ('NetApp', 'netapp.com', '全球数据管理与全闪存存储巨头'),
        ('Neural Concept', 'neuralconcept.com', 'Neural Concept, 利用3D深度学习加速工业设计与流体力学仿真的先驱'),
        ('NEXCOM', 'nexcom.com', '新汉，工业电脑、车载系统及机器人中控'),
        ('Nexuni', 'nexuni.com', 'AI智能办公协作平台'),
        ('Noble Machines', 'noblemachines.com', '高精度金属切削与AI监控'),
        ('Nscale', 'nscale.com', '高密度GPU算力云平台'),
        ('nTop', 'ntop.com', '颠覆性的3D工程力学拓扑设计软件'),
        ('NTUH', 'ntuh.gov.tw', '台大医院，台湾顶尖的智慧医疗与临床医学中心'),
        ('Nunox', 'nunox.co', '医疗数据处理'),
        ('Nutanix', 'nutanix.com', '超融合架构与多云统一部署大厂'),
        ('nVent', 'nvent.com', 'nVent, 全球领先的液冷散热、机柜配电与电子保护解决方案商'),
        ('Nyxo', 'nyxo.com', '智能硬件与计算'),
        ('nybl', 'nybl.ai', 'nybl, 工业物联网、预测性维护与企业AI操作系统'),
        ('OpenAI', 'openai.com', 'ChatGPT发布者，英伟达最大客户之一'),
        ('OpenNebula', 'opennebula.io', '开源超融合云管理平台与边缘计算算力调度系统'),
        ('Oracle', 'oracle.com', '甲骨文，企业数据库与GPU云提供商'),
        ('P1.AI', 'p1.ai', '前沿AI智能体与多模态创意内容生成平台'),
        ('Palantir', 'palantir.com', '军工与企业大数据分析绝对霸主'),
        ('Palo Alto Networks', 'paloaltonetworks.com', '全球最大的网络安全巨头'),
        ('Pegatron', 'pegatroncorp.com', '和硕联合，苹果核心组装厂及AI服务器商'),
        ('PhysicsX', 'physicsx.ai', '利用AI重塑流体力学与热力学仿真的软件'),
        ('PNY', 'pny.com', '必恩威，英伟达专业工作站显卡主力分销商'),
    ],
    # Row 10 (Total: 25)
    [
        ('PTC', 'ptc.com', '参数技术，工业CAD/PLM与三维设计龙头'),
        ('Qualcomm', 'qualcomm.com', '高通，端侧AI PC与高算力NPU代表'),
        ('Realtek', 'realtek.com', '瑞昱半导体，知名的‘螃蟹’声卡网卡芯片商'),
        ('Rafay', 'rafay.co', '企业级Kubernetes多集群运维平台'),
        ('REAS', 'reas.com', '智能云分发系统'),
        ('Red Hat', 'redhat.com', '红帽公司，企业开源Linux与OpenShift平台'),
        ('Redpanda', 'redpanda.com', '极速流数据平台，兼容Kafka协议'),
        ('Redpill VR', 'redpillvr.com', '元宇宙、虚拟现场与AI交互设计'),
        ('RLWorld', 'rlworld.com', '强化学习仿真平台'),
        ('Roboflow', 'roboflow.com', '计算机视觉一站式数据标注与训练工具'),
        ('Runway', 'runwayml.com', '生成式视频AI霸主'),
        ('Samsung', 'samsung.com', '三星，HBM显存与晶圆制造巨头'),
        ('Repurgenesis', 'repurgenesis.com', '生成式医疗与AI健康计算'),
        ('SAP', 'sap.com', '全球最大企业ERP管理系统'),
        ('Sarvam AI', 'sarvam.ai', '印度端侧小模型与LLM独角兽'),
        ('SB C&S', 'cas.softbank.jp', '日本软银旗下IT分销与AI集成服务'),
        ('Schneider Electric', 'se.com', '施耐德电气，数据中心供电与制冷龙头'),
        ('Rittal', 'rittal.com', '威图，全球数据中心机柜系统、精密空调温控与液冷散热龙头'),
        ('ServiceNow', 'servicenow.com', '全球工作流数字管理巨头'),
        ('Prime Intellect', 'primeintellect.ai', '分布式AI训练网络与去中心化AI算力共享平台'),
        ('Sharpa', 'sharpa.com', '高端智能终端与显示'),
        ('Siemens', 'siemens.com', '西门子，Omniverse数字孪生工业绝对老大'),
        ('QCT', 'qct.io', '云达科技，广达旗下全球领先的超大型数据中心与AI服务器整机柜集成商'),
        ('Quanta Computer', 'quanta.com', '广达电脑，全球领先的服务器与个人PC设计制造代工巨头'),
        ('Ryoyo Ryosan', 'ryoyo-ryosan.co.jp', 'Ryoyo Ryosan, 日本领先的半导体器件与AI计算硬件分销代理商'),
    ],
    # Row 11 (Total: 21)
    [
        ('Silicon Valley Power', 'siliconvalleypower.com', '硅谷电力，为全球科技巨头数据中心提供清洁能源与稳定电网'),
        ('Simplismart', 'simplismart.ai', 'AI推理性能提速与精简平台'),
        ('SK Hynix', 'skhynix.com', 'SK海力士，全球HBM显存最强供应商之一'),
        ('SK Telecom', 'sktelecom.com', '韩国最大的电信与智慧云服务运营商'),
        ('Skild AI', 'skild.ai', '机器人大模型与具身智能顶尖独角兽'),
        ('Solomon', 'solomon-3d.com', '所罗门，机器人3D视觉引导与机械臂防碰撞'),
        ('Spectra Cloud', 'spectracloud.com', '多云容器资源编排调度'),
        ('BPL', 'bpl.com', '工业级医疗电子与精密传感器解决方案商'),
        ('SpinQ', 'spinq.cn', '本源量子/量旋科技，桌面级超导量子计算'),
        ('Squeezebits', 'squeezebits.com', '端侧大模型超极限裁剪与量化工具'),
        ('Spingence', 'spingence.com', '希源科技，半导体智能量测与AI缺陷检测平台'),
        ('Starburst', 'starburst.io', '企业极速分布式SQL查询引擎'),
        ('Stanford University', 'stanford.edu', '斯坦福大学，AI与计算机科学泰斗高校'),
        ('Superb AI', 'superb-ai.com', 'AI视频与影像数据自动化标注平台'),
        ('Supermicro', 'supermicro.com', '美超微，全球高密度AI服务器与液冷数据中心整机柜系统霸主'),
        ('SynaXG', 'synaxg.com', '5G无线算力与AI基站集成平台'),
        ('Synopsys', 'synopsys.com', '新思科技，EDA芯片设计工具霸主'),
        ('Synera', 'synera.io', '低代码工业流程与机械设计自动化'),
        ('TMU', 'tmu.edu.tw', '台北医学大学，顶尖智慧医疗高校'),
        ('Taichung Hospital', 'tcgh.gov.tw', '台中荣民总医院，智慧医院标杆'),
        ('TSIP', 'tsip.taipei', '台北生技园区，台湾前沿的生物科技与新药研发聚落'),
    ],
    # Row 12 (Total: 22)
    [
        ('TEMC', 'temc.co.kr', '特密科，半导体光刻极紫外线气体材料供应商'),
        ('Soochow University', 'scu.edu.tw', '东吴大学，台湾知名科技人文高校'),
        ('Telit Cinterion', 'telit.com', '泰利特，全球物联网无线模组、边缘连接与物联网软件巨头'),
        ('TMA', 'tma.tw', '智能控制与边缘硬件系统'),
        ('Together.ai', 'together.ai', '高性价比开源大模型托管与API平台'),
        ('Trend Micro', 'trendmicro.com', '趋势科技，全球网络安全软件老牌巨头'),
        ('TrendAI', 'trendai.com', '边缘AI与智能化方案'),
        ('Focus', 'focus', '工业自动化与边缘智能系统'),
        ('TSMC', 'tsmc.com', '台积电（重复展示，强调至高地位）'),
        ('SMC', 'smcworld.com', 'SMC, 全球气动控制元件与工业自动化精密制造绝对龙头'),
        ('THU', 'thu.edu.tw', '东海大学，知名综合性研究型高校'),
        ('Uber', 'uber.com', '优步，利用AI调度的全球出行巨头'),
        ('Unitree', 'unitree.com', '宇树科技（重复展示，表明机器人领头羊地位）'),
        ('Universal Robots', 'universal-robots.com', '全球协作机械臂霸主'),
        ('VAST Data', 'vastdata.com', 'AI原生超大规模高性能存储底座'),
        ('vCluster', 'vcluster.com', 'Kubernetes虚拟集群与算力租用隔离技术'),
        ('Vaidio', 'vaidio.com', 'Vaidio, 顶尖AI视频图像分析与智能安防平台'),
        ('Vecow', 'vecow.com', '超恩科技，工业车载边缘AI计算平台'),
        ('Vertiv', 'vertiv.com', '维谛技术，全球数据中心高功耗液冷散热龙头'),
        ('VinDynamics', 'vindynamics.com', '智能出行与动态控制系统'),
        ('VinAI', 'vinai.io', '智能出行AI深度学习'),
        ('VinFast', 'vinfastauto.com', '越南造车新势力'),
    ],
    # Row 13 (Total: 25)
    [
        ('【美食彩蛋】阿婆水果摊 (Fruit Lady)', 'fruit_lady', '老黄夜市最爱 / 通化街切片水果'),
        ('Virphysio', 'virphysio.com', '智能健康与物理治疗AI分析'),
        ('Visionbay', 'visionbay.ai', '前沿AI视觉检测与智能感知'),
        ('Visionbey.ai', 'visionbey.ai', '视觉AI智能分析'),
        ('Vultr', 'vultr.com', '知名高性能GPU与主机云供应商'),
        ('【美食彩蛋】王记府城肉粽 (Wang Ji)', 'wang_ji', '老黄夜市宵夜 / 传统台式肉粽'),
        ('Weka', 'weka.io', '超高速分布式AI计算文件系统'),
        ('WZU', 'wzu.edu.tw', '文藻外语大学，知名外语与国际事务高校'),
        ('Taipei Hospital', 'vghpe.gov.tw', '台北荣民总医院，高精度智慧诊疗'),
        ('Wistron', 'wistron.com', '纬创资通，AI服务器计算基板独家/主力生产商'),
        ('Wiwynn', 'wiwynn.com', '纬颖科技，纬创旗下超大型云服务与AI服务器整机组装及制造龙头'),
        ('World Wide Tech', 'wwt.com', '全球最大系统集成商之一，AI部署专家'),
        ('【美食彩蛋】花娘小馆 (Hua Niang)', 'hua_niang', '老黄私房爱店 / 经典川菜馆'),
        ('xAI', 'x.ai', '马斯克创立的Grok大模型与超算提供商'),
        ('Xiaomi', 'mi.com', '小米，澎湃OS、超级工厂与智能硬件龙头'),
        ('Yo-Kai Express', 'yokaiexpress.com', '智能自动烹饪拉面机器人'),
        ('Yotta Data Services', 'yotta.co.in', '印度国家主权GPU超算云提供商'),
        ('YTL AI Labs', 'ytl.com', '马来西亚杨忠礼集团旗下AI超算实验室'),
        ('Yuan', 'yuan.com.tw', '聪泰科技，采集卡与多路视频AI处理芯片龙头'),
        ('Yuan Ze University', 'yzu.edu.tw', '元智大学，半导体与AI设计高校'),
        ('【美食彩蛋】富霸王猪脚 (Fu Ba Wang)', 'fu_ba_wang', '老黄午餐外带 / 四平街人气腿扣'),
        ('Zerone', 'zerone.io', '工业机器人与流程自动化'),
        ('Zotac', 'zotac.com', '索泰，知名的显卡与迷你AI硬件品牌'),
        ('Zscaler', 'zscaler.com', '全球安全访问与零信任云防线'),
        ('【美食彩蛋】砖窑古早味怀旧餐厅 (磚窯)', 'zhuan_yao', '老黄商务宴请 / 顶级科技大佬聚餐地'),
    ],
]

# 核心的 50 家公司，用于 partner_directory.md
core_50_domains = {
    "1x.tech", "figure.ai", "unitree.com", "abb.com", "universal-robots.com",
    "tsmc.com", "foxconn.com", "lenovo.com", "asus.com", "msi.com", "mediatek.com",
    "arm.com", "intel.com", "qualcomm.com", "samsung.com", "skhynix.com",
    "micron.com", "hpe.com", "dell.com", "deltaww.com",
    "adobe.com", "autodesk.com", "runwayml.com", "redhat.com", "crowdstrike.com", "palantir.com",
    "openai.com", "anthropic.com", "x.ai", "bytedance.com", "alibabacloud.com",
    "cloud.google.com", "microsoft.com", "oracle.com", "coreweave.com", "together.ai",
    "siemens.com", "byd.com", "mi.com", "synopsys.com", "cadence.com", "advantech.com"
}

def generate_full_directory():
    filepath = "/Users/popoya/Movies/视频生产/诸神之墙/partner_directory_full.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# 英伟达“诸神之墙”全部 13 行完整合作伙伴名录\n\n")
        f.write("这面墙代表了老黄在台北电脑展上向全球秀出的 AI 帝国生态。以下是**全部 13 行、共 285 家公司与机构**的完整对照名录，包括官网及生态定位。\n\n")
        f.write("> [!NOTE]\n")
        f.write("> 这里的 Logo 栏已恢复使用 **Clearbit 高清企业品牌 Logo API**（采用原生 Markdown 图片语法）。\n\n")
        f.write("---\n\n")

        for i, row in enumerate(partner_rows):
            f.write(f"## 📍 第 {i+1} 行 (Row {i+1})\n\n")
            f.write("| Logo | 机构/公司名称 | 官方网站 | 生态系统定位与主要技术点 |\n")
            f.write("| :---: | :--- | :--- | :--- |\n")
            
            for name, domain, desc in row:
                logo_url = f"https://logo.clearbit.com/{domain}"
                logo_tag = f"![{name}]({logo_url})"
                # Support custom eggs with google map search website
                website_url = f"https://{domain}"
                if domain.startswith("hua_niang") or domain.startswith("wang_ji") or domain.startswith("fu_ba_wang") or domain.startswith("fruit_lady") or domain.startswith("zhuan_yao"):
                    website_url = "https://www.google.com/maps"
                f.write(f"| {logo_tag} | **{name}** | [{domain}]({website_url}) | {desc} |\n")
            
            f.write("\n")
    print("Full directory generated with Clearbit API.")

def generate_curated_directory():
    filepath = "/Users/popoya/Movies/视频生产/诸神之墙/partner_directory.md"
    
    all_partners = []
    for row in partner_rows:
        all_partners.extend(row)
        
    core_partners = [p for p in all_partners if p[1] in core_50_domains]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# 英伟达“诸神之墙”核心合作伙伴黄页目录 (精选版)\n\n")
        f.write("这面墙上的所有公司、高校和机构都有官方网站。我们为您精选了最具有话题度、故事性及搞钱看点的核心企业。\n\n")
        f.write("---\n\n")
        
        f.write("| Logo | 机构/公司名称 | 官方网站 | 核心定位与合作点 |\n")
        f.write("| :---: | :--- | :--- | :--- |\n")
        
        for name, domain, desc in core_partners:
            logo_url = f"https://logo.clearbit.com/{domain}"
            logo_tag = f"![{name}]({logo_url})"
            f.write(f"| {logo_tag} | **{name}** | [{domain}](https://{domain}) | {desc} |\n")
            
    print("Curated directory generated with Clearbit API.")

if __name__ == "__main__":
    generate_full_directory()
    generate_curated_directory()
