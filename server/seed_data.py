"""省份及旅游数据初始化 seed"""
from server.models import Region
from server import db


def init_data():
    """检测 regions 表是否为空，为空则插入全部数据"""
    if Region.query.first() is not None:
        return  # 已有数据不重复插入

    provinces = _build_data()
    for p in provinces:
        children = p.pop('children', [])
        parent = Region(**p)
        db.session.add(parent)
        db.session.flush()  # 获取 parent.id
        for c in children:
            child = Region(**c, parent_id=parent.id)
            db.session.add(child)
    db.session.commit()


def _build_data():
    """返回省份数据列表，每个省份包含 children 子列表"""

    # ── 含旅游数据的城市 ──────────────────────────
    locations_data = {
        '北京': {
            'badge': '📍 中国 · 北京',
            'description': '千年古都，中国的政治文化中心。红墙黄瓦间流淌着六百年的皇家气韵，胡同深处藏着最地道的市井生活。',
            'emoji': '🏛️',
            'attractions': ['故宫博物院', '八达岭长城', '天坛公园', '颐和园', '天安门广场', '鸟巢'],
            'food': ['北京烤鸭', '炸酱面', '豆汁儿', '涮羊肉', '卤煮火烧'],
        },
        '上海': {
            'badge': '📍 中国 · 上海',
            'description': '魔都上海，国际化大都市。外滩万国建筑群与陆家嘴摩天大楼隔江相望，石库门里弄与新天地时尚街区交相辉映。',
            'emoji': '🌃',
            'attractions': ['外滩', '迪士尼乐园', '豫园', '东方明珠', '南京路步行街', '武康大楼'],
            'food': ['小笼包', '生煎包', '葱油拌面', '南翔小笼', '红烧肉'],
        },
        '贵州': {
            'badge': '📍 中国 · 贵州',
            'description': '多彩贵州，山地公园省。这里有世界自然遗产与千年苗寨，喀斯特地貌造就了绝美的山水画卷，少数民族文化在这里生生不息。',
            'emoji': '🏔️',
            'attractions': ['黄果树瀑布', '荔波小七孔', '西江千户苗寨', '梵净山', '镇远古城', '黔灵山公园'],
            'food': ['酸汤鱼', '肠旺面', '花溪牛肉粉', '丝娃娃', '豆腐圆子'],
        },
        '云南': {
            'badge': '📍 中国 · 云南',
            'description': '七彩云南，风花雪月。苍山洱海畔的大理古城，玉龙雪山下的丽江古城，人间最后的净土香格里拉。',
            'emoji': '🌸',
            'attractions': ['大理古城', '丽江古城', '玉龙雪山', '香格里拉', '洱海', '石林'],
            'food': ['过桥米线', '汽锅鸡', '鲜花饼', '野生菌火锅', '烤乳扇'],
        },
        '西藏': {
            'badge': '📍 中国 · 西藏',
            'description': '雪域高原，世界屋脊。布达拉宫在阳光下闪耀金光，纳木错的湖水蓝如宝石，这里是离天空最近的地方。',
            'emoji': '🏔️',
            'attractions': ['布达拉宫', '纳木错', '大昭寺', '羊卓雍措', '珠穆朗玛峰', '八廓街'],
            'food': ['酥油茶', '糌粑', '牦牛肉', '藏面', '甜茶'],
        },
        '桂林': {
            'badge': '📍 中国 · 桂林',
            'description': '桂林山水甲天下。漓江两岸奇峰林立，象鼻山饮江而立，阳朔西街灯火阑珊。泛舟漓江，如在画中游。',
            'emoji': '⛰️',
            'attractions': ['漓江', '阳朔西街', '象鼻山', '龙脊梯田', '十里画廊', '遇龙河'],
            'food': ['桂林米粉', '啤酒鱼', '螺蛳粉', '马蹄糕', '荔浦芋扣肉'],
        },
        '成都': {
            'badge': '📍 中国 · 成都',
            'description': '天府之国，熊猫故乡。这座来了就不想走的城市，有最萌的大熊猫、最热的火锅、最悠闲的生活节奏。',
            'emoji': '🐼',
            'attractions': ['大熊猫基地', '宽窄巷子', '都江堰', '锦里古街', '武侯祠', '青城山'],
            'food': ['火锅', '串串香', '担担面', '龙抄手', '夫妻肺片'],
        },
        '杭州': {
            'badge': '📍 中国 · 杭州',
            'description': '人间天堂，西湖美景。断桥残雪、苏堤春晓、雷峰夕照，四季皆有不同韵味。茶香袅袅，江南韵味尽在其中。',
            'emoji': '🏯',
            'attractions': ['西湖', '灵隐寺', '雷峰塔', '千岛湖', '宋城', '西溪湿地'],
            'food': ['西湖醋鱼', '龙井虾仁', '东坡肉', '片儿川', '叫花鸡'],
        },
        '西安': {
            'badge': '📍 中国 · 西安',
            'description': '十三朝古都，千年历史沉淀。兵马俑守护着始皇帝的千年之梦，大雁塔见证着古丝绸之路的繁华。',
            'emoji': '🏺',
            'attractions': ['兵马俑', '华山', '大雁塔', '西安城墙', '钟鼓楼', '大唐不夜城'],
            'food': ['肉夹馍', '凉皮', '羊肉泡馍', '油泼面', '甑糕'],
        },
        '三亚': {
            'badge': '📍 中国 · 三亚',
            'description': '东方夏威夷，热带天堂。碧海蓝天、椰风海韵，亚龙湾的沙滩细腻如雪，蜈支洲岛的海水清澈见底。',
            'emoji': '🏖️',
            'attractions': ['亚龙湾', '天涯海角', '蜈支洲岛', '南山寺', '椰梦长廊', '鹿回头'],
            'food': ['海鲜大餐', '文昌鸡', '椰子饭', '清补凉', '海南粉'],
        },
    }

    def loc(name):
        return locations_data.get(name, {})

    # ── 34 个省级行政区 ──────────────────────────
    return [
        {
            'name': '北京市', 'level': 'province', 'type': 'municipality',
            'lat': 39.90, 'lng': 116.40, 'sort_order': 1,
            **loc('北京'),
            'children': [{'name': '市区', 'level': 'city', 'lat': 39.90, 'lng': 116.40, 'sort_order': 1, **loc('北京')}],
        },
        {
            'name': '天津市', 'level': 'province', 'type': 'municipality',
            'lat': 39.13, 'lng': 117.19, 'sort_order': 2,
            'children': [{'name': '天津市', 'level': 'city', 'lat': 39.13, 'lng': 117.19, 'sort_order': 1}],
        },
        {
            'name': '上海市', 'level': 'province', 'type': 'municipality',
            'lat': 31.23, 'lng': 121.47, 'sort_order': 3,
            **loc('上海'),
            'children': [{'name': '市区', 'level': 'city', 'lat': 31.23, 'lng': 121.47, 'sort_order': 1, **loc('上海')}],
        },
        {
            'name': '重庆市', 'level': 'province', 'type': 'municipality',
            'lat': 29.56, 'lng': 106.55, 'sort_order': 4,
            'children': [{'name': '重庆市', 'level': 'city', 'lat': 29.56, 'lng': 106.55, 'sort_order': 1}],
        },
        {
            'name': '河北省', 'level': 'province', 'type': 'province',
            'lat': 38.05, 'lng': 114.50, 'sort_order': 5,
            'children': [{'name': '石家庄市', 'level': 'city', 'lat': 38.05, 'lng': 114.50, 'sort_order': 1}],
        },
        {
            'name': '山西省', 'level': 'province', 'type': 'province',
            'lat': 37.87, 'lng': 112.56, 'sort_order': 6,
            'children': [{'name': '太原市', 'level': 'city', 'lat': 37.87, 'lng': 112.56, 'sort_order': 1}],
        },
        {
            'name': '内蒙古自治区', 'level': 'province', 'type': 'autonomous_region',
            'lat': 40.82, 'lng': 111.75, 'sort_order': 7,
            'children': [{'name': '呼和浩特市', 'level': 'city', 'lat': 40.82, 'lng': 111.75, 'sort_order': 1}],
        },
        {
            'name': '辽宁省', 'level': 'province', 'type': 'province',
            'lat': 41.84, 'lng': 123.43, 'sort_order': 8,
            'children': [{'name': '沈阳市', 'level': 'city', 'lat': 41.84, 'lng': 123.43, 'sort_order': 1}],
        },
        {
            'name': '吉林省', 'level': 'province', 'type': 'province',
            'lat': 43.90, 'lng': 125.32, 'sort_order': 9,
            'children': [{'name': '长春市', 'level': 'city', 'lat': 43.90, 'lng': 125.32, 'sort_order': 1}],
        },
        {
            'name': '黑龙江省', 'level': 'province', 'type': 'province',
            'lat': 45.74, 'lng': 126.66, 'sort_order': 10,
            'children': [{'name': '哈尔滨市', 'level': 'city', 'lat': 45.74, 'lng': 126.66, 'sort_order': 1}],
        },
        {
            'name': '江苏省', 'level': 'province', 'type': 'province',
            'lat': 32.06, 'lng': 118.80, 'sort_order': 11,
            'children': [{'name': '南京市', 'level': 'city', 'lat': 32.06, 'lng': 118.80, 'sort_order': 1}],
        },
        {
            'name': '浙江省', 'level': 'province', 'type': 'province',
            'lat': 30.27, 'lng': 120.15, 'sort_order': 12,
            **loc('杭州'),
            'children': [{'name': '杭州市', 'level': 'city', 'lat': 30.27, 'lng': 120.15, 'sort_order': 1, **loc('杭州')}],
        },
        {
            'name': '安徽省', 'level': 'province', 'type': 'province',
            'lat': 31.82, 'lng': 117.23, 'sort_order': 13,
            'children': [{'name': '合肥市', 'level': 'city', 'lat': 31.82, 'lng': 117.23, 'sort_order': 1}],
        },
        {
            'name': '福建省', 'level': 'province', 'type': 'province',
            'lat': 26.07, 'lng': 119.30, 'sort_order': 14,
            'children': [{'name': '福州市', 'level': 'city', 'lat': 26.07, 'lng': 119.30, 'sort_order': 1}],
        },
        {
            'name': '江西省', 'level': 'province', 'type': 'province',
            'lat': 28.67, 'lng': 115.89, 'sort_order': 15,
            'children': [{'name': '南昌市', 'level': 'city', 'lat': 28.68, 'lng': 115.89, 'sort_order': 1}],
        },
        {
            'name': '山东省', 'level': 'province', 'type': 'province',
            'lat': 36.67, 'lng': 116.99, 'sort_order': 16,
            'children': [{'name': '济南市', 'level': 'city', 'lat': 36.67, 'lng': 116.99, 'sort_order': 1}],
        },
        {
            'name': '河南省', 'level': 'province', 'type': 'province',
            'lat': 34.75, 'lng': 113.62, 'sort_order': 17,
            'children': [{'name': '郑州市', 'level': 'city', 'lat': 34.75, 'lng': 113.62, 'sort_order': 1}],
        },
        {
            'name': '湖北省', 'level': 'province', 'type': 'province',
            'lat': 30.59, 'lng': 114.31, 'sort_order': 18,
            'children': [{'name': '武汉市', 'level': 'city', 'lat': 30.59, 'lng': 114.31, 'sort_order': 1}],
        },
        {
            'name': '湖南省', 'level': 'province', 'type': 'province',
            'lat': 28.23, 'lng': 112.94, 'sort_order': 19,
            'children': [{'name': '长沙市', 'level': 'city', 'lat': 28.23, 'lng': 112.94, 'sort_order': 1}],
        },
        {
            'name': '广东省', 'level': 'province', 'type': 'province',
            'lat': 23.13, 'lng': 113.27, 'sort_order': 20,
            'children': [{'name': '广州市', 'level': 'city', 'lat': 23.13, 'lng': 113.27, 'sort_order': 1}],
        },
        {
            'name': '广西壮族自治区', 'level': 'province', 'type': 'autonomous_region',
            'lat': 22.82, 'lng': 108.37, 'sort_order': 21,
            'children': [
                {'name': '南宁市', 'level': 'city', 'lat': 22.82, 'lng': 108.37, 'sort_order': 1},
                {'name': '桂林市', 'level': 'city', 'lat': 25.28, 'lng': 110.29, 'sort_order': 2, **loc('桂林')},
            ],
        },
        {
            'name': '海南省', 'level': 'province', 'type': 'province',
            'lat': 20.02, 'lng': 110.35, 'sort_order': 22,
            'children': [
                {'name': '海口市', 'level': 'city', 'lat': 20.02, 'lng': 110.35, 'sort_order': 1},
                {'name': '三亚市', 'level': 'city', 'lat': 18.25, 'lng': 109.51, 'sort_order': 2, **loc('三亚')},
            ],
        },
        {
            'name': '四川省', 'level': 'province', 'type': 'province',
            'lat': 30.57, 'lng': 104.07, 'sort_order': 23,
            **loc('成都'),
            'children': [{'name': '成都市', 'level': 'city', 'lat': 30.57, 'lng': 104.07, 'sort_order': 1, **loc('成都')}],
        },
        {
            'name': '贵州省', 'level': 'province', 'type': 'province',
            'lat': 26.65, 'lng': 106.63, 'sort_order': 24,
            **loc('贵州'),
            'children': [{'name': '贵阳市', 'level': 'city', 'lat': 26.65, 'lng': 106.63, 'sort_order': 1}],
        },
        {
            'name': '云南省', 'level': 'province', 'type': 'province',
            'lat': 25.05, 'lng': 102.71, 'sort_order': 25,
            **loc('云南'),
            'children': [
                {'name': '昆明市', 'level': 'city', 'lat': 25.04, 'lng': 102.71, 'sort_order': 1},
                {'name': '大理市', 'level': 'city', 'lat': 25.59, 'lng': 100.23, 'sort_order': 2},
                {'name': '丽江市', 'level': 'city', 'lat': 26.87, 'lng': 100.23, 'sort_order': 3},
            ],
        },
        {
            'name': '西藏自治区', 'level': 'province', 'type': 'autonomous_region',
            'lat': 29.65, 'lng': 91.12, 'sort_order': 26,
            **loc('西藏'),
            'children': [{'name': '拉萨市', 'level': 'city', 'lat': 29.65, 'lng': 91.12, 'sort_order': 1}],
        },
        {
            'name': '陕西省', 'level': 'province', 'type': 'province',
            'lat': 34.34, 'lng': 108.94, 'sort_order': 27,
            **loc('西安'),
            'children': [{'name': '西安市', 'level': 'city', 'lat': 34.34, 'lng': 108.94, 'sort_order': 1, **loc('西安')}],
        },
        {
            'name': '甘肃省', 'level': 'province', 'type': 'province',
            'lat': 36.06, 'lng': 103.83, 'sort_order': 28,
            'children': [{'name': '兰州市', 'level': 'city', 'lat': 36.06, 'lng': 103.83, 'sort_order': 1}],
        },
        {
            'name': '青海省', 'level': 'province', 'type': 'province',
            'lat': 36.62, 'lng': 101.78, 'sort_order': 29,
            'children': [{'name': '西宁市', 'level': 'city', 'lat': 36.62, 'lng': 101.78, 'sort_order': 1}],
        },
        {
            'name': '宁夏回族自治区', 'level': 'province', 'type': 'autonomous_region',
            'lat': 38.49, 'lng': 106.23, 'sort_order': 30,
            'children': [{'name': '银川市', 'level': 'city', 'lat': 38.49, 'lng': 106.23, 'sort_order': 1}],
        },
        {
            'name': '新疆维吾尔自治区', 'level': 'province', 'type': 'autonomous_region',
            'lat': 43.79, 'lng': 87.63, 'sort_order': 31,
            'children': [{'name': '乌鲁木齐市', 'level': 'city', 'lat': 43.79, 'lng': 87.63, 'sort_order': 1}],
        },
        {
            'name': '台湾省', 'level': 'province', 'type': 'province',
            'lat': 23.70, 'lng': 120.96, 'sort_order': 32,
            'children': [{'name': '台北市', 'level': 'city', 'lat': 25.03, 'lng': 121.56, 'sort_order': 1}],
        },
        {
            'name': '香港特别行政区', 'level': 'province', 'type': 'sar',
            'lat': 22.32, 'lng': 114.17, 'sort_order': 33,
            'children': [{'name': '香港', 'level': 'city', 'lat': 22.32, 'lng': 114.17, 'sort_order': 1}],
        },
        {
            'name': '澳门特别行政区', 'level': 'province', 'type': 'sar',
            'lat': 22.20, 'lng': 113.54, 'sort_order': 34,
            'children': [{'name': '澳门', 'level': 'city', 'lat': 22.20, 'lng': 113.54, 'sort_order': 1}],
        },
    ]
