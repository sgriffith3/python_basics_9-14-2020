#s = "This is a string"
#a = 7
#p = "pets"

#words = [s, a, p]

#print(words)

cars = ["accord", "soul", "fusion"]
#           0       1         2
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])

new_car = "camry"
cars.append(new_car)
print(cars)

fancy = ["ferrari", "lambo", "bugatti"]
#            0         1         2
cars.append(fancy)
print(cars)

# ['accord', 'soul', 'fusion', 'camry', ['ferrari', 'lambo', 'bugatti']]
#     0        1        2         3                    4
#                                           .0         .1        .2
# bugatti == cars[4]
print(cars[4][2])

old = ["Model T", "Model A"]
cars.extend(old)
print(cars)

#['accord', 'soul', 'fusion', 'camry', ['ferrari', 'lambo', 'bugatti'], 'Model T', 'Model A']
#    0        1         2        3                    4                    5           6

cars.extend("Hummer")
print(cars)
# ['accord', 'soul', 'fusion', 'camry', ['ferrari', 'lambo', 'bugatti'], 'Model T', 'Model A', 'H', 'u', 'm', 'm', 'e', 'r']

print(cars.index("Model T"))
print(cars.index("m"))

cars.pop()
print(cars)

for tup in enumerate(cars):
    print(tup)

for num, item in enumerate(cars):
    print(num, item)


cool_cars = cars[3:7]
print(cool_cars)

big = cars[7:]
print(big)

compact = cars[:4]
print(compact)
