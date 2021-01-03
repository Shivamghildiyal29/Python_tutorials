num = [1, 2, 3, 4, 5]
# i in num will represent the value in the list and with each iteration jumps to the next value
for i in num:
    print(i)

#Break keyword: breaks the loop when the condition is met
for i in num:
     if i==4:
            print("Found it")
            break #breaks the loop
     else:
        print(i)

#Continue: skip the iteration whenever required
for i in num:
        if i==4:
            print("Found it")
            continue #skips to the next iteration
        else:
               print(i)



#Nested looping, a loop inside another loop
for i in num:
     for l in "ABCD":
        print(i, l)


#using range for definite number of iteration
for i in range(10): #the value of i will go from 0 to 9 and run the loop 10 times
    print(i)

for i in range(1:11): #the value of i will go from defined range of  1 to 10 and run the loop 10 times
    print(i)


#WHILE loop: runs the conition until the given conitions are met
x=0
while x<5:
    print(x)
    x+=1

#Using Break
x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1

#if the conitions are not met, the loop can execute infinite times, break command is used to break the loop
x=0
while x>=0:
   # if x==10:
    #    break
    print(x)
    x+=1

