class DoubleEndedQueue():

	def __init__(self,lst=[]):
	    self.items = lst
	    self.len = len(lst)

	def isEmpty(self):
	    return self.items == []

	def enqueueFront(self, item):
	    self.items.append(item)
	    self.len += 1
	    self.visualise()

	def enqueueBack(self, item):
	    self.items.insert(0,item)
	    self.len += 1
	    self.visualise()

	def dequequeFront(self):
	    rm =  self.items.pop()
	    self.len -=1
	    self.visualise()
	    return rm

	def dequeueBack(self):
	    rm = self.items.pop(0)
	    self.len -=1
	    self.visualise()
	    return rm

	def visualise(self):
		print("="*40)
		for i in self.items:
			print(f" {i} ",end = "")
		print()
		print("="*40)

if __name__ == "__main__":
	dlst = DoubleEndedQueue([2,3,4])
	dlst.visualise()
	dlst.enqueueFront(5)
	dlst.enqueueBack(1)
	dlst.dequequeFront()
	dlst.dequeueBack()