from node import Node

class LinkedList():

	def __init__(self,lst=[]):
		self.head = lst[0]
		for i in range(len(lst)-1):
			lst[i].next = lst[i+1]

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
	first = Node(1)
	second = Node(2)
	third = Node(3)
	lst = LinkedList([first,second,third])

	lst.display()