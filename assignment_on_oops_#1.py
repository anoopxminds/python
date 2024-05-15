#Create a class Book with properties id,name,author,publish_date.Use parameterised constructor to initialise values to the properties. 
class Book:
    def __init__(self, id, name, author, publish_date) :
        self.id = id
        self.name = name
        self.author = author
        self.publish_date = publish_date
        
    def __repr__(self):
        return 'Book({},{},{},{})'.format(self.id, self.name, self.author, self.publish_date)
    
    
    
    
books = Book(id="01", name="New Book", author="Anoop", publish_date="01-04-2024")
print(books.id)    
print(books.author)
print(books.name)
print(books.publish_date)

print("=============================================================================")

class Student:
    pass_mark  = 300
    college_name = "Collage of Engineering"
    def __init__(self, name, roll_number, total_mark):
        self.name = name
        self.roll_number = roll_number
        self.total_mark = total_mark
        
    def getMark(self):
        status = "Failed"
        if self.pass_mark <= self.total_mark:
            status = "Passed"
        return status
        
    

student1 = Student("Student 1", "001", 200)
student2 = Student("Student 2", "002", 100)
student3 = Student("Student 3", "003", 300)
student4 = Student("Student 4", "004", 400)

print("============= Status of Student 1 ======================")

print(f"Name : {student1.name} ")
print(f"Collage : {student1.college_name}")
print(f"status: {student1.getMark() }")
print(f"Achived mark: {student1.total_mark}")

print("============= Status of Student 2 ======================")

print(f"Name : {student2.name} ")
print(f"Collage : {student2.college_name}")
print(f"status: {student2.getMark() }")
print(f"Achived mark: {student2.total_mark}")

print("============= Status of Student 3 ======================")

print(f"Name : {student3.name} ")
print(f"Collage : {student3.college_name}")
print(f"status: {student3.getMark() }")
print(f"Achived mark: {student3.total_mark}")

print("============= Status of Student 4 ======================")

print(f"Name : {student4.name} ")
print(f"Collage : {student4.college_name}")
print(f"status: {student4.getMark() }")
print(f"Achived mark: {student4.total_mark}")