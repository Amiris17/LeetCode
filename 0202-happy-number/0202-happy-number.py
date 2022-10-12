class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
       
        def get_next(n):
            happy=0
            num_list=[]
            while n:
                single_int=n%10
                #num_list.append(single_int)
                n=n/10
                happy+=(single_int)**2
            return happy
         
        fin=set()
        while n!=1 and n not in fin:
            fin.add(n)
            n=get_next(n)
        
        return n==1