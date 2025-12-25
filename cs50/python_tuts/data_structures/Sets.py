s = set()
s.add(1)
s.add(28)
s.add(50)
print(s);
print(28 in s)
print(29 in s)

ages = {"Alice": 22, "Bob": 27};

ages["Charlie"] = 28

# Alice's birthday
ages["Alice"] += 1

print(ages["Alice"])

print(ages)

# Delete Bob from dictionary
del ages["Bob"]

print(ages)