'''
-----------------------------------------------------------------------------
Solution: Final
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 12/6/2022 >
Last Mod Date: < 12/7/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Reads file & calculates num of sentences, unique words, & total words>
-----------------------------------------------------------------------------
Description of input:
<User inputs file they want to read>
Description of output:
<Outputs calu of num of sentences, unique words, total words, & lists the occurance>
-----------------------------------------------------------------------------

'''

#sort dictionary function
def sortDictionary(dictionaryObject):  
    return dict(sorted(dictionaryObject.items(), reverse=True, key=lambda kv:kv[1]))

def main():

    #local variables
    num_sentences = 0
    unique_words = 0
    number_of_words = 0
    punctuation = '''.,:;?!'"'''

    print("Text File Analyzer")

    #file name given by user
    file = input("\nFile path: ")

    #for while loop
    test = False

    while test == False:
        try: 
            #open file and read
            infile = open(file, 'r')

            #add content to list
            sentences = infile.read().lower()

            #close file
            infile.close()

            #calculate sentences
            for word in sentences:
                if word in '.!?':
                    num_sentences += 1

            #replace punctuations with space in list
            for i in punctuation:
                sentences = sentences.replace(i, ' ')

            #create set from list to remove duplicates
            ordered_words = sorted(set(sentences.split()))

            #create dictionary from set
            unique_dictionary = {ordered_words[i]: i*0 for i in range(len(ordered_words))}

            #calculate total words
            for i in sentences.split():
                number_of_words += 1
                
                #add 1 to value of key if in dictionary
                if i in unique_dictionary:
                    unique_dictionary[i] += 1

            #Use len function to get number of unique words
            unique_words = len(unique_dictionary)

            #pass dictionary to sorter
            unique_dictionary = sortDictionary(unique_dictionary)

            #stop loop
            test = True
        except IOError as ex:
            #file not found
            print("No such file or directory found:", ex)
            file = input("enter another file path: ")
        except Exception as ex:
            print('An unexpected problem occurred:', ex)
            file = input("enter another file path: ")
    
    #output calculations
    print('\nNumber of sentences:', num_sentences)
    print('Number of unique words:', unique_words)
    print('Total number of words:', number_of_words)

    #display dictionary 
    print('\nWord\t\t\tCount')
    print('----\t\t\t----')
    for k,v in unique_dictionary.items():
        print(k.capitalize()+'\t\t\t'+str(v))


if __name__ == '__main__':
    main()