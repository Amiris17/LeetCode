class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        arr_b = [(bin(n)[2:].count('1'), len(bin(n)[2:]),n) for n in arr]
        arr_b.sort()
        return [n[2] for n in arr_b]
        
        #Lets get a dictionary and store the number of 1s each has a nd then sort it like that 
        
        #for idx,stuff in enumerate(arr):
            #val=bin(stuff)
            #binary_list.append(val[2:])
            
        