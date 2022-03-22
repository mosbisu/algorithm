from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def from_tree_to_list(self, root):

        queue_tree = deque()
        queue_tree.append([root, 1])
        shows = []
        while queue_tree:
            leftp = queue_tree.popleft()
            shows.append(leftp)
            if leftp[0].left:
                queue_tree.append([leftp[0].left, leftp[1] * 2])
            if leftp[0].right:
                queue_tree.append([leftp[0].right, leftp[1] * 2 + 1])
        nodes, locs = zip(*shows)
        max_locs = max(locs)
        tree_to_list = [None for _ in range(max_locs)]
        for i in shows:
            tree_to_list[i[1] - 1] = i[0].val
        print(tree_to_list)

        return root


child2_right = TreeNode(7, None, None)
child2_left = TreeNode(15, None, None)
child1_right = TreeNode(20, child2_left, child2_right)
child1_left = TreeNode(9, None, None)
parent = TreeNode(3, child1_left, child1_right)

solution = Solution()
solution.from_tree_to_list(parent)
