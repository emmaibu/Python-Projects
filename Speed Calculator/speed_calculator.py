while True:
    try:

        distance = int(input('Entert the distance: '))
        time = int(input('Enter the time:'))

        speed = distance/time
        speed = round(speed, 2)

        print(f'The speed is {speed}')
        
        print('Do you want to calculate another speed? (yes/no)')
        if not input('> ').lower().startswith('y'):
           break

    except ValueError:
        print('Invalid. Please enter numeric values only.')

print('Goodbye!')