class Node():
    """class Node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def stringify(node):
    """function to convert linked list to string"""
    string = ''
    while node is not None:
        string += f'{node.data} -> '
        node = node.next
    return string + 'None'
