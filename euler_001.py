def summation(n):
  """Returns sum of all integers from 1 to n."""
  return n * (n + 1) / 2

def multiples_3_or_5_sum(n):
  """Returns sum of all numbers less than n that are divisible by 3 or 5."""
  num_multiples_3 = (n - 1) / 3
  num_multiples_5 = (n - 1) / 5
  num_multiples_15 = (n - 1) / 15

  return summation(num_multiples_3) * 3 + summation(num_multiples_5) * 5 - summation(num_multiples_15) * 15


if __name__ == '__main__':
  print multiples_3_or_5_sum(1000)