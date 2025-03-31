class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise ValueError
    cur = node
    while index > 0:
        if cur.next is None:
            raise ValueError
        cur = cur.next
        index -= 1
    return cur
