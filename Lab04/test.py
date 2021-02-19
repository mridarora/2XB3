# def merge_bottom(L, start, mid, end):
#     temp = L.copy()
#     i = start
#     j = mid + 1
#     k = start
#     while i <= mid and j <= end:
#         if L[i] < L[j]:
#             temp[k] = L[i]
#             i += 1
#         else:
#             temp[k] = L[j]
#             j += 1
#         k += 1
#     while i <= mid and i < len(L):
#         temp[k] = L[i]
#         k += 1
#         i += 1
#     for i in range(start, end + 1):
#         L[i] = temp[i]

# def mergesort_bottom(L):
#     h = len(L) - 1
#     l = 0
#     s = 1
#     while s <= h - l:
#         for i in range(l, h, 2*s):
#             start = i
#             mid = i + s - 1
#             end = min(i + 2*s - 1, h)
#             merge_bottom(L, start, mid, end)
#         s = 2*s
#     return L

def mergeSort(a): 
     
    current_size = 1
     
    # Outer loop for traversing Each 
    # sub array of current_size 
    while current_size <= len(a) - 1: 
         
        left = 0
        # Inner loop for merge call 
        # in a sub array 
        # Each complete Iteration sorts 
        # the iterating sub array 
        while left < len(a)-1: 
             
            # mid index = left index of 
            # sub array + current sub 
            # array size - 1 
            mid = min((left + current_size - 1),(len(a)-1))
             
            # (False result,True result) 
            # [Condition] Can use current_size 
            # if 2 * current_size < len(a)-1 
            # else len(a)-1 
            right = ((2 * current_size + left - 1, 
                    len(a) - 1)[2 * current_size 
                        + left - 1 > len(a)-1]) 
                             
            # Merge call for each sub array 
            merge(a, left, mid, right) 
            left = left + current_size*2
             
        # Increasing sub array size by 
        # multiple of 2 
        current_size = 2 * current_size 
 
# Merge Function 
def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            a[k] = R[j] 
            j += 1
        else: 
            a[k] = L[i] 
            i += 1
        k += 1
 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
 
 
# Driver code 
a = [3,5,1,4,0]
print("Given array is ") 
print(a) 
 
mergeSort(a) 
 
print("Sorted array is ") 
print(a) 