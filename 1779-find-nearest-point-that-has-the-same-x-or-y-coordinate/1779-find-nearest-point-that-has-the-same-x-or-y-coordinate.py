class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        bestD=10**4
        besti=-1
        
        
        for i,(x1,y1) in enumerate(points):
            if x==x1 or y==y1:
                dist=abs(x-x1)+abs(y-y1)
                
                if dist<bestD:
                    besti=i
                    bestD=dist
                    
        return besti
        
        
        
            
            
        
            