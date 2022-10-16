class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        Capital_A=65
        lowercase_a=97
        
        temp=0
        resulting_string=""
        special_chars="!@#$%^&*_+-=:;'/.,<>'"
        
        for i in s:
            
            # add 32 to capital_a and increase it by 1 iteration as well as lowercase_a everytime because if we get 32 then ew can just add capital to 32 and ord it
            
            #lets check if its capital first:
            
            if 65<=ord(i)<=90:
                #then we know its already uppercase
                temp=ord(i)+32
                resulting_string+=chr(temp)
                
                
                
           
            
            else:
            
                resulting_string+=i
            
                
            
            
        return resulting_string
                
                 
            
            
            
            