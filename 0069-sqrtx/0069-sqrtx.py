class Solution(object):
    def mySqrt(self, x):
        
        """
        :type x: int
        :rtype: int
        """
        if x==1 or x==0:
            return x
        
        temp = 1
        prev=0
        HIGH=x #thisll be the original number and we keep checking to see if the number were using atm is > than the squared number or = to it if it is we return the lower number or the number itself
        
        
        
        while x:
            if temp*temp>HIGH: #so if the number we are at squared is greater than the number we are looking for return the previous number
                break
            prev=temp
            temp+=1
        return prev
        
                
            
            
   
        
        
                
      
    #TRIED using newtons method
    # i tried having a guess and divi
    