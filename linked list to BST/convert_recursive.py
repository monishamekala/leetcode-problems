class Solution:
    def convertToArray(self, head: ListNode) -> list:
        ll = head
        values = list()

        while ll:
            values.append(ll.val)
            ll = ll.next

        return values

    def sortToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        values = self.convertToArray(head)

        return toBST(0, len(values))

        def toBST(l: int, r:int) -> TreeNode:
            if l > r:
                return None

            mid = (l + r) // 2

            node = TreeNode(values[mid])

            if l == r:
                return node

            node.left = toBST(l, mid - 1)
            node.right = toBST(mid + 1, r)

            return node

