class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
      
        #Two methods make a set and just compare statement with length.
        
        #second create a hash and just false if its ever added
        
        dup_list={}
        
        
        for i in nums:
            if i not in dup_list:
                dup_list[i]=i
            else:
                return True
        return False
            
            