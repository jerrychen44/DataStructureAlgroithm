'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your
algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
'''

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list)==0:
        print('empty list, return -1')
        return -1

    #find the junction
    rstidx = rotated_array_search_helper(input_list,0,len(input_list)-1,number)
    print('rstidx:',rstidx)
    return rstidx


'''
Note:
    #核心的 idea 還是binary search, 只是現在因為 roated 了, 不確定要丟哪半邊去 recursive call
    #利用到底 pivot 在中心左邊還是右邊

    #code steps:
    #找出還有 sorted 屬性的那些數  (因為如果pivot 在 mid 右邊,  mid~end 這些數會亂掉,失去鑑別力, 因此只剩下左半邊擁有完整的sorted 力量)
    #這時我們拿這左半邊出來, 當作檢查 target 的依據
    #   (因為沒有人說target 在左邊歐, 這時候我們並不知道, target 也有可能在右邊)
    #所以我們接下來要用範圍來判斷target 是不是在左邊, if target>=A[start] && target<A[mid] ==  True 的話,
    #那就表示 target 真的在左半邊, 所以丟 recursive fun arr[start:mid-1] 下去
    #如果false, 那就是target 在右邊, 丟 recursive fun arr[mid+1:end] 下去
    #key: 你看到了嗎？ 要判斷 target 是不是這半邊, 需要 if target>=A[start] && target<A[mid], 可是如果 start~mid 中間參雜了
    # 原始的第一個數, 也就是參雜了一個最小的數, 那這個 if target>=A[start] && target<A[mid] 的範圍根本不準, 這也就是為什麼
    # 要先分出哪邊的區間, 裡面的數還保持完整的sorted 數列, 這樣用 if target>=A[start] && target<A[mid] 才有意義
'''
def rotated_array_search_helper(input_list,low,hig,target):


    if low > hig:
        return -1

    mid = (low+hig)//2

    mid_val = input_list[mid]

    # three cases for rotated array
    # original : [0,1,2,4,5,6,7] ---> rotated [4,5,6,7,0,1,2], mid = 7

    #case0: arr[mid] == target: return mid
    #
    #case1: a.real start element at right hand side. ex: [4,5,6,"7",0,1,2], which means the Left hand side of mid is USEABLE.
    #       b.[low=0:mid-1] still with sorted property,
    #       c.how can we distinguish this case?
    #           arr[mid] > arr[low] > arr[hig]
    #
        # if we hit in case1:
        #   Use the serise [low=0:mid-1] to loacte the target value
        #       if target in [low=0:mid-1], then recursive call the arr[low:mid-1]
        #               else: recursive call the arr[mid-1:hig]

    #case2: real start ele at the left hand side.
    #       a.ex: [6,7,0,"1",2,4,5],
    #       b. arr[mid+1:hig=size-1] still with sorted property
    #       c. arr[mid] < arr[hig] < arr [low]
        # if we hit in case2:
        #   Use the serise [mid+1:hig=size-1] to loacte the target value
        #       if target in [mid+1:hig=size-1], then recursive call the arr[low:mid-1]
        #               else: recursive call the arr[mid+1:hig=size-1]


    #base case, case1:
    if mid_val == target:
        return mid

    #case1: pivot at right, we can use the sorted number in left hand side to locate the target.
    if input_list[hig] < mid_val:

        #locate where is the target
        if ( target < mid_val and target >= input_list[low]):
            return rotated_array_search_helper(input_list,low,mid-1,target)
        else:
        #target at right side
            return rotated_array_search_helper(input_list,mid+1,hig,target)


    else:
    #case2: pivot at left, we can use the sorted number in right hand side to locate the target.
        #locate where is the target
        if ( target > mid_val and target <= input_list[hig]):
            return rotated_array_search_helper(input_list,mid+1,hig,target)
        else:
        #target at left side
            return rotated_array_search_helper(input_list,low,mid-1,target)





def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linear_rst = linear_search(input_list, number)
    print('linear_rst:',linear_rst)
    if linear_rst == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
'''
linear_rst: 0
rstidx: 0
Pass
'''
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
'''
linear_rst: 5
rstidx: 5
Pass
'''
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
'''
linear_rst: 2
rstidx: 2
Pass
'''
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
'''
linear_rst: 3
rstidx: 3
Pass
'''
#edge case
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
'''
linear_rst: -1
rstidx: -1
Pass
'''
#edge case
test_function([[], 1])
'''
linear_rst: -1
empty list, return -1
Pass
'''
