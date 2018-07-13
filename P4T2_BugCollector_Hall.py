#CTI-110
#P42 - BUG COLLECTOR
#Kaiya Hall
#June 30,2018
#

print('This program will determine the amount of bugs collected in 7 days')




def main():

    total=0

    #User input number of bugs per day
    for day in range (1,8) :
        print('Enter the bugs collected on day', day)
        

        bugs = int(input())

        #Calculate  total
        total = bugs + total
        
        #Determine the total number of bugs in 7 days
        
    print('You have collected a total of',total,'bugs.')

main()
