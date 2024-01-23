child1 = {
    "name": "Tayo",
    "age": 15
}

child2 = {
    "name": "Janet",
    "age": 17
}

myFamily = {
    "child1": child1,
    "child2": child2
}

for x in myFamily:
    print(x)
    children = myFamily[x]
    for y in children:
        print(children[y])
