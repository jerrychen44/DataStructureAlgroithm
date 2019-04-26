#!/usr/bin/env python
# coding: utf-8

# # Strings Exercises

# #### Intro

# Strings in Python are arrays of bytes representing unicode characters. In this exercise we are going to practice our work with string manipulation.

# #### Reverse Strings

# In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.
#
# For example, if the input is the string `"water"`, then the output should be `"retaw"`.
#
# While you're working on the function and trying to figure out how to manipulate the string, it may help to use the `print` statement so you can see the effects of whatever you're trying.

# In[1]:


# Code

def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    size = len(our_string)

    news=''
    for idx in range(size):
        news = news + our_string[size-idx-1]

    return news






# In[2]:


# Test Cases
print ("======== string_reverser")
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


# <span class="graffiti-highlight graffiti-id_5y1c1sk-id_8u3k1ve"><i></i><button>Show Solution</button></span>

# #### Anagrams

# The goal of this exercise is to write some code to determine if two strings are anagrams of each other.
#
# An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).
#
# For example:
# - "rat" is an anagram of "art"
# - "alert" is an anagram of "alter"
# - "Slot machines" is an anagram of "Cash lost in me"
#
# Your function should take two strings as input and return `True` if the two words are anagrams and `False` if they are not.
#
# You can assume the following about the input strings:
# - No punctuation
# - No numbers
# - No special characters

# In[ ]:


# Code

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    '''
    str1 = str1.lower()
    str2 = str2.lower()

    hashmap1 = {}
    for str in str1:
        if str !=' ':
            if str not in hashmap1:
                hashmap1[str]=1
            else:
                hashmap1[str]+=1


    hashmap2 = {}
    for str in str2:
        if str !=' ':
            if str not in hashmap2:
                hashmap2[str]=1
            else:
                hashmap2[str]+=1

    return hashmap1 == hashmap2
    '''




    #both remove the space, lower case
    clean_str1 = str1.replace(" ","").lower()
    clean_str2 = str2.replace(" ","").lower()

    if len(clean_str1) != len(clean_str2):
        return False

    return sorted(clean_str1) == sorted(clean_str2)







# In[ ]:


# Test Cases
print ("======== anagram_checker")
print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")


# <span class="graffiti-highlight graffiti-id_hnedbqz-id_0ifjb4r"><i></i><button>Show Solution</button></span>

# #### Reverse the words in sentence

# Given a sentence, reverse each word in the sentence while keeping the order the same!

# In[ ]:


# Code

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    word_list = our_string.split(' ')
    #print(word_list)
    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]


    return " ".join(word_list)


# In[ ]:


# Test Cases
print ("======== word_flipper")
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


# <span class="graffiti-highlight graffiti-id_ttzcm4k-id_m6frlmt"><i></i><button>Show Solution</button></span>

# #### Hamming Distance

# In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. Calculate the Hamming distace for the following test cases.

# In[ ]:


# Code

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    #等長才能求 Hamming Distance
    if len(str1) == len(str2):
        count = 0

        for idx in range(len(str1)):

            if str1[idx] != str2[idx]:
                count +=1
        return count

    else:
        return None


# In[ ]:


# Test Cases
print ("======== hamming_distance")
print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")


# <span class="graffiti-highlight graffiti-id_kddwu3s-id_u1nzuf0"><i></i><button>Show Solution</button></span>
