# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        #we create a dummy variable temp, which allows us to traverse through the linked list and allow us to return HEAD to get the entirety of the lsit after altering it.
        
        #the basic idea is while the value we are at is not NULL and the next value is not null
        #if the current value is =next val
        #SKIP that value 
        
        temp=head
        prev=0
        
        while temp!=None and temp.next!=None:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        
                
        return head 