while True:

    num = int(input('Enter the number: '))

    if num % 2 == 0:
      print('This is an even number!')
    else:
      print('This is an odd number!')
   
    print('Do your want to check another number? (yes/no)')
       if not input('> ').lower().startswith('y'):
          break
print('Goodbye!')
  
