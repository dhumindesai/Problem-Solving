def dutch_flag_sort(balls):
    p1 = 0
    p2 = len(balls) - 1

    p1 = partition(balls, p1, p2, "R")
    partition(balls, p1, p2, "G")


def partition(balls, p1, p2, color):
    while p1 < p2:
        if balls[p1] == color:
            p1 += 1
        else:
            while p2 > p1:
                if balls[p2] == color:
                    balls[p1], balls[p2] = balls[p2], balls[p1]
                    p2 -= 1
                    p1 += 1
                    break
                p2 -= 1
    return p1


balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
# balls = ["G", "G", "G", "G"]
# balls = ["G", "G", "G", "R", "R", "G"]
print(balls)
dutch_flag_sort(balls)
print(balls)