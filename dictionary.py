customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("age"))
print(customer.get("has_gun", True))