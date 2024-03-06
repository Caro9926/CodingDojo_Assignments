# Reconocer python - Actividad
num1 = 42  #Variable declaration number initialize
num2 = 2.3  #Variable declaration number initialize

boolean = True  #Variable declaration boolean initialize

string = 'Hello World' #Variable declaration string initialize

#Variable declaration list initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 

#Variable declaration dictionary initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 

#Variable declaration tuples iniciatilize "En los tuples los valores no se pueden modificar"
fruit = ('blueberry', 'strawberry', 'banana') 
#Print to console, type check
print(type(fruit))
#Print to console, list access value
print(pizza_toppings[1]) #List access value
pizza_toppings.append('Mushrooms') #List add value
#Print to console, dictionary access value 
print(person['name'])
person['name'] = 'George' #Dictionary change value 
person['eye_color'] = 'blue' #Dictionary change value 
#Print to console, tuple access value
print(fruit[2]) 

#log Statem
#Conditional
if num1 > 45:        #Conditional if
    print("It's greater")
else:                #Conditional else
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#Function
#This loop starts in 0 and end in 5
for x in range(5):  
    print(x)
#This loop starts in 2 and end in 5
for x in range(2,5):
    print(x)
#This loop starts in 2 and end in 10, goes 3 by 3 
for x in range(2,10,3):
    print(x)

#While loop variable declaration 
x = 0
while(x < 5):   
    print(x)    #Print the value 
    x += 1  #While increment

pizza_toppings.pop()  #List delete value
pizza_toppings.pop(1) #List especific delete value 

#Prin to console of dictionary
print(person)
person.pop('eye_color')  #Dictionary delete value
print(person)

#Conditional for loop for a  list
for topping in pizza_toppings: 
    if topping == 'Pepperoni': #conditional if 
        continue
    print('After 1st if statement')  #print to console
    if topping == 'Olives':
        break              #Break (Here stops the loop)


#Function declaration with parameter x
def print_hello_ten_times():
    for num in range(10):  #Initialize loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):  #Initialize loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x): #Initialize loop 
        print('Hello')

#Function call goes to ten 
print_hello_x_or_ten_times()
#Funtion call goes to four 
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry'  #IndexError: list index out of range
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7])  #IndentationError: unexpected indent
#   print(boolean) 
# fruit.append('raspberry') #-AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)