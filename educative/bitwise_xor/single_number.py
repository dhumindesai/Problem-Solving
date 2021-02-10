def find_single_number(arr):
  result = 0
  for num in arr:
    result = result ^ num
  return result

def main():
    arr = [1, 4, 2, 1, 3, 2, 3, 6]
    print(find_single_number(arr))

main()