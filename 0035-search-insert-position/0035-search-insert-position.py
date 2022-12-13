class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            for i in range(len(nums)):
                if target<nums[i]:
                    return i 
            return i+1
                    
        for i in range(len(nums)):
            if nums[i]==target:
                return i
         
            
           