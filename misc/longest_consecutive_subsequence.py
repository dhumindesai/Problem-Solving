def solution(arr):
    if not arr:
        return 0
    index = set(arr)
    seen = set()

    result = 1
    for i in range(len(arr)):
        if arr[i] not in seen:
            count = 1
            current_num = arr[i] + 1
            seen.add(current_num)

            while current_num in index:
                count += 1
                current_num = current_num + 1
                seen.add(current_num)

            result = max(result, count)

    return result

print(solution([1, 9, 3, 10, 4, 20, 2]))
print(solution([0,3,7,2,5,8,4,6,0,1]))
print(solution([100,4,200,1,3,2]))