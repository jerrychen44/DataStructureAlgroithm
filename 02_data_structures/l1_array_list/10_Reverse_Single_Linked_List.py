#!/usr/bin/env python
# coding: utf-8

# # Reversing a linked list exercise
#
# Given a singly linked list, return another linked list that is the reverse of the first.

# In[ ]:


# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


# In[ ]:


def reverseinplace(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    #reversed in place
    prev = None
    cur = linked_list.head
    old = cur

    while cur != None:
        cur = cur.next
        old.next = prev
        prev = old
        old = cur

    linked_list.head = prev
    return linked_list


def reverseinNewLinked_list(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_list = LinkedList()

    node = linked_list.head

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to
    # the new linked list
    while node:
        old_head = new_list.head
        new_node = node
        node = node.next

        new_node.next = old_head
        new_list.head = new_node
    return new_list

# In[ ]:
def printList(list):

    tmp = list.head
    while tmp != None:
        print(tmp.value)
        tmp = tmp.next




llist1 = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist1.append(value)

llist2 = LinkedList()
for value in [90,2,5,1,-3,100]:
    llist2.append(value)



#printList(llist1)
#printList(reverseinNewLinked_list(llist1))


#printList(llist2)
#printList(reverseinNewLinked_list(llist2))

print(llist2)
print(reverseinplace(llist2))

print ("Pass" if (llist2 == reverseinplace(llist2)) else "Fail")


# <span class="graffiti-highlight graffiti-id_o7ebglo-id_s2dtp8f"><i></i><button>Show Solution</button></span>

a = [3,2,1]
b=  [2,3,1]

if a==b:
    print('=')
else:
    print('!=')
