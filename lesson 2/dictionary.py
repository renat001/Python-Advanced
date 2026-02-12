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