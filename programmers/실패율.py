def solution(N, stages):
    # N : 스테이지 개수, stages : 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 return
    # 실패율 = 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

    clear = []           # 스테이지를 클리어한 플레이어 수
    reach = []           # 스테이지에 도달한 플레이어 수
    failure = {}         # 스테이지별 실패율

    for i in range(1, N+1):
        # 현재 멈춰있는 스테이지가 i보다 크면 클리어한 플레이어 수
        clear.append(len([x for x in stages if x > i]))
        # i보다 크거나 같으면 도달한 플레이어 수
        reach.append(len([x for x in stages if x >= i]))
        print(f"{i}스테이지 클리어한 플레이어 수 : {clear}")
        print(f"{i}스테이지 도달한 플레이어 수 : {reach}\n")

    for i in range(N):
        if reach[i] == 0:                                # 도달한 플레이어가 없으면
            failure[i+1] = 0                             # 실패율 = 0
        else:                                            # 도달한 플레이어가 있으면
            # 1 - 클리어한 플레이어 수 / 도달한 플레이어 수
            failure[i+1] = 1 - clear[i] / reach[i]
    print(failure)

    return sorted(failure, key=lambda x: -failure[x])    # 실패율을 기준으로 내림차순 정렬


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
