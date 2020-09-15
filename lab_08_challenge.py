new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#             0     1     2       3           4          5

# When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.

#print("When I", new_list[5], "into IP addresses", new_list[3], "or", new_list[4], "I am unable to ping ports", new_list[0], ",", new_list[1], ", or", new_list[2])

print(new_list)
#print(type(new_list[0]))
#print(type(new_list[1]))
#print(type(new_list[2]))
#print(type(new_list[3]))
#print(type(new_list[4]))
#print(type(new_list[5]))

# Concatenation
sentence_01 = "When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) + "."

#print(sentence_01)

# f-string
sentence_02 = f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}."

#print(sentence_02)


# .format() method
sentence_03 = "When I {5} into IP addresses {3} or {4} I am unable to ping ports {0}, {1} or {2}.".format(*new_list)
print(sentence_03)



