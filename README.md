# Finding-divisors-of-a-number

## Task 3 - finding divisors of a number 
Your task is to write a program which prints all the divisors of a number. The number comes from the user's input.

Some of your results could look like this:
Enter number: 56
2
4
7
8
14
28
56'''


## Solution

number = int (input("Enter a number: "))

for i in range(2, number + 1):
    if number % i == 0:
        print(i)
