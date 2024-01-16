# Question: Find total ways to reach bottom right of a 2d matrix

A = [[1,2,3],[4,5,6],[7,8,9]]

# Memoization solution(Top down approach)
n = len(A)
m = len(A[0])
dp = [[-1] * m for x in range(n)]
def total_ways(A, i,j):
  if i == 0 or j == 0:
    return 1
  # if i < 0 or j < 0:
  #   return 0
  if dp[i][j] != -1:
    return dp[i][j]
  else:
    dp[i][j] = total_ways(A, i-1,j) + total_ways(A, i,j-1)
    return dp[i][j]

ans = total_ways(A,2,2)
print(ans)

# Iterative/Tabular solution(Bottom up approach)
n = len(A)
m = len(A[0])
dp = [[-1] * m for x in range(n)]

def total_ways(A, i,j):
  for i in range(n):
    for j in range(m):
      if i == 0 and j == 0:
        dp[i][j] = 1
      elif i == 0:
        dp[i][j] = dp[i][j-1]
      elif j == 0:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

  return dp[n-1][m-1]

ans = total_ways(A,2,2)
print(ans)

# Iterative approach with constant space
def total_ways(A,i,j):
  for i in range(n):
    for j in range(m):
      if i == 0:
        dp[j] = 1
      elif j == 0:
        dp[j] = 1
      else:
        dp[j] = dp[j-1] + dp[j]
  return dp

ans = total_ways(A,2,2)
print(ans)





















