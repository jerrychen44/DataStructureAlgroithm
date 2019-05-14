'''
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache.
If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element.
After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

Your job is to use appropriate data structure(s) to implement the cache.

    1.In case of a cache hit, your get() operation should return the appropriate value.
    2.In case of a cache miss, your get() should return -1.
    3.While putting an element in the cache, your set() operation must insert the element.
        If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take O(1) time.
'''

'''
#code templeate
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass

our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
'''
class Node():
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.keyNodemap = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.numele = 0

    #O(1)
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        #hit
        if key in self.keyNodemap:
            return self.keyNodemap[key].val
        #miss
        return -1
    #O(1)
    def set(self, key, value):

        if self.capacity ==0:
            return -1
        ########################
        #case 1, if key is new
        #########################
        if key not in self.keyNodemap:

            newnode = Node(key,value)
            self.keyNodemap[key] = newnode

            #if list over capacity, delete oldest task(head)
            if self.numele > self.capacity-1:
                #del oldest = del head
                #only have one element (head == tail)
                if self.numele == 1:
                    tmpnode = self.head
                    self.head  = None
                    self.tail = None
                    self.keyNodemap.pop(tmpnode.key, None)
                    del tmpnode
                    self.numele -=1

                else:#more then one element, move head right
                    tmpnode = self.head
                    self.head = tmpnode.next
                    self.head.prev = None
                    self.keyNodemap.pop(tmpnode.key, None)
                    del tmpnode
                    self.numele -=1



            #if the list is empty
            if self.numele == 0:
                self.tail = newnode
                self.head = newnode
                self.numele+=1
                return




            #append to tail
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.numele+=1

        else:
        ###########################
        #case2 key already exist, update val and order
        ###########################
            #update value
            newnode = self.keyNodemap[key]
            newnode.val = value
            #update order

            # if newnode is tail, do nothing
            if self.tail != newnode:
                #move to tail
                #if newnode is head now
                if self.head == newnode:
                    #move head
                    self.head = newnode.next
                    self.head.prev = None

                    #append to tail
                    self.tail.next = newnode
                    newnode.prev = self.tail
                    newnode.next = None
                    self.tail = newnode
                else:
                    #newnode not head and not tail
                    #  head->prenode -> newnode -> nextnode->tail
                    prenode = newnode.prev
                    nextnode = newnode.next
                    #connect prevnode , nextnode
                    prenode.next = newnode.next
                    nextnode.prev = newnode.prev

                    #append to tail
                    self.tail.next = newnode
                    newnode.prev = self.tail
                    newnode.next = None
                    self.tail = newnode



    def printlist(self):
        tmp = self.head
        rsts = ''
        while tmp != None:
            rsts = rsts + '[' + str(tmp.key) +','+str(tmp.val) +']'

            tmp = tmp.next
        print(rsts)

#test case 1

print('== test case 1')
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))     # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(3))      # return -1

'''
output:
-1
2
-1
'''


print('== test case 2')
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.printlist()
our_cache.set(4, 4)
our_cache.printlist()
print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))
print(our_cache.get(4))
print(our_cache.get(1))
our_cache.printlist()
our_cache.set(3, 99)
our_cache.printlist()
print(our_cache.get(3))
our_cache.printlist()
'''
output:
[1,1][2,2][3,3]
[2,2][3,3][4,4]
-1
2
3
4
-1
[2,2][3,3][4,4]
[2,2][4,4][3,99]
99
[2,2][4,4][3,99]
'''


print('== test case 3')
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1))
'''
output:
-1
'''


print('== test case 4')
our_cache = LRU_Cache()
our_cache.set(1, 1)
our_cache.set(2, 33)
our_cache.printlist()
our_cache.set(1, 91)
our_cache.printlist()

print(our_cache.get(2))
'''
output:
[1,1][2,33]
[2,33][1,91]
33
'''
