import math

from backend.base import _BaseCoding

class ShannonCoding(_BaseCoding):
    def __init__(self):
        super().__init__()

    def encode(self, msg):
        self.msg = msg
        self.counter = self.count(msg)
        self.counter = self.normalize_counter(self.counter)
        self.coding_result = self.code()
        self.encoded = ""
        for i in range(len(msg)):
            self.encoded += self.coding_result[1][self.coding_result[0].index(msg[i])]
        return self.encoded

    def decode(self, code):
        decoded = ""
        i = 0
        while i < len(code):
            for j in range(len(code[i:]) + 1):
                if code[i:i+j] in self.coding_result[1]:
                    decoded += self.coding_result[0][self.coding_result[1].index(code[i:i+j])]
                    i += j
                    break
        return decoded

    def normalize_counter(self, counter: list) -> list:
        """将counter中的频率转化为出现概率"""
        counter = list(map(lambda x : (x[0], x[1]/len(self.msg)), counter))
        return counter

    def code(self):
        symbs = []
        codes = []
        p_sum = 0
        for symb, p in self.counter:
            n = math.ceil(-math.log2(p)) # 计算码长
            symbs.append(symb)
            codes.append(self.decimal_to_binary(p_sum, n))
            p_sum += p # 计算累加概率
        return symbs, codes

    @staticmethod
    def decimal_to_binary(decimal, precision):
        """
        将小数转为二进制
        :param decimal: 待转化的小数
        :param precision: 精度，即保留二进制的位数
        :return: 转化结果
        """
        binary_decimal = ""
        for _ in range(precision):
            decimal *= 2
            bit = int(decimal)
            binary_decimal += str(bit)
            decimal -= bit
        return binary_decimal

    def summary(self):
        p_x = [freq for freq in map(lambda x: x[1], self.counter)]
        Hx = sum(-p * math.log2(p) for p in p_x)
        k_bar = 0
        for item in self.counter:
            p = item[1]
            symb = item[0]
            l = len(self.coding_result[1][self.coding_result[0].index(symb)])
            k_bar += p * l
        yita = Hx / (k_bar * math.log2(self.r))
        compression = (len(self.encoded) / (len(self.msg) * 8)) * 100
        content = f"信源熵：{Hx:.5f} bit\n平均码长：{k_bar:.5f}\n编码效率：{yita * 100:.5f}%\n压缩率：{compression:.2f}%({len(self.encoded)}bit/{(len(self.msg) * 8)}bit)"
        return content


if __name__ == '__main__':
    shannon = ShannonCoding()
    encoded = shannon("hello world")
    print(encoded)
    decoded = shannon.decode(encoded)
    print(decoded)
    shannon.summary()
