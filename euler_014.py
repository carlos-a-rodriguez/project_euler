def length_collatz_seq(num, d):
  """Returns the number of integers in the collatz sequence of num.
  d is dictionary cache of the solutions found so far."""
  if num in d:
    return d[num]
  else:
    if num % 2 == 0:
      d[num] = length_collatz_seq(num / 2, d) + 1
    else:
      d[num] = length_collatz_seq(3 * num + 1, d) + 1
  return d[num]


def longest_collatz_seq(n):
  """Returns the largest starting number less than n with the longest
  collatz sequence."""
  d = {1: 1}

  for i in xrange(2, n):
    length_collatz_seq(i, d)

  return sorted(d, key=d.get, reverse=True)[0]


if __name__ == '__main__':
  print longest_collatz_seq(1000000)