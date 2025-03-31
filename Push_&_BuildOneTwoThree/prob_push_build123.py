class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    lst = [3, 2, 1]
    head = None
    for el in lst:
        head = push(head, el)
    return head