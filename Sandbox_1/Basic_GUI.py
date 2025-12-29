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

#Solution:
for line in picture:
  for digit in line:
    if digit == 0:
      print(' ', end=' ')
    else:
      print('*', end=' ')
  print(' ') #This prints a new line after each row of the picture
print('Merry Christmas!') #This prints a message at the end of the picture

