family = {
    "father": {
        "name": "Ajibola",
        "age": 50
    },
    "mother": {
        "name": "Alima",
        "age": 45
    },
    "son": {
        "name": "David",
        "age": 30
    }
}

for x in family:
    print(x)
    relative = family[x]
    for y in relative:
        print(relative[y])