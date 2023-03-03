class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        temp_bin=0
        
        count=0
        
        list1=[]
        
        
        # 1. we need to iterate through the range and find the correspondent binary number,then once we do this we can count the number of 1's. This sounds like a dictionary problem, were restricted to list however,and remember we need to count the number of 1's in this binary make it a list.
        for i in range((n+1)):
            
            temp_bin=bin(i)
            temp_bin=temp_bin[2:] #here we have the binary number
            count=0
            
            for j in str(temp_bin):
        
                if j =="1":
                    count+=1
            list1.append(count)
            
        
                
                
        return list1
    
          
    
    
    #time_complex=0(n^2)
    
    #memory o(n)