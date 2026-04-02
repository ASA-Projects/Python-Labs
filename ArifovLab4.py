'''
-----------------------------------------------------------------------------
Solution: Lab 4
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 9/21/2022 >
Last Mod Date: < 9/26/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <get monthly and annual expenses from expenses>
-----------------------------------------------------------------------------
Description of input:
<Gather data about their expenses>
Description of output:
<Calculate and give them their monthly and annual expenses>
-----------------------------------------------------------------------------
'''

def main():

    #get necessary data for calculation
    loan = getLoan()
    insurance = getInsurance()
    food_drink = getFoodDrink()
    maintenance = getMaintenance()

    #I calculate the total monthly expense and total annual expense
    monthlyExpense = getMonthlyExpense(loan, insurance, food_drink, maintenance)
    annualExpense = getAnnualExpense(monthlyExpense)

    #I show my results
    print(f"Total monthly expense: ${monthlyExpense:,.2f}"
        f"\nTotal annual expense: ${annualExpense:,.2f}\n")

# def calulation for adding all expenses
def getMonthlyExpense(num1, num2, num3, num4):
    getMonthlyExpense = num1 + num2 + num3 + num4
    return getMonthlyExpense

# def calulation for muliplying monthly expense with 12 to get yearly expense
def getAnnualExpense(num1):
    multiplier = 12
    getAnnualExpense = num1 * multiplier
    return getAnnualExpense

# def get input of loan amount
def getLoan():
    getLoan = float(input("\nEnter the monthly loan amount: "))
    return getLoan

# def get input of insurance amount
def getInsurance():
    getInsurance = float(input("Enter the monthly insurance amount: "))
    return getInsurance

# def get input of food and drink
def getFoodDrink():
    getFoodDrink = float(input("Enter the monthly food_drink amount: "))
    return getFoodDrink

# def get input of maintenance
def getMaintenance():
    getMaintenance = float(input("Enter the monthly maintenance amount: "))
    return getMaintenance

main()
