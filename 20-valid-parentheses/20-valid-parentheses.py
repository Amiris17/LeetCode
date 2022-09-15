class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        top=0
        #use stack
        
        dict1={")":"(","]":"[","}":"{"}
        stack_list=[]
        
        
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[": #open parentheses
                stack_list.append(s[i])
                
            elif stack_list and dict1[s[i]]==stack_list[-1]:
                stack_list.pop()
            
            
            else:
                return False
            
        return stack_list==[]