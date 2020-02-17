with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    lines = file_object.readlines()
    # for line in file_object:
    #     print(line.rstrip())
# print(contents)

pi_string = ''
for line in lines:
    pi_string += line.strip()
    print(line.rstrip())

print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

filename = 'programming.txt'

with(open(filename, 'w')) as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")