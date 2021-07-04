import sys
sys.path.insert(1, '../data_structures/')
from node import Node
from linked_list import LinkedList

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

lnked_lst = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

lnked_lst.head = node1
node1.next = node2
node2.next = node3

check_cycle(lnked_lst)

node3.next = node1
check_cycle(lnked_lst)