# While Loop

#         syntax
# while <expression is True>:
import time

print("We are about to start our loop")


count = 0
while count < 3:
    print("Hey! It worked!")
    time.sleep(1)
    count += 1

while True:
    count += 1
    print(count)
    time.sleep(1)
    if count == 8:
        break
    print("still counting")

print("We are done with our loop!")

valid = "Double 'quotes' are good delimeters"
also_valid = 'Single quotes are too'
additionally = '''Triple Single "quotes" 'are' valid'''
and_also = """
Triple 
'''Double''' 
"quotes" 
'are'
valid"""

import pprint
pprint.pprint(and_also)
print(and_also)

