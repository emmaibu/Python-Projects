import datetime

print('Welcome to Age Calculator!')
while True:
    try:
        
        user_birth_year = int(input('Enter the year you were born: '))
        user_birth_month = int(input('Enter the month you were born (1-12): '))
        user_birth_date = int(input('Enter the day you were born (1-7): '))

        user_date = datetime.datetime(user_birth_year, user_birth_month, user_birth_date)
        current_date = datetime.datetime.now()

        user_age = current_date - user_date
        user_age = user_age.days
        
        user_year = int(user_age/365)
        user_month = int(user_age / 30.44)
        user_week = int(user_age / 7)
        print('\nResult')
        print(f"""Approximte Age: 
                You are {user_year} years old
                {user_month} month(s) old
                {user_week} week(s) old
                {user_age:,} day(s) old"""
            )
        
    except ValueError:
        print('Please enter valid numbers.')
        
    print('\nDo you want to calculate another age? (yes/no)')
    if not input('> ').lower().startswith('y'):
        break
print('Goodbye!\nThanks for using Age Calcuator!')


