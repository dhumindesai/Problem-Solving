def minSwapsCouples(row):
    partner_idx = {}

    for i in range(len(row)):
        if row[i]%2 == 0:
            row[i] = -(row[i] + 1)
        partner_idx[row[i]] = i

    swaps = 0
    p1 = 0
    while p1 < len(row) - 1:
        if row[p1] != -row[p1+1]:
            p2 = partner_idx[-row[p1]]
            partner_idx[row[p1+1]] = p2
            row[p1 + 1], row[p2] = row[p2], row[p1 + 1]
            swaps += 1
        p1 += 2

    return swaps

# print(minSwapsCouples([6,2,1,7,4,5,3,8,0,9]))
# print(minSwapsCouples([10,7,4,2,3,0,9,11,1,5,6,8]))
print(minSwapsCouples([9,12,2,10,11,0,13,6,4,5,3,8,1,7]))