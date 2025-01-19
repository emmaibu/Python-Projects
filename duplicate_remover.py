user_input = input('Enter your request: ')

no_duplicate = ''.join(dict.fromkeys(user_input))

print("Duplicates has been removed. Here is your text:", no_duplicate)
