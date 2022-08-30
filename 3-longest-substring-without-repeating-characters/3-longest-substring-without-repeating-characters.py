class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dictionary={}
        res=0
        i=0
        for j in range(0,len(s)):
            if s[j] in dictionary:
                i=max(i,dictionary[s[j]]+1)
            res=max((res,(j-i+1))) #we takle max because we are constnatly checking the next value to see if it is a dup or not an subtracting so we take max of this
            dictionary[s[j]]=j
        return res