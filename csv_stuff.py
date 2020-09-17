import csv

with open("bdays.csv", "r") as f:
#    txt = csv.reader(f)
#    print(txt)
#    for person in txt:
#        print(person)

    txt2 = csv.DictReader(f)
    for row in txt2:
        print(row)
        print(row['name'], row['age'])

with open("newdays.csv", "w") as fi:
    day1 = {"name": "Stu", "age": 40, "birthday": "December 12 1980"}
    day2 = {"name": "Hannah", "age": 35, "birthday": "May 12 1985"}
    day3 = {"name": "Layla", "age": 12, "birthday": "November 22 2008"}
    writer = csv.DictWriter(fi, fieldnames=['name', 'age', 'birthday'])
    days = [day1, day2, day3]
    writer.writeheader()
    for day in days:
        writer.writerow(day)
