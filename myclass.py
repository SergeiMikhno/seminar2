class Person:

	def __init__(self, name = "n/a", age = 0):
		self.name = name
		self.age = age

	def set_person(self, name, age):
		self.name = name
		self.age = age
        
	def get_person_name(self):
		return self.name
		
	def get_person_age(self):
		return self.age
		
	def change_person_name(self, name):
		self.name = name
		
	def change_person_age(self, age):
		self.age = age
		
		
class Student (Person):

	def __init__(self, name = "n/a", age = 0, course = 0):
		super().__init__(name, age)
		self.course = course

	def set_student(self, name, age, course):
		self.set_person(name, age)
		self.course = course
    
	def description_of_person(self):
		print('______________________________________________________________________________')
		print('Hi! My name is',self.name)
		print("I'm",self.age,'years old')
		print ('I study for',self.course,'course in a magistracy in the Astana International University')
		print('______________________________________________________________________________')
        
	def get_student_name(self):
		return self.get_person_name()
	
	def get_student_age(self):
		return self.get_person_age()
		
	def get_student_course(self):
		return self.course
		
	def change_student_name(self, name):
		self.change_person_name(name)
		
	def change_student_age(self, age):
		self.change_person_age(age)
		
	def change_student_course(self, course):
		self.course = course
		
        
