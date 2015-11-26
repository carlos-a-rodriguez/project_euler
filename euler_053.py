def generate_pascal_triangle(n):
  """Returns pascal's triangle with up to n levels as a list of lists."""
  # base triangle
  triangle = [[1],[1,1]] 

  if n == 0:
    return triangle[0]
  elif n == 1:
    return triangle

  for row in xrange(2, n):
    triangle.append([1])
    for col in xrange(row - 1):
      triangle[-1].append(triangle[row - 1][col + 1] + triangle[row - 1][col])
    triangle[-1].append(1)

  return triangle


if __name__ == '__main__':
  pascal = generate_pascal_triangle(101)

  count = 0

  for row in reversed(pascal):
    row_count = sum([1 for x in row[1:-1] if x > 1000000])

    if row_count == 0:
      break

    count += row_count

  print count