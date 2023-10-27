# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head.next
        while head.next:
            tmp = head.next
            head.next = head.next.next
            head = tmp.next
            head = head.next.next
        return dummy