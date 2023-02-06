class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        #THIS PROBLEM USES KADANES ALGOROITHM OR DYNAMIC PROGRMAMING AND WE CAN ALSO BRUTE FORCE IT WITH QUADRATIC TIME COMPLEXITY
        
        max_sum=nums[0] #We want to start with the first index so that we can keep comparing
    
        
        
        temp=0
        final=0
        
       
    
        for i in range(1,len(nums)):
            
            nums[i]=max(nums[i],nums[i]+nums[i-1])
            max_sum=max(max_sum,nums[i])
            
        return max_sum
                    