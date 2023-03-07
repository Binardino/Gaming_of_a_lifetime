print('insert new game for the DB')

#list of columns
column_list = ['game_name', 'console', 'game_type', 'finished','published_year',
               'played_year','hours_played', 'perso_score', 'multiplayed']

dict_values = {}

for column in column_list:
    game_value = input(f"Enter the {column} of the new game: ")
    dict_values[column] = game_value