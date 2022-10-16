class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        resulting_str=[]
        i=0
        while i<len(s):
            if i+2 <len(s) and s[i+2]=="#":
                val=int(s[i: i+2])    #making the hash tag number a chracter and then just storing it at and adding it and getting its ascii value
                resulting_str.append(chr(val+96))# its +96 cause character is from 1-9 lol...
                i+=3
            else:
                resulting_str.append(chr(int(s[i])+96))
                i+=1
        
        return "".join(resulting_str)
        
        
        
        
        
            