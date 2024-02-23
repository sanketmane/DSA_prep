# Check if a linked list is a palindrome
# TC: O(N)
# SC: O(N) as we are creating a copy of existing linked list.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# create a dummy linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(20)
n4 = Node(10)
n1.next = n2
n2.next = n3
n3.next = n4

# create a copy of existing linked list
head1 = n1
head2 = Node(head1.data)
temp1 = head1
temp2 = head2
while temp1.next != None:
  temp3 = Node(temp1.next.data)
  temp2.next = temp3
  temp2 = temp2.next
  temp1 = temp1.next

# reverse the new linked list copy
prev = None
current = head2
while current != None:
  next_node = current.next
  current.next = prev
  prev = current
  current = next_node

# compare the copy with the original linked list
# if it doesn't match, we print and break.
head2 = prev
temp1 = head1
temp2 = head2
while temp1 != None:
  if temp1.data != temp2.data:
    print("Not a palindrome!")
    break
  temp1 = temp1.next
  temp2 = temp2.next









