class Student:
    school="abc"
    city="bhopal"

    def detail(self):
        print("from stu class")

# obj=Student

# obj.detail()
# Student.detail()

# print(obj.school,Student.school)

obj=Student()

obj.detail()
# Student.detail()

print(obj.school,Student.school)