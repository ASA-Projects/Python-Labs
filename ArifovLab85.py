'''
-----------------------------------------------------------------------------
Solution: Lab 8.5
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/9/2022 >
Last Mod Date: < 11/10/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Software Package for Password Requirements>
-----------------------------------------------------------------------------
Description of input:
<User enters password>
Description of output:
<Program checks password to see if it meets requirements>
-----------------------------------------------------------------------------
'''
#function to check uppercase
def upper(password):
    num_upper = 0
    
    for i in password:
        if i.isupper():
            num_upper += 1
    return num_upper

#function to check lowercase
def lower(password):
    num_lower = 0

    for i in password:
        if i.islower():
            num_lower += 1
    return num_lower

#function to check numbers
def digit(password):
    num_digit = 0 

    for i in password:
        if i.isdigit():
            num_digit += 1
    return num_digit

def main():
    #purpose
    print("Create a password that has atleast 6 characters, 1 uppercase, 1 lowercase, and 1 digit \n")

    password = input("Create password: ")

    #checks if password is atleast 6 characters
    while len(password) < 6:
        print('\nThe password must have atleast 6 characters')
        password = input('Enter new password: ')

    #checks the uppercase, lowercase, and digits
    num_upper = upper(password)
    num_lower = lower(password)
    num_digit = digit(password)

    #loop to see if there is atleast 1 upper, lower, and digit
    while True: 
        if num_upper < 1:
            print("\nThe password must have atleast 1 uppercase")
            password = input("Enter new password: ")

        if num_lower < 1:
            print("\nThe password must have atleast 1 lowercase")
            password = input("Enter new password: ")

        if num_digit < 1:
            print("\nThe password must have atleast one digit")
            password = input("Enter new password: ")

        num_upper = upper(password)
        num_lower = lower(password)
        num_digit = digit(password)

        #loop breaks if upper, lower, and digit is atleast 1
        if num_lower >= 1 and num_upper >= 1 and num_digit >= 1:
            break

    #password created
    print('\nPassword Successfully Created!')


if __name__ == '__main__':
    main()