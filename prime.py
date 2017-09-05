lower=int(input('Enter lower nu: '))
upper=int(input('Enter upper nu: '))

for num in range(lower,upper+1):
 
  for i in range(2,num):
    if num%i == 0:
      break

  else:
     print(num)