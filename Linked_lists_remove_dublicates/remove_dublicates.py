class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    now = head
    while now.next is not None:
        if now.next.data == now.data:
            now.next = now.next.next
        else:
            now = now.next
    return head