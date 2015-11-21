def power_digit_sum(n):
  """Returns the sum of all the digits of n."""
  return sum([int(i) for i in str(n)])


if __name__ == '__main__':
  print power_digit_sum(2 ** 1000)