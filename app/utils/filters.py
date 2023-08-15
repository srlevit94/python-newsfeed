# tests date format and prints to terminal
from datetime import datetime


# formates the date to mm/dd/yy formate
def format_date(date):
  return date.strftime('%m/%d/%y')

#returns only the domain name of a url
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# tests url format and prints to terminal
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))

# correctly plurlizes words
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# print(format_date(datetime.now()))
# tests pluralization and prints to terminal
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))
# print(format_plural(2, 'deer'))

