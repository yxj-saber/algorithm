class WeightQuickUnionUF(object):

    def __init__(self, n):
        self.count = n
        self.array = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]
    
    def find(self, p):
        """
        p（0~N-1）所在分量的标识符
        :param p: 0~N-1
        :return: 0~lg(N-1)
        """
        while p != self.array[p]:
            p = self.array[p]
        return p

    def connected(self, p, q):
        """
        如果p和q存在与同一个分量中则返回True
        :param p: 0~N-1
        :param q: 0~N-1
        :return: True/False
        """
        return self.find(p) == self.find(q)

    def union_count(self):
        """
        联通分量的数量
        :return: self.count
        """
        return self.count

    def union(self, p, q):
        """
        在p和q之间建立一条连接
        :param p: 0~N-1
        :param q: 0~N-1
        :return: None
        """
        p_value = self.find(p)
        q_value = self.find(q)
        if p_value == q_value:
            return True
        if self.weight[p_value] > self.weight[q_value]:
            self.array[p_value] = q_value
            self.weight[p_value] += self.weight[q_value]
        else:
            self.array[q_value] = p_value
            self.weight[q_value] += self.weight[p_value]
        self.count -= 1


if __name__ == '__main__':
    # 连接数量
    data = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1),
            (8, 9), (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
    n = 10  # 节点数量
    quick_find = WeightQuickUnionUF(n)
    print(quick_find.array)
    print(quick_find.weight)
    for i, j in data:
        quick_find.union(i, j)
    print(quick_find.array)
    print(quick_find.weight)
    print(quick_find.count)
