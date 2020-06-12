
Message ="Shashwat is not that obnoxious."

def encryptMessage(message = Message, key=6):

    cipherText = ['']*key

    for col in range(key):

        index = col

        while index < len(message):

            cipherText[col] += message[index]
            index +=key

    return ''.join(cipherText)

