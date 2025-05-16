n=int(input("Enter the numbers:"))
if n < 15 :
    print(f"{n} is smaller than 15")
    print("I'm in the If block")
else:
    print(f"{n} is greater than 15")
    print("I'm in the ELSE block")

print("I'm not in the IF block and I'm not in the ELSE block")