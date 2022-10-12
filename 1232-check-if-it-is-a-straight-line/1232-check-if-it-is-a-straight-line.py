class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        #were given atleast 2 pairs of coordinates
        
        x1=coordinates[0][0]
        x2=coordinates[1][0]
        
        y1=coordinates[0][1]
        y2=coordinates[1][1]
        
        
        slope_x=x2-x1
        slope_y=y2-y1
        
        for x,y in coordinates:
            if (y2-y)*(x1-x)!=(y1-y)*(x2-x):
                return False
        return True
        
        
        #lets jsut generate more coordinates wit hte slope and check utpo the length if everything is equal
        

            
            
        
            
            