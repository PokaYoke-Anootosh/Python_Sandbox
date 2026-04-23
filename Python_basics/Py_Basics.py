# print('Anootosh the Zaalim')
# Name=input("What's your Name?")
# print(Name)
# print('Hey there, '+ Name)
# # name = input('What is your Name? ')
# # print('Hey there, ' + name)
# print(type(4+2))
# print(type(4/12))
# print(type(4*2.6))
# print(type(4+2.3))
# # To the Power of a number is shown as :
# print(2**4) #this means 2 to the power of 4
# # To get the remainder of a division is shown as :
# print(5%4) #this means 5 divided by 4 and the remainder is shown...the '%' sign is also called Modulo
# # To get the integer value of a division is shown as :
# print(5//4) #this means 5 divided by 4 and the integer value is shown
# # To get the absolute value of a number is shown as :
# print(abs(-20))
# # To get the binary value of a number is shown as :
# print(bin(5))
# To get the integer value of a binary number is shown as :
#print(round(3.8))
#print(abs(-120))
# print(str(100+20)+' Years') 
# Relationship='It\'s complicated'
# print(Relationship)
# Name='Billy'
# Age='56'
# Pet_Name='Boo' 
# print('Hi {0}. You are {1} years old, and you have a pet called {2}'.format(Name,Age,Pet_Name))
# print(f'Hey {Name}, you\'re {Age} years old, and you have a pet called {Pet_Name}')
#Self_Start = 'Ghar Ghar Ghar'
#print(Self_Start[0:13])
#print(bin(231))
#Me= 'I\'m not \"the\" smartest'
#print(Me)
#print(bin(55))
#Sample[Start : Stop : Stepover]
#Sample = '-TERRAFORM-'
#print(Sample[::-2])
#Name=input('What is your Name?: ')
#Greet = 'Hello there'
#Message = f'{Greet} {Name.upper()}'
#print(Message)


#Age calculator Code: 

#importing datetime function from Datetime library
#from datetime import datetime 

#defining variables 
#Birth_year = input('What year were you born?: ')
#Current_year = datetime.now().year
#My_Age= Current_year - int(Birth_year)

#printing the output
#print(f'Hey {Name}, Your Age is: {My_Age} years')

# Password Checker Code: 
#UserName= input('Enter a Username: ')
#Password= input('Enter a Password: ')
#PW_Length= len(Password)
#HiddenPW= Password[0:4] + str('*' * (PW_Length - len(Password[4:])))
#print(f'Hey {UserName}, your Password \'{HiddenPW}\' is {PW_Length} characters long')

#Exercise: List Slicing
#new_list = ['a', 'b', 'c']
#print(new_list[1])
#print(new_list[-2])
#print(new_list[1:3])
#new_list[0] = 'z'
#print(new_list) 

#Exercise: List mutability 
#my_list = [1,2,3]
#bonus = my_list + [5]
#my_list[0] = 'z'
#print(my_list)
#print(bonus) 

#Lists 
from typing import Counter

from sympy import false


Amazon_cart = ['Notebooks', 'Sunglasses', 'Toys', 'Grapes']
print(Amazon_cart[0:2])
New_Cart = Amazon_cart[:3]
New_Cart [1] = 'Laptop'
print(New_Cart)
print(Amazon_cart)

MyString = 'Avian,De'
print(len(MyString)) 

MyList = ['Avian','De'] 
print(len(MyList))  

MyList.append('Spitfire')
print(MyList)  
MyList.insert(2,'Bf109')
print(MyList)  
MyList.insert(4,'Heinkle') 
print(MyList)
MyList.extend(['He11','B17'])
print(MyList)  
MyList.pop()
print(MyList)  
print(MyList.index('Bf109'))
print(MyList.index('Spitfire',0,4))
print('He11' in MyList)
print('P-51 Mustang' in MyList)
print(MyList.count('He11'))
print(MyList.count('P-51 Mustang'))
#MyList.sort() #changes the values in place i.e. the original list values changes, no new values are created 
print(MyList) #printing the sorted MyList
print(sorted(MyList)) #creates a New sorted Copy of the original list 
MySentence = ' '
print(MySentence.join(['Hi','My','Name','is','Avian']))
print(MySentence)
New_MySentence = ' '.join(['Hi','My','Name','is','Avian'])
print(New_MySentence)
#List Unpacking
L1, L2, L3, * Wild, Cattle, Meat = ['Bird', 'Dog', 'Cat', 'Bear', 'Cow', 'Horse', 'Rabbit', 'Pig', 'Sheep', 'Goat']
print(L1)  
print(L2)
print(L3)
print(Wild)  
print(Cattle)
print(Meat)

#Dictionary (dict)
My_dict = [{ 
  'Numbers' : [1,2,3], 
  'BoolN' : True, 
  'Text' : 'Hello'}, 
  {'Food' : ['Beef', 'Chicken', 'Lamb', 'Pork'], 
    'Non-Veg' : True, 
    'Greet' : 'Eat my meat Vegans'}, 
  {'Food' : ['Corn', 'Potatoes', 'Tomatoes', 'Onions', 'Beans'], 
   'Veg' : True,
   'Greet' : 'Eat your Veggies'}, 
  {'Food' : ['Plant-Based sausage', 'Artificial Meat', 'Plant-Based Protein', 'Plant-Based Fat'], 
   'Vegan' : True, 
   'Greet' : 'Throw away your sht'
  }]

print(My_dict[1]['Food'][1])
print(My_dict[1]['Greet']) 

Dict1_Meat = My_dict[1]
Dict2_Veggie = My_dict[2] 
dict3_Vegan = My_dict[3]

print(Dict1_Meat.get('Food'), Dict1_Meat.get('Greet'))
print(Dict2_Veggie.get('Food'), Dict2_Veggie.get('Greet'))
print(dict3_Vegan.get('Food'), dict3_Vegan.get('Greet')) 
print(dict3_Vegan.get('Menu','Go Home Vegans'))

#Tuplpes or Immutable Lists 
#My_Tuple = ('Hero', 'Bajaj', 'TVS', 'Harley') 
#print(My_Tuple) 
#(1,2) = [1,2,3,4,5]
#print((1,2)) 

is_magician = False
is_expert = False

if is_magician and is_expert:
  print('You are a Master Magician') 
elif is_magician and not is_expert:
  print('At least you\'re getting there')
else: 
  print('You need Magic Powers')

for Nmbrs in (1,2,3,4,5,6,7,8,9,10):
  print(Nmbrs)
  print(Nmbrs)
print(Nmbrs)

users = {
  'Name' : 'Avian',
  'Age' : 27,
  'Can_Swim' : True,
  'Can_Fly' : False,
  'Can_Drive' : True,
  'Can_Shoot' : False
}

for item in users.items():
  print(item)

for item in users.values():
  print(item)

for item in users.keys():
  print(item)

for item in users.items():
  Key, Value = item;
  print(Key, Value)

for Key, Value in users.items():
  print(Key, Value)

#Excercise: Count number of items in a List (My_List) using For loop
My_List = [1,2,3,4,5,6,7,8,9,10]

my_counter = 0 #Counter is a variable that will count the number of items in the list

for Values in My_List: #Values is a variable that will take the values of the list one by one)
  my_counter = my_counter + Values #defining my_counter as the sum of my_counter and Values

print(my_counter) #Printing the value of my_counter which is basically the sum of all the values in the list

My_Range = list(range(0,100))
print(My_Range)

for item in range(0,10): 
  print(item)

for item in range(0,10,2):
  print(item)

for item in range(10,0,-1):
  print(item)

#Enumerate Function
My_Enum_List = enumerate(['Plane' , 'Bus', 'Train', 'Car', 'Boat', 'Ship', 'Helicopter'])
print(list(My_Enum_List))

#Enumerate Function starting from 1
My_Enum_List = enumerate(['Plane' , 'Bus', 'Train', 'Car', 'Boat', 'Ship', 'Helicopter'], start=1)
print(list(My_Enum_List))

My_Transprt_List = ['Plane' , 'Bus', 'Train', 'Car', 'Boat', 'Ship', 'Helicopter']
for i, char in enumerate(My_Transprt_List, start=1):
  print(i, char)
  if char == 'Ship':
    print(f'{char} is our number {i} mode of transportation')

#While Loop
i = 0

while i < 50:
  print(i)
  i = i + 1
else:
  print('Done with all the work')

item = 0

while item < len([1,2,3,4,5,6,7,8,9,10]):
  print(item)
  item += 1

My_Listy = [1,2,3,4,5,6,7,8,9,10]
c = 0

while c < len(My_Listy): #here c is < the lenght of My_Listy because c being an index counts from 0 but the List My_Listy counts from 1 
  print(My_Listy[c])
  c += 1
else: 
  print('Finito, my man. Done with all the work')

#while True:
  #Response = input('Hey there: ')
  #if Response == 'Bye' or Response == 'bye': 
      #print('See ya later, Alligator')
      #break
  #Name = input('What\'s your Name?: ')
  #print(f'Welcome to the Coding Jungle, {Name}')

My_Name = 'Red Baron'
My_Plane = 'Fokker Dr.I'

if My_Name == 'Red Baron' and My_Plane == 'Fokker Dr.I':
  print('You are the legendary Red Baron flying the Fokker Dr.I triplane!')
elif My_Name == 'Red Baron' and My_Plane != 'Fokker Dr.I':
  print('You are still Manfred von Richthofen, not yet the legendary Red Baron!')
else:
  print('You are not the Red Baron. Go learn the Belki-Diktat!')

name = input('What is your Name?: ')
print('Hello there, '+ name) 

print(2*2)

#Data Types: 
print(type(2+3)) #int
print(type('Avian')) #str
print(type(3.5)) #float 
print(type(2+3.2)) #float
print(type(9.9+1.1)) #float becuz the result will be 11.0 (see below)
Complex_Num = 3 + 5j
print(type(Complex_Num)) #complex number
print(9.9+1.1)

#Binanry Representation:
print(bin(6)) #binary representation of 5

#Operators: 
print(2 ** 3) #Exponentiation Operator (2 to the power of 3)
print(3 // 4) #Floor Division Operator (returns the integer value of the division)
print(5 % 2) #Modulus Operator (returns the remainder of the division)

print(5 ** 3.2) #5 to the power of 3.2
print(5 // 2.3) #returns the integer value of the division
print(5 % 2.3) #returns the remainder of the division

#Functions: 
print(round(3.6)) #rounds the number to the nearest integer
print(abs(-20)) #returns the absolute value of the number

#Operator Precedence
print(3 + 4 * 2) #multiplication has higher precedence than addition

#Variables: 

#Normal Variables (should always start with a letter or underscore, cannot start with a number, no spaces allowed, case-sensitive)
my_Var = 'Hello World'
#OR 
_myVar = 20
#OR
myVar2 = 30
print(my_Var)
print(_myVar)
print(myVar2)

#Dunder Variables (start and end with double underscores, used for special purposes)
__myDunderVar__ = 'I am a Dunder Variable'
print(__myDunderVar__)
#Note: Avoid using Dunder Variables unless necessary 

#Constants (should be written in uppercase letters, used for values that should not change)
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458
print(PI)
print(GRAVITY)
print(SPEED_OF_LIGHT)
#Avoid changing the value of constants 

#Expressions and Statements:
#Expression: A combination of values, variables, and operators that produces a value
result = 3 + 4 * 2 #this is an expression
print(result)
#Statement: A complete line of code that performs an action
if result > 10: #this is a statement
  print('Result is greater than 10') #this is also a statement

#Augmented Assignment Operators: 
x = 5
x += 3 #equivalent to x = x + 3
print(x)
x -= 2 #equivalent to x = x - 2
print(x)
x *= 4 #equivalent to x = x * 4
print(x)
x /= 2 #equivalent to x = x / 2
print(x)
x //= 3 #equivalent to x = x // 3
print(x)

#Type String: 
Username = 'SuperCoder'
Password = 'SuperSecret123'
print(Username)
print(Password)

#long Strings:
Long_String= '''
WOW
0 0
\_/
'''
print(Long_String)

greeting = 'Hello'
name = 'Avian'
full_greeting = greeting + ' ' + name
print(full_greeting)

#String Concatenation:
print('Hello' + ' ' + 'World')
print('Python' + ' ' + ' Rocks!')
#print('I am ' + 5) #this will give an error because we are trying to concatenate a string with an integer

#Type conversion:
print(type(int(3.8)))
print(type(str(100)))
print(type(float('12.34')))
print(int(str(100)) + 100)
print(str(50 + 50) + ' is a hundred')
print(float(5) + 2.5)

#Escape Sequences:
Weather = "It's a sunny day"
#OR
Weather_New = 'It\'s a rainy day' #escaping the single quote " ' "
print(Weather)
print(Weather_New)

print('Hey It\'s your Birthday! Wish you a Very \'Happy Birthday\' Tosh!!') #escaping single quotes inside single quotes
#AND (with a new line using \n)
print('Hey It\'s your Birthday!\n Wish you a Very \'Happy Birthday\' Tosh!!') #escaping single quotes inside single quotes with a new line
#AND using escape sequences to bypass \n, \t 
print('I am Avian.\nI love coding.') #\n is used for new line
print('I am Avian.\tI love coding.') #\t is used for tab space
#AND using escape sequences to write \ by using double backslash \\
print('I am Avian.\\I love coding.') #\\ is used to write a single backslash \

#formatted strings (f-strings):
First_Name = 'Avian'
Last_Name = 'De'
print(f' Hey {First_Name}, You\'re a {Last_Name}')

#.format() method:
First_Name = 'Avian'
Last_Name = 'De'
print(' Hey {}, You\'re a {}'.format(First_Name, Last_Name))
print(' Hey {1}, You\'re a {0}'.format(First_Name, Last_Name)) #using index to change the order
print(' Hey {fname}, You\'re a {lname}'.format(fname='Avian', lname='De')) #using keyword arguments

Name = 'Avian'
Age = 27
Pet_Name = 'Skipper'
print(f'Hi {Name}, You\'re {Age} years old and your Pet Name is {Pet_Name}')

print('Hi {}, You\'re {} years old and your pet name is {}'.format(Name, Age, Pet_Name))
print('Hi {1}, You\'re {2} years old and your pet name is {0}'.format(Name, Age, Pet_Name)) 

#String Indexing and Slicing:
MyString = 'Hello, World!'
print(MyString[0]) #H
print(MyString[7]) #W
print(MyString[-1]) #!
print(MyString[-6]) #W
print(MyString[0:5]) #Hello
print(MyString[7:12]) #World
print(MyString[:5]) #Hello
print(MyString[7:]) #World!
print(MyString[:]) #Hello, World!
print(MyString[::2]) #Hlo ol!
print(MyString[1::2]) #el,Wrd
print(MyString[::-1]) #!dlroW ,olleH
print(MyString[::-2]) #!lo olH

Intro = 'I am a Gunda'
print(Intro[3])
print(Intro[:5])
print(Intro[6:12])
print(Intro[6:-1])
print(Intro[6:-2])
print(Intro[::])
print(Intro[:])
print(Intro[::1])
print(Intro[::2])
print(Intro[6::1])
print(Intro[6::2])

#String Immutability:
MyStr = 'Hello'
#MyStr[0] = 'h' #this will give an error because strings are immutable
New_MyStr = 'h' + MyStr[1:] #creating a new string
print(New_MyStr)  
print(MyStr)

#Built-in Functions & Methods:

#len() - returns the length of the string
Greet = 'Hello, World!'
print(len(Greet)) #returns 13 the length of the string i.e. number of characters including spaces and punctuation
print(Greet[0:len(Greet)]) #returns the entire string using len() 

#upper() - converts all characters to uppercase
print(Greet.upper()) #returns 'HELLO, WORLD!'

#lower() - converts all characters to lowercase
print(Greet.lower()) #returns 'hello, world!' 

#find() - returns the index of the first occurrence of a substring
print(Greet.find('d!')) #returns 11
print(Greet.find('!')) #returns 12
print(Greet.find('z')) #returns -1 (not found) 

#replace() - replaces all occurrences of a substring with another substring 
print(Greet.replace('World', 'Universe')) #returns 'Hello, Universe! 
print(Greet) #printing the original string to show that it is unchanged 

#Boolean Methods:
I_am_Cool = True
I_am_Cool =False 
print(I_am_Cool) #returns False
print(type(I_am_Cool)) #returns <class 'bool'>

#Lists : 
My_List = ['Apple', 'Banana', 'Cherry']
print(My_List[0]) #returns 'Apple'
print(My_List[1]) #returns 'Banana'
print(My_List[2]) #returns 'Cherry'
print(My_List[-1]) #returns 'Cherry'
print(My_List[-2]) #returns 'Banana'
print(My_List[-3]) #returns 'Apple'
print(My_List[0:2]) #returns ['Apple', 'Banana']
print(My_List[:2]) #returns ['Apple', 'Banana']
print(My_List[1:]) #returns ['Banana', 'Cherry']
print(My_List[:]) #returns ['Apple', 'Banana', 'Cherry'] 
print(My_List[::2]) #returns ['Apple', 'Cherry']
print(My_List[::-1]) #returns ['Cherry', 'Banana', 'Apple'] 

#List Slicing and Mutability:
Fruit_Basket = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(Fruit_Basket) #returns the full list before Slicing ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
Fruit_Basket[1:3] = ['Blueberry', 'Cranberry'] #replacing Banana and Cherry with Blueberry and Cranberry with List Slicing
print(Fruit_Basket) #returns ['Apple', 'Blueberry', 'Cranberry', 'Date', 'Elderberry']
#Changing the Values again
Fruit_Basket[0:3] = ['Dragon fruit', 'Almonds', 'Yogurt'] #creating a new list with the first 3 items of Fruit_Basket
New_Basket = Fruit_Basket[0:3]
print(New_Basket) #returns ['Dragon fruit', 'Almonds', 'Yogurt']
print(Fruit_Basket) #returns the full list after Slicing ['Dragon fruit', 'Almonds', 'Yogurt', 'Date', 'Elderberry']
New_Basket[2] = 'Cheese' #changing the 3rd item of New_Basket
print(New_Basket) #returns ['Dragon fruit', 'Almonds', 'Cheese']
print(Fruit_Basket) #returns the full list after Slicing ['Dragon fruit', 'Almonds', 'Yogurt', 'Date', 'Elderberry'] (unchanged
#because lists are mutable but Slicing creates a new list)


#Matrix:
Matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(Matrix[0]) #returns [1,2,3]
print(Matrix[0][1]) #returns 2
print(Matrix[1][2]) #returns 6
print(Matrix[2][0]) #returns 7
print(Matrix[1][1]) #returns 5
print(Matrix[2][2]) #returns 9
print(Matrix[0][0]) #returns 1
print(Matrix[1]) #returns [4,5,6]
print(Matrix[2]) #returns [7,8,9]

#List Methods:
MyBasket = ['Laddu', 'Barfi', 'Jalebi'] 
MyBasket.append('Rasgulla') #adding items to the end of the list
#MyBasket.append('Gulab Jamun','Kheer') #this will give an error because append() takes only one argument
print(MyBasket) #returns ['Laddu', 'Barfi', 'Jalebi', 'Rasgulla']
MyBasket.insert(2, 'Gulab Jamun') #inserting item at index 1
print(MyBasket) #returns ['Laddu', 'Barfi', 'Gulab Jamun', 'Jalebi', 'Rasgulla']
MyBasket.extend(['Kheer', 'Peda']) #adding multiple items to the end of the list
print(MyBasket) #returns ['Laddu', 'Barfi', 'Gulab Jamun', 'Jalebi', 'Rasgulla', 'Kheer', 'Peda

New_List = MyBasket.append('Halwa') #this will return None because append() does not return anything
print(New_List) #returns None
print(MyBasket) #returns ['Laddu', 'Barfi', 'Gulab Jamun', 'Jalebi', 'Rasgulla', 'Kheer', 'Peda

MyBasket.pop() #removing the last item from the list
print(MyBasket) #returns ['Laddu', 'Barfi', 'Gulab Jamun', 'Jalebi', 'Rasgulla', 'Kheer'] as 'Peda' is removed
MyBasket.pop(2) #removing item at index 2
print(MyBasket) #returns ['Laddu', 'Barfi', 'Jalebi', 'Rasgulla', 'Kheer'] as 'Gulab Jamun' is removed
New_List2 = MyBasket.pop(2) #removing item at index 2 and storing it in a new variable
print(New_List2) #returns 'Jalebi' as it is removed from the list
print(MyBasket) #returns ['Laddu', 'Barfi', 'Rasgulla', 'Kheer'] as 'Jalebi' is removed 

MyBasket.remove('Barfi') #removing item by value
print(MyBasket) #returns ['Laddu', 'Jalebi', 'Rasgulla', 'Kheer'] as 'Barfi' is removed
#MyBasket.remove('Peda') #this will give an error because 'Peda' is not in the list
New_List3 = MyBasket.remove('Laddu') #removing item by value and storing it in a new variable
print(New_List3) #returns None because remove() does not return anything
print(MyBasket) #returns ['Jalebi', 'Rasgulla', 'Kheer'] as 'Laddu' is removed 

MyBasket.clear() #removing all items from the list
print(MyBasket) #returns [] as the list is now empty 
MyBasket = ['Laddu', 'Barfi', 'Jalebi', 'Rasgulla', 'Kheer', 'Peda']

print(MyBasket.index('Jalebi')) #returns 2 
print(MyBasket.index('Rasgulla')) #returns 3
print('Kheer' in MyBasket) #returns True
print('Halwa' in MyBasket) #returns False

#MyBasket.append('Kala Jamun','Rasgulla') #error because append() takes only one argument
MyBasket.append('Kala Jamun') #adding 'Kala Jamun' to the end of
MyBasket.append('Rasgulla') #adding another 'Rasgulla' to the end of the list
print(MyBasket) #returns ['Laddu', 'Barfi', 'Jalebi', 'Rasgulla', 'Kheer', 'Peda', 'Kala Jamun', 'Rasgulla']
Count_of_Kala_Jamun = MyBasket.count('Kala Jamun') #counting the number of occurrences of 'Kala Jamun' in the list 
Count_of_Rasgulla = MyBasket.count('Rasgulla') #counting the number of occurrences of 'Rasgulla' in the list
print(Count_of_Kala_Jamun) #returns 1
print(Count_of_Rasgulla) #returns 2 

MyBasket.sort() #sorting the list in ascending order
print(MyBasket) #returns ['Barfi', 'Jalebi', 'Kheer']

print(MyBasket.index('Barfi')) #returns 0
print(MyBasket.index('Jalebi')) #returns 1
print(MyBasket.index('Kheer')) #returns 2 
print(MyBasket.index('Laddu')) #returns 3 

#print(MyBasket.index('Laddu',0,2)) #this will give an error because 'Laddu' is not in the list between index 0 and 2
print(MyBasket.index('Laddu',2,5)) #returns 3 because 'Laddu' is at index 3 which is between index 2 and 5 

print('Peda' in MyBasket) #returns True
print('Halwa' in MyBasket) #returns False 

AlphaList = ['d', 'g', 'a', 'c', 'b', 'e']
#AlphaList.sort() #sorting the list in ascending order
#print(AlphaList) #returns ['a', 'b', 'c', 'd', 'e'...] 
print(sorted(AlphaList)) #returns a new sorted list ['a', 'b', 'c', 'd', 'e'...] without changing the original list
print(AlphaList) #printing the original list to show that it is unchanged 

print(AlphaList.copy()) #creating a copy of the list
AlphaList.reverse() #reversing the list 
print(AlphaList) #printing the reversed list 
AlphaList.sort() #sorting the list in ascending order
print(AlphaList.reverse()) #this will return None because reverse() does not return anything
print(AlphaList) #printing the sorted list 
print(AlphaList[::-1]) #printing the sorted list in reverse order using List slicing 
print(AlphaList) #printing the sorted list to show that it is unchanged 

range(1,50) #this will create a range object from 1 to 49
print(range(1,50)) #this will print the range object
print(list(range(1,50))) #this will print the list of numbers from 1 to 49 

My_Intro = 'Hello' 
print(My_Intro) #returns 'Hello' 
My_Intro.join([',','I', 'am', 'Avian']) #this will return 'HIamHAvianH' because join() takes the string and joins it with the items in the list using the string as a separator 
print(My_Intro) #printing the original string to show that it is unchanged 
My_Intro_with_Name = My_Intro.join(['Hi', 'My', 'Name', 'is', 'Avian']) #this will return 'Hi Hello My Hello Name Hello is Hello Avian' because join() takes the string and joins it with the items in the list using the string as a separator
print(My_Intro_with_Name) #returns 'Hi Hello My Hello Name Hello is Hello Avian' 
print(' '.join(['Hi', 'My', 'Name', 'is', 'Avian'])) #this will return 'Hi My Name is Avian' because join() takes the string and joins it with the items in the list using the string as a separator 

My_Name = ' Avian, ' 
Name_with_Intro = My_Name.join(['Hi','How are you?', 'Welcome to the Coding Jungle']) #this will return 'HiAvianHow are you,AvianWelcome to the Coding Jungle' because join() takes the string and joins it with the items in the list using the string as a separator 
print(Name_with_Intro) #returns 'HiAvianHow are you,AvianWelcome to the Coding Jungle' 

#List Unpacking: 
L1, L2, L3 = ['Bird', 'Dog', 'Cat'] #unpacking the list into 3 variables 
print(L1) #returns 'Bird' 
print(L2) #returns 'Dog' 
print(L3) #returns 'Cat' 
print(L1, L2, L3) #returns 'Bird Dog Cat' 

L1, L2, L3, *Wild = ['Bird', 'Dog', 'Cat', 'Bear', 'Cow', 'Horse', 'Rabbit', 'Pig', 'Sheep', 'Goat'] #unpacking the list into 3 variables and the rest of the items in the list are stored in a new variable called Wild 
print(L1) #returns 'Bird' 
print(L2) #returns 'Dog' 
print(L3) #returns 'Cat' 
print(Wild) #returns ['Bear', 'Cow', 'Horse', 'Rabbit', 'Pig', 'Sheep', 'Goat'] 
L1, L2, L3, *Wild, Cattle = ['Bird', 'Dog', 'Cat', 'Bear', 'Cow', 'Horse', 'Rabbit', 'Pig', 'Sheep', 'Goat'] #unpacking the list into 3 variables and the rest of the items in the list are stored in a new variable called Wild and the last 2 items in the list are stored in new variables called Cattle 
print(L1) #returns 'Bird' 
print(L2) #returns 'Dog' 
print(L3) #returns 'Cat' 
print(Wild) #returns ['Bear', 'Cow', 'Horse', 'Rabbit', 'Pig', 'Sheep'] 
print(Cattle) #returns 'Goat' 

Null_Value_in_Python = None #None is a special value in Python that represents the absence of a value or a null value 
print(Null_Value_in_Python) #returns None 

#Dictionary (dict): 
My_Lunch={
  'Sunday' : 'Biriyani', 
  'Monday' : 'Daal Chawal', 
  'Tuesday' : 'Rajma Chawal',
  'Wednesday' : 'Chole Bhature',
  'Thursday' : 'Pasta',
  'Friday' : 'Pizza',
  'Saturday' : 'Burger'
} 

print(My_Lunch['Monday']) #returns 'Daal Chawal'
print(My_Lunch['Friday']) #returns 'Pizza'
print(My_Lunch['Sunday']) #returns 'Biriyani'
print(My_Lunch['Wednesday']) #returns 'Chole Bhature'
print(My_Lunch['Thursday']) #returns 'Pasta' 

IAF ={
    'Fighters' : ['Tejas', 'Su-30MKI', 'MiG-29', 'Mirage 2000', 'Rafale'],
    'Transporters' : ['C-130J', 'C-17', 'An-32', 'IL-76'],
    'Helicopters' : ['AH-64E', 'Rudra', 'Chinook', 'Apache'],
    'Trainers' : ['HJT-16 Kiran', 'HJT-36 Sitara', 'BAE Hawk', 'Pilatus']
      }

print(IAF['Fighters']) #returns ['Tejas', 'Su-30MKI', 'MiG-29', 'Mirage 2000']
print(IAF['Transporters']) #returns ['C-130J', 'C-17', 'An-32', 'IL-76']
print(IAF['Helicopters']) #returns ['AH-64E', 'Rudra', 'Chinook', 'Apache']
print(IAF['Trainers']) #returns ['HJT-16 Kiran', 'HJT-36 Sitara', 'BAE Hawk', 'Pilatus PC-7 Mk II'] 
print(IAF['Fighters'][0]) #returns 'Tejas'
print(IAF['Transporters'][2]) #returns 'An-32'
print(IAF['Helicopters'][3]) #returns 'Apache'
print(IAF['Trainers'][1]) #returns 'HJT-36 Sitara' 
#What will give an error: 
#print(IAF['Fighters']['Mig-21']) #this will give an error because 'Mig-21' is not in the list of Fighters
#print(IAF['Fighters'][5]) #this will give an error because there are only 5 items in the list of Fighters and the index starts from 0, so the last index is 4
#print(IAF['Transporters']['Globemaster']) #this will give an error because 'Globemaster' is not in the list of Transporters
#print(IAF['Helicopters'][4]) #this will give an error because there are only 4 items in the list of Helicopters and the index starts from 0, so the last index is 3

My_Breakfast = {
  'Sunday' : ['Oats', 'Eggs', 'Toast'],
  'Monday' : ['Pancakes', 'Bacon', 'Syrup'],
  'Tuesday' : [24, 25, 35], 
  'Wednesday' : ['Idli', 'Sambar', 'Chutney'],
  #'Thursday' : [My_Breakfast['Monday'][1], 'Curd', 'Pickle'], #this will give an error because My_Breakfast is not defined yet, we cannot use a variable before it is defined
  'Thursday' : [My_Lunch['Monday'][0:4], 'Curd', 'Pickle'], #this will work because My_Lunch is defined before My_Breakfast and we can use the value of My_Lunch['Monday'][0] which is 'Daal Chawal' in the list of Thursday
  'Friday' : ['Cereal', 'Milk', 'Banana'],
  'Saturday' : ['Paratha', 'Curd', 'Aloo Sabzi']
}

print(My_Breakfast['Sunday']) #returns ['Oats', 'Eggs', 'Toast']
print(My_Breakfast['Monday'][1]) #returns 'Bacon'
print(My_Breakfast['Tuesday']) #returns [24, 25, 35]
print(My_Breakfast['Thursday'][0]) #returns ['Daal', 'Chole Bhature', 'Pasta', 'Pizza'] because My_Lunch['Monday'][0:4] returns the first 4 items in the list of My_Lunch['Monday'] which is 'Daal' 

#Dict inside a List: 
My_Dict_List = [
  {
    'Name' : 'Avian',
    'Age' : 27,
    'Can_Swim' : True,
    'Can_Fly' : False,
    'Can_Drive' : True,
    'Can_Shoot' : False
  },
  {
    'Name' : 'John',
    'Age' : 30,
    'Can_Swim' : False,
    'Can_Fly' : False,
    'Can_Drive' : True,
    'Can_Shoot' : True
  },
  {
    'Name' : 'Jane',
    'Age' : 25,
    'Can_Swim' : True,
    'Can_Fly' : False,
    'Can_Drive' : False,
    'Can_Shoot' : False
  }
] 

print(My_Dict_List[0]['Name']) #returns 'Avian'
print(My_Dict_List[1]['Age']) #returns 30 
#print(My_Dict_List[1][3]) #this will give an error because we cannot access the value of a dictionary using an index, we have to use the key to access the value
print(My_Dict_List[2]['Can_Fly']) #returns False 

#Dictionary/Dict Keys cannot be a List because lists are mutable and can be changed, so they cannot be used as keys in a dictionary. Keys in a dictionary must be immutable, which means they cannot be changed after they are created. Examples of immutable types that can be used as keys in a dictionary include strings, numbers, and tuples.
#Dictionary prioritizes Unique Keys (immutable) over values, so if we have a dictionary with duplicate keys, the last key will overwrite the previous keys and their values. For example:

#Dictionary Methods:
Heroes = {
  'Hero1': 'Bigus Dickus',
  'Age': 35,
  'Can_Fly': False,
  'Can_Swim': True,
  'Spl. Powers' : ['Stealth','Infiltration','Penetration Strikes'], 

  'Hero2': 'Humungus Jerkus', 
  'Age': 40, 
  'Can_Fly': True,
  'Can_Swim': False,
  'Spl. Powers' : ['Speed','Quake-Fists','Cannon shots'], 

  'Hero3': 'Tinyus Weakus',
  'Age': 28,
  'Can_Fly': False,
  'Can_Swim': False,
  'Spl. Powers' : ['Invisibility','Smart-talker','Beat-boxing'],  

  'Hero4': 'Dumbus Assus',
  'Age': 30,
  'Can_Fly': False,
  'Can_Swim': True,
  'Spl. Powers' : ['Influencer','Loud Noises','Farting'],  

  'Hero5': 'Stupidus Smartus',
  'Age': 32,
  'Can_Fly': False,
  'Can_Swim': True,
  'Spl. Powers' : ['Strategist','Inventor','Reader of Books'],  

  'Hero6': 'Sexyus Hotus',
  'Age': 29,
  'Can_Fly': True,
  'Can_Swim': False,
  'Spl. Powers' : ['Beauty & Charm','Seduction','Flirting']
}

print(Heroes) #returns the full dictionary with all the keys and values, but the duplicate keys 'Age', 'Can_Fly', 'Can_Swim', and 'Spl. Powers' will be overwritten by the last key-value pair, so the final dictionary will only have one key for each of these duplicate keys with the value of the last key-value pair.

#Checking if an item exists in a Dictionary with 'in' keyword -
print('Weakness' in Heroes) #returns False because 'Weakness' is not a key in the dictionary
print('Hero1' in Heroes) #returns True because 'Hero1' is a key in the dictionary

#.get Method -
print(Heroes.get('Can_Dance')) #returns None because 'Can_Dance' is not a key in the dictionary
print(Heroes.get('Can_Dance', 'Not Found')) #returns 'Not Found' which replaces 'None' in the same scenario as above 

#.keys() method -
print(Heroes.keys()) #returns a view object that displays a list of all the keys
print('Age' in Heroes.keys()) #returns True because 'Age' is a key in the dictionary 
print('Age' in Heroes.values()) #returns False because 'Age' is a key in the dictionary, not a value 

#.values() method -
print(Heroes.values()) #returns a view object that displays a list of all the values
print('Bigus Dickus' in Heroes.values()) #returns True because 'Bigus Dickus' is a value in the dictionary 
print('Bigus Dickus' in Heroes.keys()) #returns False because 'Bigus Dickus' is a value in the dictionary, not a key 

#.items() method -
print(Heroes.items()) #returns a view object that displays a list of dictionary's key-value tuple pairs

#.copy() method -
Heroes_Copy = Heroes.copy() #creates a shallow copy of the dictionary
print(Heroes_Copy) #returns {} as the original dictionary is empty 

#.pop() method -
Heroes.pop('Hero1') #removes the key 'Hero1' and its value from the dictionary
print(Heroes) #returns the dictionary without 'Hero1' and its value

#.popitem() method -
Heroes.popitem() #removes the last key-value pair from the dictionary
print(Heroes) #returns the dictionary without the last key-value pair

#.update() method -
Heroes.update({'Hero6': 'Hotus Sexyus'}) #updates the value of 'Hero6' to 'Hotus Sexyus'
print(Heroes) #returns the dictionary with the updated value of 'Hero6'

#Adding an Item with .update() method -
Heroes.update({'HeroX': 'Elonus Muskus Spermus', 'Age': 1000, 'Can_Fly': True, 'Can_Swim': True, 'Spl. Powers' : ['Tweeting Stupid stuff', 'Bitcoin Jerky', 'Half-Martian']}) #this will add a new key-value pair to the dictionary with the key 'HeroX' and the value 'Elonus Muskus Spermus'
print(Heroes) #returns the dictionary with the new key-value pair added and the value of 'Age', 'Can_Fly', 'Can_Swim', and 'Spl. Powers' updated to the new values because of the duplicate keys 

Heroes.update({'Hero1': 'Bigus Dickus'}) #Re-Updating Hero1 as 'Bigus Dickus' but not in the same order as before
print(Heroes) #returns the dictionary with 'Hero1' added back to the dictionary but not in the same order as before because dictionaries do not maintain order of items

#.clear() method - 
Heroes.clear() #removes all items from the dictionary
print(Heroes) #returns {} as the dictionary is now empty

#dict() function - creates a dictionary from a list of key-value pairs or from keyword arguments -
All_Users= dict(name='Avian', age=27, can_swim=True, can_fly=False) #creating a dictionary using the dict() function with keyword arguments
print(All_Users) #returns {'name': 'Avian', 'age': 27, 'can_swim': True, 'can_fly': False}
#this gives an error because the syntax for creating a dictionary using the dict() function is incorrect, we should use keyword arguments instead of key-value pairs separated by commas. The correct syntax is: dict(name='Avian', age=27, can_swim=True, can_fly=False)
#All_Users = dict('name' = 'Avian', 'age' = 27, 'can_swim' = True, 'can_fly' = False) 

#Tuples:
My_Tuple = ('Apple', 'Banana', 'Cherry')
print(My_Tuple) #returns ('Apple', 'Banana', 'Cherry') 
print(My_Tuple[0]) #returns 'Apple'
print(My_Tuple[1]) #returns 'Banana' 

#My_Tuple[0] = 'Grapes' #this will give an error because tuples are immutable and cannot be changed after they are created 
My_New_Tuple = (My_Tuple[0:2], 'Pomogranate') #creates a new tuple with the first two items of the original tuple
print(My_New_Tuple) #returns (('Apple', 'Banana'), 'Pomogranate')

#Tuple Methods:
print(My_Tuple.count('Apple')) #returns 1 because 'Apple' appears once in the tuple
print(My_Tuple.count('Grapes')) #returns 0 because 'Grapes' does not appear in the tuple
print(My_Tuple.index('Banana')) #returns 1 because 'Banana' is at index 1 in the tuple
#My_Tuple.index('Grapes') #this will give an error because 'Grapes' is not in the tuple
print(len(My_Tuple)) #returns 3 because there are 3 items in the tuple 

#Set:
My_Set = {'Apple', 'Banana', 'Cherry'} 
#a Set is an unordered collection of unique items, so it does not maintain the order of items and does not allow duplicate items
print(My_Set) #returns {'Cherry', 'Apple', 'Banana'} (the order may vary because sets do not maintain order
print('Apple' in My_Set) #returns True because 'Apple' is in the set
print('Grapes' in My_Set) #returns False because 'Grapes' is not in the set

#Set methods:
My_Set.add('Grapes') #adding 'Grapes' to the set
print(My_Set) #returns {'Cherry', 'Apple', 'Banana', 'Grapes'} (the order may vary because sets do not maintain order
My_Set.add('Apple') #this will not add 'Apple' to the set because it is already in the set and sets do not allow duplicate items
print(My_Set) #returns {'Cherry', 'Apple', 'Banana', 'Grapes'} (the order may vary because sets do not maintain order
print(len(My_Set)) #returns 4 because there are 4 unique items in the set
My_Set.remove('Banana') #removing 'Banana' from the set
print(My_Set) #returns {'Cherry', 'Apple', 'Grapes'} (the order may vary because sets do not maintain order
#My_Set.remove('Mango') #this will give an error because 'Mango' 

#sets do not support indexing and slicing like lists and tuples, we cannot access the items in a set using an index or a slice, 
#we can only check if an item is in the set using the 'in' keyword or we can iterate through the set using a for loop.
#print(My_Set[2]) #this will give an error because 

print('Mango' in My_Set) #returns False because 'Mango' is not in the set
print('Grapes' in My_Set) #returns True because 'Grapes'

My_New_Set = My_Set.copy() #creates a shallow copy of the set
print(My_New_Set) #returns {'Cherry', 'Apple', 'Grapes'} (the order may vary because sets do not maintain order
My_Set.clear() #removes all items from the set
print(My_Set) #returns set() as the set is now empty 

My_Set_of_Cars = {'Alto','Swift','Thar','Exeter','Jimny'}
Your_Set_of_Cars = {'Thar','Fortuner','Innova','Baleno'}

#Telling the Difference between two sets using the difference() method -
print(My_Set_of_Cars.difference(Your_Set_of_Cars)) #returns {'Alto', 'Swift', 'Exeter', 'Jimny'} which are the items that are in My_Set_of_Cars but not in Your_Set_of_Cars
print(Your_Set_of_Cars.difference(My_Set_of_Cars)) #returns {'Fortuner', 'Innova', 'Baleno'} which are the items that are in Your_Set_of_Cars but not in My_Set_of_Cars

#Updating a set with the difference_update() method -
print(My_Set_of_Cars.difference_update(Your_Set_of_Cars)) #this will update My_Set_of_Cars to only have the items that are in My_Set_of_Cars but not in Your_Set_of_Cars
print(My_Set_of_Cars) #returns {'Alto', 'Swift', 'Exeter', 'Jimny'} (the order may vary because sets do not maintain order
print(Your_Set_of_Cars) #returns {'Thar', 'Fortuner', 'Innova', 'Baleno'} (the order may vary because sets do not maintain order 

My_Set_of_Cars.add('Jimny') #adding 'Jimny' back to My_Set_of_Cars  
print(My_Set_of_Cars.discard('Jimny')) #removes 'Jimny' from My_Set_of_Cars
print(My_Set_of_Cars) #returns {'Alto', 'Swift', 'Exeter'} (the order may vary because sets do not maintain order
print(My_Set_of_Cars.discard('XUV')) #this will not give an error even though XUV is not part of the set 
print(My_Set_of_Cars) #returns {'Alto', 'Swift', 'Thar', 'Exeter'}, the order may vary because sets do not maintain order
My_Set_of_Cars.add('Thar') #adding 'Thar' back to My_Set_of_Cars 

#Opposite of Set.difference() method is the intersection() method which returns the items that are in both sets, and the opposite of difference_update() method is the intersection_update() method which updates the set to only have the items that are in both sets.
print(My_Set_of_Cars.intersection(Your_Set_of_Cars)) #returns {'Thar'} which is the only item that is in both sets
print(My_Set_of_Cars.intersection_update(Your_Set_of_Cars)) #this will update My_Set_of_Cars to only have the items that are in both sets 
print(My_Set_of_Cars) #returns {'Thar'} which is the only item that is in both sets 

#Union of two sets: 
print(My_Set_of_Cars.union(Your_Set_of_Cars)) #returns {'Thar', 'Alto', 'Swift', 'Exeter', 'Fortuner', 'Innova', 'Baleno'} which is the set of all unique items that are in either My_Set_of_Cars or Your_Set_of_Cars or both 
#Short-hand for set operations:
print(My_Set_of_Cars | Your_Set_of_Cars) #this is a shortcut for the union of two sets and returns the same result as the union() method
print(My_Set_of_Cars & Your_Set_of_Cars) #this is a shortcut for the intersection of two sets and returns the same result as the intersection() method 

#Subset and Superset:
Eicher_Motors_Set = {'Trucks','Buses','Vans', '350cc Motorcycles', '650cc Motorcycles'} 
Royal_Enfield_Set = {'350cc Motorcycles', '650cc Motorcycles'}
#Because Royal_Enfield_Set is a subset of Eicher_Motors_Set because all items in Royal_Enfield_Set are also in Eicher_Motors_Set, but Eicher_Motors_Set is not a subset of Royal_Enfield_Set because not all items in Eicher_Motors_Set are in Royal_Enfield_Set
print(Royal_Enfield_Set.issubset(Eicher_Motors_Set)) #returns True because all items in Royal_Enfield_Set are also in Eicher_Motors_Set
print(Eicher_Motors_Set.issubset(Royal_Enfield_Set)) #returns False because not all items in Eicher_Motors_Set are in Royal_Enfield_Set
#Because Eicher_Motors_Set is a superset of Royal_Enfield_Set because all items in Royal_Enfield_Set are also in Eicher_Motors_Set, but Royal_Enfield_Set is not a superset of Eicher_Motors_Set because not all items in Eicher_Motors_Set are in Royal_Enfield_Set
print(Eicher_Motors_Set.issuperset(Royal_Enfield_Set)) #returns True because all items in Royal_Enfield_Set are also in Eicher_Motors_Set
print(Royal_Enfield_Set.issuperset(Eicher_Motors_Set)) #returns False because not all items in Eicher_Motors_Set are in Royal_Enfield_Set

#If, Elif and Else Statements: 

#Example1 - 
I_Am_Optimus_Prime = False 
I_Am_Megatronus = False
I_Am_Jeff_Bezotron = False
I_Am_Donaldus_Trumpetus = False

if I_Am_Optimus_Prime:
  print('Calling All Autobots, Transform and Roll out!') #this will be printed if Optimus_Prime is True
elif I_Am_Megatronus:
  print('Decepticons, Transform and Rise up!') #this will be printed if Megatronus is True
elif I_Am_Jeff_Bezotron:
  print('There\'s a New Prime in Cybertron...Amazon Prime') #this will be printed if Jeff_Bezotron is True
elif I_Am_Donaldus_Trumpetus:
  print('Make Cybertron Great Again, Where\'s my ICE (Interplanetary Cybertronian Eliminators) Army!') #this will be printed if Donaldus_Trumpetus is True
elif I_Am_Optimus_Prime and I_Am_Megatronus:
  print('Hunt for the Allspark is on') #this will be printed if I_Am_Optimus_Prime and I_Am_Megatronus are both True 
else:
  print('Hail Primus, Next is Hailey!') #this will be printed if all arguements above are False 

#Example2 - 
Donaldus_Trumpetus_Stops_Wars = True
Donaldus_Trumpetus_Gets_Nobel_Peace_Prize = True

if Donaldus_Trumpetus_Stops_Wars: 
  print('Putin a War Hero, and Kim Jong Un a Peace Ambassador!') 
elif Donaldus_Trumpetus_Stops_Wars and Donaldus_Trumpetus_Gets_Nobel_Peace_Prize: 
  print('God Save the World!') 
else:
  print('Modi is now Christian. Pakistan is now a Hindu Country, America Loves China (again)!') 

#Truthy & Falsy Values:
#In Python, the following values are considered Falsy:
#None
#False
#0 (zero of any numeric type)
#0.0 (zero of float type)
#0j (zero of complex type)
#'' (empty string)
#[] (empty list)
#() (empty tuple)
#{} (empty dictionary)
#set() (empty set)
#All other values are considered Truthy, which means they will evaluate to True in a boolean context. For example:

#Example1: 
Your_Username = input('Enter your username: ') 
Your_Password = input('Enter your password: ') 

if Your_Username and Your_Password: #this will check if Your_Username is not empty, if it
  print(f'Welcome {Your_Username}!') 
else:
  print('Please enter both username and password!') 


#Example2: 
Name = input('What is your name? ')
Age = input('How Old are you? ')
Weight = input('How much do you Weigh? (Optional) ')

if Name and Age.isdigit() and int(Age) > 18: #this will check if Name is not empty and Age is greater than 18, if both conditions are True, it will print the message below
  print(f'Welcome {Name}, You\'re old enough to Enter the Pool!') 
elif Name and Age.isdigit() and int(Age) < 18: #this will check if Name is not empty and Age is less than 18, if both conditions are True, it will print the message below
  print(f'Sorry {Name}, You\'re not old enough to Enter the Pool!') 
elif Name: #this will check if Name is not empty, if it is True, it will print the message below
  print(f'Hello {Name}, You need to Enter your Age for Verification!') 
elif not Age.isdigit() or Age == '0': #this will check if Age is not a digit or if Age is equal to '0', if either condition is True, it will print the message below
  print(f'Hello {Name}, You need to Enter your Age for Verification!') 
else: #this will be executed if Name is empty, which means the user did not enter their name, it will print the message below
  print('Sorry, You cannot Enter the Pool without both ID & Age Verfification !') 


#Ternary Operators: 
#Ternary operators are a shorthand way of writing an if-else statement in a single line. The syntax for a ternary operator is:
#value_if_true if condition else value_if_false 

#Example1: 
Age = int(input('How Old are you? '))
Can_Drive = 'Yes' if Age >= 18 else 'Not Eligible' #this will check if Age is greater than or equal to 18, if it is True, it will assign 'Yes' to Can_Drive, otherwise it will assign 'Not Eligible' to Can_Drive 

print(Can_Drive) #this will print the value of Can_Drive based on the condition above
  
#Example2: 
Number = int(input('Enter a Number: ')) 
Even_or_Odd = 'Even' if Number % 2 == 0 else 'Odd' #this will check if the number is even or odd, if the number is divisible by 2 with no remainder, it will assign 'Even' to Even_or_Odd, otherwise it will assign 'Odd' to Even_or_Odd

print(Even_or_Odd) #this will print whether the number is even or odd based on the condition above

#Short-Circuiting with Ternary Operators:
#In Python, the ternary operator also supports short-circuiting, which means that if

Is_Friend = True
Can_Borrow_Money = True

if Is_Friend and Can_Borrow_Money:
  print('You can borrow money from your friend!')
else:  print('You cannot borrow money from your friend!') 

#Here if Is_Friend is False, the condition Can_Borrow_Money will 
# not be evaluated because of short-circuiting, and the else block 
# will be executed, which means you cannot borrow money from your friend. 
# If Is_Friend is True, then the condition Can_Borrow_Money will be 
# evaluated, and if it is also True, then the if block will be executed, 
# which means you can borrow money from your friend. 

#Logical Operators: 
#== (Equality Operator) - checks if two values are equal and returns True if they are equal, otherwise it returns False
#!= (Not Equal Operator) - checks if two values are not equal and returns True if they are not equal, otherwise it returns False
#> (Greater Than Operator) - checks if the value on the left is greater than the value on the right and returns True if it is, otherwise it returns False
#< (Less Than Operator) - checks if the value on the left is less than the value on the right and returns True if it is, otherwise it returns False
#>= (Greater Than or Equal To Operator) - checks if the value on the left is greater than or equal to the value on the right and returns True if it is, otherwise it returns False
#<= (Less Than or Equal To Operator) - checks if the value on the left is less than or equal to the value on the right and returns True if it is, otherwise it returns False 
#not (Logical NOT Operator) - negates the value of a boolean expression and returns True if the expression is False, and returns False if the expression is True
#and (Logical AND Operator) - returns True if both expressions are True, otherwise it returns False
#or (Logical OR Operator) - returns True if at least one of the expressions is True, otherwise it returns False

print(5 == 5) #returns True because 5 is equal to 5
print(5 != 5) #returns False because 5 is not not equal to 5
print(5 > 3) #returns True because 5 is greater than 3
print(5 < 3) #returns False because 5 is not less than 3
print(5 >= 5) #returns True because 5 is greater than or equal to 5
print(5 <= 5) #returns True because 5 is less than or equal to 5
print(not True) #returns False because the negation of True is False
print(not False) #returns True because the negation of False is True
print(True and True) #returns True because both expressions are True
print(True and False) #returns False because one of the expressions is False
print(False and False) #returns False because both expressions are False
print(True or True) #returns True because at least one of the expressions is True
print(True or False) #returns True because at least one of the expressions is True  
print(False or False) #returns False because both expressions are False 

#Excercise: 
is_magician = True
is_expert = False

if is_magician and is_expert:
  print('You\'re a Master Magician!') 
elif is_magician and not is_expert:
  print('At least you\'re getting there!')
else: 
  print('You need magic powers!') 

#is vs == :
#The 'is' operator checks for identity, which means it checks 
# if two variables point to the same object in memory. 

print(True == 1) #returns True because the value of True is equal to 1, but they are not the same object in memory
print('1' == 1) #returns False because the value of '1' is not equal to the value of 1, and they are not the same object in memory 
print([] == []) #returns True because the value of both lists is equal (both are empty lists), but they are not the same object in memory
print(10 == 10.0) #returns True because the value of 10 is equal to 10, but they are not the same object in memory
print([1,2,3] == [1,2,3]) #returns True because the value of both lists is equal (both have the same elements), but they are not the same object in memory

a = [1,2,3]
b = [1,2,3] 
print(a == b) #returns True because the value of both lists is equal (both have the same elements), but they are not the same object in memory

# The '==' operator checks for equality, which means it checks if 
# the values of the variables are equal, regardless of whether 
# they are the same object in memory or not.  

print(True is 1) #returns False because True and 1 are not the same object in memory, even though their values are equal
print('1' is 1) #returns False because '1' and 1 are not the same object in memory, and their values are not equal
print([] is []) #returns False because both lists are empty and have the same value, but they are not the same object in memory
print(10 is 10.0) #returns False because 10 and 10.0 are not the same object in memory, even though their values are equal
print([1,2,3] is [1,2,3]) #returns False because both lists have the same value (same elements), but they are not the same object in memory

a=[1,2,3]
b=[1,2,3] 
print(a is b) #returns True because a and b point to the same object in memory

#For Loops: 
for i in [1,2,3,4,5]: 
  print(i) #this will print the numbers from 1 to 5, each on a new line 

#Nested For Loops: 
for i in [1,2,3]: 
  for j in ['a','b','c']:
    print(i, j) #this will print the combination of numbers and letters, each on a new line 

#Iterables in Python: 
#An iterable is any Python object that can be looped over 
# (iterated over) using a for loop. The following objects are 
# considered iterables in Python: 
#* Lists: [1, 2, 3], ['a', 'b', 'c'], etc.
#* Tuples: (1, 2, 3), ('a', 'b', 'c'), etc.
#* Sets: {1, 2, 3}, {'a', 'b', 'c'}, etc.
#* Dictionaries: {'key1': 'value1', 'key2': 'value2'}, etc.
#* Strings: 'Hello', "World", etc. 

#Looping a Dictionary (Iterable):  
My_Lunch = {
  'Sunday' : 'Biriyani',
  'Monday' : 'Daal Chawal',
  'Tuesday' : 'Rajma Chawal',
  'Wednesday' : 'Chole Bhature',
  'Thursday' : 'Pasta',
  'Friday' : 'Pizza',
  'Saturday' : 'Burger'
} 

#This will print only the Keys in My_Lunch dict:  
for Day in My_Lunch:
  print(Day) #this will print the keys of the dictionary, which are the days of the week, each on a new line 
#OR
for Day in My_Lunch.keys():
  print(Day) #this will also print the keys of the dictionary, which are the days of the week, each on a new line 

#This will print only the Values in My_Lunch dict: 
for Food in My_Lunch.values():
  print(Food) #this will print the values of the dictionary, which are the meals for each day, each on a new line 

#Dict. Unpacking - This will print both the Keys and Values in My_Lunch dict: 
for Day, Food in My_Lunch.items():
  print(Day, Food) #this will print the keys and values of the dictionary in a formatted string, each on a new line 
#OR 
for Item in My_Lunch.items():
  print(Item) #this will print the key-value pairs of the dictionary as tuples, each on a new line

#Let's get a bit more creative with this using formatted strings: 
for Day, Food in My_Lunch.items():
  print(f'On {Day}, I eat {Food}.') #this will print the keys and values of the dictionary in a formatted string, each on a new line 

#For Loop Counter (Indentation matters):  
My_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

Num_Count = 0 

#Num_Count gets looped over and prints Total for each of the numbers in the My_Numbers list: 
for num in My_Numbers:
    Num_Count = Num_Count + num #this will add each number in the list to the Num_Count variable, which will give us the total sum of the numbers in the list 
    print(f'The total number of numbers in the list is: {Num_Count}') 

#Vs. Here outside the For loop Num_Count prints the final Total of all numbers in My_Numbers list once: 
print(f'The total number of numbers in the list is: {Num_Count}') 

#Range() function in For Loops: 

print(range(20)) #returns range(0, 20) which is a range object that represents the sequence of numbers from 0 to 19 

for i in range(20): 
  print(i) #this will print the numbers from 0 to 19, each on a new line
#OR 
for _ in range(20): 
  print(_) #this will also print the numbers from 0 to 19, each on a new line, but using _ as the variable name instead of i 

#Stepover in range() function:
for _ in range(0,20,5): 
  print(_) #this will print the numbers from 0 to 19 with a step of 5, which means it will print 0, 5, 10, and 15, each on a new line 

#For Reverse:
for _ in range(20, 0, -5): 
  print(_) #this will print the numbers from 20 to 1 with a step of -5, which means it will print 20, 15, 10, and 5, each on a new line 

#Converting Range to List: 
for _ in list(range(0, 20, 2)):
  print(_) #this will print the numbers from 0 to 19 with a step of 2, which means it will print 0, 2, 4, 6, 8, 10, 12, 14, 16, and 18, each on a new line 

#Enumerate: 
for _ in enumerate(list(range(1,20))): #Enumerate returns the range values from 1 to 20 but with an index/serial number for each of the values...it Enumerates teh values 
  print(_) 

for c, val in enumerate(range(1,20)): #Returns the same results as above just not in a Tuple form i.e. without the brackets 
  print(c,val)

#While Loops: 
Counter = 0

while Counter < 10: 
  print(Counter) #this will print the value of Counter, which starts at 0, and will keep printing until Counter is no longer less than 10
  Counter = Counter + 1 #this will increment the value of Counter by 1 in each iteration of the loop, which will eventually make Counter equal to 10 and stop the loop from executing further 

C = [1,2,3,4,5,6,7,8,9,10,11,12]

while val in C > 5: 
  print(C.reverse()) #this will not print anything because the condition C < 10 is False from the start, so the loop will not execute at all 
  break #this will break the loop if the condition is True, but since the condition is False, this line will not be executed at all 
else:
  print('Loop has ended: No Values > 5 in list C !') #this will be executed if the loop ends without encountering a break statement, which means the condition was False and the loop was not executed at all, so it will print 'Loop has ended!' 

#Use cases of For Loops:
#1. Iterating over a list of items and performing an action on each item
#2. Iterating over a range of numbers and performing an action for each number
#3. Iterating over a dictionary and performing an action for each key-value pair 

#Use cases of While Loops:
#1. When you want to repeat a block of code until a certain condition is met
#2. When you want to create an infinite loop that runs until a break statement is encountered

#For loop vs While loop:
#1. A for loop is generally used when you know the number of iterations in advance,
# while a while loop is used when you want to repeat a block of code until a certain condition is met, and you may not know the number of iterations in advance.
#2. A for loop is more concise and easier to read when iterating over a sequence of items, while a while loop can be more flexible and powerful when you need to perform complex logic
#3. A for loop is generally faster than a while loop because it is optimized for iterating over a sequence of items, while a while loop may require more overhead to check the condition and manage the loop state.

for i in range(5):
  print(i) #this will print the numbers from 0 to 4, each on a new line 

while i < 5:
  print(i) #this will print the value of i, which starts at 4 (from the previous for loop), and will keep printing until i is no longer less than 5, which means it will only print 4 once and then stop because i will be incremented to 5 in the next line 
  i = i + 1 #this will increment the value of i by 1 in each iteration of the loop, which will eventually make i equal to 5 and stop the loop from executing further 

#while True:
#  print('This is an infinite loop!') #this will print 'This is an infinite loop!' indefinitely because the condition for the while loop is always True, so it will never stop executing unless we manually break the loop or stop the program

while True:
  input('Enter something before Loop breaks: ') 
  break #this will break the loop (irrespective of whether use enters a value or not)

while True:
  user_input = input('Enter Something to Stop the Loop: ') 
  if user_input: #this will check if the user has entered something (i.e., if the input is not empty), if it is True, it will break the loop, otherwise it will continue to prompt the user for input
    break

while True:
  user_input = input('Continue Writing anything. Say Bye to End: ') 
  if user_input.lower() == 'bye': #this will check if the user has entered 'stop' (case-insensitive), if it is True, it will break the loop, otherwise it will continue to prompt the user for input
    break

#Break, Continue and Pass Statements:

#Break Statement - The break statement is used to exit a loop prematurely when a certain condition is
#met. When the break statement is executed, the loop is immediately terminated, and the program continues with the next statement after the loop.
while True:
  user_input = input('Enter Something to Stop the Loop: ') 
  if user_input: #this will check if the user has entered something (i.e., if the input is not empty), if it is True, it will break the loop, otherwise it will continue to prompt the user for input
    break

for i in range(10):
  if i == 5: 
    break #this will break the loop when i is equal to 5, so it will only print the numbers from 0 to 4, and then stop because of the break statement


#Continue Statement - The continue statement is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped, and the loop continues with the next iteration.
while True:
  user_input = input('Enter Something to Continue the Loop: ') 
  if user_input: #this will check if the user has entered something (i.e., if the input is not empty), if it is True, it will skip the rest of the code inside the loop for that iteration and continue to prompt the user for input, otherwise it will break the loop
    continue
  else:
    break

for i in range(10):
  if i == 5: 
    continue #this will skip the rest of the code inside the loop when i is equal to 5, so it will print the numbers from 0 to 9 except for 5, which will be skipped because of the continue statement
  print(i) #this will print the value of i for each iteration of the loop, except for when i is equal to 5, which will be skipped because of the continue statement 


#Pass Statement - The pass statement is a null statement that does nothing. It is used as a placeholder in situations where a statement is syntactically required but no action is needed. When the pass statement is executed, it simply does nothing and the program continues with the next statement. 
while True:
  user_input = input('Enter Something to Continue the Loop: ') 
  if user_input: #this will check if the user has entered something (i.e., if the input is not empty), if it is True, it will execute the pass statement, which does nothing, and then continue to prompt the user for input, otherwise it will break the loop
    pass
  else:
    break

for i in range(10):
  if i == 5: 
    pass #this will do nothing when i is equal to 5, so it will print the numbers from 0 to 9, including 5, because the pass statement does not affect the flow of the loop 

print(i) #this will print the value of i for each iteration of the loop, including when i is equal to 5, because the pass statement does not affect the flow of the loop 


#Finding Duplicates with For Loop: 
some_list = [1, 2, 3, 4, 5, 1, 2, 3]

duplicates = []
for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicates: #this will check if the item is not already in the duplicates list, if it is not, it will append the item to the duplicates list, otherwise it will skip it to avoid adding duplicate items to the duplicates list
     duplicates.append(item) #this will check if the count of the item in the list is greater than 1, which means it is a duplicate, and if it is True, it will append the item to the duplicates list 
else:
  print(duplicates)

#Python Functions:
#Functions are reusable blocks of code that perform a specific task. 
# They allow you to break down your code into smaller, more manageable 
# pieces, and they can be called multiple times throughout your program. 
# Functions can take input in the form of parameters and can return 
# output using the return statement.

def Greet_Elon(): #This is where we Define a function named Greet_Elon, which takes no parameters and does not return anything
  print('Hello Alien \99/ Welcome to Mars') #This is the body of the function, which will be executed when the function is called. In this case, it will print a greeting message to Elon Musk. 

Greet_Elon() #This is where we Call the function Greet_Elon 

print(Greet_Elon) #When we print the function name without parentheses, it will return the function object itself, which is a reference to the function in memory. It will not execute the function, but instead it will show us that Greet_Elon is a function object.







