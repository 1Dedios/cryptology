'''
    will take a hex string and decode into bytes (text) 
    then I will take the bytes and encode in base 64

'''

import base64


hex_encoding = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

hex_decoding = bytes.fromhex(hex_encoding)

base64_encoding = base64.b64encode(hex_decoding)

print(base64_encoding)
