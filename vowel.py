vowel = 'aeiou'
vowel = list(vowel)
word = input('Enter a word : ')
found = []
for letter in word:
    if letter in vowel:
        if letter not in found:
           found.append(letter)
    else:
        print(letter)
vowel.insert(3, 100)
print(found)
print(vowel)
