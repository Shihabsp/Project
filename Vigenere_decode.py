# This is vigenere cipher Decoding

def decode(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[l]
def value(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(l)
def vigenere(text, key):
    list_text = []
    list_key = []
    dec_cipher = ""

    for i in text:
        list_text.append(value(i))
    for i in key:
        list_key.append(value(i))
    for i in range(len(list_text)):
        c = list_text[i]    # C stands for Cipher Text
        k = list_key[i]     # K stands for Key
        p = (c-k)%26        #the decryption formula is "P = (C-K) mod 26"

        dec_cipher = dec_cipher + decode(p)

    print(dec_cipher)

text = input("Ciphertext: ")
key = input("Key: ")
i = 0
while len(text)!= len(key):
    key = key + key[i]
    i = i+1
vigenere(text, key)