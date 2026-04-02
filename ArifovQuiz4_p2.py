
'''
-----------------------------------------------------------------------------
Solution: Quiz 4
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 9/21/2022 >
Last Mod Date: < 9/22/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Number choosing that displays messsage if picked>
-----------------------------------------------------------------------------
Description of input:
<the person will choose between 1 and 10>
Description of output:
<displays message if numbers picked, but will end if inputed anything else>
-----------------------------------------------------------------------------
'''
def main():

    #if the input is true it will run, if it isn't it will end
    while True: 
        #It will try the to see if it works
        try:
            #asks a user for number between 1 and 10
            num_picked = int(input("\nPick number between 1 and 10: "))

            #this will check if the input if between 1 and 10
            while int(num_picked) >= 1 and int(num_picked) <= 10: 
                print("Mr. Todaro smells like hot dog water")
                num_picked = input("\nPick number between 1 and 10: ")

        #ValueError means it couldn't turn input into integer
        #Break will end the program
        except ValueError:
            break     
main()