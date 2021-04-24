#program validates if password is strong
#a strong password has both upper- and lowercase characters
#and at least one digit

#input password to validate if atrong or not

#come up with regex for password
#write function to test password

import re
###Tried cheatibg myself out of this shit
###another fucking coding homunculus
###BUT IT FUCKING WOOOOOOOORKKS!!!!!
###LOOKS LIKE SHIT BUT WORKS AS INTENDED
lower_regex = re.compile(r'[a-z]+')
number_regex = re.compile(r'[0-9]+')
upper_regex = re.compile(r'[A-Z]+')
y = input()
def is_strong_password(x):
    password = []
    l_re = []
    n_re = []
    u_re = []
    
    if len(x) >=8:
        password_1 = lower_regex.findall(x)
        if len(password_1) >= 1:
            l_re.append(password_1)
        print('Lowercase characters', l_re)
        
        password_2 = number_regex.findall(x)
        if len(password_2) >= 1:
            n_re.append(password_2)
        print('Numbers', n_re)
        
        password_3 = upper_regex.findall(x)
        if len(password_3) >= 1:
            u_re.append(password_3)
        print('Uppercase letters', u_re)
        
        password  = l_re + n_re + u_re
    
    if len(password) >= 3:
        print('Your password is strong!')
        print(password)
    else:
        print('Invalid password')

is_strong_password(y)
