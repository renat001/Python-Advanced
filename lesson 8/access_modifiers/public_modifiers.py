class MyClass:
    def __init__(self):
        self.public_variable = "This is a public variable"

my_class = MyClass()

print(my_class.__private_variable)

print(my_class.__private_method)

