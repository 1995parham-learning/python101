import collections


def print_expression_as_set(expression: str):
    "print expression as a string sorted by letters"
    set_ = set(expression)
    print(expression, "".join(sorted(set_)))


def print_word_count(expression: str):
    cnt = collections.Counter(expression)
    print(f"most_common: {cnt.most_common()}\nvalues: {cnt}")


print_expression_as_set("spam")
print_expression_as_set("eggs")
print_expression_as_set("parham")

print_word_count("eggs")
