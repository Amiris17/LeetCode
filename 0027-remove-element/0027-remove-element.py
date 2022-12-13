class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        for x in nums:
            if x!=val:
                nums[i]=x
                i+=1
        return i 
    
    
    #This problem is really bad theyu wanted like a boolean value at first then this problem got changed now they just want u to modify it in place.
    
    #Thought Process: if the number is not equal to the value were trying to remove 