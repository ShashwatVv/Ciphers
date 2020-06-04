Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bruteForce(message,Letters=Letters):
    message = message.upper()

    #trying all possible keys
    for key in range(len(Letters)):

        #empty string containing translated message 
        translated=''

        #inspecting for every symbol or aplphabet 
        for x in message:
            if x in Letters:
                num = (Letters.find(x)-key)%len(Letters)
                x = Letters[num]
            else:
                x = x

            translated = translated + x

        print(('For key {:d}, Translated message is: {:s}').format(key,translated))

