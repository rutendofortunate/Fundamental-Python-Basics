friends = ["Ralph", "Tashinga", "Rutendo", "Fortunate", "Olivia"]
print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[1:])
print(friends[1:3])

friends[1] = "Alice"
print(friends[1])
print(friends)

print("LIST FUNCTIONS")
lucky_numbers = [40, 8, 15, 16, 23, 42 ]
friends = ["Ralph", "Tashinga", "Rutendo", "Fortunate", "Olivia"]
print(friends)

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friend2 =friends.copy()
print(friend2)

friends.extend(lucky_numbers)
print(friends)
friends.append("Paul")
print(friends)

friends.insert(1, "Karen")
print(friends)

friends.remove("Ralph")
print(friends)

print(friends.index("Rutendo"))

print(friends.count("Fortunate"))

friends.pop()
print(friends)


friends.clear()
print(friends)
