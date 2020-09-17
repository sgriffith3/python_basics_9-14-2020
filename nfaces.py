#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())
# ["lo", "ens3", "docker0"]

# assign i to the first value of the list
# do the stuff in the for loop (all the lines indented underneath)
# when done, assign i to the next value of the list

# for each interface in netifaces.interfaces():
#    do x
for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
    print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address



ni = ["lo", "ens3", "docker0"]
i = ni[0]
print("details", i)
print("MAC", i)
print("IP", i)
ni.remove(i)
print(ni)

# ens3

i = ni[0]
print("details", i)
print("MAC", i)
print("IP", i)
ni.remove(i)
print(ni)

# docker0

i = ni[0]
print("details", i)
print("MAC", i)
print("IP", i)
ni.remove(i)
print(ni)
