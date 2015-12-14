def divisors(n):
  """Returns all the numbers that divide n, including n."""
  end = int(n ** 0.5) + 1

  factors = []

  for i in xrange(1, end):
    if n % i == 0:
      factors.append(i)
      factors.append(n / i)

  return factors


if __name__ == '__main__':
  sum_prop_div = {}

  # a proper divisor of i is a number less than i that divides i
  # so divisors(i) - i = proper divisors(i)
  for i in xrange(1, 10000):
    sum_prop_div[i] = sum(divisors(i)) - i

  amicable_nums = set()

  # if sum_prop_div(k) = v and sum_prop_div(v) = k
  # then k and v are amicable numbers
  for key, value in sum_prop_div.iteritems():
    if value in sum_prop_div and sum_prop_div[value] == key and key != value:
      amicable_nums.update([key, value])  

  print sum(amicable_nums)