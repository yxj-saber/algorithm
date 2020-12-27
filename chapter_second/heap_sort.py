import random

from utlis import run_time


class HeapSort(object):

    @staticmethod
    def less(array, i, j):
        """
        比较array中i和j索引位置对象的大小
        :param array: 待比较数组array
        :param i: array索引
        :param j: array索引
        :return: True/False
        """
        return array[i] < array[j]

    @staticmethod
    def exch(array, m, n):
        """
        交换array中索引m和索引n处的值
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
        for i in range(2, len(array)):
            if self.less(array, i, i - 1):
                return False
        return True

    def sink(self, array, k, n):
        while 2 * k <= n:
            child = 2 * k
            if 2 * k + 1 <= n and self.less(array, child, child + 1):
                child += 1
            if not self.less(array, k, child):
                break
            self.exch(array, k, child)
            k = child

    @run_time
    def sort(self, array):
        length = len(array) - 1
        for i in range(1, int(length / 2) + 1)[::-1]:
            self.sink(array, i, length)
        while length > 1:
            self.exch(array, 1, length)
            length -= 1
            self.sink(array, 1, length)


if __name__ == '__main__':
    heap_sort = HeapSort()
    # data = [''] + ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    # data = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10000)]
    data = [''] + [random.random() for i in range(100000)]
    # print(data)
    heap_sort.sort(data)
    print(heap_sort.is_sorted(data))
    # print(data)
