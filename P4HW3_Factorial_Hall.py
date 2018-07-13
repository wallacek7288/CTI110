#CTI-110
#P4HW3 - Factorial
#Kaiya Hall
#July 1,2018

print('This program will show the vaule of factorials')

def main():
    integer = int(input('Enter a number:'))

    while integer < 1:
        integer = int(input('Enter a positive number'))

    factorial = 1
    
    for currentNumber in range (1,integer + 1):
        factorial = factorial * currentNumber

    print(' The factorial of',integer,'is', factorial)

    
        
        
main()

    
