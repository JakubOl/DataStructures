myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

newDict = {}.fromkeys([1, 2, 3], 0)
newDict[(10, 11, 12)] = 1
print(newDict)

print(all(newDict))
