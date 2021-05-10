import string

string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.

from random import choice
import string

size = 10
value = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(size):
  password += choice(value)

print(password)
