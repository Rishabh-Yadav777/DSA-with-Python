class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        old_to_new = {}
        curr = head

        # Create a copy of each node
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Set next and random pointers
        while curr:
            new_node = old_to_new[curr]

            if curr.next:
                new_node.next = old_to_new[curr.next]

            if curr.random:
                new_node.random = old_to_new[curr.random]

            curr = curr.next

        return old_to_new[head]