#User Age Generator: 

User_Name = input('What is your name? ')
Birth_Year = input('What year were you born in? ')
Current_Year = input('What is the current year? ') 
Age = int(Current_Year) - int(Birth_Year)

print(f'Hey {User_Name}, you\'re {Age} years old in {Current_Year}. \n Welcome to Python! ')


#User Password Checker: 

User_Password =input('Create your Password: ') 
Encrypted_Password = '*' * len(User_Password)

print(f'Hey {User_Name}, your password {Encrypted_Password} is {len(User_Password)} characters long \n and is successfully Encrypted! ')

#For Loop Counter: 
My_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

Num_Count = 0 

for num in my_Numbers:
    Num_Count = Num_Count + 1 
    print(f'The total number of numbers in the list is: {Num_Count}') 

print(f'The total number of numbers in the list is: {Num_Count}') 


