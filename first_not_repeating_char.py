# -*- coding: utf-8  -*-


if __name__ == '__main__':
    char_sequence = str(raw_input('Please input the characters sequence: '))

    result = first_not_repeating_char(char_sequence)

    if result == '-':
        print('All the characters are repeated. ')
    else:
        print('The first repeated character is {}'.format(result))