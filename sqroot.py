lower=int(input('Enter lower nu: ')
upper=int(input('Enter upper nu: ')

for num in range(lower,upper+1):
  sum=0
  digit=0
  temp=num
  while temp >0:
    digit = num%10
    sum +=digit**3
    temp //=10

if num == sum
   print(num)