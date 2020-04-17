USE gamer_lifestory ;

INSERT INTO my_videogames(game_name, console, game_type, finished, published_year, played_year, hours_played, perso_score, multiplayed) 
VALUES
("Final Fantasy VI", "SNES","JRPG", False, 1994, 2019, 10, 79, False),
("Final Fantasy VII", "PS1","JRPG", True, 1997, 2018, 80, 99, False),
("Final Fantasy VIII", "PC","JRPG",True, 1998, 2000, 70, 95, False),
("Final Fantasy IX", "PS1","JRPG", True, 2000, 2019, 70, 95, False),
("Final Fantasy X", "PS2","JRPG", True, 2000, 2003, 150, 98, False),
("Final Fantasy X-2", "PS2", "JRPG", True, 2004, 2004,50,86, False),
("Final Fantasy XV", "PS4", "JRPG", True, 2015, 2017,80,95, False),
("Final Fantasy VII Remake", "PS4", "JRPG", True, 2020, 2020,40,99, False),

("The Witcher 3", "PS4 | PC","RPG", True, 2015, 2018, 250, 100, False),

("Grand Theft Auto I", "PC", "Action | Open World", True, 1997, 1998,20,88, True),
("Grand Theft Auto : Vice City", "PS2", "Action | Open World", True, 2002, 2003,100,93, True),
("Grand Theft Auto : San Andreas", "PS2", "Action | Open World", True, 2004, 2005,200,99, True),
("Grand Theft Auto IV", "PS3", "Action | Open World", True, 2008, 2016,35,94, False),
("Grand Theft Auto V", "PS3 | PC", "Action | Open World", True, 2013, 2014,210,100, True),

("Kingdom Hearts", "PS2", "Action | JRPG", True, 2002, 2008,30,90,False),
("Kingdom Hearts 2", "PS2", "Action | JRPG", True, 2005, 2009, 50,98,False),
("Kingdom Hearts 3", "PS4", "Action | JRPG", True, 2019,2019, 40,96,True),
("Kingdom Hearts : Birth by Sleep", "PSP", "Action | JRPG", True, 2010,2017, 35,92, False),

("Sonic 1", "Megadrive","Platformer", True, 1991, 1996, 40, 85,True),
("Sonic 2", "Megadrive","Platformer", True, 1992, 1996, 50, 88,True),
("Sonic 3", "Megadrive","Platformer", True, 1994, 1996, 40, 88,True),
("Sonic & Knuckles", "Megadrive","Platformer", True, 1994,1996, 20, 80,True),
("Sonic 3 & Knuckles", "Megadrive","Platformer", True, 1994,1996, 60, 94,True),

("Spiderman", "PS4", "Action | Platformer", True, 2018, 2020,30, 90,False),

("God of War", "PS4", "Action | Beat'em'all", False, 2018, 2020,10,93,False),


("The Legend of Zelda : Wind Waker", "GameCube","Action-Adventure", False, 2002, 2008, 30,91,False),
("The Legend of Zelda : A Link to the Past", "SNES","Action-Adventure",False, 1991, 2020, 20, 91,False),
("The Legend of Zelda : Twilight Princess", "Wii", "Action-Adventure", False, 2006, 2010,30 ,98,False),
("The Legend of Zelda : Link's Awakening", "GameBoy", "Action-Adventure", True, 1993,2001, 20, 90,False),
("The Legend of Zelda : Breath to the Wild", "Switch", "Action-Adventure", False, 2016,2020,1,90, True),
("The Legend of Zelda : Ocarina of Time", "N64", "Action-Adventure", False, 1998,2017,20,92, False),

("Super Mario Bros", "NES", "Platformer", True, 1985,1993,20,82,True),
("Super Mario Bros 2", "NES", "Platformer", True, 1988,1995,15,83,True),
("Super Mario Bros 3", "NES", "Platformer", True, 1988,1995,20,90,True),
("Super Mario Land", "GameBoy", "Platformer", True, 1989,1993,5,65,True),
("Mario Kart: Double Dash", "GameCube","Racing", True, 2003, 2003, 30,90,True),
("Super Smash Bros. Melee", "GameCube","Versus Fighting", True, 2002, 2002, 30,92,True),
("Mario Party 5", "GameCube","Party Game", True, 2003, 2003, 50,89,True),
("Mario Party 3", "N64","Party Game", True, 2003, 2003, 50,92,True),
("Mario Tennis", "GameCube","Sport", False, 2004, 2007, 15,75,True),
*/

#PS3
("Heavy Rain", "PS3", "Narrative", True, 2010,2016, 15,79,True),

("Red Dead Redemption", "PS3", "Action-Adventure | Open World", True, 2010,2016, 30,92,False),
("Red Dead Redemption 2", "PS4", "Action-Adventure | Open World", True, 2018,2018, 60,96,False),
#PS4

#PC GAMES
("Sid Meier's Civilization 3", "PC", "STR", True, 2001,2001,15,88,False),
("Sid Meier's Civilization 5", "PC", "STR", True, 2010,2014, 150,97,True),
("Sid Meier's Civilization Beyond Earth", "PC", "STR", True, 2014,2014,15,78,False),
("Sid Meier's Civilization 6", "PC", "STR", True, 2016,2016, 300,100,True),

("Command & Conquer", "PC", "STR", True, 1996,1998,30,89,True),
("Command & Conquer Tiberium Sun", "PC", "STR", True,1999,1999,50,92,True),
("Command & Conquer 3 : Tiberium Wars", "PC", "STR", True, 2007,2007,60,92,True),
("Command & Conquer Red Alert", "PC", "STR", True, 1996,1998,40,89,True),
("Command & Conquer Red Alert 2", "PC", "STR", True, 2000,2001,60,90,True),
("Command & Conquer Red Alert Yuri", "PC", "STR", True, 2001,2001,20,91,True),
("Command & Conquer Red Alert 3", "PC", "STR", True, 2008,2018,10,75,True),
("Command & Conquer Generals", "PC", "STR", True, 2003,2005,15,77,True),
("Age of Empire 2", "PC", "STR", False, 2000,2003,30,88,True),

("Life is Strange", "PC", "Narrative", True, 2008,2018, 10,79,True),

("Nox", "PC", "RPG | Hack&Clash", True, 2008,2018, 10,75,True),
("Diablo", "PS1 | PC", "RPG | Hack&Clash", True, 1997,1998, 40,92,True),
("Diablo 2", "PC", "RPG | Hack&Clash", True, 2000,2005, 25,89,True),
("Diablo 3", "PS3 | PC", "RPG | Hack&Clash", True, 2012,2015, 35,93,True),

("StarCraft", "PC", "STR", True, 1998,1998, 150,92,True),
("StarCraft Brood War", "PC", "STR", True, 1998,1998, 20,92,False),
("StarCraft 2 : Wings of Liberty", "PC", "STR", True, 2010,2010, 150,95,True),
("StarCraft 2 : Hearts of the Swarm", "PC", "STR", True, 2013,2013, 50,94,True),
("StarCraft 2 : Legacy of the Void", "PC", "STR", True, 2015,2015, 70,96,True),
("WarCraft 2", "PC", "STR", True, 2008,2018, 10,75,True),
("WarCraft 3 : Reign of Chaos", "PC", "STR", True, 2002,2002, 100,95,True),
("WarCraft 3 Expand : The Frozen Throne", "PC", "STR", True, 2003,2003, 30,93,True),
("Heroes of Might&Magic 2", "PC", "STR", True, 1996,1998, 30,88,True),
("Heroes of Might&Magic 3", "PC", "STR", True, 1999,2000, 60,94,True),
("Heroes of Might&Magic 4", "PC", "STR", True, 2002,2002, 45,94,True),
("Heroes of Might&Magic 5", "PC", "STR", False, 2006,2008, 25,89,True),
("Heroes of Might&Magic 7", "PC", "STR", False, 2015,2018, 10,85,True),

#good
("Star Wars Battleground", "PC", "STR", True, 2001,2001, 40,90,False),
("Star Wars : Shadows of the Empire", "PC", "Action-Adventure | Hack&Clash", True, 1996,2002, 20,85, False),
("Star Wars Jedi Knight 2", "PC", "Action-Adventure | Hack&Clash", True, 2002,2003, 30,98,True),
("Star Wars Jedi Knight 3", "PC", "Action-Adventure | Hack&Clash", True, 2003,2003, 30,97,True),
("Star Wars The Old Republic", "PC", "Action-Adventure | RPG", True, 2011,2012, 50,92,True),
("Star Wars Knights of The Old Republic", "PC", "Action-Adventure | RPG", True, 2003,2012, 25,91,False),
("Star Wars Racer", "PC", "Racing", True, 2001,2001, 30,75,False),
("Star Wars StarFighter", "PC", "Gunfight", True, 2001,2001, 20,80,False),
("Star Wars Battlefront", "PC", "FPS", True, 2015,2015, 20,80,True),
("Star Wars Battlefront 2", "PS4", "FPS", True, 2017,2017, 25,85,True),
("Star Wars Bounty Hunter", "PS2", "Action-Adventure", True, 2002,2002, 30,70,True),
("Star Wars The Force Unleashed", "PS3", "Hack&Clash", True, 2008,2016, 15,75, False),
("Star Wars Force Unleashed 2", "PS3", "Hack&Clash", True, 2008,2016, 15,75,False),
("Star Wars Lego Complete Saga", "PS3", "Hack&Clash", True, 2007,2016, 10,75,False),
("Star Wars Rogue Squadron II : Rogue Leader", "GameCube","Gunfight", True, 2001, 2003, 50,94,True),

("Tomb Raider", "PS1", "Action | Platformer", True, 1997,1997, 15,85,True),
("Tomb Raider 2", "PC", "Action | Platformer", True, 1997,1998, 10,86,True),
("Tomb Raider Reboot", "PS3", "Action | Platformer", True, 2013,2013, 30,92,True),
("Tomb Raider Rise of the Tomb Raider", "PS4", "Action | Platformer", False, 2015,2015, 10,75,True),

("Assassin's Creed 2", "PS3", "Action-Adventure | Platformer", True, 2012,2015, 35,93,True),
("Assassin's Creed 3", "PS3", "Action-Adventure | Platformer", True, 2014,2015, 35,93,True),
("Assassin's Creed 4 Black Flag", "PS3", "Action-Adventure | Platformer", True, 2013,2016, 35,94,True),
("Assassin's Creed 5 Unity", "PC", "Action-Adventure | RPG", False, 2014,2018, 40,93,True),
("Assassin's Creed Origins", "PS4", "Action-Adventure | RPG", True, 2017,2017, 50,96,True),
("Assassin's Creed Odyssey", "PC", "Action-Adventure | RPG", False, 2018,2018, 80,97,True),
("Watch Dogs", "PS3", "Action-Adventure", True, 2013,2015, 30,85, False),
("Watch Dogs 2", "PC", "Action-Adventure", True, 2016,2016, 50,89, False),

("Uncharted 1", "PS4", "Action-Adventure | Platformer", False, 2007,2020, 1,00,True),
("Uncharted 2", "PS4", "Action-Adventure | Platformer", False, 2009,2020, 1,00,True),
("Uncharted 3", "PS4", "Action-Adventure | Platformer", False, 2011,2020, 1,00,True),
("Uncharted 4", "PS4", "Action-Adventure | Platformer", False, 2016,2020, 1,00,True),

("Little Big Adventure", "PC", "Action | Platformer", True, 1994,1999, 20,85,True),
("Little Big Adventure 2", "PC", "Action | Platformer", True, 1997,2000, 50,97,True),

("Crash Bandicoot", "PS1", "Action | Platformer", False, 1996,1996, 10,79,True),
("Crash Nitro Kart", "PS2", "Racing", False, 2003,2003, 15,72,True),
("Metal Gear Solid", "PS1", "Action | Infiltration", False, 1998,2016, 5,80),
("Splinter Cell", "PS2", "Action | Infiltration", False, 2002,2002, 15,82),
("WipeOut 2097", "PS1", "Racing", False, 1996,1996, 15,82,True),
("Driver", "PC", "Racing", False, 1999,2000, 15,72,True),

("Grim Fandango", "PC", "Point&Click", True, 2008,2018, 20,80,True),
("The Curse of Monkey Island", "PC", "Point&Click", True, 1997,2018, 10,75,True),
("Escape from Monkey Island", "PC", "Point&Click", True, 2004,2004, 30,85,True),
("The Secrets of Monkey Island", "PC", "Point&Click", False, 1990,2018, 2,87,True),

("Oddworld", "PC", "Action | Platformer", True, 1997,1999, 25,85,True),
("Oddworld 2", "PC", "Action | Platformer", True, 1998,2000, 10,86,True),

("The Witcher", "PC","RPG", False, 2008, 2018, 15, 85,False),

("ToeJam&Earl", "Megadrive","Action-Adventure | Platformer", False, 1991, 1996, 10, 75,True),
("Streets of Rage 2", "Megadrive","Beat'em'all", True, 1992, 1996, 15, 70,False),
("Golden Axe", "Megadrive","Beat'em'all", False, 1989, 1993, 15, 70),
("Mighty Morphin Power Rangers", "Megadrive","Beat'em'all", False, 1994, 1994, 15, 60,True),
("Sonic 3D: Flickies' Island", "Megadrive","Platformer", True, 1996, 1996, 30, 79, False),
("Sonic Pinball", "Megadrive","Platformer", True, 1996, 1996, 30, 79,True),
("Jungle Strike", "Megadrive","Action-Adventure | Beat'em'all", False, 1993, 1996, 30, 79),
("EarthWorm Jim", "Megadrive","Action-Adventure | Platformer", False, 1994, 1995, 15, 78,True),
("Aladdin", "Megadrive","Action-Adventure | Platformer", True, 1993, 1994, 25, 89,True),
("Lion King", "Megadrive","Action-Adventure | Platformer", False, 1994, 1994, 15, 80,True),
("Dr Robotnik", "Megadrive","STR", True, 1993, 1993, 30, 89,True),
("Micromachines", "Megadrive","Racing", False, 1994, 1994, 15, 80,True),
("Tales of Symphonia", "GameCube","JRPG", True, 2003, 2008, 30,85, False),

("AAAHH!!! Real Monsters", "Megadrive","Action-Adventure | Platformer", False, 1995, 1996, 15, 68,False),
("Jurassic Park", "Megadrive","Action-Adventure | Platformer", False, 1994, 1996, 5, 62,True),
("The Lost World: Jurassic Park", "PS1","Action-Adventure | Platformer", False, 1995, 1996, 5, 62,True),
("M.U.S.H.A", "Megadrive","Gunfight | Shooter", False, 1990, 1995, 10, 65,True),

("Lemmings", "PC","RTS", False, 1991, 1993, 15, 72,True),
("MegaBomberMan", "PC","Party", False, 1993, 1999, 15, 72,True),
("SimCity 2000", "PC","RTS", False, 1994, 1995, 15, 70,False),
("RollerCoaster Tycoon", "PC","RTS", False, 1999, 2000, 15, 70,False),
("Beyong Good & Evil", "PC","Action-Adventure | Platformer", False, 2003, 2016, 5, 62,False),



("Ristar", "Megadrive","Action-Adventure | Platformer", False, 1995, 1996, 20, 80,False),

("Star Wars Rogue Squadron", "PC","Gunfight", True, 1998, 2003, 20,93,True),

("Golden Eye", "N64", "FPS", False, 1997,1998,40,92,True),
("Rayman 2 : The Great Escape", "N64", "Action-Adventure | Platformer", False, 1999,2000,20,88, True),
("Rayman", "GBA", "Action-Adventure | Platformer", True, 2000,2000,25,89, True),
("Rayman Origins", "Wii", "Action-Adventure | Platformer", False, 2011,2011,20,89, True),

("Pokémon Yellow", "GameBoy", "Action-Adventure | JRPG", True, 1997,1998,40,92,True),
("Pokémon Gold", "GameBoy", "Action-Adventure | JRPG", True, 1999,1999,40,95,True),

("SSX", "PS2", "Sport", False, 2000, 2001,10,88,True),
("SSX Tricky", "PS2", "Sport", True, 2001, 2002,30,92,True),
("SSX 3", "PS2", "Sport", True, 2003, 2003,50,96,True),
("SSX On Tour", "PS2", "Sport", True, 2005, 2005,50,95,True),

("The Lord of the Rings: The Two  Towers", "PS2", "Action-Adventure | Beat'em'all", True, 2O02, 2002, 30, 90,True),
("The Lord of the Rings: The Return of the King" , "PS2", "Action-Adventure | Beat'em'all", True, 2O03, 2003, 35, 90,True),
("The Lord of the Rings: The Battle for Middle-earth" , "PC", "STR", False, 2O03, 2003, 35, 85,True),

("The Sims" , "PC", "STR", True, 2O00, 2000, 50, 90,True),
("The Sims 2" , "PC", "STR", True, 2O04, 2005, 30, 88, False),
("Baldur's Gate" , "PC", "Action-Adventure | RPG", True, 1998, 2000, 40, 90, False),
("Baldur's Gate II" , "PC", "Action-Adventure | RPG", True, 2O00, 2001, 50, 92, False),
("Drakan: Order of the Flame" , "PC", "Action-Adventure", True, 1999, 2000, 25, 89, False),
("Heroes of the Storm" , "PC", "MOBA", False, 2016, 2016, 90, 93, True)

("Fifa 98", "PS1","Sport", False, 2004, 2007, 15,80,True),
("Fifa 2000", "PC","Sport", False, 2000, 2000, 20,75,False),
("Fifa 2015", "PS3","Sport", False, 2014, 2015, 20,80,True),
("Fifa 2016", "PS4","Sport", False, 2015, 2016, 20,80,True),
("PES5", "PS2","Sport", False, 2005, 2005, 20,75,True),
;