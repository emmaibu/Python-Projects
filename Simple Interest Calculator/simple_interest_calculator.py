print('Welcome to Simple Interest Calculator!')

def calcSimpleInterest(principal, rate, time):
    si = (principal * rate * time)/100
    return round(si, 2)

def calcPrincipal(si, rate, time):
    principal = (si *  100)/ (rate * time)
    return round(principal, 2)

def calcRate(si, principal, time):
    rate = (si * 100)/ (principal * time)
    return round(rate, 2)
    
def calcTime(si, principal, rate):
    time = (si * 100)/ (principal * rate)
    return round(time, 2)

while True:
    try:
        request = ''
        while request not in ['si', 'p', 'r', 't']:
            request = input("What do you want to find? Enter 'si' for Simple Interest, 'r' for Rate, 'p' for Pricipal, and 't' for Time.\n> ")
            if request not in ['si', 'p', 'r', 't']:
                print('Please enter a valid input.')

        if request == 'si':
            principal = float(input('Enter the principal: '))
            rate = float(input('Enter the rate: '))
            time = float(input('Enter the time: '))
            si = calcSimpleInterest(principal, rate, time)
            print(f'The simple interest is ${si}.')

        if request == 'p':
            si = float(input('Enter the simple interest: '))
            rate = float(input('Enter the rate: '))
            time = float(input('Enter the time: '))
            principal = calcPrincipal(si, rate, time)
            print(f'The principal is ${principal}.')

        if request == 'r':
            si = float(input('Enter the simple interest: '))
            time = float(input('Enter the time: '))
            principal = float(input('Enter the principal: '))
            rate = calcRate(si, principal, time)
            print(f'The rate is {rate}%.')

        if request == 't':
            si = float(input('Enter the simple interest: '))
            principal = float(input('Enter the principal: '))
            rate = float(input('Enter the rate: '))
            time = calcTime(si, principal, rate)
            print(f'The time is {time} year(s).')
            
        print('Do you want to perform another calculation? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
            
    except ValueError:
        print('Please enter numeric values only.')
        
        

print('Goodbye!')