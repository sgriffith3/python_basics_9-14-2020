# if, elif, and else

high = []
ok = []
fail = []

a = 99
if a < 50:
    print(f"{a} is less than 50")
    fail.append(a)
elif a < 85:
    print(f"{a} is less than 85")
    ok.append(a)
elif a < 97:
    print(f"{a} is between 84 and 97")
    high.append(a)
else:
    print("You got an A+! Woohoo!")

print('High', high)
print('ok', ok)
print('fail', fail)
