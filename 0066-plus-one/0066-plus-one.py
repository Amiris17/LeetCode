class Solution(object):
    def plusOne(self, digits):
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        #one plan take out integers and add then split them by commas again and make a list
        
        
        num=""
        for i in digits:
            num+=str(i)
        #print(num) #got it to str
              
        int_num=int(num)
        int_num+=1
        
        #print(int_num)#adds perfectly
        
        
        list_nums= map(int,str(int_num)) #array of chars ,map requires two arguments its like a for loop that does a function on the iterables str being the iterable here and we want integer as a return from the list int_num
        
        return list_nums