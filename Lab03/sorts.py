import random
import timeit
import math

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L,i)
    return L

def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i, i-1)
        else:
            return
        i -= 1

def selection_sort(L):
    for i in range(len(L)):
        mindex = find_min_index(L, i)
        swap(L, i, mindex)
    return L

def find_min_index(L, n):
    mindex = n
    for i in range(n+1, len(L)):
        if L[i] < L[mindex]:
            mindex = i
    return mindex

def bubbleSort(L): 
    n = len(L) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if L[j] > L[j+1] : 
                L[j], L[j+1] = L[j+1], L[j]
    return L

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n * factor)):
        r1 = random.randint(0, n-1)
        r2 = random.randint(0, n-1)
        swap(L, r1, r2)
    return L

def timetest(runs, n, f, factor):
    total = 0
    for _ in range(runs):
        L = create_near_sorted_list(n, factor)
        start = timeit.default_timer()
        f(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_2(runs, n, f):
    total = 0
    for _ in range(runs):
        L = create_random_list(n)
        L.sort(reverse=True)
        start = timeit.default_timer()
        f(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def quicksort_inplace(L):
    if len(L) <= 1:
        return L
    return partition(L,0,len(L)-1)

def partition(L,s,e):
    x = s
    pivot = L[e]  

    if s < e:  
        for i in range(s,e+1):
            if L[i] <= pivot:
                L[x], L[i] = L[i], L[x]
                if i != e:
                    x += 1
        partition(L,s,x-1)  
        partition(L,x+1,e)  
    return L

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

def dual_pivot_quicksort(L):
    list1, list2, list3 = [], [], []

    n = len(L)    
    if (n < 2):
        return L

    pivot1, pivot2 = quicksort_inplace([L.pop(0), L.pop(0)])

    for num in L[1:]:
        if (num < pivot1):
            list1.append(num)
        elif (pivot1 <= num < pivot2):
            list2.append(num)
        else:
            list3.append(num)
    return dual_pivot_quicksort(list1)+[pivot1]+dual_pivot_quicksort(list2)+[pivot2]+dual_pivot_quicksort(list3)

def tri_pivot_quicksort(L):
    list1, list2, list3, list4 = [], [], [], []

    n = len(L)
    if (n < 2):
        return L
    elif (n == 2):
        if(L[1] < L[0]):
            return [L[1],L[0]]
        else:
            return [L[0],L[1]]

    pivot1, pivot2, pivot3 = quicksort_inplace([L.pop(0), L.pop(0), L.pop(0)])
    for num in L:
        if (num < pivot1):
            list1.append(num)
        elif (pivot1 <= num < pivot2):
            list2.append(num)
        elif (pivot2 <= num < pivot3):
            list3.append(num)
        else:
            list4.append(num)

    return tri_pivot_quicksort(list1)+[pivot1]+tri_pivot_quicksort(list2)+[pivot2]+tri_pivot_quicksort(list3)+[pivot3]+tri_pivot_quicksort(list4)

def quad_pivot_quicksort(L):
    list1, list2, list3, list4, list5 = [], [], [], [], []

    n = len(L)
    if (n < 2):
        return L
    elif (n == 2):
        if (L[1] < L[0]):
            return [L[1],L[0]]
        else:
            return [L[0],L[1]]
    elif (n == 3):
        if (L[1] < L[0] and L[1] < L[2]):
            if (L[0] < L[2]):
                return [L[1],L[0],L[2]]
            else:
                return [L[1],L[2],L[0]]
        elif (L[0] < L[1] and L[0] < L[2]):
            if (L[1] < L[2]):
                return [L[0],L[1],L[2]]
            else:
                return [L[0],L[2],L[1]]
        else:
            if (L[0] < L[1]):
                return [L[2],L[0],L[1]]
            else:
                return [L[2],L[1],L[0]]

    pivot1, pivot2, pivot3, pivot4 = quicksort_inplace([L.pop(0), L.pop(0), L.pop(0), L.pop(0)])
    for num in L:
        if (num < pivot1):
            list1.append(num)
        elif (pivot1 <= num < pivot2):
            list2.append(num)
        elif (pivot2 <= num < pivot3):
            list3.append(num)
        elif (pivot3 <= num < pivot4):
            list4.append(num)
        else:
            list5.append(num)

    return quad_pivot_quicksort(list1)+[pivot1]+quad_pivot_quicksort(list2)+[pivot2]+quad_pivot_quicksort(list3)+[pivot3]+quad_pivot_quicksort(list4)+[pivot4]+quad_pivot_quicksort(list5)

# print(bubbleSort([3,6,2,9,0,-1,-5,-3,99,-99]))

for i in range(1,1001):
    print(i, timetest(20, i, bubbleSort, 0.032), timetest(20, i, selection_sort, 0.032), timetest(20, i, insertion_sort, 0.032), timetest(20, i, quad_pivot_quicksort, 0.032))