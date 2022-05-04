#  File: Radix.py

#  Description: Sort a list of words containing number and words.

#  Student Name: Alicia Ireland

#  Student UT EID: ani324

#  Course Name: CS 313E

#  Unique Number: 508455

#  Date Created: 11/2/2020

#  Date Last Modified: 11/4/2020

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

  # check if the queue if empty
    def is_empty (self):
        return (len(self.queue) == 0)

  # return the size of the queue
    def size (self):
        return (len(self.queue))

    def see_inside(self):
        print(self.queue)



# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    max_len = 0
    for word in a:
        if len(word) > max_len:
            max_len = len(word)

    a = extend_words(a, max_len)

    # Creates Dictionary of characters and their corresponding
    # index values that correlates to order of character
    char = ' 0123456789abcdefghijklmnopqrstuvwxyz'
    values = {}
    for i in range(len(char)):
        values[char[i]] = i
    
    # Create list of Queues for each possible character
    que_objects = [Queue() for x in range(37)]

    # Sort list of words based on the characters at all indexes.
    for i in range(max_len - 1, -1, -1):
        a = index_sort(a, values , que_objects,i)

    return a
        
# Sort word in Queues based on character at given index
def index_sort(a, values , que_objects, i):
    for word in a:
        index = values[word[i]]
        que_objects[index].enqueue(word)
    return get_sorted_queues(que_objects)


# Collect all sorted values in a seperate Queues
# into list a before sorting again
def get_sorted_queues(que_objects):
    b = []
    for objects in que_objects:
        while not objects.is_empty():
            b.append(objects.dequeue())
    return b



# Add spaces to end of word if word is shorter
# then the longest words
def extend_words(a, max_len):
    for i in range(len(a)):
        if len(a[i]) < max_len:
            num = max_len - len(a[i])
            a[i] = a[i] + ' ' * num
    return a

def main():
    
  # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int (line)

  # create a word list
    word_list = []
    for i in range (num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append (word)
    
    
    '''
    # print word_list
    print (word_list)
    '''
    
    
    # use radix sort to sort the word_list
    sorted_list = radix_sort (word_list)

    # print the sorted_list
    for i in range(len(sorted_list)):
        sorted_list[i] = sorted_list[i].strip()
    print (sorted_list)

if __name__ == "__main__":
    main()
