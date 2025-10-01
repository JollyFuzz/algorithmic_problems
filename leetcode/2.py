#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        prev_node = None
        extra_rank = 0
        first_node = None
        while n1 or n2 or extra_rank != 0:
            curr_sum = extra_rank
            if n1:
                curr_sum += n1.val            
                n1 = n1.next
            
            if n2:
                curr_sum += n2.val
                n2 = n2.next

            curr_node = ListNode(val=curr_sum % 10)
            extra_rank = curr_sum // 10

            if prev_node:
                prev_node.next = curr_node
            
            if not first_node:
                first_node = curr_node

            prev_node = curr_node

            
        return first_node
        