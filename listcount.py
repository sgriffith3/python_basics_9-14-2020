cars = ['accord', 'camr', 'fusion', 'cam', 'camy', 'soul', 'camry']

print(cars)

c1 = cars.count('camry')
c2 = cars.count('cam')
print(c1 + c2)

count = 0
for car in cars:
    if car == 'cam':
        count = count + 1


# Regex
cars_str = str(cars)
print(cars_str)
print(type(cars_str))

joined_cars = " | ".join(cars)
print(joined_cars)

import re
pat = 'camr?y?'
cam_count = re.findall(pat, joined_cars)
print(cam_count)
print(len(cam_count))
print(cam_count.count(pat))



#animals = ['cat', 'dog', 'fox', 'hamster', ['beaver', 'fox', 'ferret']]
##            0      1      2       3                    4
#
## Recursive lookup of fox
#animal_count = 0
#for animal in animals:
#    if isinstance(animal, str):
#        print(animal)
#        if animal == 'fox':
#            animal_count = animal_count + 1
#    else:
#        for item in animal:
#            print(item)
#            if item == 'fox':
#                animal_count = animal_count + 1
#
#print("Using a for loop to look for fox")
#print(animal_count)
#
#
#print("looking for fox")
#print(animals.count('fox'))
#
