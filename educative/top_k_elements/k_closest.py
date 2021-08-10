from heapq import *

def kClosest(points, k):
    def calculate_distance(point):
        return point[0] ** 2 + point[1] ** 2

    max_heap = []

    for i in range(k):
        heappush(max_heap, (-calculate_distance(points[i]), i))

    for i in range(k, len(points)):
        dist = calculate_distance(points[i])
        if dist < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-dist, i))

    result = []
    for _ in range(k):
        i = heappop(max_heap)[1]
        result.append(points[i])

    return result

print(kClosest([[3,3],[5,-1],[-2,4]], 2))