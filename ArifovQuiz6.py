'''
-----------------------------------------------------------------------------
Solution: Quiz 6
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/2/2022 >
Last Mod Date: < 11/2/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <This program will add what you wish to a txt file and displays it>
-----------------------------------------------------------------------------
Description of input:
<Will collect the wishlist from the user>
Description of output:
<Displays the list to the user>
-----------------------------------------------------------------------------
'''

#Write function that writes to filename
def Write_list_to_file(list, name):
    try: 
        #Open file.txt to write
        File = open(name, 'w')

        #Writes items in list to txt
        for item in list:
            File.write(item + '\n')
        
        #Close file
        File.close()

    except:
        print("Error, problem occured when writing to", name)

#Read function that reads from filename
def Read_list_from_file(name):
    try: 
        #Open file to read
        File = open(name, 'r')

        #Puts lines to list
        List = File.readlines()

        #Closes file
        File.close()

        #Index list and removes space
        for index in range(len(List)):
            List[index] = List[index].rstrip('\n')
        
        return List

    except: 
        print('Error, problem occured when reading from', name)

def main():

    #Create new list
    wishList = []

    print("\nThis program will add what you wish to a txt file and displays it\n")

    #Used to stop loop
    stop = 'y'

    #Runs loop until user stops it
    while stop.upper() != 'N': 
        item = input("What did you wish you received from Great Pumpkin?: ")
        
        #Adds item to list
        wishList.append(item)

        #Asks user to add something to list or not
        stop = input("Would you like to continue? (y/n): ")
    
    #Filename vairable
    name = 'GreatPumpkin.txt'

    #Write function to write to a txt file
    Write_list_to_file(wishList, name)

    #Read funciton to read from a txt file
    pumpkinList = Read_list_from_file(name)

    print('\n', pumpkinList, '\n')

if __name__ == "__main__":
    main()    