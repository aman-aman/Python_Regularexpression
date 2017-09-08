import re
def fg(p,s):
       if(re.search(p,s)):
              print(re.findall(r'([\w]+)([\d]))',s)
       

fg(r'([\w]+)+([\d]+))','egerg888wcw8wc392')
