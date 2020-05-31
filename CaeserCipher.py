
#CaeserCipher accepts 3 parameters
#message,mode and key
#mode: can be either 1(Encryption) or 2(Decryption)
#key: any non-negative integer smaller than 26

import pandas as pd
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
    #copying the result to clipboard        
    df = pd.DataFrame(list(result))
    df.to_clipboard(index=False,header=False)
    print("Result has been copied to clipboard!!!")
    return result
print(CaeserCipher("What is GitHub",1,3))



