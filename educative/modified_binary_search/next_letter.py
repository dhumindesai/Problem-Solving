def search_next_letter(letters, key):
  if key < letters[0] or letters[-1] <= key:
    return letters[0]
  start, end = 0, len(letters) - 1
  while start <= end:
    mid = (start + end ) // 2
    if key >= letters[mid]:
        start = mid + 1
    else:
        end = mid - 1
  return letters[start]

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()