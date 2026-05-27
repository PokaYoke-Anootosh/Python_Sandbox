#Excercise_1: 

User_Name = input('What is your name? ')
Birth_Year = input('What year were you born in? ')
Current_Year = input('What is the current year? ') 
Age = int(Current_Year) - int(Birth_Year)

print(f'Hey {User_Name}, you\'re {Age} years old in {Current_Year}. \n Welcome to Python! ')


#Excercise_2: 

print('Hello')
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to 
# be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for L1st in picture:
    for Val in L1st:
        if Val == 0:
            print('', end=' ')
        else:
            print(1, end=' ')
    print('') #This takes the cursor to the next line by default after each row of the picture is printed.

#OR with  a Star instead of 1:

for L1st in picture:
    for Val in L1st:
        if Val == 1:
            print('*', end=' ')
        else:
            print('', end=' ')
    print('') #This takes the cursor to the next line by default after each row of the picture is printed.


#RETURNING A VALUE FROM A FUNCTION:
def SUM_IF_EVEN(num1, num2):
    if num1/2 == 0 and num2/2 == 0:
        return num1 + num2
    else:
        print('One of the numbers is not even!')

SumNum = sum_if_even(4,6)
print(SumNum)


