def fibonacci(testVariable) :
    if testVariable <= 1:
        return 1
    return fibonacci(testVariable - 1) + fibonacci( testVariable - 2)

def fibonacci_iterative(testVariable):
    first, second = 0, 1
    for i in range(0, testVariable):
        temp = first + second
        first = second
        second = temp
    return first

print(fibonacci_iterative(7))