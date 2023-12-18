first = input().split()
K = int(first[0])
G = int(first[1])
M = int(first[2])

g = 0
m = 0

for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if G - g > m:
            g += m
            m = 0
        else:
            tmp = g
            g = G
            m = m - G + tmp
print(str(g) + " " + str(m))
