class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                temp = head

                while temp != slow:
                    temp = temp.next
                    slow = slow.next

                return temp

        return None