class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        
        
        
        counter = [0]
        for i in range(1, n+1):
            
            #remember in math that even numbers are 2n and odd numbers are 2n+1
            #this is the same principle applied as rshifting is the same /2 and adding the i %2 is the +1 or 0
            counter.append(counter[i >> 1] + i %2 )
        return counter