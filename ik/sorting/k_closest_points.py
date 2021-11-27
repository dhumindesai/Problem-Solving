from heapq import *


def nearest_neighbours(p_x, p_y, k, n_points):
    def calc_distance(point):
        x = point[0]
        y = point[1]

        return 0.0 + ((p_x - x) ** 2 + (p_y - y) ** 2) ** 0.5

    max_heap = []  # []

    # init the heap with k points
    for i in range(k):  # i=0
        point = n_points[i]  # (1,1)
        distance = calc_distance(point)
        heappush(max_heap, (-distance, point[0], point[1]))

    for i in range(k, len(n_points)):
        point = n_points[i]
        distance = calc_distance(point)

        if distance < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-distance, point[0], point[1]))

    result = []
    for d, x, y in max_heap:
        result.append([x, y])

    return result

print(nearest_neighbours(1,1,1,[[0,0],[1,0]]))