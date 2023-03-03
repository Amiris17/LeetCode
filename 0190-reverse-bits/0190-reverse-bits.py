class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        #so in order to solve this problem we basically just need to reverse the numbers in hte problem NOT FLIP REVERSE
        #so we need to start from the right AND keep shifting and adding it and then return the ACTUAL integer.
        
        
        final=0
        
        for i in range(32):#0-31 =32 bits
            bit_val=(n>>i) &1 #we and it so we can know if its 0 or 1 for our final value
            final=final|(bit_val<<(31-i)) #got this line from neetcode extremely clever
        return final