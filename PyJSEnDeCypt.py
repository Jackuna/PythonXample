# ----------------------------------------------------------------------------------------------  #
# PyJSEnDeCypt : Based upon famour Caesar cipher to encrypt or decrpt messages
#
# This script takes input messages to encrypt and then using the same key you 
# can decrypt the message
# ----------------------------------------------------------------------------------------------  #


def js_encrypt():

    global alphabets
    alphabets='abcdefghijklmnopqrstuvwxyz'

    
    usr_msg=input('Type your message to encrypt: ')
    key=input('Provide us your secret key : ' )

    enc_string=''

    casted_usr_msg=str(usr_msg)
    key=int(key)

    for val in casted_usr_msg:
        if val in alphabets:
            position=int(alphabets.find(val))
            enc_position=(position+key) % 26
            enc_string+=alphabets[enc_position]

        else:
            enc_string+=val
    

    print(enc_string)


def js_decrypt():

    usr_msg=input('Type or copy paste your encrypted message to descrypt: ')
    key=input('Input us your provided secret key : ' )

    dec_string=''

    casted_usr_msg=str(usr_msg)
    key=int(key)

    for val in casted_usr_msg:
        if val in alphabets:

            position=int(alphabets.find(val))
            dec_position=(position-key) % 26
            dec_string+=alphabets[dec_position]

        else:
            dec_string+=val
    

    print(dec_string)


js_encrypt()
js_decrypt()
