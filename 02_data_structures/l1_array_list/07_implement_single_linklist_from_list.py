
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list_better(input_list):
    head = None
    size = len(input_list)

    if size ==0:
        return None

    head = Node(input_list[0])
    tmp = head


    for idx in range(1,size):
        tmp.next = Node(input_list[idx])
        tmp = tmp.next

    return head



### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)



input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
