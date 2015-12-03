from euler_036 import generate_palindromes


def largest_palindrome_from_product_of_two_k_digits_numbers(k):
  lo, hi = 10 ** (k - 1), 10 ** k - 1

  pals = generate_palindromes(hi * hi + 1)

  pals = sorted([x for x in pals if x >= lo], reverse=True)

  for pal in pals:
    for i in xrange(int(pal ** 0.5 + 0.25), lo - 1, -1):
      if pal % i == 0 and pal / i <= hi:
        return pal

if __name__ == '__main__':
  print largest_palindrome_from_product_of_two_k_digits_numbers(3)
