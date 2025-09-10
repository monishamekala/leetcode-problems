class solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        mid = self.getMid(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = None
        while head and head.next:
            slow = head if not slow else slow.next
            head = head.next.next

        mid = slow.next
        slow.next = None

        return mid

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next
