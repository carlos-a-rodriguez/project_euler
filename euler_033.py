import fractions


if __name__ == '__main__':
  epsilon = 0.00001

  result = []

  for n in xrange(10):
    for d in xrange(1, 10):
      for x in xrange(n + 1, 10):
        numerator = n * 10 + x
        denominator = x * 10 + d

        if abs(float(numerator) / denominator - float(n) / d) < epsilon:
          result.append((numerator, denominator))

  num_prod = reduce(lambda (w, x), (y, z): (w * y, x * z), result)

  gcd = fractions.gcd(num_prod[0], num_prod[1])

  print num_prod[1] / gcd
