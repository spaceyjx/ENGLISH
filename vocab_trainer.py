import tkinter as tk
from tkinter import ttk, messagebox
import json
import random
import os

class VocabTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("英语单词记忆小程序")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f5f9")
        
        self.current_words = []
        self.learned_words = set()
        self.load_word_data()
        
        self.create_widgets()
        self.show_random_words()
        
    def load_word_data(self):
        data_file = os.path.join(os.path.dirname(__file__), "word_database.json")
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                self.word_database = json.load(f)
        else:
            self.word_database = self.create_sample_database()
        
        learned_file = os.path.join(os.path.dirname(__file__), "learned_words.json")
        if os.path.exists(learned_file):
            with open(learned_file, 'r', encoding='utf-8') as f:
                self.learned_words = set(json.load(f))
    
    def create_sample_database(self):
        return [
            {"word": "abroad", "phonetic": "/əˈbrɔːd/", "meaning": "在国外；到国外"},
            {"word": "accept", "phonetic": "/əkˈsept/", "meaning": "接受；认可"},
            {"word": "achieve", "phonetic": "/əˈtʃiːv/", "meaning": "实现；达到"},
            {"word": "actual", "phonetic": "/ˈæktʃuəl/", "meaning": "实际的；真实的"},
            {"word": "admire", "phonetic": "/ədˈmaɪər/", "meaning": "钦佩；欣赏"},
            {"word": "advance", "phonetic": "/ədˈvɑːns/", "meaning": "前进；提前"},
            {"word": "advantage", "phonetic": "/ədˈvɑːntɪdʒ/", "meaning": "优势；好处"},
            {"word": "adventure", "phonetic": "/ədˈventʃər/", "meaning": "冒险"},
            {"word": "advice", "phonetic": "/ədˈvaɪs/", "meaning": "建议；忠告"},
            {"word": "affect", "phonetic": "/əˈfekt/", "meaning": "影响；感染"},
            {"word": "alone", "phonetic": "/əˈloʊn/", "meaning": "独自的；单独的"},
            {"word": "amaze", "phonetic": "/əˈmeɪz/", "meaning": "使惊讶；使吃惊"},
            {"word": "anxious", "phonetic": "/ˈæŋkʃəs/", "meaning": "焦虑的"},
            {"word": "appear", "phonetic": "/əˈpɪr/", "meaning": "出现；显得"},
            {"word": "approach", "phonetic": "/əˈproʊtʃ/", "meaning": "接近；方法"},
            {"word": "argue", "phonetic": "/ˈɑːrɡjuː/", "meaning": "争论；辩论"},
            {"word": "arrange", "phonetic": "/əˈreɪndʒ/", "meaning": "安排；整理"},
            {"word": "associate", "phonetic": "/əˈsoʊʃieɪt/", "meaning": "联系；关联"},
            {"word": "attempt", "phonetic": "/əˈtempt/", "meaning": "尝试；企图"},
            {"word": "attract", "phonetic": "/əˈtrækt/", "meaning": "吸引；引起"},
            {"word": "awful", "phonetic": "/ˈɔːf(ə)l/", "meaning": "糟糕的；可怕的"},
            {"word": "basic", "phonetic": "/ˈbeɪsɪk/", "meaning": "基本的；基础的"},
            {"word": "battle", "phonetic": "/ˈbætl/", "meaning": "战斗；战役"},
            {"word": "behave", "phonetic": "/bɪˈheɪv/", "meaning": "表现；举止得体"},
            {"word": "benefit", "phonetic": "/ˈbenɪfɪt/", "meaning": "益处；好处"},
            {"word": "block", "phonetic": "/blɑːk/", "meaning": "块；街区；阻挡"},
            {"word": "brave", "phonetic": "/breɪv/", "meaning": "勇敢的"},
            {"word": "calm", "phonetic": "/kɑːm/", "meaning": "平静的；使平静"},
            {"word": "career", "phonetic": "/kəˈrɪr/", "meaning": "职业；生涯"},
            {"word": "cause", "phonetic": "/kɔːz/", "meaning": "引起；原因"},
            {"word": "certain", "phonetic": "/ˈsɜːrtn/", "meaning": "确定的；某个的"},
            {"word": "challenge", "phonetic": "/ˈtʃælɪndʒ/", "meaning": "挑战"},
            {"word": "choice", "phonetic": "/tʃɔɪs/", "meaning": "选择"},
            {"word": "command", "phonetic": "/kəˈmɑːnd/", "meaning": "命令；指挥"},
            {"word": "communicate", "phonetic": "/kəˈmjuːnɪkeɪt/", "meaning": "交流；沟通"},
            {"word": "community", "phonetic": "/kəˈmjuːnəti/", "meaning": "社区；团体"},
            {"word": "complex", "phonetic": "/ˈkɑːmpleks/", "meaning": "复杂的；复合体"},
            {"word": "concern", "phonetic": "/kənˈsɜːrn/", "meaning": "担忧；关心"},
            {"word": "conclude", "phonetic": "/kənˈkluːd/", "meaning": "得出结论；结束"},
            {"word": "confident", "phonetic": "/ˈkɒnfɪdənt/", "meaning": "自信的"},
            {"word": "consist", "phonetic": "/kənˈsɪst/", "meaning": "组成；在于"},
            {"word": "contain", "phonetic": "/kənˈteɪn/", "meaning": "包含；控制"},
            {"word": "continue", "phonetic": "/kənˈtɪnjuː/", "meaning": "继续；持续"},
            {"word": "contribute", "phonetic": "/kənˈtrɪbjuːt/", "meaning": "贡献；捐献"},
            {"word": "correct", "phonetic": "/kəˈrekt/", "meaning": "正确的；纠正"},
            {"word": "damage", "phonetic": "/ˈdæmɪdʒ/", "meaning": "损害；损坏"},
            {"word": "decide", "phonetic": "/dɪˈsaɪd/", "meaning": "决定；判决"},
            {"word": "defend", "phonetic": "/dɪˈfend/", "meaning": "防御；保卫"},
            {"word": "deliver", "phonetic": "/dɪˈlɪvər/", "meaning": "递送；交付"},
            {"word": "desire", "phonetic": "/dɪˈzaɪə(r)/", "meaning": "欲望；渴望"},
            {"word": "determine", "phonetic": "/dɪˈtɜːrmɪn/", "meaning": "决定；决心"},
            {"word": "develop", "phonetic": "/dɪˈveləp/", "meaning": "发展；开发"},
            {"word": "differ", "phonetic": "/ˈdɪfər/", "meaning": "不同；有差异"},
            {"word": "discover", "phonetic": "/dɪˈskʌvər/", "meaning": "发现"},
            {"word": "distance", "phonetic": "/ˈdɪstəns/", "meaning": "距离"},
            {"word": "effect", "phonetic": "/ɪˈfekt/", "meaning": "效果；影响"},
            {"word": "eager", "phonetic": "/ˈiːɡə(r)/", "meaning": "渴望的；热切的"},
            {"word": "emotion", "phonetic": "/ɪˈmoʊʃn/", "meaning": "情感；情绪"},
            {"word": "enable", "phonetic": "/ɪˈneɪbl/", "meaning": "使能够；使可行"},
            {"word": "encourage", "phonetic": "/ɪnˈkɜːrɪdʒ/", "meaning": "鼓励；激励"},
            {"word": "energy", "phonetic": "/ˈenərdʒi/", "meaning": "能量；精力"},
            {"word": "enjoy", "phonetic": "/ɪnˈdʒɔɪ/", "meaning": "享受；喜欢"},
            {"word": "essential", "phonetic": "/ɪˈsenʃl/", "meaning": "必要的；本质的"},
            {"word": "evidence", "phonetic": "/ˈevɪdəns/", "meaning": "证据；证明"},
            {"word": "excellent", "phonetic": "/ˈeksələnt/", "meaning": "优秀的；极好的"},
            {"word": "experience", "phonetic": "/ɪkˈspɪriəns/", "meaning": "经验；经历"},
            {"word": "explain", "phonetic": "/ɪkˈspleɪn/", "meaning": "解释；说明"},
            {"word": "explore", "phonetic": "/ɪkˈsplɔːr/", "meaning": "探索；勘探"},
            {"word": "express", "phonetic": "/ɪkˈspres/", "meaning": "表达；表示"},
            {"word": "fail", "phonetic": "/feɪl/", "meaning": "失败；不及格"},
            {"word": "familiar", "phonetic": "/fəˈmɪliər/", "meaning": "熟悉的；常见的"},
            {"word": "famous", "phonetic": "/ˈfeɪməs/", "meaning": "著名的"},
            {"word": "favor", "phonetic": "/ˈfeɪvər/", "meaning": "好意；帮助"},
            {"word": "feature", "phonetic": "/ˈfiːtʃər/", "meaning": "特征；特点"},
            {"word": "focus", "phonetic": "/ˈfoʊkəs/", "meaning": "焦点；集中"},
            {"word": "force", "phonetic": "/fɔːrs/", "meaning": "力量；武力；强迫"},
            {"word": "forget", "phonetic": "/fərˈɡet/", "meaning": "忘记；忽略"},
            {"word": "forgive", "phonetic": "/fərˈɡɪv/", "meaning": "原谅；宽恕"},
            {"word": "fortune", "phonetic": "/ˈfɔːrtʃənət/", "meaning": "幸运的"},
            {"word": "freedom", "phonetic": "/ˈfriːdəm/", "meaning": "自由；自主"},
            {"word": "friendship", "phonetic": "/ˈfrendʃɪp/", "meaning": "友谊"},
            {"word": "function", "phonetic": "/ˈfʌŋkʃn/", "meaning": "功能；运作"},
            {"word": "future", "phonetic": "/ˈfjuːtʃər/", "meaning": "未来；前途"},
            {"word": "gather", "phonetic": "/ˈɡæðər/", "meaning": "聚集；收集"},
            {"word": "generous", "phonetic": "/ˈdʒenərəs/", "meaning": "慷慨的；大方的"},
            {"word": "gentle", "phonetic": "/ˈdʒentl/", "meaning": "温和的；温柔的"},
            {"word": "glad", "phonetic": "/ɡlæd/", "meaning": "高兴的；乐意的"},
            {"word": "goal", "phonetic": "/ɡoʊl/", "meaning": "目标；进球"},
            {"word": "grateful", "phonetic": "/ˈɡreɪtfl/", "meaning": "感激的；感谢的"},
            {"word": "guide", "phonetic": "/ɡaɪd/", "meaning": "指南；向导；引导"},
            {"word": "happiness", "phonetic": "/ˈhæpinəs/", "meaning": "幸福；快乐"},
            {"word": "harm", "phonetic": "/hɑːrm/", "meaning": "伤害；损害"},
            {"word": "honest", "phonetic": "/ˈɑːnɪst/", "meaning": "诚实的；正直的"},
            {"word": "household", "phonetic": "/ˈhaʊshəʊld/", "meaning": "家庭；家庭的"},
            {"word": "imagine", "phonetic": "/ɪˈmædʒɪn/", "meaning": "想象；设想"},
            {"word": "improve", "phonetic": "/ɪmˈpruːv/", "meaning": "改进；提高"},
            {"word": "include", "phonetic": "/ɪnˈkluːd/", "meaning": "包括；包含"},
            {"word": "independent", "phonetic": "/ˌɪndɪˈpendənt/", "meaning": "独立的；自主的"},
            {"word": "individual", "phonetic": "/ˌɪndɪˈvɪdʒuəl/", "meaning": "个人；个体的"},
            {"word": "inform", "phonetic": "/ɪnˈfɔːrm/", "meaning": "通知；告知"},
            {"word": "instead", "phonetic": "/ɪnˈsted/", "meaning": "代替；反而"},
            {"word": "introduce", "phonetic": "/ˌɪntrəˈduːs/", "meaning": "介绍；引进"},
            {"word": "investigate", "phonetic": "/ɪnˈvestɪɡeɪt/", "meaning": "调查；研究"},
            {"word": "invite", "phonetic": "/ɪnˈvaɪt/", "meaning": "邀请；招待"},
            {"word": "judge", "phonetic": "/dʒʌdʒ/", "meaning": "法官；裁判；判断"},
            {"word": "justice", "phonetic": "/ˈdʒʌstɪs/", "meaning": "正义；公平"},
            {"word": "knowledge", "phonetic": "/ˈnɑːlɪdʒ/", "meaning": "知识；知晓"},
            {"word": "landscape", "phonetic": "/ˈlændskeɪp/", "meaning": "风景；景观"},
            {"word": "likely", "phonetic": "/ˈlaɪkli/", "meaning": "可能的；很可能"},
            {"word": "limit", "phonetic": "/ˈlɪmɪt/", "meaning": "限制；限度"},
            {"word": "local", "phonetic": "/ˈloʊkl/", "meaning": "当地的；本地的"},
            {"word": "lonely", "phonetic": "/ˈloʊnli/", "meaning": "孤独的；寂寞的"},
            {"word": "lose", "phonetic": "/luːz/", "meaning": "失去；丢失"},
            {"word": "loyal", "phonetic": "/ˈlɔɪəl/", "meaning": "忠诚的；忠实的"},
            {"word": "luck", "phonetic": "/lʌk/", "meaning": "运气；幸运"},
            {"word": "magic", "phonetic": "/ˈmædʒɪk/", "meaning": "魔法；魔术"},
            {"word": "manage", "phonetic": "/ˈmænɪdʒ/", "meaning": "管理；设法做到"},
            {"word": "manner", "phonetic": "/ˈmænər/", "meaning": "方式；礼貌"},
            {"word": "mark", "phonetic": "/mɑːrk/", "meaning": "标记；记号；分数"},
            {"word": "marry", "phonetic": "/ˈmæri/", "meaning": "结婚；娶；嫁"},
            {"word": "material", "phonetic": "/məˈtɪriəl/", "meaning": "材料；物质的"},
            {"word": "matter", "phonetic": "/ˈmætər/", "meaning": "事情；问题；要紧"},
            {"word": "meaning", "phonetic": "/ˈmiːnɪŋ/", "meaning": "意思；含义"},
            {"word": "measure", "phonetic": "/ˈmeʒər/", "meaning": "测量；衡量"},
            {"word": "memory", "phonetic": "/ˈmeməri/", "meaning": "记忆；记忆力"},
            {"word": "mercy", "phonetic": "/ˈmɜːrsi/", "meaning": "仁慈；宽恕"},
            {"word": "message", "phonetic": "/ˈmesɪdʒ/", "meaning": "信息；消息"},
            {"word": "mind", "phonetic": "/maɪnd/", "meaning": "头脑；介意"},
            {"word": "misery", "phonetic": "/ˈmɪzəri/", "meaning": "痛苦；悲惨"},
            {"word": "mistake", "phonetic": "/mɪˈsteɪk/", "meaning": "错误；误会"},
            {"word": "mix", "phonetic": "/mɪks/", "meaning": "混合；混合物"},
            {"word": "moral", "phonetic": "/ˈmɔːrəl/", "meaning": "道德的；道义上的"},
            {"word": "motion", "phonetic": "/ˈməʊʃ(ə)n/", "meaning": "运动；动作"},
            {"word": "nature", "phonetic": "/ˈneɪtʃər/", "meaning": "自然；天性"},
            {"word": "necessary", "phonetic": "/ˈnesəseri/", "meaning": "必要的；必需的"},
            {"word": "need", "phonetic": "/niːd/", "meaning": "需要；必要"},
            {"word": "normal", "phonetic": "/ˈnɔːrml/", "meaning": "正常的；标准的"},
            {"word": "notice", "phonetic": "/ˈnoʊtɪs/", "meaning": "注意；通知"},
            {"word": "obey", "phonetic": "/əˈbeɪ/", "meaning": "服从；遵守"},
            {"word": "observe", "phonetic": "/əbˈzɜːrv/", "meaning": "观察；遵守"},
            {"word": "obtain", "phonetic": "/əbˈteɪn/", "meaning": "获得；得到"},
            {"word": "obvious", "phonetic": "/ˈɑːbviəs/", "meaning": "明显的；显而易见的"},
            {"word": "occur", "phonetic": "/əˈkɜːr/", "meaning": "发生；出现"},
            {"word": "offer", "phonetic": "/ˈɔːfər/", "meaning": "提供；出价；提议"},
            {"word": "opinion", "phonetic": "/əˈpɪnjən/", "meaning": "意见；看法"},
            {"word": "opportunity", "phonetic": "/ˌɑːpərˈtuːnəti/", "meaning": "机会；时机"},
            {"word": "order", "phonetic": "/ˈɔːrdər/", "meaning": "顺序；命令；订购"},
            {"word": "original", "phonetic": "/əˈrɪdʒənl/", "meaning": "原始的；独创的"},
            {"word": "pain", "phonetic": "/peɪn/", "meaning": "疼痛；痛苦"},
            {"word": "patient", "phonetic": "/ˈpeɪʃnt/", "meaning": "耐心的；病人"},
            {"word": "peace", "phonetic": "/piːs/", "meaning": "和平；平静"},
            {"word": "perform", "phonetic": "/pərˈfɔːrm/", "meaning": "表演；执行；表现"},
            {"word": "permit", "phonetic": "/pərˈmɪt/", "meaning": "允许；许可证"},
            {"word": "physical", "phonetic": "/ˈfɪzɪkl/", "meaning": "身体的；物理的"},
            {"word": "place", "phonetic": "/pleɪs/", "meaning": "地方；放置"},
            {"word": "pleasant", "phonetic": "/ˈpleznt/", "meaning": "令人愉快的；舒适的"},
            {"word": "please", "phonetic": "/pliːz/", "meaning": "请；使高兴"},
            {"word": "plenty", "phonetic": "/ˈplenti/", "meaning": "丰富；大量"},
            {"word": "point", "phonetic": "/pɔɪnt/", "meaning": "点；要点；指向"},
            {"word": "polite", "phonetic": "/pəˈlaɪt/", "meaning": "有礼貌的"},
            {"word": "popular", "phonetic": "/ˈpɑːpjələr/", "meaning": "流行的；受欢迎的"},
            {"word": "position", "phonetic": "/pəˈzɪʃn/", "meaning": "位置；职位；立场"},
            {"word": "possible", "phonetic": "/ˈpɑːsəbl/", "meaning": "可能的；合理的"},
            {"word": "praise", "phonetic": "/preɪz/", "meaning": "赞扬；表扬"},
            {"word": "prepare", "phonetic": "/prɪˈper/", "meaning": "准备；预备"},
            {"word": "presence", "phonetic": "/ˈprezns/", "meaning": "存在；出席"},
            {"word": "prevent", "phonetic": "/prɪˈvent/", "meaning": "预防；阻止"},
            {"word": "pride", "phonetic": "/praɪd/", "meaning": "自豪；骄傲"},
            {"word": "primary", "phonetic": "/ˈpraɪmeri/", "meaning": "主要的；初级的"},
            {"word": "private", "phonetic": "/ˈpraɪvət/", "meaning": "私人的；私有的"},
            {"word": "prize", "phonetic": "/praɪz/", "meaning": "奖品；奖项"},
            {"word": "problem", "phonetic": "/ˈprɑːbləm/", "meaning": "问题；难题"},
            {"word": "process", "phonetic": "/ˈprɑːses/", "meaning": "过程；处理"},
            {"word": "produce", "phonetic": "/prəˈduːs/", "meaning": "生产；制造"},
            {"word": "progress", "phonetic": "/ˈprɑːɡres/", "meaning": "进步；进展"},
            {"word": "promise", "phonetic": "/ˈprɑːmɪs/", "meaning": "承诺；诺言"},
            {"word": "proper", "phonetic": "/ˈprɑːpər/", "meaning": "适当的；正确的"},
            {"word": "protect", "phonetic": "/prəˈtekt/", "meaning": "保护"},
            {"word": "proud", "phonetic": "/praʊd/", "meaning": "自豪的；骄傲的"},
            {"word": "prove", "phonetic": "/pruːv/", "meaning": "证明；证实"},
            {"word": "provide", "phonetic": "/prəˈvaɪd/", "meaning": "提供；供应"},
            {"word": "public", "phonetic": "/ˈpʌblɪk/", "meaning": "公众的；公共的"},
            {"word": "purpose", "phonetic": "/ˈpɜːrpəs/", "meaning": "目的；意图"},
            {"word": "quality", "phonetic": "/ˈkwɑːləti/", "meaning": "质量；品质"},
            {"word": "question", "phonetic": "/ˈkwestʃən/", "meaning": "问题；疑问"},
            {"word": "quick", "phonetic": "/kwɪk/", "meaning": "快的；迅速的"},
            {"word": "quiet", "phonetic": "/ˈkwaɪət/", "meaning": "安静的；平静的"},
            {"word": "raise", "phonetic": "/reɪz/", "meaning": "举起；提高；抚养"},
            {"word": "range", "phonetic": "/reɪndʒ/", "meaning": "范围；一系列"},
            {"word": "rare", "phonetic": "/rer/", "meaning": "罕见的；稀有的"},
            {"word": "reach", "phonetic": "/riːtʃ/", "meaning": "到达；达到"},
            {"word": "realize", "phonetic": "/ˈriːəlaɪz/", "meaning": "意识到；实现"},
            {"word": "reason", "phonetic": "/ˈriːzn/", "meaning": "原因；理由"},
            {"word": "receive", "phonetic": "/rɪˈsiːv/", "meaning": "收到；接待"},
            {"word": "recognize", "phonetic": "/ˈrekəɡnaɪz/", "meaning": "认出；识别；承认"},
            {"word": "recommend", "phonetic": "/ˌrekəˈmend/", "meaning": "推荐；建议"},
            {"word": "recover", "phonetic": "/rɪˈkʌvər/", "meaning": "恢复；痊愈"},
            {"word": "reduce", "phonetic": "/rɪˈduːs/", "meaning": "减少；降低"},
            {"word": "refer", "phonetic": "/rɪˈfɜːr/", "meaning": "参考；涉及；提到"},
            {"word": "reflect", "phonetic": "/rɪˈflekt/", "meaning": "反映；反射；思考"},
            {"word": "refuse", "phonetic": "/rɪˈfjuːz/", "meaning": "拒绝"},
            {"word": "regret", "phonetic": "/rɪˈɡret/", "meaning": "后悔；遗憾"},
            {"word": "relax", "phonetic": "/rɪˈlæks/", "meaning": "放松；休息"},
            {"word": "remain", "phonetic": "/rɪˈmeɪn/", "meaning": "保持；留下；剩余"},
            {"word": "remark", "phonetic": "/rɪˈmɑːrk/", "meaning": "评论；言论"},
            {"word": "remove", "phonetic": "/rɪˈmuːv/", "meaning": "移除；去掉"},
            {"word": "repair", "phonetic": "/rɪˈper/", "meaning": "修理；修复"},
            {"word": "repeat", "phonetic": "/rɪˈpiːt/", "meaning": "重复；重做"},
            {"word": "replace", "phonetic": "/rɪˈpleɪs/", "meaning": "替换；取代"},
            {"word": "reply", "phonetic": "/rɪˈplaɪ/", "meaning": "回答；答复"},
            {"word": "report", "phonetic": "/rɪˈpɔːrt/", "meaning": "报告；报道"},
            {"word": "request", "phonetic": "/rɪˈkwest/", "meaning": "请求；要求"},
            {"word": "require", "phonetic": "/rɪˈkwaɪər/", "meaning": "需要；要求"},
            {"word": "respect", "phonetic": "/rɪˈspekt/", "meaning": "尊重；方面；尊敬"},
            {"word": "respond", "phonetic": "/rɪˈspɑːnd/", "meaning": "回答；响应"},
            {"word": "responsibility", "phonetic": "/rɪˌspɑːnsəˈbɪləti/", "meaning": "责任；职责"},
            {"word": "result", "phonetic": "/rɪˈzʌlt/", "meaning": "结果；成果"},
            {"word": "return", "phonetic": "/rɪˈtɜːrn/", "meaning": "返回；归还"},
            {"word": "rich", "phonetic": "/rɪtʃ/", "meaning": "富有的；丰富的"},
            {"word": "risk", "phonetic": "/rɪsk/", "meaning": "风险；冒险"},
            {"word": "role", "phonetic": "/roʊl/", "meaning": "角色；作用"},
            {"word": "rub", "phonetic": "/rʌb/", "meaning": "擦；摩擦"},
            {"word": "rule", "phonetic": "/ruːl/", "meaning": "规则；统治"},
            {"word": "safety", "phonetic": "/ˈseɪfti/", "meaning": "安全；安全性"},
            {"word": "satisfy", "phonetic": "/ˈsætɪsfaɪ/", "meaning": "使满意；满足"},
            {"word": "save", "phonetic": "/seɪv/", "meaning": "节省；拯救；保存"},
            {"word": "scene", "phonetic": "/siːn/", "meaning": "场景；场面；景色"},
            {"word": "scold", "phonetic": "/skoʊld/", "meaning": "责骂；训斥"},
            {"word": "secret", "phonetic": "/ˈsiːkrət/", "meaning": "秘密"},
            {"word": "seek", "phonetic": "/siːk/", "meaning": "寻找；寻求"},
            {"word": "select", "phonetic": "/sɪˈlekt/", "meaning": "选择；挑选"},
            {"word": "selfish", "phonetic": "/ˈselfɪʃ/", "meaning": "自私的"},
            {"word": "sense", "phonetic": "/sens/", "meaning": "感觉；理智；意义"},
            {"word": "serious", "phonetic": "/ˈsɪriəs/", "meaning": "严肃的；严重的"},
            {"word": "serve", "phonetic": "/sɜːrv/", "meaning": "服务；招待；发球"},
            {"word": "set", "phonetic": "/set/", "meaning": "放置；一套；设定"},
            {"word": "settle", "phonetic": "/ˈsetl/", "meaning": "解决；定居"},
            {"word": "shake", "phonetic": "/ʃeɪk/", "meaning": "摇动；握手；颤抖"},
            {"word": "share", "phonetic": "/ʃer/", "meaning": "分享；份额；股份"},
            {"word": "shine", "phonetic": "/ʃaɪn/", "meaning": "发光；照耀"},
            {"word": "shock", "phonetic": "/ʃɑːk/", "meaning": "震惊；冲击"},
            {"word": "short", "phonetic": "/ʃɔːrt/", "meaning": "短的；矮的"},
            {"word": "sick", "phonetic": "/sɪk/", "meaning": "生病的；恶心的"},
            {"word": "signal", "phonetic": "/ˈsɪɡnəl/", "meaning": "信号；标志"},
            {"word": "silent", "phonetic": "/ˈsaɪlənt/", "meaning": "沉默的"},
            {"word": "similar", "phonetic": "/ˈsɪmələr/", "meaning": "相似的；类似的"},
            {"word": "simple", "phonetic": "/ˈsɪmpl/", "meaning": "简单的；朴素的"},
            {"word": "skill", "phonetic": "/skɪl/", "meaning": "技能；技巧"},
            {"word": "smile", "phonetic": "/smaɪl/", "meaning": "微笑；笑容"},
            {"word": "social", "phonetic": "/ˈsoʊʃl/", "meaning": "社会的；社交的"},
            {"word": "solution", "phonetic": "/səˈluːʃn/", "meaning": "解决方案；答案"},
            {"word": "solve", "phonetic": "/sɑːlv/", "meaning": "解决"},
            {"word": "sound", "phonetic": "/saʊnd/", "meaning": "声音；听起来；健全的"},
            {"word": "spare", "phonetic": "/sper/", "meaning": "备用的；多余的；饶恕"},
            {"word": "speak", "phonetic": "/spiːk/", "meaning": "说话；演讲"},
            {"word": "special", "phonetic": "/ˈspeʃl/", "meaning": "特别的；专门的"},
            {"word": "speed", "phonetic": "/spiːd/", "meaning": "速度；加速"},
            {"word": "spend", "phonetic": "/spend/", "meaning": "花费；度过"},
            {"word": "spirit", "phonetic": "/ˈspɪrɪt/", "meaning": "精神；心灵"},
            {"word": "spill", "phonetic": "/spɪl/", "meaning": "溢出；洒出"},
            {"word": "spread", "phonetic": "/spred/", "meaning": "传播；展开；涂抹"},
            {"word": "stage", "phonetic": "/steɪdʒ/", "meaning": "舞台；阶段；上演"},
            {"word": "stand", "phonetic": "/stænd/", "meaning": "站立；忍受；立场"},
            {"word": "start", "phonetic": "/stɑːrt/", "meaning": "开始；启动"},
            {"word": "state", "phonetic": "/steɪt/", "meaning": "状态；国家；陈述"},
            {"word": "steady", "phonetic": "/ˈstedi/", "meaning": "稳定的；稳固的"},
            {"word": "step", "phonetic": "/step/", "meaning": "步骤；步伐；阶梯"},
            {"word": "stick", "phonetic": "/stɪk/", "meaning": "粘贴；刺；忍受"},
            {"word": "still", "phonetic": "/stɪl/", "meaning": "仍然；静止的"},
            {"word": "stop", "phonetic": "/stɑːp/", "meaning": "停止；停下；车站"},
            {"word": "store", "phonetic": "/stɔːr/", "meaning": "商店；储存；仓库"},
            {"word": "storm", "phonetic": "/stɔːrm/", "meaning": "暴风雨；风暴"},
            {"word": "strange", "phonetic": "/streɪndʒ/", "meaning": "奇怪的；陌生的"},
            {"word": "street", "phonetic": "/striːt/", "meaning": "街道；马路"},
            {"word": "strength", "phonetic": "/streŋθ/", "meaning": "力量；优势；强度"},
            {"word": "strike", "phonetic": "/straɪk/", "meaning": "打击；罢工；撞击"},
            {"word": "struggle", "phonetic": "/ˈstrʌɡl/", "meaning": "斗争；挣扎；努力"},
            {"word": "study", "phonetic": "/ˈstʌdi/", "meaning": "学习；研究"},
            {"word": "succeed", "phonetic": "/səkˈsiːd/", "meaning": "成功；继任"},
            {"word": "success", "phonetic": "/səkˈses/", "meaning": "成功；成就"},
            {"word": "suffer", "phonetic": "/ˈsʌfər/", "meaning": "遭受；忍受；受苦"},
            {"word": "suggest", "phonetic": "/səˈdʒest/", "meaning": "建议；暗示"},
            {"word": "suit", "phonetic": "/suːt/", "meaning": "适合；套装；诉讼"},
            {"word": "support", "phonetic": "/səˈpɔːrt/", "meaning": "支持；支撑；供养"},
            {"word": "suppose", "phonetic": "/səˈpoʊz/", "meaning": "假设；认为"},
            {"word": "sure", "phonetic": "/ʃʊr/", "meaning": "确定的；肯定的"},
            {"word": "surface", "phonetic": "/ˈsɜːrfɪs/", "meaning": "表面；外表"},
            {"word": "surprise", "phonetic": "/sərˈpraɪz/", "meaning": "惊喜；惊讶"},
            {"word": "survive", "phonetic": "/sərˈvaɪv/", "meaning": "幸存；存活"},
            {"word": "suspect", "phonetic": "/səˈspekt/", "meaning": "怀疑；嫌疑犯"},
            {"word": "swim", "phonetic": "/swɪm/", "meaning": "游泳"},
            {"word": "sympathy", "phonetic": "/ˈsɪmpəθi/", "meaning": "同情；同情心"},
            {"word": "task", "phonetic": "/tæsk/", "meaning": "任务；工作"},
            {"word": "taste", "phonetic": "/teɪst/", "meaning": "味道；品尝；品味"},
            {"word": "teach", "phonetic": "/tiːtʃ/", "meaning": "教授；教导；传授"},
            {"word": "technology", "phonetic": "/tekˈnɑːlədʒi/", "meaning": "技术；科技"},
            {"word": "tell", "phonetic": "/tel/", "meaning": "告诉；讲述；辨别"},
            {"word": "temporary", "phonetic": "/ˈtempəreri/", "meaning": "暂时的；临时的"},
            {"word": "term", "phonetic": "/tɜːrm/", "meaning": "学期；术语；条款"},
            {"word": "terrible", "phonetic": "/ˈterəbl/", "meaning": "糟糕的；可怕的"},
            {"word": "thank", "phonetic": "/θæŋk/", "meaning": "感谢；谢谢"},
            {"word": "theory", "phonetic": "/ˈθɪri/", "meaning": "理论；学说"},
            {"word": "think", "phonetic": "/θɪŋk/", "meaning": "思考；认为；想"},
            {"word": "though", "phonetic": "/ðoʊ/", "meaning": "虽然；尽管"},
            {"word": "throw", "phonetic": "/θroʊ/", "meaning": "投掷；扔；抛"},
            {"word": "time", "phonetic": "/taɪm/", "meaning": "时间；时候；次"},
            {"word": "tired", "phonetic": "/ˈtaɪərd/", "meaning": "疲倦的；厌倦的"},
            {"word": "tolerate", "phonetic": "/ˈtɑːləreɪt/", "meaning": "忍受；容忍"},
            {"word": "tongue", "phonetic": "/tʌŋ/", "meaning": "舌头；语言"},
            {"word": "touch", "phonetic": "/tʌtʃ/", "meaning": "触摸；接触"},
            {"word": "tour", "phonetic": "/tʊr/", "meaning": "旅行；游览"},
            {"word": "tradition", "phonetic": "/trəˈdɪʃn/", "meaning": "传统；惯例"},
            {"word": "train", "phonetic": "/treɪn/", "meaning": "火车；训练；培养"},
            {"word": "travel", "phonetic": "/ˈtrævl/", "meaning": "旅行；传播"},
            {"word": "treat", "phonetic": "/triːt/", "meaning": "对待；治疗；请客"},
            {"word": "trial", "phonetic": "/ˈtraɪəl/", "meaning": "试验；审讯"},
            {"word": "trouble", "phonetic": "/ˈtrʌbl/", "meaning": "麻烦；烦恼"},
            {"word": "true", "phonetic": "/truː/", "meaning": "真实的；正确的"},
            {"word": "trust", "phonetic": "/trʌst/", "meaning": "信任；信赖"},
            {"word": "truth", "phonetic": "/truːθ/", "meaning": "真相；真理"},
            {"word": "try", "phonetic": "/traɪ/", "meaning": "尝试；努力"},
            {"word": "turn", "phonetic": "/tɜːrn/", "meaning": "转动；转弯；转变"},
            {"word": "type", "phonetic": "/taɪp/", "meaning": "类型；种类；打字"},
            {"word": "unite", "phonetic": "/juːˈnaɪt/", "meaning": "联合；团结；统一"},
            {"word": "unless", "phonetic": "/ənˈles/", "meaning": "除非"},
            {"word": "until", "phonetic": "/ənˈtɪl/", "meaning": "直到…为止"},
            {"word": "value", "phonetic": "/ˈvæljuː/", "meaning": "价值；重视"},
            {"word": "various", "phonetic": "/ˈveriəs/", "meaning": "各种各样的"},
            {"word": "view", "phonetic": "/vjuː/", "meaning": "视野；观点"},
            {"word": "visit", "phonetic": "/ˈvɪzɪt/", "meaning": "访问；参观"},
            {"word": "voice", "phonetic": "/vɔɪs/", "meaning": "声音"},
            {"word": "vote", "phonetic": "/voʊt/", "meaning": "投票；选票；表决"},
            {"word": "wait", "phonetic": "/weɪt/", "meaning": "等待；等候"},
            {"word": "wake", "phonetic": "/weɪk/", "meaning": "醒来；唤醒；叫醒"},
            {"word": "walk", "phonetic": "/wɔːk/", "meaning": "步行；散步"},
            {"word": "warm", "phonetic": "/wɔːrm/", "meaning": "温暖的；热情的"},
            {"word": "waste", "phonetic": "/weɪst/", "meaning": "浪费；废物"},
            {"word": "watch", "phonetic": "/wɑːtʃ/", "meaning": "观看；注视；手表"},
            {"word": "water", "phonetic": "/ˈwɔːtər/", "meaning": "水；雨水；海域"},
            {"word": "wave", "phonetic": "/weɪv/", "meaning": "波浪；挥手；波动"},
            {"word": "way", "phonetic": "/weɪ/", "meaning": "方式；方法；道路"},
            {"word": "weak", "phonetic": "/wiːk/", "meaning": "虚弱的；薄弱的"},
            {"word": "wealth", "phonetic": "/welθ/", "meaning": "财富；富裕"},
            {"word": "wear", "phonetic": "/wer/", "meaning": "穿着；磨损；戴"},
            {"word": "weather", "phonetic": "/ˈweðər/", "meaning": "天气"},
            {"word": "weigh", "phonetic": "/weɪ/", "meaning": "称重量；权衡"},
            {"word": "welcome", "phonetic": "/ˈwelkəm/", "meaning": "欢迎；迎接"},
            {"word": "well", "phonetic": "/wel/", "meaning": "很好地；充分地"},
            {"word": "west", "phonetic": "/west/", "meaning": "西方；西部"},
            {"word": "wet", "phonetic": "/wet/", "meaning": "湿的；弄湿"},
            {"word": "what", "phonetic": "/wʌt/", "meaning": "什么；多么"},
            {"word": "wide", "phonetic": "/waɪd/", "meaning": "宽的；广泛的"},
            {"word": "wife", "phonetic": "/waɪf/", "meaning": "妻子；太太"},
            {"word": "wild", "phonetic": "/waɪld/", "meaning": "野生的；疯狂的；狂热的"},
            {"word": "will", "phonetic": "/wɪl/", "meaning": "将要；愿意；意志"},
            {"word": "win", "phonetic": "/wɪn/", "meaning": "赢得；获胜；成功"},
            {"word": "wise", "phonetic": "/waɪz/", "meaning": "智慧的；明智的"},
            {"word": "wish", "phonetic": "/wɪʃ/", "meaning": "希望；祝愿"},
            {"word": "within", "phonetic": "/wɪˈðɪn/", "meaning": "在...之内；内部"},
            {"word": "without", "phonetic": "/wɪˈðaʊt/", "meaning": "没有；缺乏"},
            {"word": "wonder", "phonetic": "/ˈwʌndər/", "meaning": "惊奇；想知道；奇迹"},
            {"word": "work", "phonetic": "/wɜːrk/", "meaning": "工作；劳动；运转"},
            {"word": "world", "phonetic": "/wɜːrld/", "meaning": "世界；领域"},
            {"word": "worry", "phonetic": "/ˈwɜːri/", "meaning": "担心；烦恼"},
            {"word": "worth", "phonetic": "/wɜːrθ/", "meaning": "价值；值得的"},
            {"word": "write", "phonetic": "/raɪt/", "meaning": "写；书写；写作"},
            {"word": "wrong", "phonetic": "/rɔːŋ/", "meaning": "错误的；不正确的"}
        ]
    
    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="📚 英语单词记忆训练", 
            font=("微软雅黑", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=15)
        
        stats_frame = tk.Frame(self.root, bg="#ecf0f1", height=50)
        stats_frame.pack(fill=tk.X)
        stats_frame.pack_propagate(False)
        
        total_words = len(self.word_database)
        learned_count = len(self.learned_words)
        
        self.stats_label = tk.Label(
            stats_frame,
            text=f"总词汇: {total_words}  |  已掌握: {learned_count}  |  剩余: {total_words - learned_count}",
            font=("微软雅黑", 12),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.stats_label.pack(pady=10)
        
        self.words_container = tk.Frame(self.root, bg="#f0f5f9")
        self.words_container.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(self.root, bg="#f0f5f9", height=80)
        button_frame.pack(fill=tk.X, pady=10)
        button_frame.pack_propagate(False)
        
        next_btn = tk.Button(
            button_frame,
            text="🔄 下一组单词",
            font=("微软雅黑", 14, "bold"),
            bg="#3498db",
            fg="white",
            width=15,
            height=2,
            cursor="hand2",
            command=self.show_random_words
        )
        next_btn.pack(side=tk.LEFT, padx=30)
        
        save_btn = tk.Button(
            button_frame,
            text="💾 保存进度",
            font=('微软雅黑', 14, 'bold'),
            bg='#27ae60',
            fg='white',
            width=12,
            height=2,
            cursor='hand2',
            command=self.save_progress
        )
        save_btn.pack(side=tk.LEFT, padx=10)
        
        add_btn = tk.Button(
            button_frame,
            text="➕ 添加单词",
            font=('微软雅黑', 14, 'bold'),
            bg='#9b59b6',
            fg='white',
            width=12,
            height=2,
            cursor='hand2',
            command=self.add_word
        )
        add_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(
            button_frame,
            text="🚪 退出程序",
            font=('微软雅黑', 14, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=12,
            height=2,
            cursor='hand2',
            command=self.root.quit
        )
        quit_btn.pack(side=tk.RIGHT, padx=30)
    
    def add_word(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("添加新单词")
        add_window.geometry("500x300")
        add_window.configure(bg="#f0f5f9")
        add_window.transient(self.root)
        add_window.grab_set()
        
        frame = tk.Frame(add_window, bg="#f0f5f9", padx=40, pady=30)
        frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            frame,
            text="📝 手动添加单词",
            font=("微软雅黑", 16, "bold"),
            bg="#f0f5f9",
            fg="#2c3e50"
        ).pack(pady=(0, 20))
        
        word_frame = tk.Frame(frame, bg="#f0f5f9")
        word_frame.pack(fill=tk.X, pady=10)
        tk.Label(
            word_frame,
            text="单词:",
            font=("微软雅黑", 12),
            bg="#f0f5f9",
            fg="#2c3e50",
            width=10,
            anchor="e"
        ).pack(side=tk.LEFT, padx=10)
        word_entry = tk.Entry(
            word_frame,
            font=("Arial", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        word_entry.pack(side=tk.LEFT, padx=10)
        
        phonetic_frame = tk.Frame(frame, bg="#f0f5f9")
        phonetic_frame.pack(fill=tk.X, pady=10)
        tk.Label(
            phonetic_frame,
            text="音标:",
            font=("微软雅黑", 12),
            bg="#f0f5f9",
            fg="#2c3e50",
            width=10,
            anchor="e"
        ).pack(side=tk.LEFT, padx=10)
        phonetic_entry = tk.Entry(
            phonetic_frame,
            font=("Arial", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        phonetic_entry.pack(side=tk.LEFT, padx=10)
        
        meaning_frame = tk.Frame(frame, bg="#f0f5f9")
        meaning_frame.pack(fill=tk.X, pady=10)
        tk.Label(
            meaning_frame,
            text="中文翻译:",
            font=("微软雅黑", 12),
            bg="#f0f5f9",
            fg="#2c3e50",
            width=10,
            anchor="e"
        ).pack(side=tk.LEFT, padx=10)
        meaning_entry = tk.Entry(
            meaning_frame,
            font=("微软雅黑", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        meaning_entry.pack(side=tk.LEFT, padx=10)
        
        def save_new_word():
            word = word_entry.get().strip()
            phonetic = phonetic_entry.get().strip()
            meaning = meaning_entry.get().strip()
            
            if not word:
                messagebox.showerror("错误", "请输入单词")
                return
            if not phonetic:
                messagebox.showerror("错误", "请输入音标")
                return
            if not meaning:
                messagebox.showerror("错误", "请输入中文翻译")
                return
            
            for existing_word in self.word_database:
                if existing_word["word"].lower() == word.lower():
                    messagebox.showerror("错误", "该单词已存在")
                    return
            
            new_word = {
                "word": word,
                "phonetic": phonetic,
                "meaning": meaning
            }
            
            self.word_database.append(new_word)
            
            data_file = os.path.join(os.path.dirname(__file__), "word_database.json")
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(self.word_database, f, ensure_ascii=False, indent=2)
            
            self.update_stats()
            messagebox.showinfo("成功", f"已添加新单词: {word}")
            add_window.destroy()
        
        button_frame = tk.Frame(frame, bg="#f0f5f9")
        button_frame.pack(fill=tk.X, pady=20)
        
        save_btn = tk.Button(
            button_frame,
            text="💾 保存",
            font=("微软雅黑", 12, "bold"),
            bg="#27ae60",
            fg="white",
            width=10,
            height=1,
            cursor="hand2",
            command=save_new_word
        )
        save_btn.pack(side=tk.LEFT, padx=20)
        
        cancel_btn = tk.Button(
            button_frame,
            text="❌ 取消",
            font=("微软雅黑", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            width=10,
            height=1,
            cursor="hand2",
            command=add_window.destroy
        )
        cancel_btn.pack(side=tk.LEFT, padx=10)
    
    def show_random_words(self):
        for widget in self.words_container.winfo_children():
            widget.destroy()
        
        complete_words = [w for w in self.word_database if w["phonetic"] and w["meaning"]]
        if not complete_words:
            complete_words = self.word_database
        
        unlearned_words = [w for w in complete_words if w["word"] not in self.learned_words]
        if len(unlearned_words) < 5:
            sample_words = random.sample(complete_words, min(5, len(complete_words)))
        else:
            sample_words = random.sample(unlearned_words, 5)
        
        self.current_words = sample_words
        
        colors = ["#ffffff", "#f8f9fa"]
        
        for i, word_info in enumerate(sample_words):
            word_frame = tk.Frame(
                self.words_container,
                bg=colors[i % 2],
                relief=tk.RAISED,
                bd=2,
                padx=20,
                pady=15
            )
            word_frame.pack(fill=tk.X, pady=8)
            
            word_label = tk.Label(
                word_frame,
                text=word_info["word"],
                font=("Arial", 18, "bold"),
                bg=colors[i % 2],
                fg="#2c3e50",
                width=15,
                anchor="w"
            )
            word_label.pack(side=tk.LEFT, padx=5)
            
            phonetic_label = tk.Label(
                word_frame,
                text=word_info["phonetic"],
                font=("Arial", 14),
                bg=colors[i % 2],
                fg="#7f8c8d",
                width=20,
                anchor="w"
            )
            phonetic_label.pack(side=tk.LEFT, padx=10)
            
            meaning_label = tk.Label(
                word_frame,
                text=word_info["meaning"],
                font=("微软雅黑", 14),
                bg=colors[i % 2],
                fg="#27ae60",
                width=25,
                anchor="w",
                wraplength=200
            )
            meaning_label.pack(side=tk.LEFT, padx=10)
            
            learned_var = tk.BooleanVar(value=word_info["word"] in self.learned_words)
            
            def toggle_learned(word=word_info["word"], var=learned_var):
                if var.get():
                    self.learned_words.add(word)
                else:
                    self.learned_words.discard(word)
                self.update_stats()
            
            cb = tk.Checkbutton(
                word_frame,
                text="已掌握",
                font=("微软雅黑", 11),
                bg=colors[i % 2],
                fg="#e74c3c",
                variable=learned_var,
                command=toggle_learned,
                cursor="hand2"
            )
            cb.pack(side=tk.RIGHT, padx=10)
    
    def update_stats(self):
        total_words = len(self.word_database)
        learned_count = len(self.learned_words)
        self.stats_label.config(
            text=f"总词汇: {total_words}  |  已掌握: {learned_count}  |  剩余: {total_words - learned_count}"
        )
    
    def save_progress(self):
        learned_file = os.path.join(os.path.dirname(__file__), "learned_words.json")
        with open(learned_file, 'w', encoding='utf-8') as f:
            json.dump(list(self.learned_words), f, ensure_ascii=False, indent=2)
        messagebox.showinfo("保存成功", f"已保存 {len(self.learned_words)} 个已掌握单词的进度！")

def main():
    root = tk.Tk()
    app = VocabTrainer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
