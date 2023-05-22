#Update data & Insert
USE lifetime_gaming ;

#Game status to update
UPDATE gaming_lifetime
SET
hours_played = 110,
perso_score = 100
WHERE 
game_name = "The Legend of Zelda: Breath to the Wild";

#Game status to update
UPDATE gaming_lifetime
SET
hours_played = 45,
perso_score = 90,
finised = True,
multiplayed = True
WHERE 
game_name = "Demon's Souls";

###2022 - 2023 updates
INSERT INTO gaming_lifetime(game_name, console, game_type, finished, published_year, played_year, hours_played, perso_score, multiplayed) 
VALUES
("Marvel's Spider-Man: Miles Morales", "PS5", "Open World|Action-Adventure", False, 2020,2022, 20,89,False),
("Kena: Bridge of Spirits", "PS5", "RPG|Action-Adventure", False, 2021,2023, 15,89,False),
("Ghost of Tsushima", "PS5", "Open World|Action-Adventure", False, 2020,2023, 15,91,False),
("God of War: Ragnarök", "PS5", "RPG|Action-Adventure", False, 2023,2023, 45,97,False),
("The Legend of Zelda: Tears of the Kingdom", "Switch", "Open World|Action-Adventure", False, 2023,2023, 15,99,True),
("God of War: Ragnarök", "PS5", "RPG|Action-Adventure", False, 2023,2023, 45,97,False),
("The Last of Us Part I", "PS5", "Survival Horor|Action-Adventure", True, 2013,2023, 23,97,True),
("The Last of Us Part II", "PS5", "Survival Horor|Action-Adventure", True, 2020,2023, 30,97,True),
("A Way Out", "PS5", "Co-op", False, 2023,2023, 45,97,True),
