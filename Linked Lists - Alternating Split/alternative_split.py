class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise ValueError
    cur = head
    first = Node(cur.data)
    tail_1 = first
    i = 0
    if cur.next:
        second = Node(cur.next.data)
        tail_2 = second
        cur = cur.next
    while cur.next:
        cur = cur.next
        next_node = Node(cur.data)
        if i % 2 == 0:
            tail_1.next = next_node
            tail_1 = tail_1.next
        else:
            tail_2.next = next_node
            tail_2 = tail_2.next
        i += 1
        
    return Context(first, second)