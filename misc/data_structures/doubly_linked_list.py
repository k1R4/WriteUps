from node import Node

class DoublyLinkedList():

	def __init__(self,lst=[]):
		self.head=lst[0]
		for i in range(len(lst)-1):
			lst[i].next = lst[i+1]
		for i in range(len(lst)-1,0,-1):
			lst[i].prev = lst[i-1]

	def display_next(self):
		if self.head:
			current = self.head
			while True:
				print(current.data,end =" ")
				if current.next == None:
					break
				current = current.next
			print()

	def display_prev(self):
		if self.head:
			current = self.head
			while True:
				if current.next == None:
					break
				current = current.next
			while True:
				print(current.data,end=" ")
				if current.prev == None:
					break
				current = current.prev
			print()

if __name__ == "__main__":
	first = Node(1)
	second = Node(2)
	third = Node(3)
	dlst = DoublyLinkedList([first,second,third])

	dlst.display_next()
	dlst.display_prev()