def calculateSumOfSquares(q):
    result = 0
    while q > 0:
        rem = q % 10
        result += rem * rem
        q = q // 10
    return result


'''
T = O(logn)
S = O(n)
'''
def find_happy_number_1(num):
    s = {num}
    current = num

    while True:
        current = calculateSumOfSquares(current)
        if current == 1:
            return True
        elif current in s:
            return False
        s.add(current)

'''
T = O(logn)
S = O(1)
'''
def find_happy_number_2(num):
    slow, fast = num, num
    while True:
        slow = calculateSumOfSquares(slow)
        fast = calculateSumOfSquares(calculateSumOfSquares(fast))
        if fast == 1:
            return True
        if fast == slow:
            return False

def main():
    print(find_happy_number_1(23))
    print(find_happy_number_1(12))
    print(find_happy_number_1(11))
    print(find_happy_number_1(1))

    print()

    print(find_happy_number_2(23))
    print(find_happy_number_2(12))
    print(find_happy_number_2(11))
    print(find_happy_number_2(1))


main()
