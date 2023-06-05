'''
Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the
student name and class.
'''
def student_data(name,student_id,student_class ):
    print(f'student name is {name},sid is {student_id}, class is {student_class}')
    
print(" write your name , id and class respectively")
name = input()
id = input()
class_ = input()

student_data(name,id,class_)
