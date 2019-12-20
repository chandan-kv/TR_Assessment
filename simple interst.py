p = int(input('What is the Principle amount: '))
r = float(input('What is the rate of interest: '))
t = int(input('No of Years: '))

ry = r / 100

a = p + p * ry * t

interst = a - p

print('Interst amount: ',interst)
