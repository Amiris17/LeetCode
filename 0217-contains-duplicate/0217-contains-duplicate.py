class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
      
        #Two methods make a set and just compare statement with length.
        
        #second create a hash and just false if its ever added
        
        set1=set(nums)
        
        return len(set1)!=len(nums)
            
            
            