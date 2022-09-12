# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=head #so that we can get the size without messing up the original 
        prev=None
        count=0
        place_holder=0
        Middle=ListNode()#rtype Lnode
        #getSize
        while dummy:
            prev=dummy.val #value at head
            dummy=dummy.next
            count+=1
            
            
        while head:
            curr=head.val
         
            
            
            if place_holder==(count/2): 
                return head
            if place_holder==round(float(count/2)):
                print(place_holder)
                return curr
            head=head.next
            place_holder+=1
        
        
            