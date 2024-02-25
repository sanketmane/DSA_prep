# Stack implementation using LinkedList
# head represents top of the stack
# we will do add and removal first

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.length = 0

  def push(self, val):
    new_node = Node(val)
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1

  def pop(self):
    if self.is_empty():
      return -1
    val = self.head.data
    self.head = self.head.next
    self.length -= 1
    return val

  def peek(self):
    if self.is_empty():
      return -1
    return self.head.data

  def is_empty(self):
    if self.length == 0:
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