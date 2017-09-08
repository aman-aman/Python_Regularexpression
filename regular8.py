import re
def fg(p,s):
       if(re.search(p,s)):
              print(re.search(p,s))
              print(re.search(p,s).group())
       

fg(r'\w+\d+','egerg888wcw8wc392')
