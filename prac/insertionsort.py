def insertionsort1(lst):
    # 0번째 요소는 이미 정렬되어 있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur+1):
            cmp = cur - delta

            if lst[cmp] > lst[cmp+1]:
                lst[cmp], lst[cmp+1] = lst[cmp+1], lst[cmp]
            else:
                break

    return lst


def insertionsort2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp+1] = lst[cmp]
            cmp -= 1

        lst[cmp+1] = val
