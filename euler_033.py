import fractions


if __name__ == '__main__':
  epsilon = 0.00001

  result = []

  for n in xrange(10):
    for d in xrange(n + 1, 10):
      for x in xrange(n + 1, 10):
        numerator = n * 10 + x
        denominator = x * 10 + d

        if abs(float(numerator) / denominator - float(n) / d) < epsilon:
          result.append((numerator, denominator))

  frac = reduce(lambda (w, x), (y, z): (w * y, x * z), result)

  gcd = fractions.gcd(frac[0], frac[1])

  print frac[1] / gcd
