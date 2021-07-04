import sys
sys.path.insert(1, '../data_structures/')
from node import Node
from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList
from circular_linked_list import CircularLinkedList

def check_cycle(lst):
	current = lst.head
	while True:
		if current.next == None:
			print("no cycle")
			break
		elif current.next == lst.head:
			print("cycle exists")
			break
		else:
			current = current.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

lnked_lst = LinkedList([node1,node2,node3])
check_cycle(lnked_lst)

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

dbly_lnked_lst = DoublyLinkedList([node4,node5,node6])
check_cycle(dbly_lnked_lst)

node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

crclr_lnked_lst = CircularLinkedList([node7,node8,node9])
check_cycle(crclr_lnked_lst)