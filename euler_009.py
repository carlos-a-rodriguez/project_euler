if __name__ == '__main__':
  for a in xrange(1000 / 3, 0, -1):
    for b in xrange(1000 / 3, 1000, 1):
      c = 1000 - a - b

      if a ** 2 + b ** 2 == c ** 2:
        print a * b * c
        break