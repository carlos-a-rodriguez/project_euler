from numpy import product


def primes_to_n(n):
  """Returns list of all prime numbers from 2 to n."""
  if n < 2:
    return []

  prime_list = [2]

  for i in xrange(3, n, 2):
    is_prime = True
    for prime in prime_list:
      if prime * prime > i:
        break
      if i % prime == 0:
        is_prime = False
    if is_prime:
      prime_list.append(i)

  return prime_list

def smallest_multiple(n):
  """Returns the smallest positive number that is evenly divisible
  by all the numbers from 1 to n."""
  sm_mult = product(primes_to_n(n))

  for i in xrange(2, n + 1):
    if sm_mult % i != 0:
      rm = sm_mult % i
      sm_mult *= (i / rm)

  return sm_mult


if __name__ == '__main__':
  print smallest_multiple(20)