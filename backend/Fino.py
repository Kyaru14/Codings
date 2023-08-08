import math

from backend.base import _BaseCoding
from backend.strct.TreeNode import TreeNode

class FinoCoding(_BaseCoding):
    """费诺编码"""
    def __init__(self):
        super().__init__()

    def encode(self, msg):
        self.msg = msg
        self.counter = self.count(msg)
        self.counter = self.normalize_counter(self.counter)
        self.tree = self.create_tree()
        self.coding_result = self.code_tree()
        self.encoded = ''
        for i in range(0, len(msg)):
            self.encoded += self.coding_result[msg[i]]
        return self.encoded

    def decode(self, code: str):
        """
        解码
        :param code: 已编码内容
        :return: 解码结果
        """
        decoded = ''
        node = self.tree
        # 根据编码沿着编码树向下走，判断到叶子结点后即可完成一次译码，然后回到根结点进行下一次译码
        for c in code:
            node = node[int(c)]
            if node.symb is not None:
                decoded += node.symb
                node = self.tree
        return decoded

    def normalize_counter(self, counter: list) -> list:
        """将counter中的频率转化为出现概率"""
        counter = list(map(lambda x : (x[0], x[1]/len(self.msg)), counter))
        return counter

    def create_tree(self) -> TreeNode:
        """构造码树"""
        def get_p_x(counter):
            return list(map(lambda x: x[1], counter))

        def _tree(root, counter):
            if len(counter) == 1:
                root.symb = counter[0][0]
            else:
                div = self.divide(get_p_x(counter))
                root.add_child(TreeNode(sum(get_p_x(counter)[:div]), None))
                _tree(root[0], counter[:div])
                root.add_child(TreeNode(sum(get_p_x(counter)[div:]), None))
                _tree(root[1], counter[div:])

        root = TreeNode(1.0, None)
        _tree(root, self.counter)
        return root

    def code_tree(self):
        """遍历树，生成编码结果"""
        result = {}

        def _iter(r: TreeNode, code: str):
            if r.symb is not None:
                result[r.symb] = code
                return
            else:
                for i in range(len(r.children)):
                    _iter(r.children[i], code + str(i))

        _iter(self.tree, '')
        return result

    @staticmethod
    def divide(p_x: list) -> int:
        """根据提供的一组概率，找出最佳分组位置 """
        p_sum = 0
        baseline = sum(p_x) / 2 # 基准线
        for i in range(len(p_x)):
            p_sum_new = p_sum + p_x[i]
            if abs(p_sum_new - baseline) > abs(p_sum - baseline): # 判断哪种分组离基准线更近
                break
            p_sum = p_sum_new
        print(f"分组位置：{i}, ({sum(p_x[:i])}), ({sum(p_x[i:])})")
        return i

    def summary(self):
        p_x = [freq for freq in map(lambda x:x[1], self.counter)]
        Hx = sum(-p*math.log2(p) for p in p_x)
        k_bar = 0
        for item in self.counter:
            p = item[1]
            l = len(self.coding_result[item[0]])
            k_bar += p * l
        yita = Hx / (k_bar * math.log2(self.r))
        compression = (len(self.encoded) / (len(self.msg) * 8)) * 100
        content = f"信源熵：{Hx:.5f} bit\n平均码长：{k_bar:.5f}\n编码效率：{yita * 100:.5f}%\n压缩率：{compression:.2f}%({len(self.encoded)}bit/{(len(self.msg) * 8)}bit)"
        return content


if __name__ == '__main__':
    fino = FinoCoding()
    encoded = fino("hello world")
    print(encoded)
    decoded = fino.decode(encoded)
    print(decoded)
    fino.summary()
