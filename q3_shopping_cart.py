def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


#After fixing the bug
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

#THE BUG was that the list is created only once and reused for every function call.

