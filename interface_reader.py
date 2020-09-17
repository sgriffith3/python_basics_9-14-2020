#!/usr/bin/env python3

import netifaces

#for i in netifaces.interfaces():
#    print('\n****** details of interface - ' + i + ' ******')
#    try:
#        print('MAC: ', end='') # This print statement will always print MAC without an end of line
#        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
#        print('IP: ', end='')  # This print statement will always print IP without an end of line
#        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
#    except:          # This is a new line
#        print('Could not collect adapter information') # Print an error message
#
# Customization Request 01- Create a function that returns just the IP address when passed an adapter name.
def get_ip(adapter):
    ip = netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr'] # Gets the IP address
    # return IP address
    return ip

# Customization Request 02- Create a function that returns just the MAC address when passed an adapter name.
def get_mac(adapter):
    mac = netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]['addr'] # Gets the MAC address
    return mac


net = netifaces.interfaces()
print(net)
nets = ""
for i,v in enumerate(net):
    nets += f"\n{i + 1} {v}"

answer = 1
while True:
    try:
        answer = int(input(f"Which adapter do you want information for? \n{nets}\n\n"))
        adapt = net[answer - 1]
        break
    except ValueError:
        print("You got yourself a value error")
    except IndexError:
        print("Your number has to be either 1, 2, or 3.")

print("\n\nCustomization Requests\n" )
print(adapt)
print(get_ip(adapt))
print(get_mac(adapt))

