class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    head = None
    for i in s.split(' -> ')[:-1]:
        node = Node(int(i))
        if head is None:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node
    return head