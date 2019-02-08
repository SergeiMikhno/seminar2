from myclass import Person
from myclass import Student
from myboxiterator import MyBoxIterator

class MyBox:
	def __init__(self, container = None):
		if container == None:
			self.container = []
		elif type(container) is list:
			if len(container)== 0:
				self.container = container
			else:
				flag = 0
				for elem in container:
					if type(elem) is not Student:
						print("The container contains an item of the wrong type.")
						flag = 1
						break
				if flag == 0:
					self.container = container
	
	def len(self):
		return len(self.container)
	
	def add(self, obj):
		if type(obj) is Student:
			if obj in self.container:
				print("This object is already contained in a container.")
			else:
				self.container.append(obj)
		else:
			print("An object of this type cannot be added to the container.")
			
	def remove(self, obj):
		if obj in self.container:
			self.container.remove(obj)
		else:
			print("This object is not contained in a container.")
			
	def contains(self, obj):
		if obj in self.container:
			return True
		return False
		
	def iterator(self):
		return MyBoxIterator(self.container)
			
	
		
					
		
