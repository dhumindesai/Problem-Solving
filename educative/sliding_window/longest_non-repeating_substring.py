def solution(s):
    # Type your solution here
    result = 0
    visited = {}

    start = 0

    for end in range(len(s)):
        if s[end] in visited:
            result = max(result, end - start)
            newStart = visited[s[end]]
            while start <= newStart:
                visited.pop(s[start])
                start += 1
            visited[s[end]] = end
        else:
            visited[s[end]] = end

    return max(result, len(s) - start)

print(solution("nndNfdfdf"))