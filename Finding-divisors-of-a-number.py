number = int (input("Enter a number: "))

for i in range(2, number + 1):
    if number % i == 0:
        print(i)