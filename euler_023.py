def factors(n):
  """Returns a list of all the factors of n."""
  f = []

  sqrt = int(n ** 0.5)

  for i in xrange(1, sqrt):
    if n % i == 0:
      f.extend([i, n / i])

  if sqrt * sqrt == n:
    f.append(sqrt)
  elif n % sqrt == 0:
    f.extend([sqrt, n / sqrt])

  return sorted(f)


def is_abundant(n):
  """Returns True if n is an abundant number. If the sum of a number's
  proper factors is greater than the number itself, then it is an
  abundant number. sum of proper factors of 12: 1 + 2 + 3 + 4 + 6 = 16 > 12."""
  f = factors(n)
  return sum(f[:-1]) > n


if __name__ == '__main__':
  maximum = 28124
  abundants = []

  for i in xrange(1, maximum):
    if is_abundant(i):
      abundants.append(i)

  results = set()
  # find all numbers that are the sum of two abundant numbers
  for i in xrange(len(abundants)):
    for j in xrange(len(abundants)):
      results.add(abundants[i] + abundants[j])

  all_numbers = set(range(1, maximum))
  # sum of all numbers that are not the sum of two abundant numbers
  print sum(all_numbers - results)
