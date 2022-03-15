test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    idx = list(range(len(queue)))
    idx[m] = 'target'
    # 순서
    order = 0

    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값일 때
        if queue[0] == max(queue):
            order += 1

            # 두번째 if: idx의 첫번째 값 = "target"일 때
            if idx[0] == 'target':
                print(order)
                break
            else:
                queue.pop(0)
                idx.pop(0)

        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))