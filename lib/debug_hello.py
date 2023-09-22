def encode(text, key):
    print(f"text = {text}")
    cipher = make_cipher(key)
    print(f"cipher = {cipher}")

    ciphertext_chars = []
    for i in text:
        print(f"i = {i}")
        ciphered_char = chr(65 + cipher.index(i))
        print(f"ciphered_char = {ciphered_char}")
        ciphertext_chars.append(ciphered_char)
        print(f"ciphertext_chars = {ciphertext_chars}")

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    print(f"key = {key}")
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet
    print(f"cipher_with_duplicates = {cipher_with_duplicates}")

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")