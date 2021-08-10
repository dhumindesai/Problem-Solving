def bitwiseComplement(n):
    complement = 0
    right_most_bit = 1

    # iterate
    while right_most_bit <= n:
        if (n & right_most_bit) == 0:
            complement += right_most_bit
        right_most_bit = right_most_bit << 1

    return complement

print(bitwiseComplement(10))
print(bitwiseComplement(5))