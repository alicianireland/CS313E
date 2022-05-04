#  File: TestLinkedList.py

#  Description: Creating Linked List

#  Student Name: Alicia Ireland

#  Student UT EID: ani324

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 508455

#  Date Created: 11/8/2020

#  Date Last Modified: 11/8/2020

class Link (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList (object):
  # create a linked list
    def __init__ (self):
        self.first = None

  # get number of links 
    def get_num_links (self):
        current = self.first
        if current == None: #is empty
            return 0

        count = 1
        while current.next != None:
            count += 1
            current = current.next
        return count
        
      
  
  # add an item at the beginning of the list
    def insert_first (self, data):
        new_link = Link (data)
        new_link.next = self.first
        self.first = new_link
        

  # add an item at the end of a list
    def insert_last (self, data):
        new_link = Link(data)

        current = self.first

        if current == None: #is empty
            self.first = new_link
            return
          
        while current.next != None:
            current = current.next
        current.next = new_link

      

  # add an item in an ordered list in ascending order
    def insert_in_order (self, data):
        new_link = Link(data)

        current = self.first
        previous = self.first

        if current == None: #is empty
            self.first = new_link
            return
        if current.data >= data:
            self.insert_first(data)
            return
            
        while current.data < data:
            if current.next == None:
                self.insert_last(data)
                return
            previous = current
            current = current.next
            
        if current.next == None:
                self.insert_last(data)
                return

        #if current.next == self.first()   
        new_link.next = current    
        previous.next = new_link
        return


  # search in an unordered list, return None if not found
    def find_unordered (self, data):
        current = self.first
        if (current == None): #empty list
            return None
        
        while (current.data != data):
            if (current.next == None):
                return None # at the end
            else:
                current = current.next
            
        return current

  # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        current = self.first
        previous = self.first
        
        if (current == None): #empty list
            return None
        
        while (current.data < data):
            if (current.next == None):
                return None # at the end
            else:
                current = current.next

        if current.data == data:
            #print(current.data)
            return current
        else:
            return None

  # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        previous = self.first
        current = self.first

        if (current == None): #empty list
            return None  
            
        while (current.data != data):
            if (current.next == None):
                return None # at the end
            else:
                previous = current 
                current = current.next


        if (current == self.first):# want to delete first link
            self.first = self.first.next
        else:
            previous.next = current.next

        
        return current # current is now the obj afer the one just deleted
    

  # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first


        if current == None:
            return None

        count = 0
        string = ''
        while current.next != None:
            if count == 10:
                count = 1
                string += '\n' + str(current.data) + ' '
                current = current.next
            
            else:
                count += 1
                string += str(current.data) + ' ' 
                current = current.next

        
        if count < 10:
            string += str(current.data) + ' '
        else:
            string += '\n' + str(current.data) + ' '
        return string
            

  # Copy the contents of a list and return new list
    def copy_list (self):
        copy = LinkedList()
        
        current = self.first
        
        if (current == None): #empty list
            return copy

        while (current.next != None):
            copy.insert_last (current.data)
            current = current.next
            
        copy.insert_last(current.data)
        
        return copy
        

  # Reverse the contents of a list and return new list
    def reverse_list (self):
        copy = LinkedList()
        
        current = self.first
        
        if (current == None): #empty list
            return copy

        while (current.next != None):
            copy.insert_first (current.data)
            current = current.next
            
        copy.insert_first(current.data)
        
        return copy
        
    def insert_sort (self, data):
        new_link = Link(data)

        current = self.first
        previous = self.first

          
        while current.data < data:
            if current.next == None:
                self.insert_last(data)
                return    
            previous = current 
            current = current.next
           
        
        new_link.next = current
        previous.next = new_link
        

  # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        new_sort = LinkedList()
        first = self.first
        current = first.next

        if (current == None): #empty list
            return new_sort

        new_sort.insert_first(first.data)
    
        while current.next != None:
            new_sort.insert_sort(current.data)
            current = current.next
        new_sort.insert_sort(current.data)

        return new_sort
                
            

        

  # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current = self.first
        previous = self.first

        if current == None: #is empty
            return True
          
        while current.data >= previous.data:
            if current.next == None:
                return True
            previous = current
            current = current.next
        return False
            
    
    

  # Return True if a list is empty or False otherwise
    def is_empty (self):
        if self.first == None:
            return True
        return False

  # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        new_sort = LinkedList()
        current = self.first
        current2 = other.first
        
        if (current == None) and (current2 == None): #empty list
            return new_sort
        
    
        while current.next != None and current2.next != None:
            new_sort.insert_first(current.data)
            new_sort.insert_first(current2.data)
            current = current.next
            current2 = current2.next
            


        if current.next == None and current2.next != None:
            new_sort.insert_first(current.data)
            while current2.next != None:
                new_sort.insert_first(current2.data)
                current2 = current2.next
            new_sort.insert_first(current2.data)
                    

        elif current2.next == None and current.next != None :
            new_sort.insert_sort(current2.data)
            while current.next != None:
                new_sort.insert_first(current.data)
                current = current.next 
            new_sort.insert_first(current.data)

        else:
            new_sort.insert_first(current.data)
            new_sort.insert_first(current2.data)
            
        new_un = LinkedList()
        current = new_sort.first
        while current.next != None:
            new_un.insert_in_order(current.data)
            current = current.next
        new_un.insert_in_order(current.data)   

        return new_un
   
        
  # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current = self.first
        current2 = other.first

        if current == None and current2 == None:
            return True

        while current.next != None and current2.next != None:
            if current.data != current2.data:
                return False 
            current  = current.next
            current2 = current2.next

        if current.data != current2.data:
            return False

        return True


        '''
        while current.data = current2.data:
            if current.next == None and current2.next != current2.data \
               or current.next != None and current2.next == current2.data:
                return False 
            current  = current.next
            current2 = current2.next
        return False
        '''
        
    
            
            
            

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        nums = []

        noDuped = LinkedList()

        current = self.first
        previous = self.first

        if (current == None): #empty list
            return noDuped

        while (current.next != None):
            if current.data not in nums: #remove
                nums.append(current.data)
                noDuped.insert_last(current.data)
            current = current.next

            
        if current.data not in nums: #remove
            noDuped.insert_last(current.data)
        
        
        return noDuped

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
    linkOne = LinkedList()
    for i in range(20,-1,-1):
        linkOne.insert_first(i)

    linkOne.__str__()

  # Test method insert_last()
    linkOne.insert_last(21)
    linkOne.__str__()

  # Test method insert_in_order()
    linkOne = LinkedList()
    linkOne.insert_in_order(15)
    linkOne.insert_in_order(-1)
    linkOne.insert_in_order(50)
    linkOne.insert_in_order(80)
    linkOne.__str__()
    

  # Test method get_num_links()
    #print(linkOne.get_num_links())

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there
    #linkTwo = LinkedList()
    #print(linkOne.find_unordered(70))
    #print(linkTwo.find_unordered(20))

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there
    #print(linkOne.find_ordered(0))
    #print(linkTwo.find_ordered(20))
    

  # Test method delete_link()
  # Consider two cases - data is there, data is not there
    #print(linkOne.delete_link(5))
    #print(linkOne.delete_link(77))
    #linkOne.__str__()
    #print(linkTwo.delete_link(20))

  # Test method copy_list()
    #cp = linkOne.copy_list()
    #linkOne.__str__()
    #cp.__str__()

  # Test method reverse_list()
    #cp = linkOne.reverse_list()
    #linkOne.__str__()
    #cp.__str__()

    
  # Test method sort_list()
    linkthree = LinkedList()
    linkthree.insert_first(4)
    linkthree.insert_first(7)
    linkthree.insert_first(1)
    linkthree.insert_first(22)
    linkthree.insert_first(42)
    linkthree.insert_first(0)
    linkthree.__str__()
    cp = linkthree.sort_list()
    #cp.__str__()
    #linkthree.__str__()

    #linkOne.__str__()
    
    

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
    linkOne = LinkedList()
    print(linkOne.is_sorted())
    #print(linkthree.is_sorted())
   


  # Test method is_empty()
    #print(linkOne.is_empty())
    #print(linkTwo.is_empty())

  # Test method merge_list()
    #merged = linkOne.merge_list(cp)
    #merged.__str__()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
    #linkTwo.insert_first(1)
    #linkFive = LinkedList()
    #linkFive.insert_first(1)
    #print(linkOne.is_equal(cp))
    #print(linkTwo.is_equal(linkFive))

  # Test remove_duplicates()
    #for i in range(4):
    #    linkOne.insert_first(2)
    #linkOne.__str__()
    linkOne = LinkedList()
    none = linkOne.remove_duplicates()
    none.__str__()

if __name__ == "__main__":
  main()
