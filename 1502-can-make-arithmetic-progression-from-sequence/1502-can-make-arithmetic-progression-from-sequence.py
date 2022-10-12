class Solution(object):
    def canMakeArithmeticProgression(self, array):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        array.sort() #sort then subtract values any values that are next to eachotehr and if difference is different than the common i return False   
        
        
        common_difference=array[1]-array[0]
        
        cd_list=[]
        for i in range(len(array)-1):
            compare=array[i+1]-array[i]
            cd_list.append(compare)
            
        cd_list=set(list(cd_list))
        if len(cd_list)>1:
            return False
        
        
        return True
        
        # we can use a set to see if the list will become 1 since sts get rid of distinctive values
        
        
        