import re
def fg(p,s):
       if(re.search(p,s)):
              print(re.findall(p,s))
             
s=input()
fg(r'ab+',s)
fg(r'ab*',s)
fg(r'ab{3}',s)
fg(r'ab{2,3}',s)
