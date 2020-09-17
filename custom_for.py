farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    # farm == farms[0] == {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}
    # farm['name'] == farms[0]['name'] == "NE Farm" 
    # farm['agriculture'] == farms[0]['agriculture'] == ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
    print(f"The {farm['name']} raises {', '.join(farm['agriculture'])}.")
    for animal in farm['agriculture']:
        print(animal)
        # animal == farms[0]['agriculture'][0] == "sheep"

# Bad practice equivalent
print(f"The {farms[0]['name']} raises {', '.join(farms[0]['agriculture'])}.")
print(farms[0]['agriculture'][0])
print(farms[0]['agriculture'][1])
print(farms[0]['agriculture'][2])
print(farms[0]['agriculture'][3])
print(farms[0]['agriculture'][4])
print(farms[0]['agriculture'][5])

print(f"The {farms[1]['name']} raises {', '.join(farms[1]['agriculture'])}.")
print(farms[1]['agriculture'][0])
print(farms[1]['agriculture'][1])
print(farms[1]['agriculture'][2])


print(f"The {farms[2]['name']} raises {', '.join(farms[2]['agriculture'])}.")
print(farms[2]['agriculture'][0])
print(farms[2]['agriculture'][1])
print(farms[2]['agriculture'][2])

