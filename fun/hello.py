# working with expressions
print("Hello world of python")
print(1 + 1)
print(1.0 + 1)
parham = 1
print(parham)

# working with tuples
a = ("Parham", "Navid", "Mohammad")
b = (a, "Bahador")
print(b)
print(a.count("Parham"))

# working with lists - 1
a = ["Parham", "Navid", "Mohammad"]
b = [a, "Bahador"]
print(b)
b[0][0] = "Parham Alvani"
print(a)
a.sort()
print(a)

# working with lists - 2
var = [10, 20, 30]
c = (var, 10)
print(c)
var = var.append(40)
print(c)

# for-loop with else
for name in a:
    print(name)
else:
    print("loop finish correctly without break")


# defining an inner-function, functions are first-class citizenes
def retfunc(a):
    def f(b):
        print("%d %d" % (a, b))

    return f


retfunc(10)(20)
