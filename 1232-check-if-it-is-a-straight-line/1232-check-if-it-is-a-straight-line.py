from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2 - x1 == 0:
    
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != x1:
                    return False
            return True

        m = (y2 - y1) / (x2 - x1)

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if y != m * (x - x1) + y1:
                return False

        return True
