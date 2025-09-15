class Solution:
    def findSize(self, head):
        ptr = head
        c = 0

        while ptr:
            ptr = ptr.next
            c += 1

        return class

    def sortToBST(self, head) -> TreeNode:
        
        size = self.findSize(head)

        def formBST(l, r):
            nonlocal head

            if l > r:
                return None

            mid = (l + r) // 2

            left = formBST(l, mid - 1)

            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = formBST(mid + 1, r)

            return node

        return formBST(0, size - 1)
