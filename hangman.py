#-*- conding:utf-8 -*-
import random

IMAGES = ['''

 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          ||
| |     
| |     
| |     
| |     
| |     
| |     
| |         
| |         
| |         
| |         
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |          -`--'.
| |         
| |     
| |      
| |     
| |         
| |         
| |         
| |         
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   |
| |          | . |
| |          |   |
| |          -----
| |         
| |         
| |         
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . | 
| |     ')   |   | 
| |          -----     
| |               
| |               
| |               
| |                
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          -----
| |               
| |               
| |               
| |                
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'--
| |          ||   
| |          ||   
| |          ||   
| |         / |    
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''

___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''', '''
''']

WORDS = [
    'hardware',
    'software',
    'mouse',
    'keyboard',
    'monitor',
    'card',
    'network',
    'bandwidth'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print ('')
    print(hidden_word)
    print(' --- *' * (len(hidden_word) -1) )

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Choose a Letter: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('sorry, you loose.  The right word is {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Contrats!  You win! The winner word is {}'.format(word))
            break




if __name__ == '__main__':
    print('HANGMAN GAME.')
    run()
