#making a list
Subjects= ["History", "maths", "Science","Physical education" ]
print(Subjects)

#determining the length of the list
length = len(Subjects)
print(length)
#indexes are the location of the data in the list, it starts with 0 and is always 1 less than the length
print(Subjects[0])
print(Subjects[1])
print(Subjects[2])
print(Subjects[3])
#data in the list can be accessed from the last data onwards when negative of the index is taken from -1, increasing by 1 as it moves to left
print(Subjects[-1])
print(Subjects[-2])
print(Subjects[-3])
print(Subjects[-4])

#accesing a partial list
print(Subjects[0:2]) #starts with the initial index and goes till one less than the second index
#when a limit is not mentioned it is taken as the extreme limit
print(Subjects[:2])
print(Subjects[1:])

#adding a data using append, always add the data at the end
Subjects.append("Arts")

#adding a data using insert, adds data at the desired location
Subjects.insert(0,"Arts")
print(Subjects)

#adding a data using extend,
optional = ['civics', "computers"]
Subjects.extend(optional)
print(Subjects)


#removing values
Subjects.remove("Arts")
removed_value =Subjects.pop() #automatically removes the last value and returns the removed value


#reversing the list
Subjects.reverse()

#sorting with alteration in the original file
Subjects.sort()
numbers =[13,5484,1,46,13846,481]
numbers.sort()#ascending order for numbers
numbers.sort(reverse=True)#decending order for numbers
print(numbers.sort(reverse=True))
 #sorting without altering the original
new_lest=sorted(Subjects)

#min max and sum
print(min(numbers))
print(sum(numbers))
print(max(numbers))

#finding the index of a value
print(Subjects.index("maths"))
#finding the  value in the list
print('arts' in Subjects)
print('maths' in Subjects)

#Empty lists
empty_lists = []
empty_lists = list()
