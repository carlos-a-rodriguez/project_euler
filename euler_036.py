def generate_k_digit_palindromes(k):
  """Returns a list of all positive k digit palindromes."""
  if k == 1:
    return range(10)

  if k == 2:
    return [x * 11 for x in xrange(1, 10)]
  
  result = []

  if k % 2 == 0:
    stop, step = 100, 11
    lhs_digits = (k - 2) / 2
  else:
    stop, step = 10, 1
    lhs_digits = (k - 1) / 2

  for lhs in xrange(10 ** (lhs_digits - 1), 10 ** lhs_digits):
    for mid in xrange(0, stop, step):
      # if even, the middle is two digits but zero is just one
      # so add another zero to have a double 0 middle
      if mid == 0 and k % 2 == 0:
        num_string = str(lhs) + str(mid) + '0' + str(lhs)[::-1]
      else:
        num_string = str(lhs) + str(mid) + str(lhs)[::-1]
      result.append(int(num_string))

  return result

def generate_palindromes(n):
  """Returns a list of all palindromes less than n."""
  result = []
  digits = len(str(n - 1))

  for d in xrange(1, digits):
    result.extend(generate_k_digit_palindromes(d))

  result.extend(filter(lambda x: x < n, generate_k_digit_palindromes(digits)))

  return result

def is_palindrome(s):
  """Returns True if the string s is a palindrome.""" 
  return s == s[::-1]


if __name__ == '__main__':
  palindromes = generate_palindromes(1000000)
  print sum([x for x in palindromes if is_palindrome(bin(x)[2:])])
