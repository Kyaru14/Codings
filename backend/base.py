class _BaseCoding:
    """编码基类"""
    def __init__(self):
        self.msg = None  # 原始消息
        self.counter = None  # 记录每个符号出现的频率
        self.tree = None  # 编码树
        self.coding_result = None  # 编码结果
        self.n = 1 # n重序列，默认为1
        self.r = 2 # r进制编码，默认为2

    def __call__(self, *args, **kwargs):
        return self.encode(*args, **kwargs)

    def count(self, msg: str) -> list:
        """统计消息中不同符号的出现频率"""
        counter = {}
        for i in range(0, len(msg), self.n):
            counter.setdefault(msg[i:i+self.n], 0)
            counter[msg[i:i+self.n]] += 1
        counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)  # 按出现频率从大到小排序
        return counter

    def encode(self, msg):
        raise NotImplementedError

    def decode(self, code):
        raise NotImplementedError

    def summary(self):
        """评估编码性能指标，平均码长，编码效率，信息熵等"""
        raise NotImplementedError
