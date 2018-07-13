#CTI-110
#P4HW1 - Distance Traveled
#Kaiya Hall
#July 1,2018

print('This program will determine the  distance traveled')

def main():
    speed = 0
    time = 0

    #user input the speed and hours

    speed = int(input('Enter the speed of the vehicle in mph:'))
    time = int(input('Enter the amount of hours traveled:'))

    #distance traveled cauculated

    print('Hour','\t','Distance Traveled')

    print('-----------------------------')

    for currentHour in range (1,time + 1):
        distance = speed * currentHour
        print(currentHour, '\t', distance)

main()


    
