print([{x + 10 for x in range(5)}])


print([n for n in range(11) if n % 2 == 0])
print([n for n in range(11) if n % 2 == 1])


pessoas = [' Ana', 'manuela', 'FELIPe', 'PedrO ']

print(pessoas)

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]

print(pessoas_normalizadas)