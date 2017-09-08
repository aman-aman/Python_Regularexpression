import re
t=input('enter the text ')
p=input('enter the pattern ')
#search the pattern in the text
if re.search(p,t):
    print('search successfull...!!!')
    print('searched pattern was\n')
    #print the searched pattern in the text
    print(re.search(p,t).group())
#any three character then a f
if re.search('...f',t):
    print('search succesfull')
else:
    print('unsucessfull search...!!!')
    
