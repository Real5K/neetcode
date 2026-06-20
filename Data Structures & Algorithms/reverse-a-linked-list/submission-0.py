# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        while curr is not None:
            l.append(curr.val)
            curr = curr.next

        l.reverse()
        if len(l) == 0:
            return None

        h = ListNode(l[0])
        c = h
        for val in l[1:]:
            c.next = ListNode(val)
            c = c.next

        return h

