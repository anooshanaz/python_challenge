#Day 3 python challenge:

#write a program which check the number is prime number or not
x = int(input("Enter your number:"))
if x > 1:
        for i in range(2, x):
            if x % 2 == 0:
                print(x,"It is not a prime number")
        else:
                print(x,"It is a prime number")
