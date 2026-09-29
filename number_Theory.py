#Number theory and mathing system
xtra= int(input("enter the number: "))

for x in range(1, xtra):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 5 ==0:
        print("Buzz")
    elif x % 3 ==0:
        print("Fuzz")
    else:
        print(x)
