import re
def fg():
           s='thequickbrownfoxjumpoverthelazydog'
           if(re.search(r'amanjha|dog',s)):
                  print('search successfull')
           else:
                  print('search unsuccessfull')
             

fg()
