from myclass import Person
from myclass import Student
from myboxiterator import MyBoxIterator
from mybox import MyBox

Student_1 = Student('Anton', 20, 3)
Student_2 = Student('Mariya', 19, 2)
Student_3 = Student('Pavel', 21, 4)
Student_4 = Student('Viktor', 21, 3)
myBox = MyBox([Student_1, Student_2])
itr = myBox.iterator()
for student in itr:
	print(student.get_student_name(), student.get_student_age(), student.get_student_course())
print('')
myBox.add(Student_3)
itr = myBox.iterator()
for student in itr:
	print(student.get_student_name(), student.get_student_age(), student.get_student_course())
	
print(myBox.len())

myBox.remove(Student_4)
myBox.remove(Student_2)
itr = myBox.iterator()
for student in itr:
	print(student.get_student_name(), student.get_student_age(), student.get_student_course())
myBox.add(1)
if myBox.contains(Student_1):
	print("!")


