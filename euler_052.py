def anagram(x, y):
  """Returns True if x and y are anagrams."""
  if len(x) != len(y):
    return False

  letters = {}

  for char in x:
    if char in letters:
      letters[char] += 1
    else:
      letters[char] = 1

  for char in y:
    if char not in letters:
      return False
    letters[char] -= 1

  return all([val == 0 for key, val in letters.iteritems()])


if __name__ == '__main__':
  exp = 2
  ans = None

  while ans is None:
    for x in xrange(1 * 10 ** exp, int(1.7 * 10 ** exp)):
      ys = [x * y for y in xrange(1, 7)]
      
      if all([anagram(str(ys[i]), str(ys[i - 1])) for i in xrange(1, len(ys))]):
        ans = x
    exp += 1

  print ans