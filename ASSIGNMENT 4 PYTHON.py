ANSWER 1

x=float(input("Enter your grade-"))
if x>80:
    print("Your grade is A")
if 60<x<=80 :
    print("Your grade is B")
if 50<x<=60:
    print("Your grade is C")
if 45<x<=50:
    print("Your grade is D")
if 25<x<=50:
    print("Your grade is E")
if x<=25:
    print("your grade is F")


ANSWER 2

x=int(input("Enter the year to be analyzed--"))
if x%4==0:
    print("The given year is a leap year")
elif x%100==0 and x%400==0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")

ANSWER 3

import random

i=0
while i<10:
    i=i+1
    x=random.randint(1,10)
    y=random.randint(1,10)
    z=x*y
    print("Multiply-            ",x,"x",y)
    answer=int(input("Input your answer--"))
    if answer==z:
        print("Your answer is correct")
    else:
        print("your answer is incorrect, The correct answer is",z)


ANSWER 4

#let x be the amount of candy in the bowl
for i in range(200):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i,"Number of candies are present in the Box!!")
