class Queue():

	def __init__(self,lst=[]):
		self.items = lst
		self.len = len(lst)

	def empty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)
		self.len += 1
		self.visualise()

	def dequeue(self):
		if self.empty():
			return "Underflow"
		rm = self.items.pop()
		self.len -= 1
		self.visualise()
		return rm

	def visualise(self):
		print("="*40)
		for i in self.items:
			print(f" {i} ",end = "")
		print()
		print("="*40)

if __name__ == "__main__":
	q = Queue([2,3,5])
	q.visualise()
	q.enqueue(7)
	q.enqueue(11)
	q.dequeue()