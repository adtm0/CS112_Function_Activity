def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    
    # Are the numbers distinct?
    a = is_distinct(num1,num2,num3)

    # If yes (numbers are distinct)
    if a == 'True':
        print(f"Result is {num1 + num2 + num3}")
        
    # If no (some/all numbers are the same)
    else:
        print(f"Result is {not_distinct(num1,num2,num3)}")

# Checks if the numbers are distinct
def is_distinct(num1,num2,num3):
    if (num1 != (num2 & num3)) & (num2 != (num1 & num3)) & (num3 != (num1 & num2)) :
        return True
    else:
        return False

# For numbers that are not distinct
def not_distinct(num1,num2,num3):
    if num1 == num2 == num3:
        return num1 ** 3
    
    elif (num1 == num2) & (num1 !=num3):
        return ((num1 ** 2) + num3)
    
    elif (num1 == num3) & (num1 !=num2):
        return ((num1 ** 2) + num2)
    
    elif (num2 == num3) & (num2 !=num1):
        return ((num2 ** 2) + num1)
    else:
        return
        
main()