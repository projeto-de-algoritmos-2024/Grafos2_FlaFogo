from heapq import heappop, heappush
from typing import List, Tuple

class No:
    def __init__(self, number, neighbors= None ) -> None:
        """Cria um no, colocando o seu numero e os seus vizinhos""" 
        self._number = number
        # neighbors é uma lista de tuplas
        self._neighbors =[]

class Graph:
    def __init__(self, n, neighbors) -> None:
        """Cria a lista de adjacência""" 
        self._nodes = [No(i) for i in range(n)]
        self.add_neighbors(neighbors)

    def add_neighbors(self, neighbors):
        """Adiciona os vizinhos de um no com o seus respectivos pesos""" 
        for neighbor in neighbors:
            goal= (neighbor[1],neighbor[2])
            back= (neighbor[0],neighbor[2])
            self._nodes[neighbor[0]]._neighbors.append(goal)
            self._nodes[neighbor[1]]._neighbors.append(back)
        
    def add_no(self,path):
       """Adiciona no em uma lista de adjacencia especifica"""
       self._nodes[path[0]]._neighbors.append(path[1])


class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        graph = Graph(n, edges)
        dist1 = self.dijkstra(0, graph) # Menor distancia de 0 para os n-1 nos
        dist2 = self.dijkstra(n-1, graph) # Menor distancia de n-1 para todos
                                          # os nos
        less_dist = dist2[0]
        if less_dist == float('inf'):
            return [False] * len(edges)

        answer = []

        for a, b, weight in edges:
            if((dist1[a] + weight+ dist2[b]) == less_dist
               or dist2[a] + dist1[b] + weight == less_dist):
                answer.append(True)
            else:
                answer.append(False)
        return answer


    def dijkstra(self, source, graph):   
        heap =  [(0, source)]
        dist = [float('inf') for _ in range(len(graph._nodes))]

        while heap:
            current_dist, node = heappop(heap)
            if dist[node] > current_dist:
                dist[node] = current_dist
                for neighbor, weight in graph._nodes[node]._neighbors:
                    heappush(heap, (weight + current_dist, neighbor))
        return dist