def all_variants(text):
    length = len(text)
    for j in range(length + 1):
        yield text[:j]
    for j in range(length + 1):
        yield text[1:j]
    for j in range(length + 1):
        yield text[2:j]


a = all_variants('abc')
for i in a:
    print(i)
