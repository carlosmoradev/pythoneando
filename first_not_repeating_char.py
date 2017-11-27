# -*- coding: utf-8  -*-
"""
El objetivo de este algorimo es encontrar el primer caracter que no se repite 
en una secuencia de caracteres.  En caso the que todos esten repetidos, lo 
informará y terminará el programa.

Ejemplo:

|       secuencia       | caracter no repetido  |
| abavabpad             |           v           |
| atgcaatgcccata        |           _ (NO HAY)  |

"""

def first_not_repeating_char(char_sequence):
    for letter in char_sequence:
        if letter[0] == letter[1]:
            print('boths are equals')






if __name__ == '__main__':
    char_sequence = str(raw_input('Please input the characters sequence: '))

    result = first_not_repeating_char(char_sequence)

    if result == '-':
        print('All the characters are repeated. ')
    else:
        print('The first not repeated character is {}'.format(result))

