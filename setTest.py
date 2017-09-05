vowels='aeeiouuaa'
vowels=set(vowels)
word=input("enter string to test")
vowels = vowels.union(set(word))
print(word)
print(sorted(list(vowels)))
