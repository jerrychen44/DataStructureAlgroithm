
'''
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
'''

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        print('input must >=0, return -1')
        return -1

    low = 0
    hig = number

    rst = sqrt_helper(low,hig,number)
    print('sqrt(',(number),'),', 'ans:',rst)
    return rst



def sqrt_helper(low,hig,target):


    if target == 0 or target ==1:
        return target

    #use the idea from binary searching
    #we assume we can find the sqrt number from
    # 0,1,2,......, target
    # ex: if the target is 27
    # we set our finding array as
    # 0,1,2,3....,27
    # and the first mid = (0+27)//2

    mid = (low+hig)//2

    if mid <= 0:
        return -1

    cur_val = pow(mid,2)
    next_cur_val = pow(mid+1,2)

    #base case
    if  cur_val <= target and next_cur_val>target :
        return mid

    # recursive call for the one of half part,
    # which cause the T(n) = T(n/2) + 1
    if cur_val > target:
        return sqrt_helper(low,mid-1,target)
    elif cur_val < target:
        return sqrt_helper(mid+1,hig,target)



#################
# testing section
#################

print ("Pass" if  (3 == sqrt(9)) else "Fail")
#edge cases
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
#edge cases
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (8 == sqrt(66)) else "Fail")
#edge cases

print ("Pass" if  (-1 == sqrt(-100)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
print ("Pass" if  (15 == sqrt(250)) else "Fail")
