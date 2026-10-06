class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # If there is no left child, go to the right
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If there is no right child, go to the left
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # If both children exist, take the smaller depth
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))