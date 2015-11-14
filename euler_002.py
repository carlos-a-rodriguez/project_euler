def fibonacci_even_sum(n):
  """Returns sum of all even terms in the fibonacci sequence less than n."""
  count = 0
  fib = [1, 1, 0]

  while fib[0] < n:
    fib[2] = fib[1]
    fib[1] = fib[0]
    fib[0] = fib[1] + fib[2]

    if fib[0] % 2 == 0:
      count += fib[0]

  return count


if __name__ == '__main__':
  print fibonacci_even_sum(4000000)