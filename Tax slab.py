name = input('Name of individual: ')
gender = input('Gender: ')
marital = input('Marital Status: ')
age = int(input('Age: '))
income = int(input('Taxable Income: '))

male = True
female = False
Married = True
Unmarried = False

if ( male  and Married ):
    print('Taxable Income: ', income * 0.2)
    
elif ( male and Unmarried):
    print('Taxable Income: ', income * 0.1)

elif ( female and Married):
    print('Taxable Income: ', income * 0.1)

else :
    print('Taxable Income: ', income * 0.5)
