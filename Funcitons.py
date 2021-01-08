#functions: set of codes that performs specific tasks, it allows the reuse of the code.

#creating a funcion
def hello_func():
    print("hello Functions!")
#    pass #keyword that allows an empty function and doent generate an error
hello_func()

#Return function: the funciton returns a value and is stored in the object during the execution of the function
def even_no():
    return 3 #the return value can be of any datatype

print(even_no())

#argunments to function: the prerequisit values or inputs of the function
def making(x):
   return 'i' + x+ 'i'

print(making('a')) #calling a function and passing the value

#passing a default argument in the parameters, This allows to run the function using the given values if the calues are not passed
def hello_moto(x = "Hi", Name ="Dhilae"):
    return "{} {}".format(x, Name)

print(hello_moto('Hello', "GO"))    #output - Hello GO
print(hello_moto("Hello"))          #output - Hello Dhilae, default value of second parameter is used
print(hello_moto())                  #output - Hi Dhilae, default vlaue of both parameter is used


#accept arbitrary numbers of data in the function using * in parameter, it converts the data into dictionary and tuples
def students_data(*args, **kwargs):
    print(args)
    print(kwargs)

#students_data("math","arts", name= "Jason", age = 22)


#Using * to pass data in the function

courses=["math","arts"]
info={" name" : "Jason", "age" : 22}
#students_data(courses, info) #this passses all the data and makes a list
students_data(*courses, **info) #adding a * in front of the list and ** in front of the dictionary specifu the datatype to the function
