def sieve_of_eratosthenes(n):
  """Returns a list of all prime numbers less than or equal to n."""
  # added small value to correct for possible floating point issues
  end = int(n ** 0.5 + 0.1)

  primes = dict([(key, True) for key in xrange(3, n, 2)])
  primes[2] = True

  step = 3

  while step < end:
    for i in xrange(step * step, n, step):
      if i % 2 == 1:
        primes[i] = False

    step += 2

    while not primes[step] and step < end:
      step += 2

  return [key for key, value in primes.iteritems() if value]


if __name__ == '__main__':
  print sum(sieve_of_eratosthenes(2000000))