'''
-----------------------------------------------------------------------------
Solution: Lab 3
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 9/18/2022 >
Last Mod Date: < 9/20/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <is to double $500 every year in the stock market>
-----------------------------------------------------------------------------
Description of input:
<Get data on how many years the person was in the stock market>
Description of output:
<Table showing the years and its correponding year total. Then the whole total>
-----------------------------------------------------------------------------
'''

#I assign variables
total = 0
multiplier = 2
start_amount= 500

#I explain the program
print(f"\nThis program will double your money on the stock market starting at ${start_amount}")

#I gather data about years in market
num_years = int(input("\nThe number of years in the stock market? ")) 

#validate number of years
while num_years < 0:
    print ("\nERROR: the number cannot be negative")
    num_years = int(input("\nEnter the correct years in the market "))

#I create table
print('\nYear\tTotal')
print('--------------')

#I use a loop to calculate the amount after doubling
#I did + 1 to make years work
for num in range(0, num_years + 1):
    year_total = start_amount*multiplier**num
    total += year_total
    print(f'{num}\t{year_total:,.1f}')

#I give data about years and total     
print(f"\nThe total value of your account after {num_years} years is: ${total:,.1f}")