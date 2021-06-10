def get_permutations(arr):
    # Write your code here
    result = []

    def helper(arr, i, slate):

        # leaf nodes
        if i == len(arr):
            result.append(slate[:])
            return

        # internal nodes
        else:
            for pick in range(i, len(arr)):
                arr[pick], arr[i] = arr[i], arr[pick]
                slate.append(arr[i])
                helper(arr, i+1, slate)
                slate.pop()
                arr[pick], arr[i] = arr[i], arr[pick]

    helper(arr, 0, [])
    return result

print(get_permutations([1,2,3]))
print(get_permutations([1,1,1]))