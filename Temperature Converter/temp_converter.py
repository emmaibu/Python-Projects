print('Welcome to TempConverter!')


def convertToFahren(cel):
    fahren = (cel * 9/5) + 32
    return round(fahren, 2)


def convertToCelsius(fahren):
    cel = (fahren - 32) * 5/9
    return round(cel, 2)


while True:
    conversion = ''
    while conversion not in ['fc', 'cf']:
        print('Please enter "fc" for Fahrenheit to Celsius or "cf" for Celsius to Fahrenheit.')
        conversion = input('''What conversion do you want to perform? celsius to fahrenheit? Enter(cf) or fahrenheit to celsius? Enter(fc)\n> ''').lower()

    try: 
        if conversion == 'fc':
            fahren = int(input('Enter the degree in farenhiet: '))
            convert = convertToCelsius(fahren)
            print(f'{fahren} degree fahrenheit equals {convert} degree celsius.')

        elif conversion == 'cf':
            cel = int(input('Enter the degree in celsius: '))
            convert = convertToFahren(cel)
            print(f'{cel} degree celsius equals {convert} degree fahrenheit.')
            
    except ValueError:
        
        print('Please enter a valid input!')

    print('Do you want to perform another conversion? (yes/no)')
    if not input('> ').lower().startswith('y'):
        break
print('Goodbye!')

