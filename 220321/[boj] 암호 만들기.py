# 3. 연산
# a의 askii값은 97이므로 97부터 순회
def back_track(idx=97, length=0):

    # 3-1. 종료조건:
    # length (암호의 길이)가 L일때
    if length == L:
        # 3-2 정답 출력 조건
        # 모음이 1개 이상, 자음이 2개 이상.

        ai_len = 0  # 모음의 갯수 연산
        for aski in result_lst:  # 결과값을 순회하며
            if aski in aieou_set:  # 모음이 있을 때마다
                ai_len += 1  # 모음 갯수에 1개씩 더해줌

        # 4. 출력
        if ai_len and L - ai_len >= 2:  # 만약 모음이 있고 자음 또한 2개 이상 있을 때
            print(''.join(map(chr, result_lst)))  # 조건에 맞게 변환 후 출력.

    # 3-2. 재귀:
    # z의 askii 값이 124이므로 124까지만 순회
    for i in range(idx, 124):
        if aski_list[i]:  # 만약 특정 알파벳이 남았다면

            aski_list[i] = 0  # 특정 알파벳을 사용 처리 후
            result_lst.append(i)  # 결과 리스트에 삽입.

            # '오름차순' 정렬해야 하므로 idx +1, 길이가 늘어났으니 length+1 후 재귀
            back_track(i+1, length + 1)

            result_lst[:] = result_lst[:-1]  # == result_lst.pop()
            aski_list[i] = 1

# 소문자 아스키 전체 값:  [97, 122]
# set으로 사용하면 시간을 더 절약할 수 있다.


# 1. 입력.
# L : 암호의 길이
# C : 주어진 알파벳의 종류
L, C = map(int, input().split())

# 2. 선언
aski_list = [0] * 128  # 1) 아스키 리스트
aieou_set = {97, 101, 105, 111, 117}  # 2) 모음들의 아스키 값을 모은 집합
result_lst = []  # 결과값 입력받을 리스트

# 1 - 1. 입력 (2)
ipt = list(map(ord, input().split()))  # 값을 입력 받은 뒤 askii 값으로 변환 후
for aski in ipt:  # 모든 값들을 순회하며
    aski_list[aski] = 1  # askii리스트에 '있음' 표시

# 3. 연산
back_track()
