def fixed_point(lst):
    low = 0
    high = len(lst)

    # 결과값 low는 i < low 인 모든 i에 대하여 lst[i] < i
    while low < high:
        mid = (low+high) // 2

        if lst[mid] < mid:
            low = mid + 1
        else:
            high = mid

    # 범위를 벗어나거나, 없는 경우.
    # low는 0에서부터 출발하므로, low < 0인 것은 검사하지 않아도 된다
    if low >= len(lst) or low != lst[low]:
        return -1
    return low
