def loop_size(node):
    dct = {}
    count = 0
    cur = node
    while cur:
        if cur in dct:
            return count - dct[cur]
        dct[cur] = count
        cur = cur.next
        count += 1
    return None