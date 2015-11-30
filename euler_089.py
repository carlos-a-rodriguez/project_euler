def minimize_roman_numeral(roman):
  """Returns the minimized roman numeral from a valid roman numeral."""
  translations = [('DCCCC', 'CM'), ('CCCC', 'CD'), ('LXXXX', 'XC'), 
                  ('XXXX', 'XL'), ('VIIII', 'IX'), ('IIII', 'IV')]

  for key, value in translations:
    roman = roman.replace(key, value)

  return roman


if __name__ == '__main__':
  diff = 0
  
  with open('res/p089_roman.txt', 'r') as f:
    for line in f:
      line = line.strip()
      min_roman = minimize_roman_numeral(line)
      diff += len(line) - len(minimize_roman_numeral(min_roman))

  print diff
