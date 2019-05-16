import sys
from queue import PriorityQueue

class Tour:
    def __init__(self, level=None, path=None, bound=0):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return (self.bound < other.bound)

class TSP:
    tour = Tour()
    bestTour = []
    bestLength = sys.maxsize

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

    def travel(self):
        queue = PriorityQueue()

        newTour = Tour(0, [0])
    
        queue.put(newTour)

        while not queue.empty():
            newTour = queue.get()
            if newTour.bound < self.bestLength:
                self.tour.level = newTour.level + 1
                for i in filter(lambda x: x not in newTour.path, range(1, len(self.city))):
                    self.tour.path = newTour.path[:]
                    self.tour.path.append(i)
                    if self.tour.level == len(self.city) - 2:
                        l = set(range(1, len(self.city))) - set(self.tour.path)
                        self.tour.path.append(list(l)[0])
                        self.tour.path.append(0)

                        if self.length(self.tour) < self.bestLength:
                            self.bestLength = self.length(self.tour)
                            self.bestTour = self.tour.path[:]
                    else:
                        self.tour.bound = self.bound(self.tour)
                        if self.tour.bound < self.bestLength:
                            queue.put(self.tour)

                    self.tour = Tour(level=self.tour.level)


    def length(self, tour):
        result = 0
        for i in range(len(tour.path) - 1):
            result = result + self.weight[tour.path[i]][tour.path[i + 1]]
        return result
        


    def bound(self, node):
        bound = 0
        n = len(self.city)
        for i in range(len(node.path) - 1):
            bound += self.weight[node.path[i]][node.path[i + 1]]
        return bound


