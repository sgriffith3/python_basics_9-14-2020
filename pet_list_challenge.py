#Tuesday Morning Challenge:

#Start with this list of pets:

pets = ['fido', 'spot', 'fluffy']

#Use the input() function three times to gather names of three more pets. 
pet1 = input("pet 1 name: ")
pet2 = input("pet 2 name: ")
pet3 = input("pet 3 name: ")

#Add each of these new pet names to the pets list.
pets.append(pet1)
pets.insert(1, pet2)
pets = pets + [pet3]

#print(pets)
#print(enumerate(pets))
#for ind, val in enumerate(pets):
#    print(ind, val)
#Using the pets list, print each out, along with their index. 
#
#The output should look like:
#
#0 fido
#1 spot
#2 fluffy

print(0, pets[0])
print(1, pets[1])
print(2, pets[2])
print(3, pets[3])
print(4, pets[4])
print(5, pets[5])


counter = 0
for pet in pets:
    print(counter, pet)
    counter += 1
    # counter = counter + 1


for pe in pets:
    print(pets.index(pe), pe)
