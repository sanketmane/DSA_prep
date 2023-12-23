# DNF problem solution using 3-pointer approach

def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

def dnf(A):
  n = len(A)
  low = 0
  mid = 0
  hi = n-1
  while mid <= hi:
    if A[mid] == 0:
      swap(A, mid, low)
      low += 1
      mid += 1
    elif A[mid] == 2:
      swap(A, mid, hi)
      hi -= 1
    else:
      mid += 1
  return A


A = [0, 1, 2, 0, 1, 2]
print(dnf(A))