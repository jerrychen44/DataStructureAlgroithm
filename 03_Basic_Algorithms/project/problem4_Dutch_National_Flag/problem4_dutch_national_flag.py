'''
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2,
sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n)
solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
'''
def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    #if len(arr) == 0:
    #    return []


    cur_idx = 0
    zero_idx = 0
    two_idx = len(arr)-1


    while cur_idx <= two_idx:

        cur_val = arr[cur_idx]

        if cur_val == 2:
            #swap
            tmp = arr[two_idx]
            arr[two_idx] = cur_val
            arr[cur_idx] = tmp

            two_idx -=1
            # don't move cur_idx here.
            # we still need to check the cur_val next round


        elif cur_val == 1:
            #we don't swap 1,keep it in the position now.
            #It will be swap when we hit the 0 as cur_val later.
            cur_idx +=1
        elif cur_val == 0:
            #swap
            tmp = arr[zero_idx]
            arr[zero_idx] = cur_val
            arr[cur_idx] = tmp

            zero_idx +=1
            # because you must changed a 1 in cur_idx.
            # so we can move cur_idx +1
            cur_idx +=1

    #print('arr:',arr)
    return arr










def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#edge case
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test_function([])

#
