# This is vigenere cipher encoding

def encode(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[l]
def value(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(l)
def vigenere(text, key):
    list_text = []
    list_key = []
    enc_cipher = ""

    for i in text:
        list_text.append(value(i))
    for i in key:
        list_key.append(value(i))
    for i in range(len(list_text)):
        p = list_text[i]    # p stands for Plain Text
        k = list_key[i]     # K stands for Key
        c = (p+k)%26        # The Ecryption formula is " C = (P+K) mod 26"

        enc_cipher = enc_cipher + encode(c)

    print(enc_cipher)

text = input("Plaintext: ")
key = input("Key: ")
i = 0
while len(text)!= len(key):
    key = key + key[i]
    i = i+1
vigenere(text, key)