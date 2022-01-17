num1 = 42 #variable declaration
num2 = 2.3 #variable declaration, Numbers
boolean = True #variable declaration, Boolean
string = 'Hello World' #Strings, variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') #Tuples, initialize
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #dictionary, access value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #Tuples, access value
 
if num1 > 45: #if statemente
    print("It's greater")
else: #else statemente
    print("It's lower")

if len(string) < 5: #length check
    print("It's a short word!")
elif len(string) > 15:  #length check
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop, start and end
    print(x)
for x in range(2,10,3): #for loop, start, end and increase
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #List, delete value
pizza_toppings.pop(1) #List, delete value in certain position

print(pizza_toppings)

print(person)
person.pop('eye_color') #dictionary, delete value
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #break 

def print_hello_ten_times(): #function that prints 10 times "hello"
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #function that prints X times "hello"
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function that prints 10 times "hello", or X times if is needed
    for num in range(x):
        print('Dojo')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) - NameError: name <num3> is not defined
# num3 = 72
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) -  KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - - IndentationError: unexpected indent
# fruit.append('raspberry') -  AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'

