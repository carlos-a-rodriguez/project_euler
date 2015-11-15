def nth_prime(n):
  """Returns the nth prime number."""
  prime_list = []

  if n < 1:
    return prime_list

  prime_list.append(2)

  num = 3

  while len(prime_list) < n:
    is_prime = True
    for prime in prime_list:
      if prime * prime > num:
        break
      if num % prime == 0:
        is_prime = False
    if is_prime:
      prime_list.append(num)
    num += 2

  return prime_list[-1]