def search_ceiling_of_a_number(arr, key):
  if not arr or arr[-1] < key:
    return -1
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = (start + end ) // 2
    if arr[mid] == key:
        return mid
    if key > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1
  return start

def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()