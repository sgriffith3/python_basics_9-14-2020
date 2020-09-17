# Opening files

fi = open("something.txt", "r")

print(fi)
# print(help(fi))
txt = fi.read()
print(txt)
if "text" in txt:
    print("yes!!!")

fi.close()


# New Way - with
with open("something.txt", "r") as f:
    print(f)
    txt2 = f.readlines()
    print(txt2)
    if "parse" in txt2:
        print("parsing it")


print("File is closed")
