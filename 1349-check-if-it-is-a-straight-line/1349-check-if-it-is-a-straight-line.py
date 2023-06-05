class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        x1,y1,x2,y2=coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1]
        
        for x,y in coordinates:
            if (y2-y)*(x1-x) != (y1-y)*(x2-x):
                return False
        return True

