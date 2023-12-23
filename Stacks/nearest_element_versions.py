# Nearest smaller/greater right/left code versions

# Nearest smaller element array from the right.
def nearest_small_element_right(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n-1,-1,-1):
        while len(stack) > 0 and stack[-1] >= A[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(A[i])

    ans = [ x for x in reversed(ans) ] # reverse because we will get earlier ans from left to right.
    return ans

# print(nearest_small_element_right(A))

# Nearest smaller element left index
def nearest_small_element_left_index(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n):
        while len(stack) > 0 and A[stack[-1]] >= A[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    return ans
# print(nearest_small_element_left_index(A))


# Nearest greater element left
def nearest_greater_element_left(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n):
        # remove smaller elements from stack till its empty or we reach the element > A[i]
        while len(stack) > 0 and stack[-1] <= A[i]: 
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(A[i])
    return ans
# print(nearest_greater_element_left(A))

# Nearest greater element left index
def nearest_greater_element_left_index(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n):
        # remove smaller index from stack till its empty or we reach the element > A[i]
        while len(stack) > 0 and A[stack[-1]] <= A[i]: 
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    return ans
# print(nearest_greater_element_left_index(A))

# Nearest greater element right
def nearest_greater_element_right(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n-1,-1,-1):
        # remove smaller index from stack till its empty or we reach the element > A[i]
        while len(stack) > 0 and stack[-1] <= A[i]: 
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(A[i])

    ans = [x for x in reversed(ans)]
    return ans
# print(nearest_greater_element_right(A))


# Nearest greater element right index
def nearest_greater_element_right_index(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n-1,-1,-1):
        # remove smaller index from stack till its empty or we reach the element > A[i]
        while len(stack) > 0 and A[stack[-1]] <= A[i]: 
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)

    ans = [x for x in reversed(ans)]
    return ans
# print(nearest_greater_element_right_index(A))

# Get the distance from Nearest smaller element on the left 
def distance_from_nearest_small_element_left_index(A):
    n = len(A)
    ans = []
    stack = []
    for i in range(n):
        while len(stack) > 0 and A[stack[-1]] >= A[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            dist = i-stack[-1]
            ans.append(dist)
        stack.append(i)
    return ans
# print(distance_from_nearest_small_element_left_index(A))

def nearest_small_element_right_index(A):
  n = len(A)
  ans = []
  stack = []
  for i in range(n-1,-1,-1):
    while len(stack) > 0 and A[stack[-1]] >= A[i]:
      stack.pop()
    if len(stack) == 0:
      ans.append(n)
    else:
      ans.append(stack[-1])
    stack.append(i)

  ans_len = len(ans)
  ans = [x for x in reversed(ans)] # need to reverse
  return ans

A = [1,4,2,3,5,1]
x = nearest_small_element_right_index(A)
print(x)