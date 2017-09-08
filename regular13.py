import re
def fg(p):
       s='amankumarjhaiscurrentlyinkolkata'
       if(re.search(p,s)):
              print('search successfull')
              print(re.search(p,s).group())
       else:
           print('search unsuccessfull')
             
p=input()
fg('^p')
