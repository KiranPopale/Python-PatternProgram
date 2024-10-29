
row=5

# * half pyramid pattern
for i in range (1,row+1):
    for j in range (1,i+1):
        print("*",end=" ")
    print()


# 123 half pyramid pattern
for i in range (1,row+1):
    for j in range (1,i+1):
        print(i,end=" ")
    print()

# 1start half pyramid pattern
for i in range (1,row+1):
    val=1
    for j in range (1,i+1):
        print(val,end=" ")
        val+=1
    print()

# alphabets A start half pyramid pattern
for i in range (1,row+1):
    val=65
    for j in range (1,i+1):
        print(chr(val),end=" ")
        val+=1
    print()

# alphabets A,B,C row start half pyramid pattern
val=65
for i in range (1,row+1):
    for j in range (1,i+1):
        print(chr(val),end=" ")
    val+=1
    print()

# * full pyramid pattern
for i in range (1,row+1):
    for space in range(i,row):
        print(end=" ")
    for j in range (1,i+1):
        print("*",end=" ")
    print()

# 1,2,3 row full pyramid pattern
for i in range (1,row+1):
    for space in range(i,row):
        print(end=" ")
    for j in range (1,i+1):
        print(i,end=" ")
    print()

# 1 each row start full pyramid pattern
for i in range (1,row+1):
    val=1
    for space in range(i,row):
        print(end=" ")
    for j in range (1,i+1):
        print(val,end=" ")
        val+=1    
    print()

# Alphabet A,B,C row start full pyramid pattern
val=65
for i in range (1,row+1):
    for space in range(i,row):
        print(end=" ")
    for j in range (1,i+1):
        print(chr(val),end=" ")
    val+=1
    print()

# Alphabet A each row start full pyramid pattern
for i in range (1,row+1):
    val=65
    for space in range(i,row):
        print(end=" ")
    for j in range (1,i+1):
        print(chr(val),end=" ")
        val+=1    
    print()
#END OF CODE

