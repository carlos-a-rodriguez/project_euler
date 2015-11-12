def largest_prime_factor(n):
  """Returns the largest prime factor of n."""
  if n % 2 == 0 and n > 2:
    return largest_prime_factor(n / 2)
    
  # add 0.1 for floating point error and 1 so the range includes the sqrt
  end = int(n ** 0.5 + 1.1)

  for i in xrange(3, end, 2):
    if n % i == 0:
      return largest_prime_factor(n / i)

  return n

print largest_prime_factor(600851475143)