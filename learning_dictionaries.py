# Dictionaries

# Key Value Pairs

# {key1: value1, key2: value2}
#                         {key2: value2, value3}
pets = {'cat': 'fluffy', 'dogs': ['fido', 'bingo']}

print(pets['cat'])
print(pets['dogs'])
print(type(pets['dogs']))
print(pets['dogs'][1])

#print(pets['geckos'])  < --- Breaks the code
print(pets.get('geckos'))
print(pets['dogs'])
print(pets.get('dogs'))


new_pets = {'lizards': ['lizzy']}
pets.update(new_pets)
print(pets)
new_dogs = {'dogs': 'spot'}
pets.update(new_dogs)
print(pets)

pets['snakes'] = 'slithers'
print(pets)
pets['cat'] = 'snowball'
print(pets)

# del pets['lizards']
print(pets)



import pprint
hospital = {'cats': [{'name':'fluffy', 'age': 14,'room': 12}], 'dogs': [{'name': 'fido', 'age': 7, 'room': 3}, {'name': 'fido', 'age': 4, 'room' :2}, {'name': 'fido', 'age': 12, 'room': 1}, {'name': 'bingo', 'age': 2, 'room': 8}, {'name': 'fido', 'age': 8, 'room': 6}]}
# type, name, age, room
#pprint.pprint(hospital)

#print(hospital.keys())
#for animal in hospital.keys():
#    print(animal)
#    print(hospital[animal])
#    for pet in hospital[animal]:    
#        print(pet)
#        info = f"The {animal} name is {pet['name']}, age {pet['age']}, and is in room {pet['room']}."
#        print(info)


#print(hospital.values())






#nums = [1, 2, 3, 4, 5]
#for num in nums:
#    print(num, num + 100)




