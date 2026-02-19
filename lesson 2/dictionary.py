

contact_info ={"Festa": "123-456",
               "Melina": "456-321"
}

festa_phone = contact_info["Festa"]
print(festa_phone)

contact_info["Festa"] = "123-123"
print(contact_info)

contact_info["Egzon"] = "111-2222"
print(contact_info)

del contact_info["Melina"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {

    "Renato":{
        "phone_number" : "123-456",
        "email" : "renato@gmail.com",
        "home_address" : "Bregu i Diellit",
        "birthday" : "08/09/2009"

    },
     "Sara":{
        "phone_number" : "123-4786",
        "email" : "sara@gmail.com",
        "home_address" : "Bregu i Diellit",
        "birthday" : "06/03/2007"

    },
    "Liron":{
        "phone_number" : "123-4796",
        "email" : "liron@gmail.com",
        "home_address" : "Bregu i Diellit",
        "birthday" : "01/04/2008"

    }
}

print(contact_information)

renato_information = contact_information["Renato"]
print(renato_information)

contacts = {
    "Renato":("123_456", "renato@gmail.com"),
    "Sara":("123-4786", "sara@gmail.com"),
    "Liron":("123-4796", "liron@gmail.com")
}

renato_info = contacts["Renato"]
phone_number = renato_info[0]
print(phone_number)
email = renato_info[1]
print(email)


phone_number, email = contacts["Renato"]