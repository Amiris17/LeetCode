class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp=dict()
        
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        
        
        
        for key,value in mp.items():
            if value ==1:
                return key
            
            