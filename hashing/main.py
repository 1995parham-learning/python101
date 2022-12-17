t1 = (1, 2, 3)
print(f"{hash(t1)}")

t2 = (1, 2, 3)
print(f"{hash(t2)}")

if hash(t1) == hash(t2):
    print("t1 and t2 have equal hashes")

if t1 == t2:
    print("t1 is equal to t2")


# l1 = [1, 2, 3]
# TypeError: unhashable type: 'list'
# print(hash(l1))

# t3 = (1, 2, 3, [1, 2, 3])
# TypeError: unhashable type: 'list'
# print(hash(t3))


class Koochooloo:
    # The __hash__() method should return an integer.
    # The only required property is that objects which
    # compare equal have the same hash value;
    # it is advised to mix together the hash values of the components
    # of the object that also play a part in comparison
    # of objects by packing them into a tuple and hashing the tuple.
    def __hash__(self):
        return 1378

    def __eq__(self, _):
        return True


k1 = Koochooloo()
k2 = Koochooloo()

print(f"k1 id: {id(k1)}")
print(f"k2 id: {id(k2)}")

print(f"k1 has: {hash(k1)}")
print(f"k1 has: {hash(k2)}")

# seems python used both hash and eq
# for dictionary and set keys
# remove __eq__ method to see k1 and k2
# are actually different under dict

kdict = {}
kdict[k1] = 10
kdict[k2] = 30

print(f"kset after adding k1 and k2: {kdict}")
