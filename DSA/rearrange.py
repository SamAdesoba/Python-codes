import collections

from pythonProject.DSA import linked_list
from pythonProject.DSA.linked_list import LinkedList


def rearrange_element(head : collections.deque):
    prev = None
    current = head
    next = head.next
    while current is not None:
        next = current.next
        # chang the direction of the nodes
        current.next = prev
        # shifting the nodes
        prev = current
        current = next
    head = prev
    return head


llist = collections.deque()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

print(rearrange_element(llist))
