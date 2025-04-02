class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new = head.next
    head.next = swap_pairs(new.next)
    new.next = head

    return new