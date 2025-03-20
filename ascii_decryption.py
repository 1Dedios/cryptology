'''
Code = list of ascii values

decoded_ascii = list of ascii values (also called ordinal numbers) converted to their char equivalent

print = a string with the decoded_ascii values

- chr() converts arguments in ascii to their character equivalent
- ord() does the opposite of chr()

'''

code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
decoded_ascii = []

for i in range(len(code)):
    decoded_ascii.append(chr(code[i]))

print(''.join(decoded_ascii))
