import string
import os
import random

a = string.ascii_lowercase
a += ' '

def encrypt(word):
    encrypted_word = ''
    keystr = ''
    for x in word:
        key = random.randint(1, 10)
        keystr += str(key)
        keystr += ' '
        index = a.index(x)
        new_index = index + key
        if new_index >= (len(a) - 1):
            new_index -= len(a)
        y = a[new_index]
        encrypted_word += y

    f = open('key','w')
    f.write(keystr.strip())
    f.close()

    return encrypted_word


def decrypt():
    word = input('Enter the word to decrypt: ').strip()
    f = open('key', 'r')
    key_list = f.read().split(' ')
    decrypted_word = ''
    i = 0
    for x in word:
        index = a.index(x)
        new_index = index - int(key_list[i])
        if new_index < 0:
            new_index += len(a)
        letter = a[new_index]
        decrypted_word += letter
        i += 1

    return decrypted_word


user_action = input('Menu: \n \'e\' to encrypt\n \'d\' to decrypt\n \'q\' to quit\nUser input: ').lower()

while user_action != 'q':
    if user_action == 'e':
        text = input('Type your message:\n').lower()
        b = encrypt(text)
        print(b)
        user_action = input('User input: ')
    elif user_action == 'd':
        print(decrypt())
        user_action = input('User input: ')
    else:
        print('...command not found')
        user_action = input('User input: ')