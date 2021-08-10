'''
Problem Statement #
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.


Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.


Time complexity #
As we are iterating through both the lists once, the time complexity of the above algorithm is O(N + M)O(N+M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.

Space complexity #
Ignoring the space needed for the result list, the algorithm runs in constant space O(1)O(1).
'''
# def is_overlap(int1, int2):
#     if int1[0] >= int2[0] and int1[0] <= int2[1]:
#         return True
#     if int2[0] >= int1[0] and int2[0] <= int1[1]:
#         return True
#
#
# def find_intersection(int1, int2):
#     return [max(int1[0], int2[0]), min(int1[1], int2[1])]
#
#
# def merge(intervals_a, intervals_b):
#     result = []
#     first, second = 0, 0
#
#     while first < len(intervals_a) and second < len(intervals_b):
#         if is_overlap(intervals_a[first], intervals_b[second]):
#             result.append(find_intersection(intervals_a[first], intervals_b[second]))
#
#         if intervals_a[first][1] <= intervals_b[second][1]:
#             first += 1
#         else:
#             second += 1
#     return result
def merge(firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """

    def is_conflict(interval_1, interval_2):
        if interval_2[0] >= interval_1[0] and interval_2[0] <= interval_1[1]:
            return True
        if interval_1[0] >= interval_2[0] and interval_1[0] <= interval_2[1]:
            return True
        return False

    result = []
    i = 0
    j = 0

    while i < len(firstList) and j < len(secondList):
        s1, e1 = firstList[i][0], firstList[i][1]
        s2, e2 = secondList[j][0], secondList[j][1]

        if (is_conflict([s1, e1], [s2, e2])):
            result.append([max(s1, s2), min(e1, e2)])

        if e1 <= e2:
            i += 1
        else:
            j += 1

    return result


def main():
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
    print("Intervals Intersection: " + str(merge([[4,6],[7,8],[10,17]], [[5, 10]])))


main()
