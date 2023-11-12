
def letterCount(letter,text):
  count = 0
  i = 0

  while i < len(text):
     if text[i] == letter:
          count = count + 1
     i = i + 1

  return count   


text = 'You never get a second chance to make a first impression' 
x = input('Enter the letter: ')
print(f'The letter {x} appears {letterCount(x,text)} times in the text.')