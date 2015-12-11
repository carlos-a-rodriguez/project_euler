from euler_010 import sieve_of_eratosthenes
from itertools import permutations


if __name__ == '__main__':
  # get all four digit primes
  primes = filter(lambda x: x > 999 and x < 10000, sieve_of_eratosthenes(10000))
  primes = set(primes)

  result = set()

  # find all permutations of each prime number
  for prime in primes:
    perms = set()
    for perm in permutations(str(prime)):
      perms.add(int(''.join(list(perm))))

    # keep only the permutations of the prime number that are themselves prime
    perms = set(filter(lambda x: x in primes, perms))

    # find primes where the difference between adjacent primes is 3330
    for p in perms:
      if p + 3330 in perms and p + 3330 * 2 in perms:
        result.add(str(p) + str(p + 3330) + str(p + 3330 * 2))

  print result
