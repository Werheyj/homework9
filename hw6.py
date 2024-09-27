def all_variants(text):
    length = len(text)
    result = []
    stack = [('', 0)]
    while stack:
        current, index = stack.pop()
        if current:
            result.append(current)
        for s in range(index, length):
            stack.append((current + text[s], s + 1))
    yield result


a = all_variants('abc')
for i in a:
    print(i)
