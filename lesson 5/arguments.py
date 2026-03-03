
def person(name, greeting="Hello"):
    message= f"{greeting}, {name}"
    return message
default_greeting = person("Renato")
custom_greeting = person("Renato", "Hi")

print(default_greeting)
print(custom_greeting)
