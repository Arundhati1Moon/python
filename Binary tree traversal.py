'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def printInorder(root): 
  
    if root: 
        printInorder(root.left) 
        
        print(root.val), 
        
        printInorder(root.right) 
  
def printPostorder(root): 
  
    if root: 
        printPostorder(root.left) 
        
        printPostorder(root.right) 
        
        print(root.val), 
  
def printPreorder(root): 
  
    if root: 
  
        print(root.val), 
        
        printPreorder(root.left) 
        
        printPreorder(root.right) 
        

root = Node(1) 
root.left  = Node(2) 
root.right  = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

printPreorder(root) 
  
printInorder(root) 
  
printPostorder(root) 
