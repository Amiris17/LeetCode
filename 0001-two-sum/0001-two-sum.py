class Solution(object):
    def twoSum(self,numbers,target):
        hash_table={}
        for i,n in enumerate(numbers):
            complement=target-n
            if complement in hash_table:
                return [hash_table[complement],i]
            hash_table[n]=i
      
