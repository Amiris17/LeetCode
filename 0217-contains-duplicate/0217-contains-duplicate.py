class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
      
        #Two methods make a set and just compare statement with length.
        
        #second create a hash and just True if its ever added more than once
        
        dup_list={}
            
            
        for i in range(len(nums)):
            if nums[i] not in dup_list:
                dup_list[nums[i]]=1
            else:
                return True
                
        return False