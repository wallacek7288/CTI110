#Determine test grade average of 5 test
#July 4, 2018
#CTI-110 P5HW1 - Test Average and Grade
#Kaiya Hall
#.

print(' This program will determine the average of 5 test grades')

    
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 +score5) / 5
    return average

def determineGrade ( userscore ):
    if (userscore >= 90):
        return 'A'
    elif (userscore >= 80 and userscore < 90):
        return 'B'
    elif (userscore >= 70 and userscore < 80):
        return 'C'
    elif (userscore>= 60 and userscore <70):
        return 'D'
    else:
        return 'F'
    
def printGrade( score1,score2,score3,score4,score5):
    print(' \nScore\tLetter Grade')
    print ( str(score1) + "\t\t" + determineGrade( score1 ), \
            str(score2) + "\t\t" + determineGrade( score2 ), \
            str(score3) + "\t\t" + determineGrade( score3 ), \
            str(score4) + "\t\t" + determineGrade( score4 ), \
            str(score5) + "\t\t" + determineGrade( score5 ), sep = "\n")
    
def askForScore():
    score1 = float(input( 'Enter score 1:'))
    score2 = float(input( 'Enter score 2:'))
    score3 = float(input( 'Enter score 3:'))
    score4 = float(input( 'Enter score 4:'))
    score5 = float(input( 'Enter score 5:'))

    return score1,score2,score3,score4,score5

def main():
    score1, score2, score3, score4,score5 = askForScore()
    printGrade( score1,score2,score3,score4,score5)
    print('Your average is :', calc_average(score1,score2,score3,score4,score5))
    
main()



