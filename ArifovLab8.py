'''
-----------------------------------------------------------------------------
Solution: Lab 8 (IMPROVED CODE)
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 11/13/2022 >
Last Mod Date: < 11/15/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Function: Translate Word to PigLatin>
-----------------------------------------------------------------------------
Description of input:
<The user inputs a txt file for the program >
Description of output:
<The program creates new text file with pig latin translation>
-----------------------------------------------------------------------------
'''

# Chapter 8 Lab - Pig Latin Translator

def main():
    print("Pig Latin Translator\n")
    print("This program translates the contents of a text file to Pig Latin.\n")

    while True:      
        try:
            # Get file path from user
            filePath = input("File path: ")

            # Attempt to open and read contents of specified file and 
            # Split the text into a list based on newline character (each line of text becomes an element in list)
            linesList = readFile(filePath).split("\n")
        except Exception as ex:
            # If there is an error opening file
            print(ex)
        else:
            break       # Exit loop if there are no problems
        # end try        
    # end while

    # Translate and add each line to translated list
    translatedLinesList = []
    for line in linesList:
        translatedLinesList.append(translateLineToPigLatin(line))
    # end for

    try:
        # Determine name for translated file
        periodIndex = filePath.rfind(".")
        translatedFilePath = filePath[:periodIndex] + "PigLatin" + filePath[periodIndex:]

        # Write translation to file
        print("\nTranslating...")
        writeFile(translatedFilePath, translatedLinesList)
        print("Translated file written to", translatedFilePath)
    except Exception as ex:
        # If there is an error writing file
        print(ex)
    # end try    
# end function


def readFile(filePath):
    try:
        # Open file path for reading
        fileObject = open(filePath, "r")

        # Read all lines from file
        fileContents = fileObject.read()
    except FileNotFoundError:
        raise FileNotFoundError("Unable to open file: the specified file does not exist.")
    except:
        raise Exception("An unexpected problem occurred whilst opening the file.")
    else:
        fileObject.close()

        return fileContents
    # end try
# end function


def writeFile(filePath, linesList):
    try:
        # Open file path for writing
        fileObject = open(filePath, "w")

        # Ensure there is at least 1 item in list
        if len(linesList) > 0:
            # Process each line of text in list
            for line in linesList:
                # Write each translated line to file
                fileObject.write(line)
            # end for
        else:
            raise Exception("Unable to translate: the file does not contain any text.")
        # end if
    except:
        raise Exception("An unexpected problem occurred whilst writing the file.")
    else:
        fileObject.close()
    # end try
# end function


def translateLineToPigLatin(line):
    translatedLine = ""
    
    # If line has one or more character
    if len(line) > 0:
        # If line ends with a newline character, remove it
        if line.endswith("\n"):
            line = line.rstrip("\n")
        # end if
        
        # Split line into a words list based on a space
        wordList = line.split(" ")

        # Concatenate each translated word with a trailing space to translatedLine
        for word in wordList:
            translatedLine += translateWordToPigLatin(word) + " "
        # end for
    # end if

    return translatedLine + "\n"    # Return translated line with trailing newline character
# end function


def translateWordToPigLatin(word):

    #true or false if 1st letter is uppercase
    was_up = word[0].isupper()
    
    #if word has more than 1 characters
    if len(word) > 0:
        
        #It's one terminator because we process 1 word at a time
        terminator = ''

        #If terminator detected, then assign variable and remove it
        if word[-1] in '.,:;?!' or word.endswith("..."): 
            terminator = word[-1]
            word = word[:-1]

        #if first letter is vowel, then add 'yay' and terminator
        if word[0].lower() in 'aeiou':
            word = word + 'yay' + terminator

        #if consontant then
        #move 1st letter using string slice to end and add 'ay' and terminator
        if word[0].lower() in 'bcdfghjklmnpqrstvwxyz':
            word = word[1:].lower() + word[0].lower() + 'ay' + terminator
        
        #If true, capitalize first letter
        if was_up is True:
            word = word.capitalize()

        return word

    else:
        return word
        	
# end function


# DO NOT MODIFY CODE BELOW THIS LINE
if __name__ == "__main__":
    main()
# end if