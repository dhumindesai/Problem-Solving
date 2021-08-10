def search_triplets(arr):
    triplets = []
    arr.sort()

    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if start == i:
                start += 1
                continue
            if end == i:
                end -= 1
                continue

            sum = arr[start] + arr[end]

            if sum == -arr[i]:
                triplets.append([arr[i], arr[start], arr[end]])
                while start < end and arr[start] == arr[start + 1]:
                    start += 1
                while start < end and arr[end] == arr[end - 1]:
                    end -= 1
                start += 1
                end -= 1
            elif sum < -arr[i]:
                start += 1
            else:
                end -= 1

    return triplets


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))