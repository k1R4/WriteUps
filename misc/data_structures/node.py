class Node:
	def __init__(self,data=None,prev=None,nxt=None):
		self.data = data
		self.next = nxt
		self.prev = prev

if __name__ == "__main__":
	node = Node("node_value")
	print(node.data)