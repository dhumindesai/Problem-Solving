def minWindow(s, t):
    def count_freq(t):
        freq = {}
        for c in t:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq

    def controlled(freq):
        for k, v in freq.items():
            if v > 0:
                return False
        return True

    min_len = float("inf")
    rs, re = -1, -1
    i, j = 0, 0
    t_freq = count_freq(t)  # {a:0, b:0}

    while j < len(s):
        while not controlled(t_freq) and j < len(s):
            # expand the window
            if s[j] in t_freq:
                t_freq[s[j]] -= 1
            j += 1

        while controlled(t_freq) and i < len(s):
            # Record the window if min found
            current_win = j - i + 1
            if current_win < min_len:
                min_len = j - i + 1
                rs, re = i, j - 1

            # Shrink the window
            if s[i] in t_freq:
                t_freq[s[i]] += 1
            i += 1

    if rs == -1:
        return ""
    return s[rs:re + 1]