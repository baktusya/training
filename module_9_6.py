import itertools

def all_variants(text):
    for i in range(1, len(text) + 1):
        for value in itertools.combinations(text, i):
            yield ''.join(value)

a = all_variants("abc")
for i in a:
    print(i)

