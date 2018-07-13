#CTI-110
#P5T1 - Kilometer Converter
#Kaiya Hall
#July 4, 2018

print('This program will convert kilometers to miles')

conversion_factor = 0
.6214

def main():

    kilometers = float(input('Enter the distance in kilometers:'))

    show_miles(kilometers)

def show_miles(km) :

    miles = km * conversion_factor

    print(km,'kilometers equals',miles,'miles.')

main()
