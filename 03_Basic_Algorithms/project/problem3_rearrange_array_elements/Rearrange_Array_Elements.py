'''
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the
expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''
def merge(left,right):
    output = []

    lidx = 0
    ridx = 0

    while lidx < len(left) and ridx < len(right):
        if left[lidx] > right[ridx]:
            output.append(left[lidx])
            lidx +=1
        else:
            output.append(right[ridx])
            ridx +=1

    output += left[lidx:]
    output += right[ridx:]

    return output

def mergesort(arr):

    #print(arr)
    if len(arr) <=1:
        return arr

    #we want to know the half position of array
    #not the low, hig index as we done before
    low = 0
    hig = len(arr) #*** directly use len(arr) not len(arr) -1
    mid = low + (hig-low)//2
    #divide
    left  = arr[low:mid]
    right = arr[mid:hig]

    outputL = mergesort(left)
    outputR = mergesort(right)

    #merge
    merged_rst = merge(outputL,outputR)

    return merged_rst


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #sorted, chose a O(nlogn) algo.
    #merge sort
    sorted_input = mergesort(input_list)
    print('sorted_input:',sorted_input)


    #split to 2 number, O(n)
    rstnum = [0,0]
    powertenl = 0
    powertenr = 0

    for idx in range(len(sorted_input)-1,-1,-1):

        if idx%2 ==0:
            rstnum[0]=rstnum[0] + (sorted_input[idx]*pow(10,powertenl))
            powertenl +=1

        else:
            rstnum[1]=rstnum[1] + (sorted_input[idx]*pow(10,powertenr))
            powertenr +=1

    print(rstnum)
    return rstnum



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)
'''
sorted_input: [5, 4, 3, 2, 1]
[531, 42]
Pass
'''
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
'''
sorted_input: [9, 8, 6, 5, 4, 2]
[964, 852]
Pass
'''
#edge case
test_case = [[], [0,0]]
test_function(test_case)
'''
sorted_input: []
[0, 0]
Pass
'''

#edge case
test_case = [[9, 9,9, 9, 9, 9,9], [9999, 999]]
test_function(test_case)
'''
sorted_input: [9, 9, 9, 9, 9, 9, 9]
[9999, 999]
Pass
'''
