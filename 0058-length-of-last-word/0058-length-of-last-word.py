class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        #We could use regex and get the last use of the space.
        new_str=s.split()[-1]
        
        return len(new_str)