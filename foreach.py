# For Loop


#      syntax
# for <iterator> in <iterable>:

# <iterator> - any valid variable name
import time
cats = ['fluffy', 'snowball', 'garfield']

for cat in cats:
    time.sleep(1)
    print(cat)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
