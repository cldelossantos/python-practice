import pprint
# TOP 20 GOAL LEADERS OF FIFA WOMEN'S WORLD CUP 2019

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

# 1) Print the length of the array.
    # print(len(player_stats))

# 2) Print a player's stat sheet.
    # print(player_stats['name'])

# 3) Print the names of each player.
    # for i in player_stats:
    #   print(i['name'])


# 4) Print all the player names that scored 6 goals.
    # for i in player_stats:
    #   if i["goals"] == 6:
    #     print(i['name'])


# 5) Print all the names and the team or the players that played 7 games.
    # for i in player_stats:
    #   if i["games_played"] == 7:
    #     print(i['name'], i['team'])


# 6) Print all the player names that scored 3 goals or less.
    # for i in player_stats:
    #   if i['goals'] <= 3:
    #       print(i['name'])