class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == "":
            return "-1"
        
        
        lsum=0
        rsum=0
        
        
        
        for i in range(len(nums)):
            lsum+=nums[i]
            rsum=sum(nums[i:])
            
            
            if lsum==rsum:
                return i
        return -1
                
            