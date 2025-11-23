size = int(input("Enter the size of the pattern: "))   
while size >= 0:
    for i in range(size):
        for j in range(size):
                print("*", end="")
        print()