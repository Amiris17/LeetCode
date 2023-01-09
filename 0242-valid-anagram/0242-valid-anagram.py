class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        
        #create a hash table and if each word is of equal letter usage. then return True return statement betwene two of em
        
        
        
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in dict2:
                dict2[t[i]]=1
            else:
                dict2[t[i]]+=1
        
        
        return dict1==dict2