class Solution(object):
    def twoSum(self,numbers,target):
        
        
        hash_={}
        for i in range(len(numbers)):
            if target-numbers[i] in hash_:
                return [hash_[target-numbers[i]],i]
            hash_[numbers[i]]=i
        return [-1,-1]
            
            
            
            
      
