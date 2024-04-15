A = [1,5,2,3,7]
# Selection Sort

def selection_sort(A):
  def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

  n = len(A)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if A[j] < A[min_idx]:
        min_idx = j
    swap(A, i, min_idx)

  return A

ans = selection_sort(A)
print(ans)

# Insertion Sort
def insertion_sort(A):
  def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
  n = len(A)
  for i in range(n):
    j = i-1
    while j >= 0 and A[j] > A[j+1]:
      swap(A,j,j+1)
      j -= 1
  return A

ans = insertion_sort(A)
print(ans)