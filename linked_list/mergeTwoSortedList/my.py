# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    dummy.next = list1
                    dummy = dummy.next
                    list1 = list1.next
                else:
                    dummy.next = list2
                    dummy = dummy.next
                    list2 = list2.next
            elif not list1:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            elif not list2:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            else:
                return
        return head.next
