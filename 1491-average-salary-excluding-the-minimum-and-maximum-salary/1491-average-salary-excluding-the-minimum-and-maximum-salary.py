class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        minimum=min(salary)
        maximum=max(salary)
        
        
        salary.remove(minimum)
        salary.remove(maximum)
        
        
        result=0
        count=0
        for i in salary:
            result+=i
            count+=1
        return (result/count)