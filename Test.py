import unittest
from Graph import *


class Test1(unittest.TestCase):
    def test1(self):
        graph = create_graph('wed1.txt')
        all_v = all_vertex('wed1.txt')
        first_graph = graph.bfs(all_v[0])
        second_graph = create_second_graph(all_v, first_graph)
        couple_count(first_graph, second_graph)
        self.assertEqual(couple_count(first_graph, second_graph), 6)


class Test2(unittest.TestCase):
    def test2(self):
        graph = create_graph('wed2.txt')
        all_v = all_vertex('wed2.txt')
        first_graph = graph.bfs(all_v[0])
        second_graph = create_second_graph(all_v, first_graph)
        couple_count(first_graph, second_graph)
        self.assertEqual(couple_count(first_graph, second_graph), 4)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(Test1())
    runner.run(Test2())
