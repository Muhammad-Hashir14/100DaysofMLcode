# list
fruits = ['Apple','Mango','Banana','Orange','Grapes']
print(fruits)

# length of list
print(len(fruits))

# Appending Item to the list
fruits.append('Watermelon')
print(fruits)

# Adding Item in the middle of the list
fruits.insert(2,'Strawberries')
print(fruits)

# Adding list in to list
vegetables = ['Tomato','Cucumber','Pumpkin']
fruits.insert(1,vegetables)
print(fruits)
print(fruits[1])

# Removing Item from list
fruits.remove('Grapes')
print(fruits)

# Poping Item from the list
poped_item = fruits.pop(4)
print(fruits)
print(poped_item)

# List Slicing
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[0:2])
print(fruits[:4])
print(fruits[4:])

# Sorting list
numbers = [3,5,1,4,2]
numbers.sort()
print(numbers)

# reversing list
numbers.reverse()
print(numbers)

# finding values in list
fruits.index('Mango')
print(fruits.index('Mango'))
index_of_Mango = fruits.index('Mango')
print(fruits[index_of_Mango])

# looping values of list
for fruit in fruits:
    print(fruit)
for index, fruit in enumerate(fruits):
    print(index," - ",fruit)

# Tuples
hardware = ('mouse','keyboard','monitor','speaker')
print(hardware[0:3])
# Tuples of immutable means their values donot change

# Sets
stationary = {'pen','pencil','pen','pointer','scale','scale','pointer','sharpner','pen'}
print(stationary)

# Functions of sets
stationary_1 = {'pen','Rubber','compas','scale','pencil','Marker'}
print(stationary.intersection(stationary_1))
print(stationary.union(stationary_1))
print(stationary.difference(stationary_1))