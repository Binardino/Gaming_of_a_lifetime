#Update data & Insert
USE gamer_lifestory ;

#Game status to update
UPDATE my_videogames
SET
hours_played = 110,
perso_score = 99
WHERE 
game_name = "The Legend of Zelda: Breath to the Wild";

UPDATE my_videogames
SET
hours_played = 70,
game_type = 'RPG|Open World'
WHERE 
game_name = "Assassin's Creed Origins";

UPDATE my_videogames
SET
hours_played = 100,
game_type = 'RPG|Open World'
WHERE 
game_name = "Assassin's Creed Odyssey";


UPDATE my_videogames
SET
console = "PS4|PC",
hours_played = 50,
perso_score = 90
WHERE 
game_name = "Star Wars Battlefront II";

#("Horizon Zero Dawn", "PS4", "Action-Adventure|Open World", False, 2017,2019, 10,91,True),
#("The Legend of Zelda: Breath to the Wild", "Switch", "Action-Adventure|Open World", False, 2016,2020,110, 99, True),
#("Assassin's Creed Origins", "PS4", "RPG|Open World", True, 2017,2017, 70,96,True),
#("Assassin's Creed Odyssey", "PC", "RPG|Open World", False, 2018,2018, 90,97,True),
#("Star Wars Battlefront II", "PS4|PC", "FPS|Space Shooter", True, 2017,2017, 40,90,True),


INSERT INTO my_videogames(game_name, console, game_type, finished, published_year, played_year, hours_played, perso_score, multiplayed) 
VALUES

("Cyberpunk 2077", "PC", "RPG|Open World", True, 2020,2020,120,99, False),
("WatchDogs Legion", "PC", "Action-Adventure|Open World", True, 2020,2020,50,95, True),
("Among Us", "Android", "Party game", False, 2018,2020,7,70,True),
("Mario Galaxy", "Switch","Platformer", False, 2008, 2020,20,94,True),
("Mario Sunshine", "Switch","Platformer", False, 2003, 2020,10,75,True),
("Final Fantasy XII", "Switch","JRPG", True, 2006, 2021, 40, 93, False),

###2021 - 2022 updates
INSERT INTO my_videogames(game_name, console, game_type, finished, published_year, played_year, hours_played, perso_score, multiplayed) 
VALUES
("Hades", "Switch","Action-Adventure|Hack&Clash", False, 2020, 2021, 30, 93, False),
("New Super Mario Bros U Deluxe", "Switch","Platformer", False, 2020, 2021, 25, 90, True),
("Hyrule Warriors : Age of Calamity", "Switch","Action-Adventure|Hack&Clash", False, 2020, 2021, 15, 90, True),
("Assassin's Creed Valhalla", "PC", "RPG|Open World", False, 2020,2021, 50,92,False),
("Demon's Souls", "PS5", "JRPG|Action-Adventure", False, 2020,2022, 20,90,False),
("Horizon Forbidden West", "PS5", "RPG|Open World", False, 2022,2022, 50,93,False),
("Star Wars Jedi Fallen Order", "PC", "RPG|Action-Adventure", True, 2019,2020, 25,89,False),


/*
UPDATE my_videogames
SET
(game_name, console, game_type, finished, published_year, played_year, hours_played, perso_score, multiplayed)
WHERE 
game_name = "Horizon Zero Dawn";
*/