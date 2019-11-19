from collections import defaultdict


class Graph:

    def __init__(self, count):
        self.count = count
        self.graph = defaultdict(list)

    def __del_(self):
        pass

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, node):
        first_graph = [node]
        visited = []
        queue = [node]
        while queue:
            vertex = queue.pop()
            for w in self.graph[vertex]:
                if w not in visited:
                    visited.append(w)
                    queue.append(w)
                    if w not in first_graph:
                        first_graph.append(w)
        return first_graph


def create_graph(file_name):
    with open(file_name) as file:
        num = file.readline()
        graph = Graph(int(num))
        for line in file.readlines():
            edge = line.split(" ")
            u = int(edge[0])
            v = int(edge[1])
            graph.add_edge(u, v)
    return graph


def all_vertex(file_name):
    all_v = []
    with open(file_name) as file:
        file.readline()
        for line in file.readlines():
            edge = line.split(" ")
            all_v.append(int(edge[0]))
            all_v.append(int(edge[1]))
    return all_v


def create_second_graph(all_vertex, first_graph):
    second_g = []
    for i in range(len(all_vertex)):
        if all_vertex[i] not in first_graph:
            second_g.append(all_vertex[i])
    return second_g


def couple_count(first_g, second_g):
    first_girls, first_boys, second_girls, second_boys = [], [], [], []
    for i in range(len(first_g)):
        if first_g[i] % 2 == 0:
            first_girls.append(first_g[i])
        else:
            first_boys.append(first_g[i])
    for i in range(len(second_g)):
        if second_g[i] % 2 == 0:
            second_girls.append(second_g[i])
        else:
            second_boys.append(second_g[i])
    return len(first_girls) * len(second_boys) + len(first_boys) * len(second_girls)
