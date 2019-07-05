#!/usr/bin/python3

import clipboard # import pyperclip
import random

def generatesecretkey(): 
    letters=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '.', '<', '>', '?', '-', '=']

    # The length of the string is 50 
    secret_key_list=random.sample(numbers, 10) + random.sample(numbers, 10) + \
    random.sample(symbols, 10) + random.sample(symbols, 10) + random.sample(letters, 10)

    random.shuffle(secret_key_list)
    secret_key=''.join(secret_key_list)

    # print(secret_key)
    
    return secret_key

    clipboard.copy(secret_key) # pyperclip.copy(secret_key)
    secret_key_clip=clipboard.paste() # secret_key_clip=pyperclip.paste()


if __name__=='__main__':
    generatesecretkey()
