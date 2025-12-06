#class variable
class Student:
    school_name='shss' #inside class
    def __init(self,name,rollno):
        self.n=name
        self.r=rollno
        Student.school_city="bhpl"
        print(Student.school_city,Student.school_name)
    def add_new(self):
        print(Student.school_city,Student.school_name,Student.school_code,Student.contact)

Student.contact=1234567890
obj=