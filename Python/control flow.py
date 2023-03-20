a = True
b = True
c = False
if (a and c):
    print("Hello")
elif a and b:
    print('World')
else :
    print("Hello world")

num1 = int(input("Enter values of number 1 : "))
num2 = int(input("Enter values of number 2 : "))
if(num1 > num2):
    print("Number 1 is greater than number 2")
elif (num1 < num2):
    print("Number 1 is less than number 2")
else:
    print("Error")

# Temperature Conditions
temp = int(input("Enter Today's Temperature"))
if(temp > 30):
    print("Its hot today try drinking lots of water")
elif(temp < 30 and temp > 20):
    print("It's Normal temperature today")
else:
    print("It's cold today")