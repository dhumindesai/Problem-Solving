def generate_all_combinations(arr, target):
    arr.sort()
    result = []

    def helper(i, slate, curSum):
        if curSum == target:
            result.append(slate[:])
            return
        if curSum > target or i == len(arr):
            return

        count = 0
        for j in range(i, len(arr)):
            if arr[i] != arr[j]:
                break
            count += 1

        helper(i + count, slate, curSum)  # exclude

        for c in range(1, count + 1):
            slate.append(arr[i])
            helper(i + count, slate, curSum + arr[i])
            curSum += arr[i]

        for c in range(count):
            slate.pop()

    helper(0, [], 0)

    return result

print(generate_all_combinations([1, 3, 2, 2], 4))
print(generate_all_combinations([1,1,1], 4))