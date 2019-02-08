class MyBoxIterator:
	def __iter__(self):
		return self
		
	def __init__(self, my_list):
		self.my_list = my_list
		self.counter = 0
		
	def __next__(self):
		if self.counter < len(self.my_list):
			it = self.my_list[self.counter]
			self.counter += 1
			return it
		else:
			raise StopIteration
	
