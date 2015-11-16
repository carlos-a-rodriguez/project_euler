import numpy as np


def largest_product_in_series(num_list, k):
  """Returns largest product of adjacent k numbers in a list of integers."""
  prod_list = [np.product(num_list[:k])]

  for i in xrange(k, len(num_list)):
    if num_list[i - k] != 0:
      prod_list.append(prod_list[-1] / num_list[i - k] * num_list[i])
    else:
      prod_list.append(np.product(num_list[i - k + 1: i + 1], dtype=np.int64))

  return max(prod_list)


if __name__ == '__main__':
  text = "73167176531330624919225119674426574742355349194934" + \
         "96983520312774506326239578318016984801869478851843" + \
         "85861560789112949495459501737958331952853208805511" + \
         "12540698747158523863050715693290963295227443043557" + \
         "66896648950445244523161731856403098711121722383113" + \
         "62229893423380308135336276614282806444486645238749" + \
         "30358907296290491560440772390713810515859307960866" + \
         "70172427121883998797908792274921901699720888093776" + \
         "65727333001053367881220235421809751254540594752243" + \
         "52584907711670556013604839586446706324415722155397" + \
         "53697817977846174064955149290862569321978468622482" + \
         "83972241375657056057490261407972968652414535100474" + \
         "82166370484403199890008895243450658541227588666881" + \
         "16427171479924442928230863465674813919123162824586" + \
         "17866458359124566529476545682848912883142607690042" + \
         "24219022671055626321111109370544217506941658960408" + \
         "07198403850962455444362981230987879927244284909188" + \
         "71636269561882670428252483600823257530420752963450"

  numbers = [int(i) for i in text]

  print largest_product_in_series(numbers, 13)