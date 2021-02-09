'''
Time O(N*N!)
Space O(N*N!)
'''

from collections import deque


def generate_permutations(nums):
    result = []
    last_perms = deque()
    last_perms.append([])

    for i in range(len(nums)):
        for _ in range(len(last_perms)):
            perm = last_perms.popleft()
            for j in range(len(perm) + 1):
                new_perm = list(perm)
                new_perm.insert(j, nums[i])
                if i == len(nums) - 1:
                    result.append(new_perm)
                else:
                    last_perms.append(new_perm)
    return result

print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))