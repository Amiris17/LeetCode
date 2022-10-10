class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #count_bit_holder=0#were gonna update this by one everytime we encounter a 1 so that we can do 2^count_bit_holder
        # we need the length of n
        
        #this idea would have worked but for some reason the input isnt really being read properly so we hjad to goggle bthe bit manipulation.
        #tldr anding and n-1 the amount of times that and occurs will show how many 1s are in the integer
        bit_count=0
        while n>0:
            n=n&(n-1)
            bit_count+=1
        
        return bit_count