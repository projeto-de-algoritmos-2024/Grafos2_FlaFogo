from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        pass

    def dijkstra(self,grid):
        heap = [(0,0)]
        dist = [float('inf') for _ in range(sum(map(len, grid)))]
