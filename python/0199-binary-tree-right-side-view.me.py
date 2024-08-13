# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = defaultdict(list)
        q = deque()
        q.append([root, 0])

        while q:
            node, level = q.popleft()
            if node:
                res[level].append(node.val)
                q.append([node.left, level+1])
                q.append([node.right, level+1])
                   
        keys = list(res.keys())
        keys.sort()
        answer = []
        for key in keys:
            answer.append(res[key][-1])

        return answer