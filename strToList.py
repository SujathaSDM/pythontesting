phrase = 'Don`t panic!'
plist = list(phrase)

print(phrase)
print(plist)
print(''.join(plist))
for i in range(4):
    plist.pop()
print(''.join(plist))
plist.remove("`")
print(''.join(plist))
plist.pop(0)
print(''.join(plist))
plist.extend([plist.pop(),plist.pop()])
print(''.join(plist))
plist.insert(2,plist.pop(3))
print(''.join(plist))
print(''.join(plist))
