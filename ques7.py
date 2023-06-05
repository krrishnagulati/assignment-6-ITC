class Student:
    pass

class Marks:
    pass


student = Student()
marks = Marks()
#the first argument is the instance we want to check, and the second argument is the class we want to check against.
#If the instance is an instance of the class, isinstance() returns True, otherwise False

print(isinstance(student, Student))  
print(isinstance(marks, Marks))  


print(issubclass(Student, object))  
print(issubclass(Marks, object))  
