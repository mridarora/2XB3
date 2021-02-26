import math

class KHeap():
    length = 0
    values = []
    k = 2

    def __init__(self, values, k):
        self.values = values
        self.length = len(values)
        self.k = k

    def build_heap(self, values):
        i = (self.length-1)//self.k
        for i in range(i, -1, -1): 
            self.sink(i)

    def sink(self, i):
        maximum = i
        for j in range(0, self.k):
            if self.alt_children(j, i) < self.length and self.values[self.alt_children(j, i)] > self.values[i]:
                if self.values[self.alt_children(j, i)] > self.values[maximum]:
                    maximum = self.alt_children(j, i)
        if maximum != i:
            self.values[i], self.values[maximum] = self.values[maximum], self.values[i]
            self.sink(maximum)

    def parent(self, i):
        return (i - 1) // self.k

    def children(self, i):
        l = []
        for j in range(1, self.k + 1):
            l.append(self.k*i + j)
        return l
    
    def alt_children(self, i, j):
        return (self.k*i + 1 + j)