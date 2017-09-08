import re
def se(p,t):
    if(re.search(p,t)):
        print('search successfull')
        print(re.search(p,t).group())
    else:
        print('unsucessfull search')

t=input('input text : ')
p=input('input pattern : ')

se(p,t)

print("searching the character starting with a\n")
se('a^',t)
print("searching the character starting with aman\n")
se('aman^',t)
print("searching the character ending with g\n")
se('...g',t)

se('..h','fndufdfndidfehoenmeo much better:aman')

#starting with a and ending with n
se('a..n','vfviemvefoewekpowamanded much better:aman')

#return object of string which start with c. and end with l
# r denote to read the given format 
se(r'c\.l','c.dndooefoemfol much better mn')
        


#return object of string which start with c. and end with d
se(r'c\.d','c.dndooefoemfol much better mn')

#\w denote the word or a letter in given format (only the first appreance)
se(r'c\w\w','gsfomfdiosmsmdcdmfd')
se(r'c\w\w\w','gsfomfdiosmsmdcdmfd')
se(r'c\w\w\w\w','gsfomfdiosmsmdcdmfd')
se(r'c\w\w','gsfomfdiosmsmdcdmfdamamamsmsckjl')

#\d denote the digit in given format
se(r'c\d\d','gsfomfdiosmsmdc456fd')
se(r'c\d\w','gsfomfdiosmsmdc4e6fd')

#\s denote the whitespace in given format
se(r'c\s\d','gsfomfdiosmsmdc 456fd')

#+ denote any number of time
se(r'c\s+\d+\w','gsfomfdiosmsmdc       456fd')


se(r'\w+@\w+.\w+','gsfomfdiosmsmd jhakraman@gmail.com dn232')


