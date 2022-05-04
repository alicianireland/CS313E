#  File: Reducible.py

#  Description: Use Hashing to find  words that  are reducible

#  Student Name: Alicia Ireland

#  Student UT EID: ani324

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 508455

#  Date Created: 10/30/2020

#  Date Last Modified: 10/30/2020

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False
    
    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    key = hash_word(s,const)
    return const - ( key % const )

    
# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    size = len(hash_table)
    index = hash_word (s, size)
    if hash_table[index] == '':
        hash_table[index] = s
    else:
        step = step_size (s, 13)
        while hash_table[index] != '':
            step += step
            index = (index + step) % size
        hash_table[index] = s

       
        
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    size = len(hash_table)
    index = hash_word (s, size)

    if hash_table[index] == s:
        return True
    if hash_table[index] != '':
        step = step_size (s, 13)
        while hash_table[index] != '':
            if hash_table[index] == s:
                return True
            step += step
            index = (index + step) % size  
    return False
    
    

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    if len(s) == 1:
        return is_vowel(s)
    else:
        if (find_word(s, hash_memo)):
            return True
        elif not find_word(s, hash_table):
            return False
        for i in range(len(s)):
            if is_reducible(s[:i] + s[i + 1:], hash_table, hash_memo):
                insert_word(s[:i] + s[i + 1:], hash_memo)
                return True
        return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    pass
   
            
def is_vowel(s):
    for letter in s:
        if letter in ['a','o','i']:
            return True
    return False
    
def main():
    # create an empty word_list
    word_list = []


    # open the file words.txt
    word_file = open('words.txt', 'r')

    # read words from words.txt and append to word_list
    for word in word_file:
        word = word.strip()
        word_list.append(word)
        

    # close file words.txt
    word_file.close()

    # find length of word_list
    words_len = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    words_len *= 2
    while not is_prime(words_len):
        words_len += 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    hash_list.extend('' for i in range(words_len))
    

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word (word, hash_list)
    

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    hash_memo = []

    # populate the hash_memo with M blank strings
    m_len = int(.25 * words_len)
    while not is_prime(m_len):
        m_len += 1
    hash_memo.extend('' for i in range(m_len))
    

    # create an empty list reducible_words
    reducible_words = []
   

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible (word, hash_list, hash_memo):
            reducible_words.append(word)
            
    
    # find words of length 10 in reducible_words
    for word in reducible_words:
        if len(word) == 10:
            print(word)
    # print the words of length 10 in alphabetical order
    # one word per line

if __name__ == "__main__":
  main()
