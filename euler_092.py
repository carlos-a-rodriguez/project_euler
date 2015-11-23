def sum_of_squares(xs):
  """Returns the sum of all the squares of the numbers in the list xs."""
  return sum([x ** 2 for x in xs])

def square_digits_chain(x):
  """Returns a dictionary where the key is a number and the value 
  is the last number in the square digit chain if you start from the key."""
  cache = {1: 1, 89: 89}

  for i in xrange(1, x):
    chain = [i]

    while chain[-1] not in cache:
      chain.append(sum_of_squares([int(d) for d in str(chain[-1])]))

    for number in chain:
      cache[number] = cache[chain[-1]]

  return cache


if __name__ == '__main__':
  maximum = 10000000
  print sum([1 for key, value in square_digits_chain(maximum).iteritems() if value == 89 and key < maximum])