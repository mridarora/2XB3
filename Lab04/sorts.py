import random
import timeit

def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

def mergesort_bottom(L):  
    s = 1
    while s < len(L):     
        low = 0 
        while low < len(L)-1: 
            middle = min((low + s - 1),(len(L)-1))
            high = ((2 * s + low - 1, len(L) - 1)[2 * s + low - 1 > len(L)-1]) 
            merge_bottom(L, low, middle, high) 
            low += s*2
        s *= 2
    return L

def merge_bottom(L, start, mid, end): 
    l1 = mid - start + 1
    l2 = end - mid 
    left = [0] * l1 
    right = [0] * l2 
    for i in range(0, l1): 
        left[i] = L[start + i] 
    for i in range(0, l2): 
        right[i] = L[mid + i + 1] 
    a = 0
    b =  0
    c = start 
    while b < l2 and a < l1: 
        if left[a] > right[b]: 
            L[c] = right[b] 
            b = b + 1
        else: 
            L[c] = left[a] 
            a = a + 1
        c = c + 1
    while a < l1: 
        L[c] = left[a] 
        a = a + 1
        c = c + 1
    while b < l2: 
        L[c] = right[b] 
        b = b + 1
        c = c + 1

def timetest(runs, n, f):
    total = 0
    for _ in range(runs):
        L = create_random_list(n)
        start = timeit.default_timer()
        f(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

# for i in range(1,5000):
#     print(i, timetest(20, i, mergesort), timetest(20, i, mergeSort))