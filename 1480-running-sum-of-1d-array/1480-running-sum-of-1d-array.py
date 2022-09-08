class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_sum=nums[0]
        
        
        for i in range(len(nums)):
            
            #we need to replace the i at the index we are at
            if i >0:
                left_sum+=nums[i]
                nums[i]=left_sum
            
            
                
                
                
    
        return nums
    