class Solution(object):
    def twoSum(self,nums,target):
        
        
        # we only caer about indices
        
        
        beg=0
        end=len(nums)-1
        res=0
        
        
        
        while beg<end:
            if nums[beg]+nums[end]==target:
                return beg,end
            
            end-=1
            
            if beg==end:
                beg+=1
                end=len(nums)-1
    
            
            
            
      
