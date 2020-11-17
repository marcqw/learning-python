number = input('Number ?')


print('Choisir un chiffre')
state = 'xx'

while state != 'win':
    test = input('essai: ')
    if test > number:
        print('moins')
    elif test < number:
        print('plus')
    elif test == number:
        print('Yes!')
        state = 'win'
