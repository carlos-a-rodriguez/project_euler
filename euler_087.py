from euler_010 import sieve_of_eratosthenes


if __name__ == '__main__':
  limit = 50000000

  last_sqrt = int(limit ** (1 / 2.)) + 1

  result = set()

  primes = sorted(sieve_of_eratosthenes(last_sqrt))

  for c in primes:
    for b in primes:
      partial_sum = c ** 4 + b ** 3
      if partial_sum >= limit:
        break

      for a in primes:
        full_sum = partial_sum + a ** 2
        if full_sum >= limit:
          break

        result.add(full_sum)

  print len(result)
