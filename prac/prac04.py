class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    # 삽입
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)

lst = [1, 2, 3]
l1 = LinkedList()
for e in lst:
    l1.append(e)
print(l1)