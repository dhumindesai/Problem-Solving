def fruits_into_baskets(fruits):
    basket1, basket2 = {}, {}
    start, end = 0, 0
    result = 0

    for end in range(len(fruits)):
        fruit = fruits[end]
        if fruit in basket1:
            basket1[fruit] += 1
        elif fruit in basket2:
            basket2[fruit] += 1
        else:
            if not basket1:
                basket1[fruit] = 1
            elif not basket2:
                basket2[fruit] = 1
            else:
                if fruits[start] in basket1:
                    basket1.pop(fruits[start])
                    basket1[fruit] = 1
                elif fruits[start] in basket2:
                    basket2.pop(fruits[start])
                    basket2[fruit] = 1
                start += 1
        result = max(result, countTotalFruitsInBasket(basket1, basket2))

    return result


def countTotalFruitsInBasket(basket1, basket2):
    count = 0
    if basket1:
        count += list(basket1.values())[0]
    if basket2:
        count += list(basket2.values())[0]
    return count


print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))