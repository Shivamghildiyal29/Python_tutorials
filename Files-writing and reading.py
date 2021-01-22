#A file can be read, write(create) or append using the open funtion
r =open("E:\\Example1.txt",'r')
print(r.read())
r.close() #mandatory to close a file in order to regulate changes

n =10
#dealing with a file usinf with command and open function, no need to close the file in this method
with open("E:\\Example1.txt",'r') as e:
    print(e.read()) #reads the whole file
    print(e.readline()) #reads only one line
    print(e.readline(n))  # reads n characters from the file
    print(e.readlines()) #reads all the lines and store it in a list

#reading each line using a loop
with open("E:\\Example1.txt",'r') as e:
    for line in e:
        print(line, end ='')#gives each line in the file, ends with ''

#Reading a constant number of characters with each cycle
n =10
with open("E:\\Example1.txt",'r') as e:
    print(e.readline(n))  # reads first n characters from the file
    print(e.readline(n))  # reads next n characters from the file, returns 0 when the file is read


#Reading the file at a constant character per cycle
with open("E:\\Example1.txt",'r') as e:
    size =20
    content = e.read(size)
    while len(content)> 0: #the loop iterates till the end of the file
        print(content, end='')
        content =e.read(size)


#file_name.tell() = returns the postion in the file where the pointer is
#file_name.seek(n)= returns to the nth reading position on the file

#Writting a file: This can be used to create a new file and can also overwrite any preexisting fil
with open("E:\\Example2.txt", 'w') as e: #creating new file
    e.write("Testing of write command to create a file")
    e.write(' 11212') #next command will write after the first one finishes.
#output: Testing of write command to create a file 11212

with open("E:\\Example2.txt", 'w') as e: #creating new file
    e.write("Testing of write command to create a file")
    e.seek(0)
    e.write(' 11212') #the command will start writing from the location seek in the above function .
#output:  11212g of write command to create a file


#Copying a file and writing its context to another file
with open("E:\\Example1.txt",'r') as er: #reading Example1.txt file
    with open("E:\\Example2.txt", 'w') as ew: #writting in example2 file
        for line in er: #reading the file object er(example1)
            ew.write(line) #writting in file object ew(example2)

#Writting and  reading a file in binary, example jpeg file etc
with open("C:\\Users\\Shivam Ghildiyal\\Downloads\\img.jpg",'rb') as er: #reading jpg file as binary
    with open("C:\\Users\\Shivam Ghildiyal\\Downloads\\untitiled.jpg", 'wb') as ew:
        for line in er: #reading the file object er(img)
            ew.write(line) #writting in file object ew(img_copy)

#Writting and  reading a file in binary,using smaller parts
with open("C:\\Users\\Shivam Ghildiyal\\Downloads\\img.jpg",'rb') as er:
    with open("C:\\Users\\Shivam Ghildiyal\\Downloads\\Untitled.jpg", 'wb') as ew:
        size = 4000
        content = er.read(size)
        while len(content) > 0:  # the loop iterates till the end of the file
            ew.write(content)
            content = er.read(size)