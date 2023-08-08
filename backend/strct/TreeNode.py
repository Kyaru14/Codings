class TreeNode:
    """
    树结点类
    """
    def __init__(self, freq, symb: str | None, children: list | None = None):
        if children is None:
            children = []
        self.freq = freq # 出现频率
        self.symb = symb # 结点代表的符号，若符号不为None则为叶子结点
        self.children = children # 子结点

    def __getitem__(self, item):
        """重载下标，返回对应的子结点"""
        return self.children[item]

    def add_child(self, node):
        """将一个结点挂在另一个结点下，此时父结点的频率应当加上子结点的频率"""
        self.children.append(node)
        self.freq += node.freq

    def __lt__(self, other):
        """重载比较方法，便于排序"""
        return self.freq < other.freq

    def __repr__(self):
        if self.symb is not None:
            return "<" + str(self.freq) + "," + self.symb + ">"
        else:
            return "<" + str(self.freq) + ">"
