class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

head1 = a
head2 = Node(head1.data)
temp = a
current_node = head2
while temp.next != None:
  temp1 = Node(temp.next.data)
  current_node.next = temp1
  current_node = current_node.next
  temp = temp.next

x = head2
while x != None:
  print(x.data)
  x = x.next