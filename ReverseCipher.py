#Reverse Cipher

plain_text = "Cephalus said that justice was about paying one debts and speaking the truth, to which Socrates refuted."

def Encrypt(PlainText = plain_text):
    cipher_text= ''
    
    i = len(PlainText)-1
    while(i>=0):
        cipher_text = cipher_text+PlainText[i]
        i= i-1

    return cipher_text
