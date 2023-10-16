import sys
import math
from os import rename
import requests

print(sys.version)
print(sys.executable)

print("Hello World")

name = input('Your name? ')
print("Hello,", name)
print(f"Hello, {name}")

s = math.sqrt(4)
f = math.factorial(3)
print(s)
print(f)

r = requests.get("https://docs.python.org/")
print(r.status_code)
