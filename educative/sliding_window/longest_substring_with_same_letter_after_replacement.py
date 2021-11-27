def characterReplacement(s, k):
    current_visited = {}
    max_so_far = 0
    start, end = 0,0

    def get_most_frequent_in_window():
        return max(current_visited.values())

    def window_ok():
        window_size = end - start + 1
        return window_size - get_most_frequent_in_window() <= k

    while end < len(s):
        update_freq(current_visited, end, s)
        if window_ok():
            max_so_far = max(max_so_far, end - start + 1)
        else:
            current_visited[s[start]] -= 1
            start += 1
        end += 1

    return max_so_far


def update_freq(current_visited, end, s):
    if s[end] not in current_visited:
        current_visited[s[end]] = 1
    else:
        current_visited[s[end]] += 1


print(characterReplacement("AABABBA", 1))
print(characterReplacement("ABBB", 1))