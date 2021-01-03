#sorting is a arrangement of the collection of items in the lists, touple in an order
li = [12,156,48,6984,84,13,4648,45]
#The function sorted makes a new list and sorts in a assending order
new_li = sorted(li)
print(new_li)
#sorting in decending order
rev_li = sorted(li, reverse = True)
print(rev_li)

#The sort nethod edits the lists without creating a new list
li.sort()
print(li)
#sorting in reverse order using sort method
li.sort(reverse= True)
print(li)

#sourting tuples: sort method does not wor with tuple
tu=(12,156,1518,48,64,13,49,68,31)
new_tu = sorted(tu)
print(new_tu)

#Sorting Dictionary: sorting a dictionary will sort the keys of the dictionary
di = {"John": " Pharmacist", 'carl': "Baker", "zak": "Coder" }
new_di =sorted(di)
print(new_di)

#Sorting can be done using the keys as the function which provides the value to sort
num_list = [-6, 5,-7,-1,-5,6,-2,1]
s_num =sorted(num_list, key =abs) #abs funciton gives the values to be sorted
print(s_num)

#Keys can be used to pass the methods so that data attributes of the instance can be sorted
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
    def __repr__(self):
        return (f"{self.name}:{self.age}:{self.pay}")

def e_sort(em):
   #return em.name
    #return em.age
     return em.pay

e1 = Employee("xak", 34, 600000)
e2 = Employee("Mac", 40, 400000)
e3 = Employee("Stan", 20, 700000)
e4 = Employee("Ash", 19, 800000)

roster = [e1, e2, e3, e4]

sorted_objects= sorted(roster, key = e_sort)
print(sorted_objects)