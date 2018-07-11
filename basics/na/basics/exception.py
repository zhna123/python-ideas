import math

number = int(input("Please enter a number:"))

# if number < 0:
#     raise RuntimeError("wrong value!")
# else:
#     print(math.sqrt(abs(number)))

try:
    print(math.sqrt(number))
except ValueError:
    print("bad value!")
    print(math.sqrt(abs(number)))
