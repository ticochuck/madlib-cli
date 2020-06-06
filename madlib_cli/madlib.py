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
    ''')

requeted_words = [
    'an Adjective', 
    'an Adjective', 
    'a Firt Name', 
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
def words_input():
    for i in requeted_words:
        print(f'Please enter {i}')
        word = input()
        words.append(word)
    print(f'words entered: {words}')

def open_template():
    with open('./template.txt', 'rb') as original_template:
        contents = original_template.read()
        print(contents)
        for x in contents:
            a = contents.find(123) 
            b = contents.find(125)
            tobereplaced = contents[a:b+1]
            #print(x)
            print(tobereplaced, 'to be replcaed')
            value = 'words[0]'
            print(value, 'value')
            
            #contents.replace(tobereplaced, value)

    with open('./final_text.txt', 'wb') as final_text:
        final_text.write(contents)

def main():
    welcome_mesage()
    #words_input()
    open_template()

main()

