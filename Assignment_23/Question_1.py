# Write Python Program to implement a class named BookStore with the following specifications:
# The class should contain two instance variables.
        # Name (Book Name)
        # Author (Book Author)
# The class should contain one class variable:
        # NoOfBooks(Initialize it to 0)
# Define a constructor (__init__) that accepts Name and Author and intitializes instance variables.
# Inside the constructor,increment the class variable NoOfBooks by 1 whenever a new object is created.
# Implement an instance method:
        # Display()- Should display book details in the format:
        # <BookName> by <Author>. No of Books: <NoOfBooks>

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name,"by",self.Author,". No of book :",self.NoOfBooks)

obj1 = BookStore("Wings of fire","APJ Abdul Kalam")
obj2 = BookStore("Rich dad Poor dad","Robert Kiyosaki")

obj1.Display()
obj2.Display()

