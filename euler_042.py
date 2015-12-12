def word_value(word):
  values = [ord(c.upper()) - ord('A') + 1 for c in word]
  return sum(values)

def calc_triangle_nums(maximum=1000):
  tri_nums = [1]

  while tri_nums[-1] < maximum:
    n = len(tri_nums) + 1
    m = int(0.5 * n * (n + 1))
    tri_nums.append(m)

  return tri_nums


if __name__ == '__main__':
  words = []

  with open('res/p042_words.txt') as f:
    words = f.readline().strip().split(',')
    # remove quotes
    words = map(lambda x: x.replace('"', ''), words)

  word_values = map(word_value, words)
  # only calculate the triangle numbers you need
  maximum = max(word_values)
  tri_nums = set(calc_triangle_nums(maximum))
  # how many triangle words are there in the file
  print len(filter(lambda x: x in tri_nums, word_values))