def sum_of_self_powers(n):
  """Returns the sum of all self powers from 1 to n (inclusive), 
  where a self power is in the for x^x."""
  return sum(map(lambda x: x ** x, range(1, n + 1)))


if __name__ == '__main__':
  # print last 10 digits of the sum of the first 1000 self powers
  print str(sum_of_self_powers(1000))[-10:]