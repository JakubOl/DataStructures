from array import *

my_array = array('i', [1, 2, 3, 4, 5])
print(my_array)

# for i in my_array:
#     print(i)

print(my_array[3])

my_array.append(3)
print(my_array)

my_array.insert(0, 10)
print(my_array)

my_array.extend([23, 32, 43])
print(my_array)

tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

my_array.remove(3)
print(my_array)

my_array.pop()
print(my_array)

print(my_array.index(21))

my_array.reverse()
print(my_array)

print(my_array.buffer_info())

print(my_array.count(11))

print(my_array.tolist())

print(my_array[1:6])
