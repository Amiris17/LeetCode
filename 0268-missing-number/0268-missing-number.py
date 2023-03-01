class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
             
        length=len(nums)
        

        nums.sort()
        
        print(nums)
        
        for i,n in enumerate((nums)):
            
            if i!=n:
                return i
        return i+1
            
            
            
        
        
        