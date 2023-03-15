print('insert new game for the DB')

#list of columns
column_list = ['game_name', 'console', 'game_type', 'finished','published_year',
               'played_year','hours_played', 'perso_score', 'multiplayed']

#game_list = list(input('input list of game:'))

#input list of games
list_size = int(input('how many games to input today ?'))
game_list =  [input('input game to insert to the videogame dg: ') for _ in range(list_size)]

dict_game = {}

for game in game_list:
    dict_game[game] = {}
    print(f'dict for {game} created --- input values')
    for column in column_list:
        game_value = input(f"Enter the {column} of the new game: ")
        dict_game[game][column] = game_value
    print(f'dict for {game} completed --- GG')