# LCA -> Lowest common ancestor
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr = []
        def helper(root, k):
            if root == None:
                return False
            if root.val == k: # deepest node in tree is first added to the array.
                arr.append(root)
                return True
            if helper(root.left, k):
                arr.append(root)
                return True
            if helper(root.right, k):
                arr.append(root)
                return True
            return False

        helper(root, p.val)
        arr1 = arr[:] # do a deep copy of list

        arr.clear()

        helper(root, q.val)
        arr2 = arr[:] # do a deep copy of list

        # check first value in array
        n = len(arr1)
        for i in range(n):
            if arr1[i] in arr2:
                return arr1[i]