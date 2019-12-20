import re
data = ['ab','abc','a5e','a6f','123 a6c','a5b','a55b','a555b','a5555b','a55555b','a555555b','a5xb','1/4','3+2=5','def ghi','abc ab']
for item in data:
    m = re.search(r'(55){2}', item)
    if m:
        print (m.group() + ' matched in ' + '\'' + item + '\'')
################################################################

import re
expr = '37.0 degree centigrate is equal tp +98.6 farhenheit'
pattern = r'-|\+?\d+\.?\d*|\.?\d+'
print(expr)
print ('Trying to find a floating point numbers in the statement...')

match = re.findall(pattern, expr)
if match:
    print('Following numbers are matched', match)
else:
    print('Seems like there is no floating point number')
    
