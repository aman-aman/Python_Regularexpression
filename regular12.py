import re
def fg(p):
       s='amankumarjhalivesinjamshedpur'
       if(re.match(p,s)):
              print('search successfull')
              print(re.match(p,s).group())
       else:
           print('search unsuccessfull')
             
p=input()
fg(p)
