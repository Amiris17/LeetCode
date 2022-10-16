class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #we can make a set and a list and if the list!= set then we know values appeared twice
        
        
        set1=set(nums)
        
        
        return (len(set1)!=len(nums))
    