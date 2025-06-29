## Learn Python

### Simple Object
```
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

u = User("Bob")
print(u.greet())  # Output: Hello, Bob!

```

### Simple List/array Example
'''
# Array
filenames = ["photo1.jpg", "document.pdf", "notes.txt"]
print(filenames[0])         # Output: photo1.jpg
for name in filenames:
    print(f"File: {name}")

**********************
# Array of object
uploaded_files = [
    {"filename": "image.png", "size": 2048},
    {"filename": "report.docx", "size": 4096},
    {"filename": "video.mp4", "size": 1048576}
]

for file in uploaded_files:
    print(f"{file['filename']} is {file['size']} bytes")
'''

### if and for loop 
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

age = 20
if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")
```

## Working with Dictionaries

```
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

users.append({"name": "Charlie", "age": 35}) #add
#update
for user in users:
    if user["name"] == "Bob":
        user["age"] = 26

#delete
users = [user for user in users if user["name"] != "Alice"]

```

🧱 Working with Class Objects
```
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

users = [
    User("Alice", 30),
    User("Bob", 25)
]

users.append(User("Charlie", 35))
for u in users:
    if u.name == "Bob":
        u.age = 26

users = [u for u in users if u.name != "Alice"]

```




