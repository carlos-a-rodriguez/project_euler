import math


if __name__ == '__main__':
  numbers = []

  with open('res/p099_base_exp.txt') as f:
    for line in f:
      base, exp = line.strip().split(',')
      numbers.append((int(base), int(exp)))

  logs = map(lambda (base, exp): exp * math.log10(base), numbers)

  # add one to find the line number because python list is zero indexed
  print logs.index(max(logs)) + 1