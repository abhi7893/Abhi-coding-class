#take two input from user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print()
print("Prime numbers between", lower, "and", upper, "are:")

#display the result
for num in range(lower, upper + 1):
    if num > 1: 
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)