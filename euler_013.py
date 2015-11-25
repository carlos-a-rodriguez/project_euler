def first_k_digits_of_sum(numbers, k):
  """Returns the first k digits of the sum of all the values in numbers."""
  return str(sum(numbers))[:k]


if __name__ == '__main__':
  path = 'res/p013_numbers.txt'
  numbers = []

  with open(path, 'r') as f:
    for line in f:
      numbers.append(long(line.strip()))

    print first_k_digits_of_sum(numbers, 10)