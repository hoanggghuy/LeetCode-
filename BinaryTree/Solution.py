from typing import Optional, List
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
            

if __name__ == '__main__':
    s=Solution()
