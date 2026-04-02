'''
-----------------------------------------------------------------------------
Solution: Lab 1
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 9/1/2022 >
Last Mod Date: < 9/3/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <To calculate how many rations a Player can buy while also showing their stats>
-----------------------------------------------------------------------------
Description of input:
<I'm gathering info about their name, level, and gold>
Description of output:
<I use the data given to calculate the amount of rations they can buy>
-----------------------------------------------------------------------------
'''

# Im gathering data about the person
name = input("What is your character's name? ")
level = int(input('What is your level? '))
gold = float(input('How Much Gold Do You Have? '))

# I divide using integer division to not get partial rations
# I divide by 5 since 1 ration costs 5 gold
rations = (gold) // 5.0

# I print the data and the rations. 
# I combine print statements with \n
print('Here is the data you entered: ' 
    '\nName:  ', name,
    '\nlevel: ', level, 
    '\ngold:  ', gold, 
    '\nThe number of rations that you can purchase is ', rations)


  