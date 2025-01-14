import string


print('Welcome to Word Counter!\nEnter a word or sentence and we count the amount of letters in it.')
letters = list(string.ascii_lowercase)
while True:
    num_of_letters = []
    word = input('Enter your word: ').lower()
    
    for i in word:
        if i in letters:
            num_of_letters.append(i)
            

    print(f'The number numbers of letters in the word/sentence is {len(num_of_letters)}.')
    
    print('Do you want to count again? (yes/no)')
    if not input('> ').lower().startswith('y'):
        break

print('Goodbye!')

    