from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Logic is simple, we will do level order traversal and keep adding and popping
        # non-null nodes to the queue till the first null node.
        # We wil then pop the null node
        # Lastly,  we will check if there are any non-null nodes left in the queue
        # If yes, then this is not a complete binary tree.

        q = deque()
        q.append(root)
        # add and popout non-null nodes to the queue till the first non-null node
        while q[0] != None:
            front = q.popleft()
            q.append(front.left)
            q.append(front.right)
        # pop first null node from queue
        while len(q) > 0 and q[0] == None:
            q.popleft()

        # check if the queue has any non-null nodes left
        # If yes, then we return False else return True.
        if len(q) > 0:
            return False
        return True

