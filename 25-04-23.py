def f(n):
    if n<=10:
        return
    print(n-1)         
    f(n-1)
    print(n-1)

f(13)




#fibonacci using recursion
def fibonacci(n):
    if (n < 0) :
        print("Enter a valid number")
    if (n ==1 ):
        return 0
    if n==2:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)      

print(fibonacci(5))
print(fibonacci(10))




#to calculate the sum of all fibonacci numbers
def fibonacciSeries(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    first, second  = 0, 1
    result = first + second
    for i in range(n-2):                   
        third = first + second
        result += third
        first = second
        second = third
    print(result)

fibonacciSeries(10)



#dictionary
my_dict = {
    "name": "sana", 
    "age" : 21, 
    "occupation" : "student"
}
print(type(my_dict))
print(my_dict["name"])
my_dict["name"] = "sanabi"                    
print(my_dict)

updated_name = {
    "name" : "Sanasana"
}
my_dict.update(updated_name)
print(my_dict["name"])




#Classes
class Car:
    engineType = "strongest Engine"
    numberOfTyers = 4
    numberOfWindow = 6
    isFridgeAValble = True


    def getNumberOfWindows(self):
        return self.numberOfWindow

    def getNumberOfTyres(self):
        return self.numberOfTyers

car1 = Car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())


