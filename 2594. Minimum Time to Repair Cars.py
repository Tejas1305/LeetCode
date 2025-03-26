class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        
        left, right = 1, min(ranks) * (cars ** 2)
        def canrepairintime(mid):
            total_cars = 0

            for r in ranks:
                total_cars+=int(math.sqrt(mid//r))
                if total_cars>=cars:
                    return True
            return False
        
    
        while left < right:
            mid = (left + right)//2
            if canrepairintime(mid):
                right =mid
            else:
                left = mid+1

        return left
        
