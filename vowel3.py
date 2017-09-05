vowel = ['a','e','i','o','u']
found = {}
word = input("Enter word to count no of vowels :")

#for letter in vowel:
#    found[letter] = 0
for letter in word:
    if letter in found:
        found[letter] +=1
    else:
        found[letter] = 1    

for k,v in sorted(found.items()):
    if v != 0 :
         print('Key ', k , 'was found', v , 'times(s)')
