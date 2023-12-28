# Nesting List: Key chứa list hoặc 1 key chứa 1 dictionary

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a Dictionary
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

#Nesting Dictionary in a Dictionary 
travel_log = {
    "France": {"cities_visited":["Paris","Lille","Dijon"] , "total_visited":12},
    "Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visited":12}
}

#Nesting Dictionary in List
travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"] , 
        "total_visited":12},
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visited":12
    }
]

# # Lặp qua list của Key trong Dictionary
# for key in travel_log:
#     for val in travel_log[key]:
#         print(val)

# # Lặp qua key in ra list 
# for key,val in travel_log.items():
#     print(f"{key}: {val}")