#CTI-110
#P3HW1 - Age Classifier
#Kaiya Hall
#6.23.18
#

#Determine Age

def main():
    print('This program will classify age')
    age = int(input (' Enter  age'))

    # if person is 1 or younger
    if age <= 1:
        print('Person is an infant')
    # if person is older than 1 but younger than 13
    elif age > 1 and age < 13:
        print('Person is a child')
    # if person is at least 13 , but less than 20
    elif age >= 13 and age < 20:
        print('Person is a  teenager')
    else:
        age >= 20
        print('Person is an adult')

main()

