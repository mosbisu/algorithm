from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:        # 요소 x를 스택에 삽입
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:                  # 스택의 첫 번째 요소를 삭제
        return self.q.popleft()

    def top(self) -> int:                  # 스택의 첫 번째 요소를 가져옴
        return self.q[0]

    def empty(self) -> bool:               # 스택이 비어 있는지 여부 리턴
        return len(self.q) == 0