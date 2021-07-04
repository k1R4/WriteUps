from node import Node

class CircularLinkedList():

	def __init__(self,lst=[]):
		self.head = lst[0]
		for i in range(len(lst)-1):
			lst[i].next = lst[i+1]
		for i in range(len(lst)-1,0,-1):
			lst[i].prev = lst[i-1]
		lst[0].prev = lst[len(lst)-1]
		lst[len(lst)-1].next = lst[0]

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
	second = Node(2)
	third = Node(3)
	clst = CircularLinkedList([first,second,third])

	clst.display()
	clst.display(second)