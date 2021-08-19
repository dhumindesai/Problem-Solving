def featuredProduct(products):
    # count frequenencies of the purchased products
    purchase_freq = {}
    for product in products:
        if product in purchase_freq:
            purchase_freq[product] += 1
        else:
            purchase_freq[product] = 1

    result = None
    current_freq = 0
    # find the max frequency
    for item, freq in purchase_freq.items():
        if freq > current_freq:
            result = item
            current_freq = freq
        elif freq == current_freq:
            result = max(result, item)

    return result

print(featuredProduct(['yellowShirt', 'redHat', 'blackShirt',
                       'bluePants', 'redHat', 'pinkHat',
                       'blackShirt', 'yellowShirt', 'greenPants', 'greenPants']))