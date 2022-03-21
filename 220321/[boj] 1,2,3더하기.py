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


def bt(value, sum):
    global cnt

    if sum >= n:
        return

    sum += value
    if sum == n:
        cnt += 1
    bt(1, sum)
    bt(2, sum)
    bt(3, sum)


T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    bt(0, 0)
    print(cnt)
