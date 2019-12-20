n = int(input('Enter the Number: '))

assume = 1
for d in range(2, n):
    if (n%d ==0):
        assume = 0
        break
if assume :
    print('This is prime number')

else:
    print('THis is not Prime number')


' ' '

    
