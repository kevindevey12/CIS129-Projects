# Kevin Devey
# March 15, 2024
# Module Lab 5 - This program inputs the number of bottles collected over 7 days and returns the total payout.

# Lab 5 The Bottle Return Program
# Declare variables
totalbottles = 0
todaybottles = 0
counter = 1
totalpayout = 0
keepgoing = 'y'
NBR_OF_DAYS = 7
PAYOUT_PER_BOTTLE = 0.10

# Loop main program
while keepgoing == 'y':
    while counter <= NBR_OF_DAYS:
        # Get daily bottles and add to accumulator
        print ('Enter number of bottles returned for day #' + str(counter) + ":", end='')
        todaybottles = input()
        totalbottles = totalbottles + int(todaybottles)
        counter = counter + 1
    #Calculate and display results
    totalpayout = totalbottles * PAYOUT_PER_BOTTLE
    print('\nThe total number of bottles collected is ' + str(totalbottles))
    print(f'The total paid out is $ {totalpayout:.2f}\n')
    #Prompt to repeat
    print('Do you want to enter another week\'s worth of data?')
    print('(Enter y or n): ', end='')
    keepgoing = input()
    # Reset values if repeating
    if keepgoing == 'y':
        print()
        totalbottles = 0
        totalpayout = 0
        counter = 1
# End Program