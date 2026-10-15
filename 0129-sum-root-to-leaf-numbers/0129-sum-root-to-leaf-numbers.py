class Solution:
    def sumNumbers(self, root):
        def dfs(node, num):
            if node is None:
                return 0

            num = num * 10 + node.val

            # If it is a leaf node, return the number formed
            if node.left is None and node.right is None:
                return num

            # Calculate the sum from left and right subtrees
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)