# Convert Feet to Inches
# July 4,2018
# CTI-110 P5T2_FeetToInches
# Kaiya Hall

INCHES_PER_FOOT = 12

def main():

    feet = int(input('Enter number of feet:'))

    print(feet,' equals',feet_to_inches(feet),'inches.')

def feet_to_inches(feet) :
    return feet * INCHES_PER_FOOT

main()
