import sys, copy
class roads:
    def __init__(self):
         self.city = [
             '서울', '인천', '대구', '인천',
             '대전', '광주', '울산', '세종',
             '강릉', '춘천', '원주', '속초',
             '양양', '철원', '순천', '전주',
             '남양주', '영덕', '울진', '제주시',
         ]
         self.weight = [
            [0, 14, 4, 10, 20, 46, 4, 1, 43, 21, 12, 34, 53, 23, 52,13, 2, 1, 23, 13],
            [14, 0, 1, 8, 7, 2, 9, 1, 43, 12, 123, 123, 42, 234, 12, 132, 64, 34, 23, 1],
            [4, 5, 0, 7, 16, 2, 1, 10, 76, 73, 30, 82, 86, 68, 22, 99, 42, 88, 90, 65],
            [1, 7, 9, 0, 2, 12, 6, 10, 13, 1, 1, 5, 3, 2, 1, 56, 23, 45, 2, 2],
            [18, 7, 17, 4, 0, 1, 11, 5, 13, 2, 14, 35, 53, 72, 41, 56, 33, 5, 2, 2],
             
            [1, 2, 7, 1, 3, 0, 10, 5, 13, 6, 1, 5, 3, 1, 1, 1, 22, 43, 1, 1],
            [1, 4, 4, 3, 1, 8, 0, 2, 134, 36, 34, 52, 13, 12, 14, 6, 2, 5, 9, 2],
            [3, 1, 1, 2, 0, 7, 9, 0, 1, 69, 5, 5, 55, 22, 11, 56, 23, 45, 2, 2],
            [1, 14, 4, 10, 20, 46, 4, 1, 0, 6, 11, 555, 33, 21, 10, 56, 23, 45, 2, 2],
            [14, 0, 1, 8, 7, 2, 9, 1, 10, 0, 89, 51, 38, 20, 10, 6, 923, 5, 1, 1],
             
            [4, 5, 0, 7, 16, 2, 1, 10, 11, 60, 0, 45, 33, 1, 44, 55, 88, 11, 11, 21],
            [1, 7, 9, 0, 2, 12, 6, 10, 10, 16, 6, 0, 1, 4, 100, 6, 3, 5, 12, 12],
            [18, 7, 17, 4, 0, 1, 11, 5, 3, 6, 8, 7, 0, 4, 3, 5, 33, 40, 20, 1],
            [1, 2, 7, 1, 3, 1, 10, 5, 3, 9, 1, 2, 3, 0, 7, 1, 93, 15, 62, 22],
            [1, 4, 4, 3, 1, 8, 1, 2, 4, 60, 2, 50, 3, 22, 0, 77, 40, 41, 21, 2],
             
            [3, 1, 1, 2, 0, 7, 9, 8, 12, 6, 100, 25, 33, 42, 51, 0, 3, 1, 12, 20],
            [18, 7, 17, 4, 0, 1, 11, 5, 13, 66, 1, 1, 3, 2, 1, 56, 0, 45, 2, 2],
            [1, 2, 7, 1, 3, 1, 10, 5, 40, 60, 10, 50, 13, 32, 91, 73, 1, 0, 19, 12],
            [1, 4, 4, 3, 1, 8, 1, 2, 14, 16, 1, 85, 33, 82, 13, 65, 45, 23, 0, 9],
            [3, 1, 1, 2, 0, 7, 9, 8, 1, 62, 10, 25, 37, 72, 41, 12, 23, 45, 9, 0],
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
    


  

            
        

