#CTI-110
#P3LAB
#Kaiya Hall
#6.24.2018
#

def main():
    #This program takes a number grade and outputs a letter grade.

    #system uses a 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    score = int(input('Enter grade'))

    if score >= 90:
        print('Your grade is: A')
    elif score < 90 and score >= 80:   
        print('Your grade is : B')
    elif score < 80 and score >= 70:
        print('Your grade is: C')
    elif score < 70 and score >= 60:
        print('Your grade is: D')
    else:
        print('Your grade is: F')
        
        
# Program Start
main()

    
