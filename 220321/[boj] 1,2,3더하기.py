# T = int(input())
# n = [0] * 11
# n[1] = 1
# n[2] = 2
# n[3] = 4

# for i in range(4, 11):
#     n[i] = n[i-3] + n[i-2] + n[i-1]

# for _ in range(T):
#     m = int(input())
#     print(n[m])


T = int(input())


def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-3) + sol(n-2) + sol(n-1)


for _ in range(T):
    n = int(input())
    print(sol(n))


def backtracking(sum, n):
    global cnt
    if sum == n:
        cnt += 1
        return
    elif sum > n:
        return
    else:
        for i in range(1, 4):
            backtracking(sum+i, n)


T = int(input())

for _ in range(T):
    cnt = 0
    n = int(input())
    backtracking(0, n)
    print(cnt)
