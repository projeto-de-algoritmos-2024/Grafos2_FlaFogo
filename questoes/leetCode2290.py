from typing import List,Tuple
from heapq import heappop, heappush

class No:
    def __init__(self, number, neighbors= None ) -> None:
        """Cria um no, colocando o seu numero e os seus vizinhos""" 
        self._number = number
        # neighbors é uma lista de tuplas
        self._neighbors =[]

class Graph:
    def __init__(self, n) -> None:
        """Cria a lista de adjacência""" 
        self._nodes = [No(i) for i in range(n)]
     
    def add_no(self,number,path):
       """Adiciona no em uma lista de adjacencia especifica"""
       self._nodes[number]._neighbors.append(path)

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        graph = Graph(sum(map(len, grid)))
        self.build_graph(grid,(len(grid), len(grid[0])),graph)
        return (self.dijkstra(0,graph))
        # self.analyze(graph)

    def build_graph(self, grid, limit_grid, graph ):
        line = 0
        column = 0
        for line_ in grid:
            for column_ in line_:
                if(column + 1 < limit_grid[1]):
                    number = limit_grid[1]*line + column
                    graph.add_no(number,(number + 1, grid[line][column + 1]))
                    graph.add_no(number + 1, (number, grid[line][column]))
                
                if(line + 1 < limit_grid[0]):
                    number = limit_grid[1]*line + column
                    graph.add_no(number,(number + limit_grid[1] ,grid[line + 1][column]))
                    graph.add_no(number + + limit_grid[1],(number ,grid[line][column]))
                column +=1 
                
                
            line +=1
            column = 0
                    

    # def analyze(self, graph):
    #     for i in graph._nodes:
    #         print(f"No {i._number}")
    #         for j in i._neighbors:
    #             print(j, end = ' ')
    #         print()

    def dijkstra(self, source, graph):   
        heap =  [(0, source)]
        dist = [float('inf') for _ in range(len(graph._nodes))]

        while heap:
            current_dist, node = heappop(heap)
            if dist[node] > current_dist:
                dist[node] = current_dist
                for neighbor, weight in graph._nodes[node]._neighbors:
                    heappush(heap, (weight + current_dist, neighbor))
        
        return dist[len(graph._nodes)-1]

# teste = Solution()
# teste.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])
# print(teste.analyze())
