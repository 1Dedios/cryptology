
'''
        takes hex encryption and decrypts to text
        
        bytes.fromhex() will convert a hex string to bytes (text) 
        .hex() will convert a byte string to hex representation
'''

hex_encryption = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

print(bytes.fromhex(hex_encryption))
