from node import Node

class LinkedList():

	def __init__(self):
		self.head = None

	def display(self):
		if self.head:
			current = self.head
			while True:
				print(current.data,end =" ")
				if current.next == None:
					break
				current = current.next
			print()

if __name__ == "__main__":
	lst = LinkedList()
	lst.head = Node("first")
	second = Node("second")
	third = Node("third")
	lst.head.next = second
	second.next = third

	lst.display()