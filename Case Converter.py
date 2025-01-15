 print('Welcome to case converter!')

def to_upper(text):
	return text.upper()

def to_lower(text):
	return text.lower()


text = input('Enter your text: ')
request = input('\nWhat case do you want to convert to? \nEnter (lower/upper): ').lower()


if request.startswith('u'):
	text_to_upper = to_upper(text)
    print('Your text has been converted!')
    print(text_to_upper)

elif request.startswith('l'):
	text_to_lower = to_lower(text)
    print('Your text has been converted!')
    print(text_to_lower)

print('Goodbye!😄')




