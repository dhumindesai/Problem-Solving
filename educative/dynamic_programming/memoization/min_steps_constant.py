def min_steps(num):
    result = 0

    while num > 1:
        if num % 3 == 0:
            num = num / 3
        elif num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        result += 1

    return result

print(min_steps(6))
print(min_steps(8))
print(min_steps(10))
print(min_steps(15))
print(min_steps(300))