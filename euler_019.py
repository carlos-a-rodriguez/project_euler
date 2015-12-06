import datetime


if __name__ == '__main__':
  # first sunday of 1900
  date = datetime.date(1900, 1, 7)
  # find the first sunday of the year 1901
  while date.year < 1901:
    date += datetime.timedelta(days=7)

  count = 0

  while date.year < 2001:
    if date.day == 1:
      count += 1
    date += datetime.timedelta(days=7)

  print count
