first = input().split()
N = int(first[0])
M = int(first[1])
S = str(input())
flag = False
N = 0
while not flag:
    m = M
    new = N
    for i in range(len(S)):
        if S[i] == "1":
            if m > 0:
                m -= 1
            else:
                new -= 1
        elif S[i] == "2":
            new -= 1
        else:
            m = M
            new = N
        if m < 0 or new < 0:
            N += 1
            break
        if i == len(S) - 1:
            flag = True
print(N)
