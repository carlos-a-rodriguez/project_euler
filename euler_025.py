if __name__ == '__main__':
  fib = [2, 1, 1]

  i = 3
  while fib[0] < 10 ** 999:
    fib[2] = fib[1]
    fib[1] = fib[0]
    fib[0] = fib[1] + fib[2]
    i += 1

  # print index of the first term in the fibonacci sequence that has
  # 1000 digits
  print i 
