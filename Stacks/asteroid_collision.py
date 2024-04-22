# Asteroid Collision - Leetcode 735 problem
# https://leetcode.com/problems/asteroid-collision/
# Nice explanation by Neetcode: https://www.youtube.com/watch?v=LN7KjRszjk4

class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      """
      Our goal is to check what is left after all the collisions have happened.
      For collisions to happen:
          left side asteroid should be +ve
          right side asteroid should be -ve
      Since we have to discard an asteroid after collision, 
      stack fits the usecase as it allows to pop in O(1) time.
      """
      n = len(asteroids)
      stack = []
      # For each asteroid, check if stack is not empty and right asteroid is -ve
      # and left asteroid sitting at the top of stack is +ve. This will set the scene for collision.
      for i in range(n):
          while len(stack) > 0 and asteroids[i] < 0 and stack[-1] > 0:
              diff = asteroids[i] + stack[-1]
              # if diff is -ve that means right asteroid is bigger in size and destroyed left asteroid
              # Hence, we pop the destroyed asteroid from the stack
              if diff < 0: 
                  stack.pop()
              # if diff is +ve, left asteroid is bigger is size and right asteroid is destroyed.
              # For this we just right asteroid temporarily as 0 as will cause the while loop to exit
              # for the right asteroid and we will move to the next asteroid in the list of asteroids.
              elif diff > 0:
                  asteroids[i] = 0
              # This final case means both left and right asteroids are destroyed,
              # hence we mark right asteroid as 0 and remove the left one from stack.
              else:
                  asteroids[i] = 0
                  stack.pop()

          # after the above is complete and right asteroid is not marked 0,
          # that means, it continues to move further towards left to collide with remainaing asteroids.
          # so we add it to the stack.
          if asteroids[i] != 0:
              stack.append(asteroids[i])

      # In the end, whatever remains in the stack tells how many asteroids are still present.
      return stack

