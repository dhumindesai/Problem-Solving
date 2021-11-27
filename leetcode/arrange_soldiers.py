'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:       i = 0 []
combination = [] i=1, [2], i=1
Input: rating = [2,5,3,4,1]
                 0 1 2 3 4
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4
Explanation: We can form three teams given the conditions. (1,2,3), (1,3,4), (1,2,4), (2, 3, 4). 

global count = 0

 i = 0 []
 i=1 [2]                 i=1[]
 i=2 [2,5], i=2[2]       i=2[5] i=2[]
 i=3 [2,5,3], i=2 [2]
'''


def is_valid(combination):
    if combination[0] < combination[1] < combination[2]:
        return True
    if combination[0] > combination[1] > combination[2]:
        return True
    return False


def soldier_combination(ratings):
    result = [0]

    def helper(i, combination):
        # base
        if len(combination) == 3:
            if is_valid(combination):
                print(combination)
                result[0] += 1
            return
        if i == len(ratings):
            return

        # recursive

        #include
        combination.append(ratings[i])
        helper(i + 1, combination)
        combination.pop()

        # exclude
        helper(i + 1, combination)

    helper(0, [])
    return result[0]


print(soldier_combination([2,5,3,4,1]))
print(soldier_combination([2,1,3]))
print(soldier_combination([1,2,3,4]))


