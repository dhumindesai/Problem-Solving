def generate(numRows):
    result = [[1]]

    for i in range(2, numRows + 1):
        current = [1 for _ in range(i)]
        for j in range(1, i - 1):
            current[j] = result[i - 2][j - 1] + result[i - 2][j]

        result.append(current)

    return result

print(generate(5))