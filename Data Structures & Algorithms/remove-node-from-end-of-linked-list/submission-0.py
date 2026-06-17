# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev_head = self.reverseLinkedList(head)
        # print(reveresed_head.val)
        # Use a dummy node to elegantly handle deleting the first element
        dummy = ListNode(0, rev_head)
        curr = dummy
        counter = 1

        # Traverse until we are standing right BEFORE the node to delete
        while curr.next:
            if counter == n:
                curr.next = curr.next.next  # Bypass/Delete the node
                break
            curr = curr.next
            counter += 1
        # Reverse back to restore original order
        return self.reverseLinkedList(dummy.next)

    def reverseLinkedList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        curr = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev