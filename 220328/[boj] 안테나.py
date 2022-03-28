import sys
input = sys.stdin.readline

N = int(input())
location = list(map(int, input().split()))

location.sort()

print(location[(N-1)//2])  # 중간값 출력
