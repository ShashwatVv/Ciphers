
#CaeserCipher accepts 3 parameters
#message,mode and key
#mode: can be either 1(Encryption) or 2(Decryption).
#key: any non-negative integer smaller than 26.
#Letters: string of characters on which the cipher is based.
#A default string of 26 English alphabets has already been provided.

import pandas as pd
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def CaeserCipher(message, mode, key, Letters = Letters ):
    message = message.upper()
    result = ''
    n = len(Letters)
    ##if encryption
    if mode == 1:
        for x in message:
            if x in Letters:
                num = (Letters.find(x) + key) %n
                x = Letters[num]
            else:
                x = x
            result = result + x

    ##if decryption
    elif mode == 2:
        for x in message:
            if x in Letters:
                num =(Letters.find(x) - key)%n
                x = Letters[num]
            else:
                x = x
            result = result + x
    #copying the result to clipboard        
    df = pd.DataFrame(list(result))
    df.to_clipboard(index=False,header=False)
    print("Result has been copied to clipboard!!!")
    return result



