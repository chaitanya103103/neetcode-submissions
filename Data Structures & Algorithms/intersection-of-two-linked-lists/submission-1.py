# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curr1 = headA
        curr2 = headB
        l1,l2 = 0,0

        while curr1:
            curr1 = curr1.next
            l1 += 1

        while curr2:
            curr2 = curr2.next
            l2 += 1

        if l1>l2:
            for i in range(l1-l2):
                headA = headA.next
        else:
            for i in range(l2-l1):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            