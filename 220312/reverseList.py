from typing import Optional

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# 재귀 구조로 뒤집기
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# 반복 구조로 뒤집기
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev