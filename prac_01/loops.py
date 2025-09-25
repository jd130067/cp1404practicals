for i in range(1, 21, 2):
    print(i, end=' ')
print()


# QUESTION A
print ("\n Loop A: ")
for i in range(0,101,10):
    print(i, end = ' ')

# QUESTION B
print ("\n Loop B: ")
for i in range(20,0,-1):
    print(i, end = ' ')

# QUESTION C
print ("\n Loop C: ")
num_stars_C = int(input("Input Integer Number of Stars: "))
for i in range(0, num_stars_C, 1):
    print("*", end='')

# QUESTION D
print ("\n Loop D: ")
numLines = int(input("Input Integer Number of Lines: "))
for i in range(0, numLines, 1):
    for j in range(0,i+1, 1):
        print("*", end='')
    print()