t1 = (30, 20, [10, 15])

# "__setitem__" method not defined
# on type "tuple[Literal[30], Literal[20], list[int]]
# t1[0] += 10

print(f"t1: {t1}")
print(f"t1 id: {id(t1)}")
print(f"t1[2] id: {id(t1[2])}")

t1[2].append(30)

print(f"t1: {t1}")
print(f"t1 id: {id(t1)}")
print(f"t1[2] id: {id(t1[2])}")

# list is mutable so you can change it
# without changing its id.
# actually in tuples you cannot change items
# id but if they are mutable, you can mutate them.
