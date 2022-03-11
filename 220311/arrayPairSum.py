
# 오름차순 풀이
def arrayPairSum1(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum
print(arrayPairSum1([1, 4, 3, 2]))

# 짝수 번째 값 계산
def arrayPairSum2(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum
print((arrayPairSum2([1, 4, 3, 2])))

# 파이썬다운 방식
def arrayPairSum3(nums):
    return sum(sorted(nums)[::2])
print(arrayPairSum3([1, 4, 3, 2]))