# list - a mutable list of items
l1 = [1, 2, 3]
print(l1)
l1.append(4)
print(l1)

# tuple
primes = (1, 2, 3, 5, 7)

# convert a range into list
numbers = list(range(10))
# list comprehension
not_primes = [number for number in numbers if number not in primes]
print(not_primes)

# convert a range into list
numbers = list(range(10))
# filter by another tuple
not_primes = list(filter(lambda number: number not in primes, numbers))
print(not_primes)
