def no_ways(n):
    f = [0 for _ in range(n)]
    g = [0 for _ in range(n)]
    h = [0 for _ in range(n)]

    f[0] = 1
    f[1] = 2

    g[0] = 1
    g[1] = 2

    h[0] = 1
    h[1] = 2

    for i in range(2, n):
        f[i] = f[i-1] + f[i-2] + h[i-2] + g[i-2]
        h[i] = f[i-1] + g[i-1]
        g[i] = f[i-1] + h[i-1]

    return f[n-1]

print(no_ways(5))