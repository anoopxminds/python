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