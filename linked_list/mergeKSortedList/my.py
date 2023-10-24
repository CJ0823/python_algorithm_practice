# Definition for singly-linked list.
import sys
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # list of heads
        dummy = ListNode()
        value = sys.maxsize
        for idx, head in enumerate(lists):
            if head.val < value:
                value = head.val
                dummy.next = head
        # compare heads