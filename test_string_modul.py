import string

ls = [i * i for i in range(10)]
print(ls)

s = 'fjgdlfjhjh'
ls = [i * 3 for i in s]
print(ls)

s = 'fjgdlfjhjh'
STR = 'fgv'
ls = [i in STR for i in s]
print(ls)

print(all(ls))
print(any(ls))

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.printable)
# print(string.punctuation)
# print(string.whitespace)
