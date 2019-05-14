'''
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return 'None of Node in this list'
        cur_head = self.head
        out_string = "    "
        while cur_head:# value/address
            out_string += str(cur_head.value)+ '/' + hex(id(cur_head))[-4:-1] + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    if llist_1.head == None and llist_2.head != None:
        llist_1.head = llist_2.head
        return llist_1
    elif llist_1.head == None and llist_2.head == None:
        return 'None of nodes could be union'

    # Your Solution Here
    appeared_map = {}

    tmpl1 = llist_1.head
    while tmpl1!=None:
        appeared_map[tmpl1.value] = 1
        if tmpl1.next == None:
            break
        tmpl1 = tmpl1.next


    #now tmpl1 is the tail of llist_1
    #print(tmpl1)
    curpointer = tmpl1

    #concatenate to the tail of list 1
    tmpl2 = llist_2.head
    while tmpl2 !=None:
        if tmpl2.value not in appeared_map:
            appeared_map[tmpl2.value] = 1
            curpointer.next = tmpl2
            curpointer = tmpl2
            tmpl2 = tmpl2.next
            curpointer.next = None
        else:
            tmpl2 = tmpl2.next


    #print(appeared_map)
    return llist_1



def intersection(llist_1, llist_2):
    # Your Solution Here
    appeared_map = {}
    tmpl1 = llist_1.head
    while tmpl1!=None:
        appeared_map[tmpl1.value] = 1
        if tmpl1.next == None:
            break
        tmpl1 = tmpl1.next

    #now tmpl1 is the tail of llist_1
    #print(tmpl1)
    curpointer = None
    llist_1.head = None#we reuse the list 1


    #reassign list1.head when we found the intersection item in list2
    #we rebuild link at the same time when we looping the list2
    tmpl2 = llist_2.head
    while tmpl2 !=None:

        #find intersection node
        if tmpl2.value in appeared_map and appeared_map[tmpl2.value] ==1:
            appeared_map[tmpl2.value] += 1
            #first intersection node, we assign the head
            if llist_1.head == None:
                llist_1.head = tmpl2
                tmpl2 = tmpl2.next
                llist_1.head.next = None
                curpointer = llist_1.head
            else:
                #we linked the next pointer to intersection nodes
                curpointer.next = tmpl2
                curpointer = tmpl2
                tmpl2 = tmpl2.next
                curpointer.next = None
        else:
        #not an intersection node, keep looping list2
            tmpl2 = tmpl2.next


    #print(appeared_map)
    return llist_1




#####################
# testing section
#####################

# Test case 1
print('test case 1')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

#print(linked_list_1)
#print(linked_list_2)
print('union')
print (union(linked_list_1,linked_list_2))
'''
output:
union
    3/78d -> 2/790 -> 4/794 -> 35/797 -> 6/79b -> 65/79e -> 6/7a2 -> 4/7a5 -> 3/7a9 -> 21/7ac -> 32/7b3 -> 9/7ba -> 1/7c1 -> 11/7c5 ->
'''


################
# because I reused the list1, so the list1 has been changed as ans which doesn't need extra space.
# if you need test intersection, please redefined another list1b again
################


linked_list_1b = LinkedList()
linked_list_2b = LinkedList()

for i in element_1:
    linked_list_1b.append(i)

for i in element_2:
    linked_list_2b.append(i)

print('intersection')
print (intersection(linked_list_1b,linked_list_2b))
'''
output:

intersection
    6/7eb -> 4/7f2 -> 21/008 ->
'''



# Test case 2
print('test case 2')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print('union')
print (union(linked_list_3,linked_list_4))
'''
output:
union
    3/7ef -> 2/7b7 -> 4/789 -> 35/7cf -> 6/7d3 -> 65/7d6 -> 6/7da -> 4/7dd -> 3/7e1 -> 23/7e4 -> 1/7be -> 7/00b -> 8/004 -> 9/00f -> 11/012 -> 21/016 ->
'''

linked_list_3b = LinkedList()
linked_list_4b = LinkedList()


for i in element_1:
    linked_list_3b.append(i)

for i in element_2:
    linked_list_4b.append(i)
print('intersection')
print (intersection(linked_list_3b,linked_list_4b))

'''
output:
intersection
None of Node in this list
'''


# Test case 3
print('test case 3')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print('union')
print (union(linked_list_5,linked_list_6))

'''
output:

union
    3/024 -> 2/027 -> 4/02b -> 35/02e -> 6/032 -> 65/035 -> 6/039 -> 4/03c -> 3/01d -> 23/05c ->

'''


linked_list_5b = LinkedList()
linked_list_6b = LinkedList()


for i in element_1:
    linked_list_5b.append(i)

for i in element_2:
    linked_list_6b.append(i)
print('intersection')
print (intersection(linked_list_5b,linked_list_6b))
'''
output:

intersection
None of Node in this list
'''


# Test case 4
print('test case 4')
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
print('union')
print (union(linked_list_7,linked_list_8))

'''
output:

union
    1/071 -> 7/074 -> 8/078 -> 9/07b -> 11/07f -> 21/082 -> 1/063 ->

'''


linked_list_7b = LinkedList()
linked_list_8b = LinkedList()


for i in element_1:
    linked_list_7b.append(i)

for i in element_2:
    linked_list_8b.append(i)
print('intersection')
print (intersection(linked_list_7b,linked_list_8b))
'''
output:

intersection
None of Node in this list
'''

# Test case 5
print('test case 5')
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)
print('union')
print (union(linked_list_9,linked_list_10))
'''
output:

union
None of nodes could be union


'''

linked_list_9b = LinkedList()
linked_list_10b = LinkedList()


for i in element_1:
    linked_list_9b.append(i)

for i in element_2:
    linked_list_10b.append(i)
print('intersection')
print (intersection(linked_list_9b,linked_list_10b))
'''
output:

intersection
None of Node in this list
'''
