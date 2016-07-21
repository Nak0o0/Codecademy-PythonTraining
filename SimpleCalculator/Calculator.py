
import sys
addition = 0
subtraction = 0
multiplication = 0
division = 0
result = 0
global num_1=0
global num_2=0

def main_menu():
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

main_menu()
user_choice = int(input("Please choose what would you like to do: "))
def numbers():
    #global num_1
    num_1 = int(input("Please enter a number! Your first number is: "))
    #global num_2
    num_2 = int(input("Please enter a second number!Your second number is: "))


if user_choice == 1:
    numbers()
    result = num_1 + num_2
    print (result)
    
elif user_choice == 2:
    numbers()
    result = num_1 - num_2
    print (result)
    
elif user_choice == 3:
    numbers()
    result = num_1 * num_2
    print (result)
    
elif user_choice == 4:
    numbers()
    result = num_1 / num_2
    print (result)
    
else:
    print ("Not a valid answer!")
    sys.exit(0)