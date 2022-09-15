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
                
                #pushing opening down 
                
            elif stack_list and dict1[s[i]]==stack_list[-1]: # stack_list checks to make sure the stakc isnt empty and dict[s[i]] is just looking up to match the parentheses we also have the parenthese in reverse order due to the fact that stacwks are naturally lifo and we are mathcing opposites.

                stack_list.pop()
            
            
            else:
                return False
            
        return stack_list==[]