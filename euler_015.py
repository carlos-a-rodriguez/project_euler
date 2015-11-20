from numpy import product


def lattice_path(m, n):
  """Returns the number of lattice paths in a m by n grid."""
  return round(product([float(m + n + 1 - k) / k for k in xrange(1, m + 1)]))


if __name__ == '__main__':
  print int(lattice_path(20, 20))