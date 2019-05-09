import sys, copy
class roads:
    def __init__(self):
         self.city = [
             '서울', '인천', '대구', '인천',
             '대전', '광주', '울산', '세종'
         ]
         self.weight = [
            [0, 14, 4, 10, 20, 46, 4, 1],
            [14, 0, 1, 8, 7, 2, 9, 1],
            [4, 5, 0, 7, 16, 2, 1, 10],
            [1, 7, 9, 0, 2, 12, 6, 10],
            [18, 7, 17, 4, 0, 1, 11, 5],
            [1, 2, 7, 1, 3, 1, 10, 5],
            [1, 4, 4, 3, 1, 8, 1, 2],
            [3, 1, 1, 2, 0, 7, 9, 8],
         ]
         self.tour = [0] * len(self.city)
         self.bestLength = sys.maxsize
         self.bestTour = None
            
    def promising(self, index):
        if self.calcLength(index) < self.bestLength:
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
    
    def calcLength(self, last):
        totalLength = 0
        prev = self.tour[0]
        i = 1
        while i < last:
            totalLength = totalLength + self.weight[prev][self.tour[i]]
            prev = self.tour[i]
            i = i + 1
        return totalLength
    
    def travel(self, index):
        if index == len(self.city) - 1:
            currentPos = self.tour[index]
            resultLength = self.calcLength(len(self.tour)) + self.weight[currentPos][0]
            if resultLength < self.bestLength:
                self.bestLength = resultLength
                self.bestTour = copy.deepcopy(self.tour)
                return
        if not self.promising(index):
            return
        for cityIndex in range(len(self.city)):
            if not self.visited(index, cityIndex):
                self.tour[index + 1] = cityIndex
                self.travel(index + 1)
    


  

            
        

