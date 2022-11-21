capital={
    "France":"paris",
    "Germany":"Berlin",
}
# Nesting list in dictionary
travel_log={
    "France":["city 1","city 2","Paris","Dijon"]
}

print(travel_log)
print()

#Nesting Dictionary in dictionary
travel={
    "France":{"cities_visited":["city 1","city 2","Paris","Dijon"],"total_visits":12}
}
print(travel)
print()

#Nesting Dictionary in List

travel_l=[
    {"contry":"France",
    "cities_visited":["city 1","city 2","Paris","Dijon"],
    "total_visits":12
    },
]
print(travel_l)