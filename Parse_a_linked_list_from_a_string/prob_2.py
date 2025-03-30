class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    head = None
    tail = None
    for el in s.split():
        if el != '->' and el != 'None':
            new_node = Node(el)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
    return head