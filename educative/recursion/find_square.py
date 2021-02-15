def findSquare(targetNumber) :
  if targetNumber == 0:
    return 0
  return findSquare(targetNumber - 1) + 2 * targetNumber - 1


print(findSquare(6))