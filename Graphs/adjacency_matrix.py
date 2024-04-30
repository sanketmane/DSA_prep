# Adjacency matrix
A = [1,2,3,4,2,3,1]
B = [4,5,2,3,4,5,2]
C = [[0] * (max(A)+2) for x in range(max(A)+2)]

for i in range(len(C)):
  row = A[i]
  col = B[i]
  C[row][col] = 1
  C[col][row] = 1

print(C)
