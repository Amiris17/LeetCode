class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        customers=len(accounts)
        banks=len(accounts[0])
        max_sum=0
        
        for i in range(customers):
            sumz=0
            for j in range(banks):
                sumz+=accounts[i][j]
                
                if sumz>max_sum:
                    max_sum=sumz
                    
        return max_sum