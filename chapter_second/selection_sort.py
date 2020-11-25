import random

from utlis import run_time


class Selection(object):

    @staticmethod
    def less(v, w):
        """
        比较v和w的大小
        :param v: 可比较对象
        :param w: 可比较对象
        :return: True/False
        """
        return v < w

    @staticmethod
    def exch(array, m, n):
        """
        交换array中索引m和索引n处的值
        :param array:
        :param m: array索引
        :param n: array索引
        :return: None
        """
        array[m], array[n] = array[n], array[m]

    def is_sorted(self, array):
        """
        判断array是否有序，有序返回True，无序返回False
        :param array: 可迭代对象
        :return: True/False
        """
        for i in range(1, len(array)):
            if self.less(array[i], array[i - 1]):
                return False
        return True

    @run_time
    def sort(self, array):
        """
        对array进行升序排序
        :param array: 可迭代对象
        :return: None
        """
        length = len(array)
        for i in range(length):
            for j in range(i + 1, length):
                if self.less(array[j], array[i]):
                    self.exch(array, i, j)


if __name__ == '__main__':
    selection = Selection()
    # data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    # data = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10000)]
    data = [random.randint(1, 100) for i in range(100000)]
    # print(data)
    selection.sort(data)
    # print(data)
