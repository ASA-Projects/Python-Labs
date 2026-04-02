'''
-----------------------------------------------------------------------------
Solution: Lab 9
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/17/2022 >
Last Mod Date: < 11/18/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Program creates dictionaries & identifies key with it's values>
-----------------------------------------------------------------------------
Description of input:
<Asks user to input a key from dictionary>
Description of output:
<Displays the key with its associated values>
-----------------------------------------------------------------------------

'''

def main():

    #create lists
    Name = ['Crusher', 'Riker', 'Spock', 'Sulu', 'Troi']
    Rank = ['Commander', 'Capitain', 'Ambassador', 'Lt. Commander', 'Counselor']
    Salary = ['120,000', '240,000', '360,000', '100,000', '125,000']

    #create dictionaries using dictionary comprehension
    nameRankDic = {Name[i]: Rank[i] for i in range(len(Name))}
    nameSalaryDic = {Name[i]: Salary[i] for i in range(len(Name))}

    #Display table 1
    print('\nName(key)\tRank(value)')
    print('---------------------------')
    for key, value in nameRankDic.items():
        print(key +'\t\t'+ value)

    #Display table 2
    print('\nName(key)\tSalary(value)')
    print('-----------------------------')
    for key, value in nameSalaryDic.items():
        print(key +'\t\t'+ value)

    #Do again variable
    again = 'y'

    #Displays purpose of code
    print("\nThis program finds a person's rank and salary")
    
    #Runs until user puts any other character than y
    while again.upper() == 'Y':
        #Get user input
        user_input = input('\nEnter name to find their rank and salary: ')
        Rank = nameRankDic.get(user_input.capitalize(), 'default')
        Salary = nameSalaryDic.get(user_input.capitalize(), 'default')

        print('\n\t' + user_input.capitalize())
        print('-----------------------')
        print(Rank +'\t'+ Salary)

        again = input('\nPress y or Y to continue: ')
    
if __name__ == '__main__':
    main()