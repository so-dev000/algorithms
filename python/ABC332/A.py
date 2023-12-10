first = input().split()
N = int(first[0])
S = int(first[1])
K = int(first[2])
ls = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in ls:
    total += i[0] * i[1]
if total < S:
    total += K
print(total)
