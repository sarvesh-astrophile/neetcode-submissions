class MinStack:

    def __init__(self):
        self.data = []
        self.data_min = [] 

    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val, self.data_min[-1] if self.data_min else val)
        self.data_min.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.data_min.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data_min[-1]
