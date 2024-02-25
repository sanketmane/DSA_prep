# Stack implementation using arrays

class Stack:
  def __init__(self):
    self.arr = []

  def push(self, val):
    self.arr.append(val)

  def pop(self):
    if self.is_empty():
      return -1

    x = self.arr.pop()
    return x

  def peek(self):
    return self.arr[-1] if not self.is_empty() else -1

  def is_empty(self):
    if len(self.arr) == 0:
      return True
    return False


s = Stack()
s.push(1)
s.push(2)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.is_empty())
s.push(1)
print(s.is_empty())