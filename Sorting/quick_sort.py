# Quick Sort implementation
# Best case TC: O(nlogn), Worst case TC: O(n2), Avg TC: O(nlogn)
# Best case SC: O(logn), Worsr case SC: O(n)

A = [3,2,1,5,6,9]

def swap(A, l, r):
  A[l], A[r] = A[r], A[l]

def partition_array(A, start, end):
  n = len(A)
  pivot = A[start]
  l = start+1
  r = end
  while l <= r:
    if A[l] <= pivot:
      l += 1
    elif A[r] > pivot:
      r -= 1
    else:
      swap(A, l, r)
      l += 1
      r -= 1
  swap(A, start, r)
  return r

def quick_sort(A,start,end):
  if start < end:
    pivot = partition_array(A,start,end)
    quick_sort(A,start,pivot-1)
    quick_sort(A,pivot+1,end)

quick_sort(A,0,len(A)-1)
print(A)


