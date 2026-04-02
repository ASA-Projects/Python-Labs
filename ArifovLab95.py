'''
-----------------------------------------------------------------------------
Solution: Lab 9.5
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/17/2022 >
Last Mod Date: < 11/18/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Creates a 6 digit combination and stores it in a file>
-----------------------------------------------------------------------------
Description of input:
<The program generates 6 digit number>
Description of output:
<The program displays the combination and writes it to a file>
-----------------------------------------------------------------------------

'''
import random

def main():
    
    #List creation
    Chest_Combination = []

    #Counter for loop
    count = 0

    #Loop runs 6 times and generates random number for list
    while count < 6:
        rand_num = str(random.randint(0,6))
        Chest_Combination.append(rand_num)
        
        count += 1
    
    print('\nThe Combination for the Chest is: ')

    #Displays the combination 
    for item in Chest_Combination:
        print(item, end=' ')

    #filename assigned
    file_name = 'christmasrecipes.txt'

    #list and name goes to function 
    Write_List_File(Chest_Combination, file_name)

#This function writes the 6 digit combination from list to a file
def Write_List_File(list, name):
    try: 
        file = open(name, 'w')

        for item in list:
            file.write(item + ' ')

        file.close()

    except IOError: 
        print('Problem occured while opening and writing to a file')

    except Exception:
        print('Unexpected problem occured')

if __name__ == '__main__':
    main()