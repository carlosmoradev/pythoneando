# -*- coding: utf-8 -*-

def foreign_echange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('       CALCULADORA DE DIVISAS')
    print('Convertir pesos mexicanos a colombianos')
    print('=======================================')

    ammount =float(raw_input('Ingresa la cantidad en pesos mexicanos que quieres convertir: '))

    result = foreign_echange_calculator(ammount)

    print('${} mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('_________________________________________________')

if __name__ == '__main__':
    run()
    print('Final {}')