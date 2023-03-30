import array

# check the following code for typecode for converting arrays into bytes
# and then cast bytes into memoryview object.
# https://docs.python.org/3/library/array.html
b = bytes(array.array("i", [1, 2, 3]))

print(b)

d = memoryview(b).cast("i")

# memory view object is an array actually so we can expand it.
print(*d)
