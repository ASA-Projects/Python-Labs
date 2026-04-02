'''
-----------------------------------------------------------------------------
Solution: Lab 2
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 9/7/2022 >
Last Mod Date: < 9/16/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Calculates dog's years based on human years>
-----------------------------------------------------------------------------
Description of input:
<Person gives data of dog in human years>
Description of output:
<The code calculates the dog years based on human years>
-----------------------------------------------------------------------------
'''
#I Define the Equation
FIRST_YEAR = 15
SECOND_YEAR = 9
THREE_PLUS_YEARS_MULTI = 5

#I display the purpose of code
print('''This program calculates a dog's approximate age in "dog years" based on human years.\n''')

#I gather data about dog in human years
human_years = float(input("Dog's age in human years? "))

#I calculate based on what was given
#I display the end result in second block so it doesn't interfer with 1st
if human_years < 0:
    print('\nHuman years must be a positive number.')
else: 
    if human_years <= 1:
        dog_age = FIRST_YEAR * human_years
    elif human_years <= 2: 
        dog_age = FIRST_YEAR + SECOND_YEAR * (human_years - 1)
    else:
        dog_age = FIRST_YEAR + SECOND_YEAR + THREE_PLUS_YEARS_MULTI * (human_years - 2)
    print(f"\nA dog with a human age of {human_years:.1f} years is {dog_age:.1f} in dog years.")
    

    
    

