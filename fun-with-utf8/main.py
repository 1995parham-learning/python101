# utf-8 strings

p = "پرهام الوانی"
e = "الهه داستان"

print(f"p: {len(p)} -- {p}")
print(f"e: {len(e)} -- {e}")

# convert utf-8 string into byte representation
p = p.encode("utf-8")
print(f"p in bytes: {len(p)} -- {p}")

e = e.encode("utf-8")
print(f"e in bytes: {len(e)} -- {e}")
