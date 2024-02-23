print("This below is a list and the list can be updated")
coordinates = [4, 5]
coordinates[1] = 10
print(coordinates[1])

print("Now tuples cannopt be updated")
coordinates = (4, 5)
print(coordinates[1])

print("tuples inside a list")
coordinates=[(4, 5), (6, 7), (80, 34)]
coordinates[1] = 10
print(coordinates)