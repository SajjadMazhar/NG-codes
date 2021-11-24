#Task - create a program for a Library, where Students can take out and return books. The library can lend, and update the collection (when a student returns books)
#Here we will be demonstrating abstraction and encapsulation (more on encaspulation later)
#=======For the Library Class, layers of abstraction ==> *display available books, *lend books, *add books
#=======For the Student Class, layers of abstraction: ==> *request a book* and *return a book*
#Note for abstraction: You are only dealing with the important and relevant details of a library...not the irrevelant details like no. of shelves, or the cobwebs on the cielings!
"""
Task: Based on the creation of this class implementation of a library management system, try and attempt the following:
>>Car rental system.
Your program should perform the following:
1. SUV, Sports and Hatchback are the type of cars that are available for rent
2. Cost per day: Hatchback - �10 Sedan - �100 SUV - �200
3. Prompt the customer for: Type of Car, and the no. of days he would like to borrow the car for.
4. Provide the fare details/output to the customer.

"""
import sys
class Library:
      def __init__(self,listofbooks):#this init method is the first method to be invoked when you create an object
            #what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")
            

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

def main():            
      library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()
                  
main()
