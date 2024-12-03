from typing import List
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

    def find_weigth(self, coordinate1, coordinate2):
        coordinate_x = abs(coordinate1[0] - coordinate2[0])
        coordinate_y = abs(coordinate1[1] - coordinate2[1])
        return coordinate_x + coordinate_y

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        len_points = len(points)
        graph = Graph(len_points)
        count = 0
        for i in points:
            j = count + 1
            while j < len_points:
                weight = self.find_weigth(points[count], points[j])
                graph.add_no(count, (j, weight))
                graph.add_no(j,(count, weight))
                j +=1
            count +=1
        r = self.prim(0,graph)
        return r

    def prim(self, source, graph):  
        heap =  [(0, source)]
        visit = [0 for _ in range(len(graph._nodes))]
        final_res = 0
        while heap:
            current_visit, node = heappop(heap)
            if not visit[node]:
                visit[node] = 1
                final_res += current_visit
                for neighbor, weight in graph._nodes[node]._neighbors:
                    heappush(heap, (weight, neighbor))
        return final_res
    
