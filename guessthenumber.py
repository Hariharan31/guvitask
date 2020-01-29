import random
A=['A','B','c']
a=random.choice(A)
for i in range(3):
     b=input(' ')
     if a==b:
         print('win')
     else:
         print('try again')
print('lost')
