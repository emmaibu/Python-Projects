print('Calculate the area of your triangle here!')

while True:
    try:
        height = float(input('Enter the height of the triangle: '))
        base = float(input('Enter the base of the triangle: '))
        area = (base * height)/2
        area = round(area, 2)
        
        print(f'The area of the triangle is {area} units.')
        print('Do you want to count again? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
        
    except ValueError:
        print('Please enter numeric values only')
    

print('Goodbye!')