from collections import defaultdict, deque


# Provided
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # space complexity:
        # - map containing logn int keys and n int values
        # - deque containing n TreeNodes and n int indexes
        # = O(log2(n) + n + n + n) = O(log2(n) + 3n) = O(n)
        #
        # time complexity: linear
        # = O(n)

        if not root:
            return []

        log = defaultdict(list)
        tree = deque([(root, 0)])
        while len(tree) > 0:
            node, idx = tree.popleft()
            log[idx].append(node.val)
            if node.left is not None:
                tree.append((node.left, idx + 1))
            if node.right is not None:
                tree.append((node.right, idx + 1))

        return list(log.values())
