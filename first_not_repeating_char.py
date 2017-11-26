# -*- coding: utf-8  -*-
"""
El objetivo de este algorimo es encontrar el primer caracter que no se repite 
en una secuencia de caracteres.  En caso the que todos esten repetidos, lo 
informará y terminará el programa.

Ejemplo:

|       secuencia       |   caracter repetido   |
| abavabad              |           v           |
| atgcaatgcccata        |           _ (NO HAY)  |

"""

def first_not_repeating_char(char_sequence):
    pass





if __name__ == '__main__':
    char_sequence = str(raw_input('Please input the characters sequence: '))

    result = first_not_repeating_char(char_sequence)

    if result == '-':
        print('All the characters are repeated. ')
    else:
        print('The first repeated character is {}'.format(result))

