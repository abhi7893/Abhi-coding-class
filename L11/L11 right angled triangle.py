print("half Pyramid Pattern of stars (*):")
n = int(input("enter the number of rows: "))

for i in range(n): #outer loop to handle of rows
    for j in range(i+1): #inner loop to handle number of columns
        print("* ", end="") #display result

    print()