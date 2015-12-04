import itertools
import string


def apply_key_to_cipher(ascii_cipher, key):
  """Returns the XOR of the ascii_cipher and the key.
  
  Args:
    ascii_cipher: a list of ascii encoded characters
    key: a string

  Returns:
    A list of ascii encoded characters resulting from
      XORing the ascii_cipher with the key
  """
  key = [ord(k) for k in key]

  xor = []

  for i in xrange(len(ascii_cipher)):
    xor.append(ascii_cipher[i] ^ key[i % len(key)])

  return xor


if __name__ == '__main__':
  with open('res/p059_cipher.txt') as f:
    cipher = f.readline().strip().split(',')

  cipher = [int(x) for x in cipher]

  results = {}

  for perm in itertools.product(string.ascii_lowercase, repeat=3):  
    xor = apply_key_to_cipher(cipher, ''.join(list(perm)))
    text = ''.join([chr(x) for x in xor])
    # split by a space to separate out the words
    words = text.split(' ')
    # count the number of words
    results[''.join(list(perm))] = len(words)

  # use the text with the most words (may not always work on every text)
  code = max(results, key=results.get)

  print sum(apply_key_to_cipher(cipher, code))
