class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # Find the middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list
        if prev:
            prev.next = None

        # Middle node becomes root
        root = TreeNode(slow.val)

        # Only one node
        if slow == head:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root