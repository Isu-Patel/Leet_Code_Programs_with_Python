# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head

        def reverseList(node):
            prev, curr = None, node

            while curr:
                nextTemp = curr.next
                curr.next = prev
                prev = curr
                curr = nextTemp
            return prev

        def helperRemoveNthNode(node):
            count = 1

            while node:
                count += 1
                if count == n:
                    nextTemp = node.next
                    node.next = nextTemp.next
                    node = nextTemp
                    break
                node = node.next
                
        startP = reverseList(temp)
        temp = startP
        helperRemoveNthNode(startP)
        if n == 1:
            temp = temp.next
        ret = reverseList(temp)
        return ret
