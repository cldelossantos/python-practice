import pprint
player_stats = [
    {
        "name": "Ellen White",
        "team": "ENG",
        "games_played": 6,
        "minutes_played": 514,
        "goals": 6,
        "assists": 0,
    },
    {
        "name": "Megan Rapinoe",
        "team": "USA",
        "games_played": 5,
        "minutes_played": 429,
        "goals": 6,
        "assists": 2,
    },
    {
        "name": "Alex Morgan",
        "team": "USA",
        "games_played": 6,
        "minutes_played": 491,
        "goals": 6,
        "assists": 3,
    },
    {
        "name": "Sam Kerr",
        "team": "AUS",
        "games_played": 4,
        "minutes_played": 360,
        "goals": 5,
        "assists": 0,
    },
    {
        "name": "Wendie Renard",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 4,
        "assists": 0,
    },
    {
        "name": "Cristiane",
        "team": "BRA",
        "games_played": 4,
        "minutes_played": 301,
        "goals": 4,
        "assists": 0,
    },
    {
        "name": "Sara Daebritz",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 3,
        "assists": 1,
    },
    {
        "name": "Kosovare Asllani",
        "team": "SWE",
        "games_played": 7,
        "minutes_played": 575,
        "goals": 3,
        "assists": 1,
    },
    {
        "name": "Carli Lloyd",
        "team": "USA",
        "games_played": 7,
        "minutes_played": 193,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Rose Lavelle",
        "team": "USA",
        "games_played": 6,
        "minutes_played": 427,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Jennifer Hermoso",
        "team": "ESP",
        "games_played": 4,
        "minutes_played": 360,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Vivianne Miedema",
        "team": "NED",
        "games_played": 7,
        "minutes_played": 627,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Aurora Galli",
        "team": "ITA",
        "games_played": 5,
        "minutes_played": 302,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Cristiana Girelli",
        "team": "ITA",
        "games_played": 4,
        "minutes_played": 279,
        "goals": 3,
        "assists": 0,
    },
    {
        "name": "Amandine Henry",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Eugenie Le Sommer",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 380,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Valerie Gauvin",
        "team": "FRA",
        "games_played": 5,
        "minutes_played": 333,
        "goals": 2,
        "assists": 0,
    },
    {
        "name": "Alexandra Popp",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 450,
        "goals": 2,
        "assists": 0,
    },
    {
        "name": "Lina Magull",
        "team": "GER",
        "games_played": 5,
        "minutes_played": 301,
        "goals": 2,
        "assists": 1,
    },
    {
        "name": "Sofia Jakobsson",
        "team": "SWE",
        "games_played": 6,
        "minutes_played": 540,
        "goals": 2,
        "assists": 0,
    },
]
# pprint.pprint(player_stats[1]['team'])

# 1) Write a function called array_length that takes an array as an argument and returns the length of that array.

def array_length(arr):
    return len(arr)


print(array_length(player_stats))


# 2) Write a function called find_player that takes an array and a name as arguments and returns that player's stat sheet.


def find_player(arr,name):
    for player in arr:
        if player['name'] == name:
            return player

pprint.pprint(find_player(player_stats, 'Alex Morgan'))




# 3) Write a function called player_names that takes an array as an argument and returns a new array containing only the names of each player.

def player_names(arr):
    for player in arr:
        if player ['name'] == name:
            return player
print(player_names(player_stats))