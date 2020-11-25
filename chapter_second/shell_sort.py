import random

from utlis import run_time


class Shell(object):

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
        h = 1
        while h < length / 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(1, length):
                for j in range(1, i + 1, h)[::-1]:
                    if self.less(array[j], array[j - h]):
                        self.exch(array, j, j - h)
            h = int(h / 3)


if __name__ == '__main__':
    shell = Shell()
    # data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    data = [random.randint(1, 100000) for i in range(10000)]
    # print(data)
    shell.sort(data)
    print(shell.is_sorted(data))
    # print(data)
