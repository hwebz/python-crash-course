message = '\tHello World!"'
another_message = f"{message} with an extra message"
# Python 2
# another_message = "{} with an extra message".format(message)
print(message.title())
print(another_message)

message = "Hello's World! This is the Python Crash Course"
print(message)

languages = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(languages)

striped_spaces = "   python  "
print(striped_spaces.rstrip())
print(striped_spaces.lstrip())
print(striped_spaces.strip())

a = 2
b = 4
c = a * b
d = a ** b
e = b / a
print(f"{a} * {b} = {c}, {a} ** {b} = {d}, {a} / {b} = {e}")

a = 0.1
b = 0.5
c = a * b
d = a ** b
print(f"{a} * {b} = {c}, {a} ** {b} = {d}")

# for readable reason
price = 18_800_000
print(price)

a, b, c = 5, 6, 7
print(a, b, c)

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

truth = True