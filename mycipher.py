import sys

def caesar_cipher(shift, text):
    encrypted_text = []
    for char in text.upper():
        if 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encrypted_text.append(chr(shifted))
        # Ignore any characters outside A-Z
    return ''.join(encrypted_text)

def format_output(encoded):
    blocks = [encoded[i:i+5] for i in range(0, len(encoded), 5)]
    lines = [' '.join(blocks[i:i+10]) for i in range(0, len(blocks), 10)]
    return '\n'.join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mycipher.py <shift>")
        sys.exit(1)
    shift = int(sys.argv[1])  # Accepts the shift amount from command line argument
    input_text = sys.stdin.read()

    # Encrypt the input text
    encrypted_message = caesar_cipher(shift, input_text)

    # Format and print the output
    formatted_encrypted_message = format_output(encrypted_message)
    print(formatted_encrypted_message)
