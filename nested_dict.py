travel_log = [
    {
        "country": "France",
        "visited": 5,
        "cities": ["Paris", "Nice", "Lille"]
    },
    {
        "country": "USA",
        "visited": 6,
        "cities": ["California", "Maimi", "San Fransico", "Florida"]
    }
]

def add_travels(countryName, visted, cities):
    add = {"country": countryName, "visited": visted, "cities": cities}
    travel_log.append(add)

add_travels("Nigeria", 4, ["Edo", "Lagos", "Abuja", "Calabar"])

print(travel_log)