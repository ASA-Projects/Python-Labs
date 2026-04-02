'''
-----------------------------------------------------------------------------
Solution: Lab 6
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 10/27/2022 >
Last Mod Date: < 10/27/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <student web page generator>
-----------------------------------------------------------------------------
Description of input:
<Gets user input of data>
Description of output:
<Uses data to push to void function that generates html file>
-----------------------------------------------------------------------------
'''


def main():

    #purpose
    print('Student Web Page Generator'
        '\nThis program generates a web page based on entered information.')

    #gather data
    name = input('\nName: ')
    while len(name) <= 0: 
        name = input("Must enter one or more characters. Enter your name: ")

    major = input('Major: ')
    while len(major) <= 0: 
        major = input("Must enter one or more characters. Enter your major: ")

    college = input('College: ')
    while len(college) <= 0: 
        college = input("Must enter one or more characters. Enter your college: ")

    graduationYear = input('Graducation Year: ')
    while len(graduationYear) <= 0: 
        graduationYear = input("Must enter one or more characters. Enter your expected graducation year: ")
    
    hobbiesInterests = input('Hobbies and interests: ')

    fileName = 'biography.html'

    #goes through function
    writeBiography(fileName, name, major, college, graduationYear, hobbiesInterests)

    #void function
def writeBiography(fileName, userName, major, college, graduationYear, hobbiesInterests):

    #tries to write code
    try: 

        print(f'\nWriting web page to "{fileName}."')

        outPutFile = open(fileName, 'w')

        outPutFile.write("<html>" + '\n')
        outPutFile.write("<head><title>" + college +' student: ' + userName + '</title></head>\n')
        outPutFile.write('<body>\n')
        outPutFile.write('<center><h1>' + userName + '</h1></center>\n')
        outPutFile.write('<hr />\n')
        outPutFile.write('My name is ' + userName + '. I am a ' + major + ' major at ' + college + '. I expect to graduate in ' + graduationYear + '.\n')
        outPutFile.write('<br /><br />\n')
        outPutFile.write(hobbiesInterests + '\n')
        outPutFile.write('<hr />\n')
        outPutFile.write('</body>\n')
        outPutFile.write('</html>\n')

        outPutFile.close()

        print('Done!')

    except: 
        print("Error, something went wrong")

if __name__ == "__main__":
    main()

