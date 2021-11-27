def countOrders(n):
    result = [0]
    inputs = []

    for i in range(1, n + 1):
        inputs.append(i)
        inputs.append(-i)

    def helper(idx, slate):

        # base
        if idx == len(inputs):
            result[0] += 1
            return

        # recursive
        for pick in range(idx, len(inputs)):
            if inputs[pick] > 0:
                if -inputs[pick] not in slate:
                    continue
            inputs[pick], inputs[idx] = inputs[idx], inputs[pick]
            slate.add(inputs[idx])
            helper(idx + 1, slate)
            slate.remove(inputs[idx])
            inputs[pick], inputs[idx] = inputs[idx], inputs[pick]

    helper(0, set())

    return result[0]

print(countOrders(10))