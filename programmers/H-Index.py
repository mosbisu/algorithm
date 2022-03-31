def solution(citations):
    citations.sort(reverse=True)
    cnt = len(citations)

    for i in range(cnt):
        if i >= citations[i]:
            return i
    return cnt
