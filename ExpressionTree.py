#  File: ExpressionTree.py

#  Description: Creating a Expression Tree to evaluate math expression

#  Student's Name: Alicia Ireland

#  Student's UT EID: ani324

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 508455

#  Date Created: 11/132/2020

#  Date Last Modified: 11/13/2020

import sys

class Stack (object):
    def __init__ (self):
      self.stack = []

  # add an item on the top of the stack
  # top of stack = end of list
    def push (self, item):
      self.stack.append (item)

  # remove an item from the top of the stack
    def pop (self):
      return self.stack.pop()

  # check the item on the top of the stack
    def peek (self):
      return self.stack[-1]

  # check if the stack is empty
    def is_empty (self):
      return (len(self.stack) == 0)

  # return the number of elements in the stack
    def size (self):
      return (len(self.stack))

    def add_to_end(self,item):
        self.stack.insert(0,item)


class Node (object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree (object):
    def __init__ (self):
        self.root = None
        
    # create expression tree given math expression 
    def create_tree (self, expr):
        theStack = Stack()
        operators = ['+','-','/','//','*','**','%']


        root = Node(None)
        self.root = root
        current = self.root
      
        for item in expr:
            if item == '(':
                new = Node(item)
                current.left = new
                theStack.push(current)
                current = current.left
            elif item == ')':
                if theStack.is_empty():
                    current = self.root
                else:
                    current = theStack.pop()
            elif item in operators:
                new = Node(item)
                current.data = item
                theStack.push(new)
                current.right = new
                current = current.right
            else:
                current.data = item
                current = theStack.pop()
      
    # evaluate the expression tree and return the result
    def evaluate (self, aNode):
        operators = ['+','-','/','//','*','**','%']
        theStack2 = Stack()
        self.post_order_eval (aNode,theStack2)

        post = []
        
        while not theStack2.is_empty():
            token = theStack2.pop()
            post.insert(0, token)
  
        #print(post)
        theStack3 = Stack()

        # adapted the rpn code from class
        # to evaluate the postfix expression list
        for item in post:
            if item in operators:
                val1 = theStack3.pop()
                val2 = theStack3.pop()
                result = eval(str(val2) + item + str(val1))
                theStack3.push(result)
            else:
                 theStack3.push(item)
        return float(theStack3.pop())
                
            
            
            
    
    # create a stack in using post ordertraversal  
    def post_order_eval (self, aNode, theStack2):
        if (aNode != None):
            self.post_order_eval (aNode.left, theStack2)
            self.post_order_eval (aNode.right, theStack2)
            theStack2.push(aNode.data)
        
    # read and print the values in pre - order traversal
    # center(print), left, right
    def pre_order (self, aNode): 
        if (aNode != None): #if has children
            print(aNode.data, end = ' ')
            self.pre_order (aNode.left)
            self.pre_order (aNode.right)

    # read and print the values in post - order traversal
    # left, right, center(print)
    def post_order (self, aNode):
        if (aNode != None):
            self.post_order (aNode.left)
            self.post_order (aNode.right)
            print (aNode.data, end = ' ')


    

def main():
  # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    
  # evaluate the expression and print the result
    expr2 = expr.split()

    ExprTree = Tree()
    ExprTree.create_tree(expr2)

    aNode = ExprTree.root
    print(expr, '=', ExprTree.evaluate(aNode))


  # get the prefix version of the expression and print
    
    print('Prefix Expression:', end = ' ')
    ExprTree.pre_order(aNode)
    print()

    

  # get the postfix version of the expression and print
    print('Postfix Expression:', end = ' ')
    ExprTree.post_order(aNode)
    print()

if __name__ == "__main__":
  main()
