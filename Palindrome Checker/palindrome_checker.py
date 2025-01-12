while True:
    user_word = input('Enter your word: ')

    reversed_word = user_word[::-1]

    if reversed_word == user_word:
        print("This is a palindrome word!")
    else:
        print("This is not a palindrome word")

    print("Do you want to check another word? (yes/no)")
    if not input("> ").lower().startswith("y"):
        print("Adios!")
        break
