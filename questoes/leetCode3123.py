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

    def print_graph(self):
            """Imprime cada nó do grafo e suas arestas com os pesos"""
            for node in self._nodes:
                print(f"Nó {node._number}:")
                for neighbor in node._neighbors:
                    print(f"  -> Vizinhos: {neighbor[0]} com peso {neighbor[1]}")

class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        graph = Graph(n, edges)

# graph  = Graph(6,[[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]])

# graph.print_graph()