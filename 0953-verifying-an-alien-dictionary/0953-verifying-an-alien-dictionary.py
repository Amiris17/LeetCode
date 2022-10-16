class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        #were given a order..
        
        
        # So lesson learned you can apparently just map this and compare the numbers between the numbers in the order list
        #You want to find the first character that doesnt match and compare it with the numbers in order idx and verify if the letters are where they are supposed to be based on the number idx in order
        
        
        order_idx={c:i for i,c in enumerate(order)}
        
        
        
        for i in range(len(words)-1):
            word1,word2=words[i],words[i+1]
            for j in range(len(word1)): #looping thorugh first words and stumbling upon 
                if j==len(word2):
                    return False
                if word1[j]!=word2[j]:
                    if order_idx[word2[j]]<order_idx[word1[j]]:
                        return False
                    break    #You basically want to continue comparing eachnletter since we already have the condition if they differ
                
        return True
            
            
        # we can use enmuerate to iterate over the order and then store the index of each letter and compare the numerical values and return True if s[0] <s[i] etc.. 
        # I had right idea just didnt know how to implement this is a really good problem
        
        
        
                                    