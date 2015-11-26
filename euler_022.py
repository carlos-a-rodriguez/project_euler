import csv


def total_name_score(names):
  total_score = 0

  for i in xrange(len(names)):
    name_score = 0
    for letter in names[i].lower():
      name_score += ord(letter) - ord('a') + 1
    total_score += name_score * (i + 1)

  return total_score


if __name__ == '__main__':
  path = 'res/p022_names.txt'

  try:
    with open(path, 'r') as f:
      csvfile = csv.reader(f, delimiter=',')
      names = []

      for line in csvfile:
        names.extend(line)

      print total_name_score(sorted(names))
  except IOError as e:
    print e