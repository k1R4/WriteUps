class Stack():

	def __init__(self,lst=[]):
		self.items = lst
		self.len = len(lst)

	def empty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)
		self.len += 1
		self.visualise()

	def pop(self):
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
	stk = Stack([1,2,4])
	stk.visualise()
	stk.push(8)
	stk.push(33)
	stk.pop()