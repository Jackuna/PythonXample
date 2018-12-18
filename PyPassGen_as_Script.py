from random import choice

# User defined Inputs
pass_len=input("Your desired Password Length (ie : 0-16) characters  :  ")
pass_no=input('How many Passowords ? :  ')

# Casting string to integers
cast_pass_len=int(pass_len)
cast_pass_no=int(pass_no)

keyboard_char='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_-'
print()

for i in range(cast_pass_no):
    if i == 0:
        print('Here are your', cast_pass_no, 'random passwords ! \n')
        
    hard_pass=''
    for j in range(cast_pass_len):
        hard_pass+=choice(keyboard_char)
 
    print(hard_pass)

    
   # Same Script as an User defined function.

def Gen_Strong_Pass(pass_len,pass_no):
    
    # User defined Inputs
    pass_len=input("Your desired Password Length (ie : 0-16) characters  :  ")
    pass_no=input('How many Passowords ? :  ')
    
    # Casting string to integers
    cast_pass_len=int(pass_len)
    cast_pass_no=int(pass_no)
    print()
    
    for i in range(cast_pass_no):
        if i == 0:
            print('Here are your', cast_pass_no, 'random passwords ! \n')
            
        hard_pass=''
        for j in range(cast_pass_len):
            hard_pass+=choice(keyboard_char)

        print(hard_pass)
        
 
Gen_Strong_Pass(8,3)