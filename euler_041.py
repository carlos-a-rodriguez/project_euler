import itertools


def is_prime(n):
  if n <= 1:
    return False

  if n == 2:
    return True

  sqrt = int(n ** 0.5)

  for i in xrange(2, sqrt + 1):
    if n % i == 0:
      return False

  return True


if __name__ == '__main__':
  found = False
  numbers = '987654321'

  while len(numbers) > 0:
    for perm in itertools.permutations(numbers):
      num = int(''.join(list(perm)))
      if num % 2 == 1:
        if is_prime(num):
          found = True
      if found:
        break

    if found:
      break

    numbers = numbers[1:]

  print num