
import itertools
import time
import string

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def decrypt_with_partial_key(numbers, used_letters, perm):
    partial_mapping = dict(zip(used_letters, perm))
    return ''.join(partial_mapping[char] for char in numbers)

cipher_text = input("Enter the cipher text (letters only): ").upper()
cipher_text = ''.join([c for c in cipher_text if c.isalpha()])
used_letters = sorted(set(cipher_text))

attempts = 0
start_time = time.time()

for perm in itertools.permutations(string.ascii_uppercase, len(used_letters)):
    mapping = dict(zip(used_letters, perm))
    _ = ''.join(mapping[char] for char in cipher_text)
    attempts += 1

end_time = time.time()
elapsed = end_time - start_time

print(f"Attempts: {attempts}")
print("Elapsed time: %.2f seconds" % elapsed)
