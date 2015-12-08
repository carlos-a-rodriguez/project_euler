import itertools


if __name__ == '__main__':
  perm = []

  for p in itertools.permutations('0123456789'):
    perm.append(''.join(list(p)))

    if len(perm) == 1000000:
      break

  print perm[-1]