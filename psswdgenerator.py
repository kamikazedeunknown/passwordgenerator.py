import string
import random

x = input("Length of password: ")
x = int(x)
list1 = string.ascii_letters
list2 = string.digits
list3 = string.punctuation
list0 = list1 + list2 + list3

gen = "".join(random.choice(list0) for i in range(x))

print("Your password is %s" % gen)
