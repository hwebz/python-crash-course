bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())

bicycles[0] = 'custom'
print(bicycles)

bicycles.append('extra')
print(bicycles)

bicycles.insert(2, 'inserting element')
print(bicycles)

del bicycles[2]
print(bicycles)

poped_bicycles = bicycles.pop()
print(bicycles)
print(poped_bicycles)

second_bicycle = bicycles.pop(1)
print(bicycles)
print(second_bicycle)

bicycles.remove('redline')
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list of cars: ")
print(cars)

print("Here is the sorted list: ")
print(sorted(cars))

print("Here is the original list again: ")
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars.reverse()
print(cars)

print(len(cars))
print(cars[-2])

# motorcycles = []
# print(motorcycles[-1])