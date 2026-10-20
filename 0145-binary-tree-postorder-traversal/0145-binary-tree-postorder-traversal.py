class Solution:
    def postorderTraversal(self, root):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

        traverse(root)
        return result