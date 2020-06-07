requeted_words = [
    'an Adjective', 
    'an Adjective', 
    'a First Name', 
    'a Past Tense Verb', 
    'a First Name',
    'an Adjective', 
    'an Adjective', 
    'a Plural Noun', 
    'a Large Animal', 
    'an Small Animal', 
    "a Girl's Name", 
    'an Adjective', 
    'a Plural Noun', 
    'an Adjective', 
    'a Plural Noun', 
    'a Number 1-50', 
    "a First Name's", 
    'a Number', 
    'a Plural Noun', 
    'a Number', 
    'a Plural Noun']
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

def words_input():
    """
    Function to promt the user to input the different words/numbers
    to be used in the madlib template. 
    """
    for i in requeted_words:
        
        print(f'Please enter {i}')
        word = input()
        words.append(word)
    print(f'words entered: {words}')

def open_template():
    """
    Open and read the template.txt file locate in the assets folder
    """
    try:
        with open('./assets/template.txt', 'r') as original_template:
            contents = original_template.read()
            count = 0
            while count < len(words):
                for x in contents[:1]:
                    a = contents.find('{')
                    b = contents.find('}') 
                    tobereplaced = contents[a:b+1]
                    value = words[count]
                    new_content = contents.replace(tobereplaced, value, 1)
                    contents = new_content
                count += 1

        with open('./assets/final_text.txt', 'w') as final_text:
            final_text.write(new_content)
            print(new_content)
    except FileNotFoundError:
        with open('./assets/error_log.txt', 'w') as error_log:
            error_log.write('File does not exits error')


def main():
    """
    Calls the functions needed to run the program.
    """
    welcome_mesage()
    words_input()
    open_template()

main()

