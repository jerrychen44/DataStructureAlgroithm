'''
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data.
The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character.
The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm.
At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

    1.Take a string and determine the relevant frequencies of the characters.
    2.Build and sort a list of tuples from lowest to highest frequencies.
    3.Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
    4.Trim the Huffman Tree (remove the frequencies from the previously built tree).
    5.Encode the text into its compressed form.
    6.Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas.


'''
import sys
import heapq

#################
# Node section
#################
class Node():
    def __init__(self,char,frq):
        self.char = char
        self.frq = frq
        self.left = None
        self.right = None

    #because we want to use heapq to mantain the heap
    #we need to rewrite the comparsion
    #check the error msg below
    #TypeError: '<' not supported between instances of 'Node' and 'Node'
    # defining comparators less_than and equals

    def __lt__(self, other):
        return self.frq < other.frq
    def __gt__(self, other):
        return self.frq > other.frq
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.frq == other.frq


################
# Huffman section
################

def build_frequence(data):

    #space , T, t we treat as different char
    frq_dic={}#<key,freq>
    for c in data:
        if c not in frq_dic:
            frq_dic[c]=1
        else:
            frq_dic[c]+=1
    return frq_dic


def build_sorted_listOfHeapNode(freq_dict):

    #freq_sorted_node_list = []
    sorted_heap_node = []
    for key in freq_dict:
        #print(key)
        #<key,freq>
        newnode = Node(key,freq_dict[key])
        heapq.heappush(sorted_heap_node,newnode)

    #debug
    #for item in range(len(sorted_heap_node)):
    #    print(heapq.heappop(sorted_heap_node).frq)

    return sorted_heap_node

def bfs_print_tree(head):

    qu = []
    qu.append(head)
    while len(qu)!=0:
        cur = qu.pop(0)
        print('cur node:',cur.frq,cur.char)

        if cur.left:
            print(' left',cur.left.frq,cur.left.char)
            qu.append(cur.left)

        if cur.right:
            print(' right',cur.right.frq,cur.right.char)
            qu.append(cur.right)


def build_huffman_tree(sorted_heap_node):

    ##############
    # merged node from low freq to high freq
    #############
    while len(sorted_heap_node) >1:#the last one is the root node
        #pop out the lowest freq 1th and 2th
        node1 = heapq.heappop(sorted_heap_node)
        node2 = heapq.heappop(sorted_heap_node)
        #create the parent of node1,node2
        merged_node = Node('internal', node1.frq + node2.frq)
        merged_node.left = node1
        merged_node.right = node2

        #put the node back to heap with right place
        heapq.heappush(sorted_heap_node,merged_node)

    #print(sorted_heap_node)
    return sorted_heap_node[0]




def huffman_encode_helper(node,curcode):
    if node == None:
        return

    if node.char  != 'internal':
        encode_map_char_bit[node.char] = curcode
        #for decode
        encode_map_bit_char[curcode] = node.char

        return
    #if this is an internal node
    #keep recursive calling
    huffman_encode_helper(node.left,curcode+'0')
    huffman_encode_helper(node.right,curcode+'1')



def huffman_encode_char(root):
    curcode = ''
    huffman_encode_helper(root,curcode)


def get_encoded_text(text):
    #totally append together
	encoded_text = ""
	for character in text:
		encoded_text += encode_map_char_bit[character]
	return encoded_text


def huffman_encoding(data,encode_map_char_bit,encode_map_bit_char):

    if data == None or len(data) ==0:
        print('input data with some problem!')
        exit()
    #print('input:', data)
    ##########################################################################
    #1.Take a string and determine the relevant frequencies of the characters.
    ##########################################################################
    freq_dic = build_frequence(data)
    #print('freq_dic:',freq_dic)
    ##########################################################################
    #2.Build and sort a list of tuples from lowest to highest frequencies.
    # use Node as a storage
    ##########################################################################
    sorted_heap_node = build_sorted_listOfHeapNode(freq_dic)
    #print('sorted_heap_node:',sorted_heap_node)


    ##########################################################################
    #3.Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters.
    ##########################################################################
    huffmanTreeHead = build_huffman_tree(sorted_heap_node)
    #bfs_print_tree(huffmanTreeHead)


    ##########################################################################
    #4.Trim the Huffman Tree (remove the frequencies from the previously built tree).
    ##########################################################################
    #I keep the frq in the Node class var


    ##########################################################################
    #5.Encode the text into its compressed form.
    ##########################################################################
    #5.a build encode_map
    #left 0, right 1
    huffman_encode_char(huffmanTreeHead)
    #print(encode_map_char_bit)
    encoded_text = get_encoded_text(data)
    return encoded_text, huffmanTreeHead



def huffman_decoding(encoded_data,tree):
    ##########################################################################
    #6. Decode the text from its compressed form.
    ##########################################################################

    decoded_text = ''
    bitstream = ''

    for bit in encoded_data:
        bitstream += bit
        if bitstream in encode_map_bit_char:
            decoded_text +=encode_map_bit_char[bitstream]
            bitstream = ''
    return decoded_text


if __name__ == "__main__":
    codes = {}


    #########
    # test1
    ########
    encode_map_char_bit = {}
    encode_map_bit_char = {}
    print('test1')
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence,encode_map_char_bit,encode_map_bit_char)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    '''
    output:
        The size of the data is: 69

        The content of the data is: The bird is the word

        The size of the encoded data is: 36

        The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

        The size of the decoded data is: 69

        The content of the encoded data is: The bird is the word
    '''
    #########
    # test2
    ########
    encode_map_char_bit = {}
    encode_map_bit_char = {}
    print('test2')
    a_great_sentence = "How Are You today?"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence,encode_map_char_bit,encode_map_bit_char)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    '''
    output:
        The size of the data is: 67

        The content of the data is: How Are You today?

        The size of the encoded data is: 36

        The content of the encoded data is: 100011010011110110101100001110010110001111101111100101010010100001

        The size of the decoded data is: 67

        The content of the encoded data is: How Are You today?
    '''


    #########
    # test3
    ########
    encode_map_char_bit = {}
    encode_map_bit_char = {}
    print('test3')
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence,encode_map_char_bit,encode_map_bit_char)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    output:

        The size of the data is: 49

        The content of the data is:

        input data with some problem!
    '''
