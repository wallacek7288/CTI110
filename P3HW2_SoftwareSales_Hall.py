#CTI-110
#P3HW2 - Software Sales
#Kaiya Hall
#6.24.2018
#

#Determine the bulk discounts

def main():
    print('This program will determine the discount for buying in bulk')

    quantity = int(input('Enter quantity to be bought'))

    # Discount for less than 10 
    if quantity < 10:
        print('No Discount Applies')
        discount = 1.0
    #Discount for more than 10 but less than 19
    elif quantity >= 10 and quantity <= 19:
        print('10% discount Applies')
        discount = 0.9
    #Discount for more than or equal to 20 but less than or equal to 49
    elif quantity >= 20 and quantity <= 49:
        print('20% discount applies')
        discount = 0.8
    #Discount for more than or equal to 50 but less than or equal to 99
    elif quantity >= 50 and quantity <=99:
        print('30% discount Applies')
        discount = 0.7
    #Discount for sales more than 100
    else:
        print('40% Discount Applies')
        discount = 0.6
    total(quantity,discount)

def total(quantity, discount):
    total_amount = quantity * discount * 99.0

    full_price = quantity * 99.0
    print('the amount of discount is', full_price - total_amount)
    print('your total purchase is',total_amount)



main()
