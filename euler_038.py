import itertools


if __name__ == '__main__':
  found = False

  for perm in itertools.permutations('987654321'):
    pandigital = ''.join(perm)

    for i in xrange(1, 5):
      num = int(pandigital[:i])

      result = ''
      for n in xrange(1, 10):
        result += str(num * n)

        if len(result) >= len(pandigital):
          break

      if result == pandigital:
        found = True
        break

    if found:
      break

  print pandigital
