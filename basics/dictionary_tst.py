customer={
    "name": "James Camp",
    "age":  19,
    "gender": "male"
}

print(f'name of the customer is {customer.get("name")}')

customer.setdefault("name", "something else")
print(f'after changing the name of the customer: {customer}')

customer.pop("name")
print(f'after popping name out {customer}')

if customer.get("name") != None :
    print(f"after popping name out '{customer.get('name', "default name")}'")
else:
    print(f'name not present in the customer {customer}')
