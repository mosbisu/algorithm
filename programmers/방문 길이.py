def solution(dirs):
    answer = []
    x, y = 0, 0

    for i in dirs:
        if i == "U" and y < 5:
            y += 1
            if ((x, y-1), (x, y)) not in answer:
                answer.append(((x, y-1), (x, y)))
        elif i == "D" and y > -5:
            y -= 1
            if ((x, y), (x, y+1)) not in answer:
                answer.append(((x, y), (x, y+1)))
        elif i == "L" and x > -5:
            x -= 1
            if ((x, y), (x+1, y)) not in answer:
                answer.append(((x, y), (x+1, y)))
        elif i == "R" and x < 5:
            x += 1
            if ((x-1, y), (x, y)) not in answer:
                answer.append(((x-1, y), (x, y)))
    return len(answer)
