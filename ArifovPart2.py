'''
-----------------------------------------------------------------------------
Solution: Midterm Part 2
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 10/11/2022 >
Last Mod Date: < 10/12/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Max function will return greater number from two integers>
-----------------------------------------------------------------------------
Description of input:
<The user will be asked to enter two integer numbers>
Description of output:
<The program will show the greater number or both if equal>
-----------------------------------------------------------------------------
'''

def main():

    #Purpose of the program
    print("\nThe program will check two numbers and show the greater number or both if equal")

    #Asks user for two integer numbers
    num1 = int(input("Enter one number "))
    num2 = int(input("Enter another number "))

    #The numbers will go through the max function
    answer = max(num1, num2)

    #This will show the greater number or both if equal
    print(str(answer) + "\n")


#The max function will identify the greater number or if they are equal
def max(int1, int2):
    if int1 < int2:
        return int2
    elif int1 > int2:
        return int1
    else:
        return int1, int2

#end main
main()