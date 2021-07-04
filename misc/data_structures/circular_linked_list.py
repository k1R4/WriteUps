from node import Node

class CircularLinkedList():

	def __init__(self,head=None):
		self.head = head

	def display(self,node=None):
		if node == None:
			node = self.head
		current = node
		while True:
			print(current.data,end=" ")
			current = current.next
			if current == node:
				break
		print()

if __name__ == "__main__":
	first = Node(1)
	clst = CircularLinkedList(first)
	second = Node(2,first)
	third = Node(3,second,first)
	first.next = second
	second.next = third

	clst.display()
	clst.display(second)