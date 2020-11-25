import random

from utlis import run_time


class Merge(object):

    @staticmethod
    def less(v, w):
        """
        比较v和w的大小
        :param v: 可比较对象
        :param w: 可比较对象
        :return: True/False
        """
        return v < w

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

    def merge(self, array, low, mid, high):
        start = low
        end = mid + 1

        for k in range(low, high + 1):
            self.aux[k] = array[k]

        for k in range(low, high + 1):
            if start > mid:
                array[k] = self.aux[end]
                end += 1
            elif end > high:
                array[k] = self.aux[start]
                start += 1
            elif self.less(self.aux[end], self.aux[start]):
                array[k] = self.aux[end]
                end += 1
            else:
                array[k] = self.aux[start]
                start += 1

    def _sort(self, array, low, high):
        if high <= low:
            return
        mid = low + int((high - low) / 2)
        self._sort(array, low, mid)
        self._sort(array, mid + 1, high)
        self.merge(array, low, mid, high)

    @run_time
    def sort(self, array):
        self.aux = [0] * len(array)
        self._sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    merge_sort = Merge()
    # data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    # data = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10000)]
    data = [random.random() for i in range(1000000)]
    # print(data)
    merge_sort.sort(data)
    print(merge_sort.is_sorted(data))
    # print(data)
