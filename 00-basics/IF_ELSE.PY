marks=int(input("Enter the marks"))

if(marks>=90):
    Grade="A"
elif(marks>=80 and marks<=90):
    Grade="B"
elif(marks>=70 and marks<=80):
    Grade="C"
else:
    Grade="D"

print("Grade of the student-->",Grade)

## odd and even from user input

num=int(input("Enter the number"))

rem=num%2

if(rem==0):
    print("Even")
else:
    ("Odd")

## find greatest of 3 number

a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))

if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third largest ",c)