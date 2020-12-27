import random
from utlis import run_time


class Quick(object):

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

    def partition(self, array, low, high):
        left = low
        right = high + 1
        v = array[low]
        while True:
            while True:
                left += 1
                if not self.less(array[left], v):
                    break
                if left == high:
                    break
            while True:
                right -= 1
                if not self.less(v, array[right]):
                    break
                # if right == low:
                #     break
            if left >= right:
                break
            self.exch(array, left, right)
        self.exch(array, low, right)
        return right

    def _sort(self, array, low, high):
        if high <= low:
            return
        j = self.partition(array, low, high)
        self._sort(array, low, j - 1)
        self._sort(array, j + 1, high)

    @run_time
    def sort(self, array):
        self._sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    quick_sort = Quick()
    # data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    # data = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10000)]
    data = [random.random() for i in range(100000)]
    # print(data)
    quick_sort.sort(data)
    print(quick_sort.is_sorted(data))
    # print(data)
