import math
import random


class MaxPriorityQueue(object):

    def __init__(self):
        self.priority_queue = [None]
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def site(self):
        return self.count

    def insert(self, v):
        self.priority_queue.append(v)
        self.count += 1
        self.swim(self.count)

    def del_max(self):
        # 此处应该先验空，为真抛出异常
        max_value = self.priority_queue[1]
        self.exch(1, self.count)
        self.priority_queue.pop()
        self.count -= 1
        self.sink(1)
        return max_value

    def less(self, i, j):
        return self.priority_queue[i] < self.priority_queue[j]

    def exch(self, i, j):
        self.priority_queue[i], self.priority_queue[j] = \
            self.priority_queue[j], self.priority_queue[i]

    def swim(self, k):
        while k > 1 and self.less(int(k / 2), k):
            self.exch(int(k / 2), k)
            k = int(k / 2)

    def sink(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j < self.count and self.less(j, j + 1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def print_max_pq(self):
        i = 0
        flag = 1
        # length = 2 ** math.ceil(math.log2(self.count)) - 1
        while flag <= self.count:
            line = '-'.join(map(lambda item: str(item), self.priority_queue[flag:flag + 2 ** i]))
            # line = line.center(length, '-')
            print(line)
            flag = flag + 2 ** i
            i += 1


if __name__ == '__main__':
    max_pq = MaxPriorityQueue()
    for _ in range(10):
        max_pq.insert(random.randint(1, 1000))
    print(max_pq.priority_queue)
    max_pq.print_max_pq()
    x = max_pq.del_max()
    print(x)
    print(max_pq.priority_queue)
    max_pq.print_max_pq()
