class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n

        result = [[0] * n for i in range(m)]  #creating an empty grid

        for i in range(m):
            for j in range(n):
                oldPos = i * n + j  #finding original flattened position
                newPos = (oldPos + k) % total  #finding shifted position

                newRow = newPos // n
                newCol = newPos % n

                result[newRow][newCol] = grid[i][j]  #placing element in new position

        return result


print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
