def sum_of_squares(n):
  """Returns the sum of the squares of all numbers from 1 to n."""
  return n * (n + 1) * (2 * n + 1) / 6

def square_of_sum(n):
  """Returns the square of the sum of all numbers from 1 to n."""
  return (n * (n + 1) / 2) ** 2


if __name__ == '__main__':
  print square_of_sum(100) - sum_of_squares(100)