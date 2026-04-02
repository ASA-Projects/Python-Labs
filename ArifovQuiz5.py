'''
-----------------------------------------------------------------------------
Solution: Quiz 5
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 10/27/2022 >
Last Mod Date: < 10/27/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <create character txt with levels to stats>
-----------------------------------------------------------------------------
Description of input:
<No inputs, only runs code>
Description of output:
<writes code to character txt about character stats with random numbers>
-----------------------------------------------------------------------------
'''
import random

def main():

    #using try and except
    try:  
        myfile = open('character.txt', 'w')

        #writing to myfile
        myfile.write('Strength ' + str(random.randint(1,18)) + '\n')
        myfile.write('Constitution ' + str(random.randint(1,18)) + '\n')
        myfile.write('Wisdom ' + str(random.randint(1,18)) + '\n')
        myfile.write('Intelligence ' + str(random.randint(1,18)) + '\n')
        myfile.write('Dexterity ' + str(random.randint(1,18)) + '\n')
        myfile.write('Charisma ' + str(random.randint(1,18)) + '\n')
    
        myfile.close()

        print("character.txt updated\n")

    #except error
    except IOError: 
        print("Error, something went wrong")


if __name__ == "__main__":
    main()
