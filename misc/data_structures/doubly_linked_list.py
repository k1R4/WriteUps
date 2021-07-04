from node import Node

class DoublyLinkedList():

	def __init__(self,head=None):
		self.head=head

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
	dlst = DoublyLinkedList(first)
	second = Node(2,first)
	third = Node(3,second)
	first.next = second
	second.next = third

	dlst.display_next()
	dlst.display_prev()