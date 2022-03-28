import sys
input = sys.stdin.readline

N = int(input())
students = []

for _ in range(N):
    name, kor, eng, math = input().split()
    students.append(name, int(kor), int(eng), int(math))

# 1 국어 점수가 감소하는 순서로 → -x[1]
# 2 영어 점수가 증가하는 순서로 → x[2]
# 3 수학 점수가 감소하는 순서로 → -x[3]
# 4 이름이 사전 순으로 증가하는 순서로 → x[0]
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in students:
    print(i[0])
