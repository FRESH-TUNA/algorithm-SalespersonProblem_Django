import sys, copy
class roads:
    def __init__(self):
         self.city = [
             '서울', '인천', '대구', '인천',
             '대전', '광주', '울산', '세종'
         ]
         self.weight = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
         ]
         self.tour = [] * len(self.city)
         self.bestLength = sys.maxsize
         self.bestTour = None
    
    def travel(self, index):
        if index == len(self.city) - 1:
            currentPos = self.tour[index]
            resultLength = calcLength(len(self.tour)) + self.weight[currentPos][0]
            if resultLength < self.bestLength:
                self.bestLength = resultLength
                self.bestTour = copy.deepcopy(self.tour)
                return
        if not promising():
            return
        for cityIndex in range(len(city)):
            if not visited(index, cityIndex):
                self.tour[index + 1] = cityIndex
                travel(index + 1)
    
    def calcLength(self, last):
        totalLength = 0
        prev = self.tour[0]
        i = 1
        while i < last:
            totalLength = totalLength + self.weight[prev][self.tour[i]]
            prev = self.tour[i]
            i = i + 1
        return totalLength

    def promising(self, index):
        if calcLength(index) > self.bestLength:
            return True
        else:
            return False

    def visited(self, last, cityIndex):
        i = 0
        while i <= last:
            if self.tour[i] == cityIndex:
                return True
            i = i + 1
        return False

            
        

