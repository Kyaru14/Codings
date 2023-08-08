import math

from backend.base import _BaseCoding
from backend.strct.TreeNode import TreeNode


class HuffmanEncoding(_BaseCoding):
    """霍夫曼编码"""

    def __init__(self, n=1, r=2):
        """
        q元符号（不需要给出），n重序列（默认1重，即一个符号编一个码），r进制编码
        """
        super().__init__()
        self.n = n
        self.r = r

    def set_n_r(self, n:int, r:int):
        self.n = n
        self.r = r

    def encode(self, msg: str):
        """
        编码
        :param msg: 待编码内容
        :return: 编码结果
        """
        self.msg = msg
        self.counter = self.count(msg)
        self.tree = self.create_tree()
        self.coding_result = self.code_tree()
        self.encoded = ''
        for i in range(0, len(msg), self.n):
            self.encoded += self.coding_result[msg[i:i + self.n]]
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

    def create_tree(self):
        """生成霍夫曼树"""
        assert 2 <= self.r <= 10
        nodes = [TreeNode(freq, symb) for symb, freq in self.counter]
        while len(nodes) != 1:
            node = TreeNode(0, None)
            times = self.r if len(nodes) >= self.r else len(nodes)
            for i in range(times):
                node.add_child(nodes.pop())
            nodes.append(node)
            nodes = sorted(nodes, reverse=True)
        return nodes[0]

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

    def summary(self):
        l_msg = self.tree.freq
        p_x = [freq / l_msg for freq in map(lambda x: x[1], self.counter)]
        Hx = sum(-p * math.log2(p) for p in p_x)
        k_bar = 0
        for item in self.counter:
            p = item[1] / l_msg
            l = len(self.coding_result[item[0]])
            k_bar += p * l
        yita = Hx / (k_bar * math.log2(self.r))
        if self.r == 2:
            compression = (len(self.encoded) / (l_msg*8)) * 100
            content = f"信源熵：{Hx:.5f} bit\n平均码长：{k_bar:.5f}\n编码效率：{yita * 100:.5f}%\n压缩率：{compression:.2f}%({len(self.encoded)}bit/{(l_msg*8)}bit)"
        else:
            content = f"信源熵：{Hx:.5f} bit\n\n平均码长：{k_bar:.5f}\n\n编码效率：{yita * 100:.5f}%"
        return content


if __name__ == '__main__':
    huffman = HuffmanEncoding(n=1, r=2)
    encoded = huffman.encode("Hello World!")
    print(encoded)
    print(huffman.coding_result)
    huffman.summary()
    print(huffman.decode(encoded))
