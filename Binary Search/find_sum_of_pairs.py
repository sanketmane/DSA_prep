A = [-5,-2,1,6,10,12,5]
k = 11


def find_sum(A, k):
  n = len(A)
  for i in range(n):
    lo = i+1
    hi = n-1
    x = k-A[i]
    while lo <= hi:
      mid = lo + (hi-lo)//2
      if A[mid] == x:
        return (i,mid)
      elif A[mid] < x:
        lo = mid+1
      else:
        hi = mid-1
  return -1

ans = find_sum(A,k)
print(ans)