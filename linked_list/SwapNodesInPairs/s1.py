from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(f"val = {self.val}, next = {self.next.val}")
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(None, head) # dummy의 next에 head 처리하기
    prev, cur = dummy, head
    while cur and cur.next:
        prev.next = cur.next # prev, cur의 각자 next를 하나씩 바꿔준다.
        cur.next = cur.next.next # 3개 까지 본다. prev, cur과 차이 2
        prev.next.next = cur
        prev, cur = cur, cur.next
    return dummy.next