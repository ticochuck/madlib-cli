
from datetime import datetime

dateTimeObj = datetime.now()
words = []

def welcome_mesage():
    """
    This function displays a welcome message to a user and
    provides some basic intructions on how the game works. 
    """
    print('''
    Welcome to Madlib!
    
    How it works

    Madlibs is a phrasal template word game where 
    one player prompts others for a list of words
    to substitute for blanks in a story before 
    reading aloud. 
                            'Source: Wikipedia.'

    You will be prompted to enter a series of words/numbers.
    When you are done, the program will display a story
    based upon your input.
    ''')

def get_words(contents):
    curly = "{"
    last_word = False
    count = 0
    
    while not(last_word):
        for x in contents[:1]:
            if curly not in contents:
                last_word = True
            else: 
                a = contents.find('{')
                b = contents.find('}') 
                tobereplaced = contents[a:b+1]
                print(f'Please enter {tobereplaced[1:-1]}')
                word = input()
                words.append(word)
                value = words[count]
                new_content = contents.replace(tobereplaced, value, 1)
                contents = new_content
            count += 1
    
    return new_content

def write_new_content(new_template):
    with open('./assets/final_text.txt', 'w') as final_text:
            final_text.write(new_template)
            print(new_template)


def open_template():
    """
    Open and read the template.txt file locate in the assets folder
    """
    try:
        with open('./assets/template.txt', 'r') as original_template:
            contents = original_template.read()
            
            get_words(contents)
            write_new_content(get_words)
        
    except FileNotFoundError as err:
        with open('./assets/error_log.txt', 'a' ) as error_log:
            error_log.write(f'\nFile does not exits error: \n{err}\n{str(dateTimeObj)}\n')
    except TypeError as err:
        with open('./assets/error_log.txt', 'a' ) as error_log:
            error_log.write(f'\nType Error encountered: \n{err}\n{str(dateTimeObj)}\n')


def main():
    """
    Calls the functions needed to run the program.
    """
    try:
        welcome_mesage()
        open_template()    
    except KeyboardInterrupt:
        print('Program was closed by the user')    

main()

