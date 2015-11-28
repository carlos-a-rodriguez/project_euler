def fact(n):
  """Returns the factorial of n, i.e. n!."""
  if n == 1 or n == 0:
    return 1
  return reduce(lambda x, y: x * y, range(1, n + 1))

def digit_sum(n):
  """Returns the sum of the digits in n."""
  return reduce(lambda x, y: int(x) + int(y), str(n))


if __name__ == '__main__':
  print digit_sum(fact(100))