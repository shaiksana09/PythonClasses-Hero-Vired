class Book:
    numofpages = 145
    author = "sana"
    scope = "to be sold in India"
    
    def __init__(self, zone):
        self.zone = zone

my_book = Book("Mystery")
print(my_book.numofpages)
print(my_book.zone)



class Book:
    numofpages = 145
    author = "sana"
    scope = "to be sold in India"
    
    def __init__(self, zone, dob):
        self.zone = zone
        self.dob = dob

my_book = Book("Mystery", '26-04-23')
print(my_book.numofpages)
print(my_book.zone)
print(my_book.dob)


#destructor
class Book:
    numofpages = 145
    author = "sana"
    scope = "to be sold in India"
    
    def __init__(self, zone, dob):
        self.zone = zone
        self.dob = dob
    
    def __del__(self):
        print("destructor is called")

my_book = Book("Mystery", '26-04-23')
print(my_book.numofpages)
print(my_book.zone)
print(my_book.dob)
del my_book
print(my_book.zone)       
#o/p: the object my_book is not defined


#single inheritance
class School:
    name = "KRPS"
    
    def __init__(self, age):
        self.age = age
    def getAge(self):
        return self.age
        
class Subschool(School):
    def __init__(self):
        print("child instructor")
    def getparentname(self):
        return "KRPS"
    def getName(self):
        return 'Gyan Sagar'
        
my_school = Subschool()
print(my_school.getParentname())
print(my_school.getName())


#multiple inheritance
class parent1:
    def getname(self):
        return "parent1"
        
class parent2:
    def getname(self):
        return "parent2"
        
class parent3:
    def getname(self):
        return "parent3"

class child(parent1, parent2, parent3):
    def __init__(self):
        self.getAllParent()
    def getAllParent(self):
        print("trying to get all the parents")
        parent_list = []
        for base in Child.__bases__:
            parent_list.append(base)
        print(parent_list)
my_child = child()
#for base in Child.__bases__:
#    print(base, end = " ")
#print(my_child.__bases__)
#print(my_child.getname())



#signature arguments
def addNumbers(a, b):
    print(a+b)

def addNumbers2(*args):
    sum = 0
    for value in args:
        sum += value
    print(sum)
    
addNumbers2(10)
addNumbers2(10, 20)
addNumbers2(10, 20, 30)
 
def addNumbers3(arg1, arg2, *arg3):
    print(arg1, arg2, arg3)
    
addNumbers3(10, 20, 30)
addNumbers3(10, 20, 30, 40, 50, 60)

def addNumbers(a, b, c=2):
    print(a+b+c)
    
addNumbers(10, 20)
addNumbers(10, 20, 30)



def dojob(arg1, arg2, arg3):
    print("sana")

def dojob(arg1):
    print("shaik sana mehaboob bi")
    
dojob(10)
dojob(10, 20, 30)
    

class Library:
    book = []
    my_book = {}
    def getAllbooks():
        pass
    def addBook():
        pass
    def getBooksbyauthorname():
        pass
    def sortBooksintopologicalorder():
        pass
    def getAllsubscribers():
        pass
    def getAllearnings():
        pass
    def getUnavailablebooks():
        pass

class Mylibrary(Library):
    #it can not have it's own data structure to store 
    
    def getFaviouratebook():
        pass
    def getFaviouratecustomer():
