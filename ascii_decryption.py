"""
Decrypts ASCII values to their alphabetical equivalent.

Args:
    ascii_val (list): ascii values in list form

Returns:
    Human readable, ASCII decrypted message.
"""


def ascii_decrypter(ascii_val):
    message = ""
    for val in ascii_val:
        message += chr(val)
    return message


def main():

    code = [
        99,
        114,
        121,
        112,
        116,
        111,
        123,
        65,
        83,
        67,
        73,
        73,
        95,
        112,
        114,
        49,
        110,
        116,
        52,
        98,
        108,
        51,
        125,
    ]

    message = ascii_decrypter(code)
    print(message)


if __name__ == "__main__":
    main()
