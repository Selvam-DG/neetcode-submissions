# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if not root:
            return res
        if root:
            q.append(root)
        while q:
            qLen = len(q)            
            inside_list = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    inside_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if inside_list:
                res.append(inside_list)
        return res
        