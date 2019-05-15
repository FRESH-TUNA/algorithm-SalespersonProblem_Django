import search

if __name__ == '__main__':
    tsp = search.TSP()
    tsp.travel()
    print(tsp.bestTour, tsp.bestLength)
