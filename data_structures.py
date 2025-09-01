class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
if __name__ =='__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())
    print(s.peek())
    s.push(20)
    print(s.peek())
    print(s.is_empty())
    print(s.size())
    