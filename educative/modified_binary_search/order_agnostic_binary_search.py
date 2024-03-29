def binary_search(arr, key):
  if not arr:
    return -1
  start, end = 0, len(arr) - 1
  is_ascending = arr[start] < arr[end]
  while start <= end:
    mid = (start + end ) // 2
    if arr[mid] == key:
        return mid
    if is_ascending:
      if key > arr[mid]:
        start = mid + 1
      else:
        end = mid - 1
    else:
      if key > arr[mid]:
        end = mid - 1
      else:
        start = mid + 1
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))
  print(binary_search([10], 10))


main()
