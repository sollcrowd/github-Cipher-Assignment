def caesar_cipher(text, shift, direction='right'):
    if direction == 'left':
        shift = -shift
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char  # Non-alphabetic characters are not changed

    return result

# Example usage:
text_to_encode = "Hello, World!"
shift_amount = 2
encoded_text = caesar_cipher(text_to_encode, shift_amount)
print("Encoded:", encoded_text)

# To decode:
decoded_text = caesar_cipher(encoded_text, shift_amount, direction='left')
print("Decoded:", decoded_text)
