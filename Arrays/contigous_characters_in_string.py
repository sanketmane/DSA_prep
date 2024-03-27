# This problem was asked in March TCT 1.5 and
# related to LeetCode problems 3 and 424.
# Logic here involves using dynamic sliding window using 2 pointers.

class Solution:
  # @param A : string
  # @param B : integer
  # @param C : string
  # @return an integer
  def solve(self, A, B, C):
      n = len(A)
      i = 0
      j = 0
      other_cnt = 0
      max_len = 0
      while j < n:
         if A[j] != C:
             other_cnt += 1
         j += 1

         while other_cnt > B:
             if A[i] != C:
                 other_cnt -= 1
             i += 1
         max_len = max(max_len, j-i)
      return max_len	     