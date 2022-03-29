n = int(input())
a = []

for _ in range(n):
    word = str(input())
    word_cnt = len(word)
    a.append((word_cnt, word))

# 1. 중복 삭제
a = list(set(a))

# 2. 단어 숫자 정렬
# 3. 단어 알파벳 정렬
a.sort(key=lambda word: (word[0], word[1]))

for word in a:
    print(word[1])
