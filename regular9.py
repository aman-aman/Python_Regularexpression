import re
def fg(p,s):
       if(re.search(p,s)):
              #print(re.search(p,s))
              print(re.search(p,s).group())
              print(re.findall(p,s))
              #print(re.findall(p,s).group())

fg(r'[a-zA-Z0-9]','egerg888wcw8wc392')
fg(r'[Pp]ython','amanjha loves python')
fg(r'[aeiou]','amankumarjhaiscurrentlyatkolkata')
