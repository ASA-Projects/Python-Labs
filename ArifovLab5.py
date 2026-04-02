'''
-----------------------------------------------------------------------------
Solution: Lab 5
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 10/11/2022 >
Last Mod Date: < 10/12/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Yoda will test user with guessing the random number>
-----------------------------------------------------------------------------
Description of input:
<The guess number will be inputed by user until user gets the number correct>
Description of output:
<Yoda will either accept or decline user depending on requirements>
-----------------------------------------------------------------------------
'''

#main
def main():
    #import random module
    import random

    #Assign variables
    guess = 0.0
    passGuess = 3.0
    
    #get random number
    num = random.randint(1,20)

    #Yoda's test for user
    print("\nHrrmmm. Into the jedi council to get, pass my test you must.. Hrmmm.")

    #Get guessed number from user
    numGuessed = int(input("guess a number between 1 and 20: "))

    #testing code
    #print(num)

    #Run while loop if random number isn't equal to guessed number
    while numGuessed != num:
        #if and else statement for right print statement
        #when it runs, it adds 1 to guess on every loop
        if numGuessed < num:
            numGuessed = int(input("Too Low, Guess Again! "))
            guess += 1 
        elif numGuessed > num: 
            numGuessed = int(input("Too High, Guess Again! "))
            guess += 1

    #if and else statement to see if user meets the requirements
    if guess <= passGuess:
        print("\nCongratulations, been accepted to the Jedi Council you have\n")
    else: 
        print("\nReady for the Jedi Council you are not. Weak with the force you are!\n")

#end main
main()