# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:36:26 2017
##code test
@author: candid
"""


from Crypto.Cipher import AES

key = '0123x4567xxxxxxxxxxx89abcdef'
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'j' * 64 + 'i' * 128+ 'Ajit' *128+'LTI'*16
ciphertext = encryptor.encrypt(text)

print (ciphertext)
# Decrypt 

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

print (plain)

'''
1. Create a Key file in S3
2.Keep all the keys in the S3 : Access key+ Secrete Key , 
(Assign to variable )
3.Retrive the S3 Keys use BOTO
4.Encrypt the file using Salt 
5.Store back the file in Encrypt file in S3

Decrypt: 
6.Retrive the encrypted file 
7.Decrypt it using the Salt 

