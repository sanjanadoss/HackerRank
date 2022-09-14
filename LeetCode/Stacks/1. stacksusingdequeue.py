from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(string):
    stack = Stack()
    for ch in string:
        stack.push(ch)
    
    string = ''
    while stack.size()!=0:
        string += stack.pop()
    return string

if __name__ == '__main__':
    print(reverse_string('hello wassup'))

