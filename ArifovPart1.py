'''
-----------------------------------------------------------------------------
Solution: Midterm Part 1
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 10/11/2022 >
Last Mod Date: < 10/12/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <This program uses human years to calculate dog years>
-----------------------------------------------------------------------------
Description of input:
<Gets user input of dog age in human years>
Description of output:
<The program calculates and returns the approximate dogs age>
-----------------------------------------------------------------------------
'''
# Constants
FIRST_YEAR_EQUIV = 15
SECOND_YEAR_EQUIV = 9
THREE_PLUS_YEARS_MULTIPLIER = 5

def main():
    # Output program's purpose
    print("\nThis program calculate's a dog's approximate age in \"dog years\" based on human years.")

    #assign variable to run loop again
    again = 'y'

    #loop to run calculation again
    while again == 'y' or again == 'Y':
        # Get human years from user
        humanYears = float(input("\nDog's age in human years? "))

        #validate to number for it to be positive
        while humanYears < 0:
            print("\nTo calculate a dog's age in human years, please enter a value of zero or greater.")
            humanYears = float(input("Dog's age in human years? "))
    
        #goes through function to run calculation
        dogYears = getDogYears(humanYears)

        #prints results from calculation
        print("\nA dog with a human age of", format(humanYears, ",.1f"), "years is", 
            format(dogYears, ",.1f"), "in dog years.")

        #asks user if they want to run loop again
        again = input("Would you like to calculate another dog age? (Y/n): ")

#function to run calculation
def getDogYears(humanYears):
    if humanYears <= 1:
        dogYears = FIRST_YEAR_EQUIV * humanYears
    elif humanYears <= 2:
        dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV * (humanYears - 1)
    else:
        dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV + THREE_PLUS_YEARS_MULTIPLIER * (humanYears - 2)
    return dogYears

# DO NOT MODIFY CODE BELOW THIS LINE
if __name__ == "__main__":
    main()
# end if

