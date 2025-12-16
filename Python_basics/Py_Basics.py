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
print(9.9+1.1)

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





#Type conversion:
#print(int(3.8))