'''
-----------------------------------------------------------------------------
Solution: Lab 7
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/2/2022 >
Last Mod Date: < 11/3/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Program that calculates monthly electric bills>
-----------------------------------------------------------------------------
Description of input:
<Monthly electric bills is entered to the program>
Description of output:
<Displays the total, average, highest, and lowest bill in the year>
-----------------------------------------------------------------------------
'''

#Total funciton
def get_total(list):
    #Counter 
    total = 0.0

    #Adds items in a list
    for num in list:
        total += num
    return total

def main():

    #Create two lists
    electricBill = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
 
    #For loop to display each month
    for m in months:
        item = int(input(f'Enter the electric bill for {m}: '))
        electricBill.append(item)
    
    #Put list into funciton to get total
    total = get_total(electricBill)

    #Average calculation
    average = total / len(electricBill)

    #Use build-in functions to get max and min
    highestBill = max(electricBill) 
    lowestBill = min(electricBill)

    #Find where highest and lowest is located in a list
    monthHighest = electricBill.index(highestBill)
    monthLowest = electricBill.index(lowestBill)

    #Display the total and average
    #The last two uses the location of the highest and lowest on bill list to use it on the month list
    print(f'Total electric bill: ${total:.2f}'
        f'\nAverage electric bill: ${average:.2f}' 
        f'\nHighest electric bill: {months[monthHighest]}'
        f'\nLowest electric bill: {months[monthLowest]}\n')

if __name__ == "__main__":
    main()