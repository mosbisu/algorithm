class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:  # 요소 x를 큐 마지막에 삽입
        self.input.append(x)

    def pop(self) -> int:            # 큐 처음에 있는 요소 제거
        self.peek()
        return self.output.pop()

    def peek(self) -> int:           # 큐 처음에 있는 요소 조회
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:         # 큐가 비어 있는지 여부 리턴
        return self.input == [] and self.output == []