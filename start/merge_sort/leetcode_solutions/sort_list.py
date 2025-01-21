# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid_node = self.get_middle(head)
        head_right = mid_node.next
        mid_node.next = None
        
        left = self.sortList(head)
        right = self.sortList(head_right)
        return self.merge(left, right)    
    
    
    def get_middle(node):
        slow, fast = node, node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(l1, l2):
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
        
        if l1:
            current.next = l1
        
        if l2:
            current.next = l2
        
        return dummy.next