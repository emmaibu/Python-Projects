print('Welcome to consonant counter!')

def count_consonant(text):
  count = 0
  for i in text.lower():
    if i.isalpha() and i not in ' aeiou':
      count += 1
  return count


text = input('Enter a string: ')
num_of_consonant = count_consonant(text)
print('Counting...\nDone..')
print(f'There are {num_of_consonant} consonants in the string')
