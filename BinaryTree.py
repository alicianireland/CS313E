#  File: TestBinaryTree.py

#  Description: Creating new level and subtree f'n for Binary trees.

#  Student Name: Alicia Ireland

#  Student UT EID: ani324

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 508455

#  Date Created: 09/18/2020

#  Date Last Modified: 09/18/2020


import sys


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))
    
class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.level = None
        self.visited = False

class Tree (object):
    def __init__ (self):
        self.root = None

    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
            self.root.level = 1
            return
        else:
            current = self.root
            parent = self.root
            level = self.root.level
            while (current != None):
                level += 1
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

          # found location now insert node
            new_node.level = level
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node
            

  # search for a node with given data
    def find (self, data):
        current = self.root
        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild
        return current



    # post order traversal - left, right, center
    # Go through the tree and add level if it is greater
    # then the max height.
    def post_order (self, aNode, height):
        if aNode != None:
            if aNode.level > max(height):
                height.append(aNode.level)
            self.post_order (aNode.lchild, height)
            self.post_order (aNode.rchild, height)
            
                
    # Go through the tree in order and print the nodes
    # at the given level.
    def in_order (self, aNode,level):
        if (aNode != None):
             self.in_order (aNode.lchild, level)
             if aNode.level == level:
                 print (aNode.data, end = ' ')
                 return
             self.in_order (aNode.rchild, level)
    
  # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        
        if self.root == None or pNode == None:
            if self.root == pNode:
                return True
            else:
                return False
            
        q_one = Queue()
        q_two = Queue()
        q_one.enqueue(self.root)
        q_two.enqueue(pNode)

     # Creat two queues to do a BFS and compare the values at each
     # level. Return False if different at any point.
        while not (q_one.is_empty()) and not (q_two.is_empty()):
            current_one = q_one.dequeue()
            current_two = q_two.dequeue()
            if current_one == None or current_two == None:
                if current_one != current_two:
                    return False
                else:
                    continue
            elif current_one.data != current_two.data:
                return False
            q_one.enqueue(current_one.lchild)
            q_one.enqueue(current_one.rchild)
            q_two.enqueue(current_two.lchild)
            q_two.enqueue(current_two.rchild)
        return True
            
    


             
  # Prints out all nodes at the given level
    def print_level (self, level):
        self.in_order(self.root, level)
        print()
    
            

  # Returns the height of the tree
    def get_height (self):
        height = [0]
        if self.root == None:
            return None
        
        self.post_order(self.root, height)
        return max(height)
        
        
        

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
    def num_nodes (self):
        print(self.nodes(self.root))
        return
    
   # Recursively goes through the left and right subtress staring
   # from the root and counts the number of nodes.
    def nodes(self, aNode):
        if aNode == None:
            return 0
        else:
            return 1 + self.nodes(aNode.lchild) + self.nodes(aNode.rchild)
        

def main():
# Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    # Creat Three Trees
    tree1 = Tree()
    tree2 = Tree()
    tree3 = Tree()
    tree4 = Tree()
    
    #Insert values in the three trees based on input
    for num in tree1_input:
        tree1.insert(num)

    for num in tree2_input:
        tree2.insert(num)

    for num in tree3_input:
        tree3.insert(num)
        

    # Test your method is_similar()
    # Insert the root of the other trepython3  TestBinaryTree.py < bst.ine to see if it is similar to the
    # first tree. Tree one is compared to tree two , which is the identical
    # to it. Tree one is also compared to tree three which is not identical
    # to it.
    root_two = tree2.root
    root_three = tree3.root
    print(tree1.is_similar(root_two))
    print(tree1.is_similar(root_three))

    # Print the various levels of two of the trees that are different
    # Testing Tree one, two, and three, for level that contains nodes (n = 3).
    # Testing Tree 1 for level that does not exist (n = 0, n = 20) and the
    # first level (n = 1)
    # three for nodes in levels that do not exsisst ( n = 0, n = 3)
    tree1.print_level(3)
    tree2.print_level(3)
    tree3.print_level(3)

    tree1.print_level(0)
    tree1.print_level(20)
    tree1.print_level(1)
    
    # Get the height of the two trees that are different.
    print(tree1.get_height())
    print(tree3.get_height())
    print('4',tree4.get_height())

    # Get the total number of nodes a binary search tree.
    tree1.num_nodes()
    tree2.num_nodes()
    tree3.num_nodes()

if __name__ == "__main__":
  main()
