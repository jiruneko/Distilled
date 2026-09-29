def func(x, items = []):
    items.append(x)
    return items

print(func(1))
print(func(2))
print(func(4))