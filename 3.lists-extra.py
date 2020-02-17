magicians = ['alice', 'david', 'carilina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone. That was great magi")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

print(squares[0:3])
print(squares[:4])
print(squares[1:])
print(squares[-3:])

for square in squares[:3]:
    print(square)

another_squares = squares[:]
another_squares[2] = 22
print(squares)
print(another_squares)

# tuple is immutable list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tuple with 1 element
demo = (3,)
print(demo[0])

for dimension in dimensions:
    print(dimension)

# Writing over tuple
dimensions = (400, 50)
for dimension in dimensions:
    print(dimension)