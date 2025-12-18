# escape sequences
# This module provides functions to handle escape sequences in strings.


print("Hello,\nWorld!")  # New line escape sequence
print("Column1\tColumn2")  # Tab escape sequence
print("This is a backslash: \\")  # Backslash escape sequence
print("She said, \"Hello!\"")  # Double quote escape sequence
print('It\'s a beautiful day!')  # Single quote escape sequence
print("This is a bell sound:\ahello")  # Bell/alert escape sequence

print("This is a form feed:\fhello")  # Form feed escape sequence

print("This is a carriage return:\rhi this is")  # Carriage return escape sequence


print("This is a vertical tab:\v")  # Vertical tab escape sequence
print('\x41')  # Hexadecimal escape sequence
print('\101')  # Octal escape sequence
print('\u0041\u0042\u0043')  # Unicode escape sequence
print('\U00000041')  # Unicode escape sequence with 8 digits
print('\N{LATIN SMALL LETTER i}')  # Named Unicode escape sequence

print("\N{GRINNING FACE}")                # 😀
print("\N{SMILING FACE WITH SMILING EYES}") # 😊
print("\N{FACE WITH TEARS OF JOY}")        # 😂
print("\N{SMILING FACE WITH SUNGLASSES}")  # 😎
print("\N{THINKING FACE}")                 # 🤔
print("\N{LOUDLY CRYING FACE}")            # 😭
print("\N{WINKING FACE}")                  # 😉

