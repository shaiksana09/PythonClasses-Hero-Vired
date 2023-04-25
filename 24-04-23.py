
def addNumbers():
    try: 
        a = int(input())
    except ValueError as err:
        print(err)
    try: 
        b = int(input())
    except ValueError as err:
        print(err)
    print(a+b)
    
addNumbers()




def addNumbers():
    a = 10
    b = 20
    return (a+b)
sum = addNumbers()
print(sum)




def addNumber(a, b):
    return a+b
sum = addNumber(10, 20)
print(sum)




def returningMultipleValues():
    return 10, 20, 20
output = returningMultipleValues()
print(output)




#fibonacci series
def fibonacciSeries(n):
    if n<=0:
        print("Inavlid argument")
        return -1
    if n==1:
        print(0)
        return -1
    if n==2:
        print(0)
        print(1)
    if(n>=3):
        first = 0
        second = 1
        print(first)
        print(second)
        for i in range(n-2):
            third = first + second
            first = second
            second = third
            print(third)
n = int(input("Enter a range: "))
fibonacciSeries(n)




# finding hcf
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
HCF = 1
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i
 
print("First Number is: ",a)
print("Second Number is: ",b)
print("HCF of the numbers is: ",HCF)




#finding lcf
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
 
HCF = 1
 
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i
 
print("First Number is: ",a)
print("Second Number is: ",b)
 
LCM = int((a*b)/(HCF))
print("LCM of the two numbers is: ",LCM)




def do(n):
    if n<=2:
        return       
    print(n)
    do(n-1)
    print(n)

do(10)




def do(n):
    if n<=5:
        return       
    do(n-1)
    print(n)
    do(n-1)
    print(n)

do(8)
