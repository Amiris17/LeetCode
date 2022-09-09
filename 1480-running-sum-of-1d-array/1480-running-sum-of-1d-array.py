class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_sum=0
        
        
        for i in range(len(nums)):
            left_sum+=nums[i]
            #after the first element, the running sum can bne computed normally.
            if i:
                
                nums[i]=left_sum
            
            
                
                
                
    
        return nums
    