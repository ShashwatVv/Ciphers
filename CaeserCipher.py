
#CaeserCipher accepts 3 parameters
#message,mode and key
#mode: can be either 1(Encryption) or 2(Decryption)
#key: any non-negative integer smaller than 26
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def CaeserCipher(message, mode, key ):
    message = message.upper()
    result = ''
    ##if encryption
    if mode == 1:
        for x in message:
            if x in Letters:
                num = (Letters.find(x) + key) %26
                x = Letters[num]
            else:
                x = x
            result = result + x

    ##if decryption
    elif mode == 2:
        for x in message:
            if x in Letters:
                num =(Letters.find(x) - key)%26
                x = Letters[num]
            else:
                x = x
            result = result + x

    return result
