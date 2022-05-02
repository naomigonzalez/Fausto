# import random
# a=[]
# n=int(input("Enter number of elements:"))
# for j in range(n):
#     a.append(random.randint(1,20))
# print('Randomised list is: ',a)

# generate random integer values
# import random import seed
from random import randint
# seed random number generator
# seed(1)
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)