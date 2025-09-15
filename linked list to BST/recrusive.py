class solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevPtr = None
        slow = head
        fast = head

        while fast and fast.next:
            prevPtr = slow
            slow = slow.next
            fast = fast.next.next

        if prevPtr:
            prevPtr.next = None

        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        mid = self.findMid(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node