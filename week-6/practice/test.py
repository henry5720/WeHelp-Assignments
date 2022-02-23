data = [('test', 'test', 'test'), ('first', 'one', '1111')]

name1 = []
for i in data:
    print(i[0])
    name1.append(i[0])
print(name1)

print("----------")

name2 = [i[0] for i in data]
print(name2)
