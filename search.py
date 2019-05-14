
'''
Travelling Sales Person problem
Bround and bound algorithm
gitHub@MostafaBahri
gitLab@Mostafa_c6
'''
import sys
from utility import Node, PriorityQueue

class TSP:
    def __init__(self):
        self.city = [
            '서울', '인천', '대구', '인천',
            '대전', '광주', '울산', '세종',
            '강릉', '춘천', '원주', '속초',
        ]
        self.weight = [
            [0, 14, 4, 10, 20, 46, 4, 8, 43, 21, 12, 1],
            [14, 0, 1, 8, 7, 2, 9, 10, 43, 12, 13, 123],
            [4, 5, 0, 7, 1, 2, 1, 10, 76, 73, 30, 82],
            [1, 7, 9, 0, 2, 1, 6, 10, 13, 1, 1, 5],
            [18, 7, 17, 1, 0, 1, 11, 5, 13, 2, 14, 35],

            [1, 2, 7, 1, 3, 0, 10, 5, 1, 6, 1, 5],
            [1, 4, 4, 3, 1, 8, 0, 1, 1, 36, 34, 52],
            [3, 1, 1, 2, 90, 7, 9, 0, 1, 69, 5, 5],
            [1, 14, 4, 10, 20, 46, 4, 1, 0, 6, 11, 555],
            [14, 2, 1, 8, 7, 2, 1, 1, 10, 0, 89, 51],

            [4, 5, 1, 7, 16, 2, 1, 10, 11, 1, 0, 45],
            [1, 1, 9, 65, 2, 12, 6, 10, 10, 16, 6, 0],
        ]

    def travel(self, start=0):
        u = Node()
        PQ = PriorityQueue()

        vertex = Node(level=0, path=[0])
        min_length = sys.maxsize
        vertex.bound = self.bound(vertex)
        PQ.put(vertex)

        while not PQ.empty():
            vertex = PQ.get()
            if vertex.bound < min_length:
                u.level = vertex.level + 1
                for i in filter(lambda x: x not in vertex.path, range(1, len(self.city))):
                    u.path = vertex.path[:]
                    u.path.append(i)
                    if u.level == len(self.city) - 2:
                        l = set(range(1, len(self.city))) - set(u.path)
                        u.path.append(list(l)[0])
                        # putting the first vertex at last
                        u.path.append(0)

                        _len = self.length(u)
                        if _len < min_length:
                            min_length = _len
                            optimal_length = _len
                            optimal_tour = u.path[:]

                    else:
                        u.bound = self.bound(u)
                        if u.bound < min_length:
                            PQ.put(u)

                    u = Node(level=u.level)

        # shifting to proper source(start of path)
        optimal_tour_src = optimal_tour
        if start is not 1:
            optimal_tour_src = optimal_tour[:-1]
            y = optimal_tour_src.index(start)
            optimal_tour_src = optimal_tour_src[y:] + optimal_tour_src[:y]
            optimal_tour_src.append(optimal_tour_src[0])

        return optimal_tour_src, optimal_length


    def length(self, node):
        tour = node.path
        # returns the sum of two consecutive elements of tour in adj[i][j]
        return sum([self.weight[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])


    def bound(self, node):
        path = node.path
        _bound = 0

        n = len(self.city)
        determined, last = path[:-1], path[-1]
        # remain is index based
        remain = list(filter(lambda x: x not in path, range(n)))

        # for the edges that are certain
        for i in range(len(path) - 1):
            _bound += self.weight[path[i]][path[i + 1]]

        # for the last item
        _bound += min([self.weight[last][i] for i in remain])

        p = [path[0]] + remain
        # for the undetermined nodes
        for r in remain:
            _bound += min([self.weight[r][i] for i in filter(lambda x: x != r, p)])
        return _bound


