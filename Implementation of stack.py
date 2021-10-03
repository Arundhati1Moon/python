'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, dataval):
# Used list push method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
# Used list pop method to remove element
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.push(1)
AStack.push(2)
AStack.push(3)
AStack.push(4)
print(AStack.pop())
print(AStack.pop())
