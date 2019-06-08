'''
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
'''
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None


    print('input:',ints)

    maxval = -1
    minval = 999999

    #simgle pass
    for item in ints:
        #O(n)
        if item > maxval:
            maxval = item
        #O(n)
        if item < minval:
            minval = item

    print((minval,maxval))
    return (minval,maxval)



## Example Test Case of Ten Integers
import random
count = 0

for _ in range(300):
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    rst = ( ((0, 9) == get_min_max(l)))
    if rst == True:
        print("Pass, count:",count)
    else:
        print("Fail, count:",count)
        break
    count +=1

#Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
