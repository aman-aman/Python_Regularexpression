import re
def se(p,t):
    if(re.search(p,t)):
        print('search successfull')
        print(re.search(p,t).group())
        #group(n) nth set of paranthesis
        print(re.search(p,t).group(1))
        print(re.search(p,t).group(2))
    else:
        print('unsucessfull search')



#[] are used for special setof character
#se(r'\w+@[\w+.]\w+','gsfomfdiosmsmd jhakraman@gmail.com dn232')
se(r'([\w]+)+@([\w.]+)([\w+])','gsfomfdiosmsmd jhakraman@gmail.com dn232')
