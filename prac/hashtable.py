# [해시테이블 시간 복잡도]
# Insertion, Deletion, Search: O(1)
# 대단히 유용한 자료구조.

# 핵심 아이디어: 고윳값을 준다!
# "거기 가면, 거의 비어 있어 or 혼자 있어"

# 고윳값 가지는게 쉬울까?
# - 생일 문제

# 하고 싶은 말은, 우리가 해시테이블을 쓸 때 거의 key 값의 중복이 일어나는 경우가
# 흔할 수 있다는 것. -> 상자의 크기를 잘 잡아야 한다.
# - load factor: 자바 경험적으로 0.75 (상자 4개 중 3개 차면, 공간 재할당한다)
# (파이썬 0.66, 루비 0.5)

# 오케이. 그럼 해싱 함수 성능이 정말 중요하겠네. 보통 뭘 쓰지?
# 1. easy - modular 연산.
#     - x mod m 일 때, m이 해시 테이블의 크기.
#     - m 은 2의 멱수(거듭제곱수)에 가깝지 않은 소수가 좋다

# 다시 핵심 질문: 그럼 충돌이 일어나면 어떻게 해결하지?
# 1) 개별 체이닝 - 쭉쭉 연결하기. 일반적. 최악의 경우 탐색 O(n)
# 2) 오픈 어드레싱 - probing 전략따라 다름. 선형이 제일 쉬움. 클러스터링 문제.

# 파이썬은?
# 딕셔너리에 해시테이블(오픈 어드레싱) 사용.
# "페이닝 시 메모리 할당하는 오버헤드가 높아 오픈 어드레싱 채택"

# 생일 문제
import random


def test_birthday_problem():
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")


if __name__ == "__main__":
    test_birthday_problem()
