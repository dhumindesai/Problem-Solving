def make_squares(arr):
    squares = []
    right = findFirstPositiveNumberIndex(arr)
    left = right - 1

    while left >= 0 and right < len(arr):
        if arr[left] * arr[left] < arr[right] * arr[right]:
            squares.append(arr[left] * arr[left])
            left -= 1
        else:
            squares.append(arr[right] * arr[right])
            right += 1

    while right < len(arr):
        squares.append(arr[right] * arr[right])
        right += 1

    while left >= 0:
        squares.append(arr[left] * arr[left])
        left -= 1

    return squares


def findFirstPositiveNumberIndex(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            return i
    return -1

print(make_squares([-2, -1, 0, 2, 3]))