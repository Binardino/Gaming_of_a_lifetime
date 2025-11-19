-- public.gaming_lifetime definition

-- Drop table

-- DROP TABLE public.gaming_lifetime;

CREATE TABLE IF NOT EXISTS public.gaming_lifetime (
	id serial4 NOT NULL,
	game_name varchar(255) NOT NULL,
	console varchar(20) NOT NULL,
	game_type varchar(50) NOT NULL,
	finished bool NOT NULL,
	published_year int2 NOT NULL,
	played_year int2 NOT NULL,
	hours_played int2 NULL,
	perso_score int2 NOT NULL,
	multiplayed bool NOT NULL,
	country_dev varchar(255) NOT NULL,
	studio varchar(255) NOT NULL,
	editor varchar(255) NOT NULL,
	CONSTRAINT idx_225486_primary PRIMARY KEY (id)
);
CREATE UNIQUE INDEX idx_225486_game_name ON public.gaming_lifetime USING btree (game_name,console,published_year);

INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Final Fantasy VI','SNES','JRPG',false,1994,2019,10,79,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy VII','PS1','JRPG',true,1997,2018,80,99,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy VIII','PS1','JRPG',true,1998,2000,70,95,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy IX','PS1','JRPG',true,2000,2019,70,95,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy X','PS2','JRPG',true,2000,2003,200,99,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy X-2','PS2','JRPG',true,2004,2004,50,86,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy XV','PS4','JRPG|Open World',true,2015,2017,80,95,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy XVI','PS5','JRPG',true,2023,2023,45,68,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy VII Remake','PS4','JRPG',true,2020,2020,50,96,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Final Fantasy VII Rebirth','PS5','JRPG|Open World',false,2024,2024,70,99,false, 'Japan', 'Square Enix','Square Enix'),
	 ('The Witcher 3: Wild Hunt','PS4|PC','RPG|Open World',true,2015,2018,300,100,false, 'Poland', 'CD Projekt Red','CD Projekt Red'),
	 ('The Witcher 2: Assassins of Kings','PC','RPG|Open World',false,2011,2018,15,85,false, 'Poland', 'CD Projekt Red','CD Projekt Red');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('The Witcher','PC','RPG|Open World',false,2008,2018,15,85,false, 'Poland', 'CD Projekt Red','CD Projekt Red'),
	 ('Grand Theft Auto','PC','Open World|Action-Adventure',true,1997,1998,20,88,true, 'UK', 'Rockstar Games','Take Two Interactive'),
	 ('Grand Theft Auto: Vice City','PS2','Open World|Action-Adventure',true,2002,2003,100,93,true, 'UK', 'Rockstar Games','Take Two Interactive'),
	 ('Grand Theft Auto: San Andreas','PS2','Open World|Action-Adventure',true,2004,2005,200,99,true, 'UK', 'Rockstar Games','Take Two Interactive'),
	 ('Grand Theft Auto IV','PS3','Open World|Action-Adventure',true,2008,2016,35,94,false, 'UK', 'Rockstar Games','Take Two Interactive'),
	 ('Grand Theft Auto V','PS3|PC','Open World|Action-Adventure',true,2013,2014,210,100,true, 'UK', 'Rockstar Games','Take Two Interactive'),
	 ('Kingdom Hearts','PS2','Action|JRPG',true,2002,2008,30,90,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Kingdom Hearts II','PS2','Action|JRPG',true,2005,2009,50,98,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Kingdom Hearts III','PS4','Action|JRPG',true,2019,2019,40,95,true, 'Japan', 'Square Enix','Square Enix'),
	 ('Kingdom Hearts: Birth by Sleep','PSP','Action|JRPG',true,2010,2017,35,92,false, 'Japan', 'Square Enix','Square Enix');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('The Legend of Zelda: The Wind Waker','GameCube','Action-Adventure',false,2002,2008,35,91,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: A Link to the Past','SNES','Action-Adventure',false,1991,2020,20,91,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Twilight Princess','Wii','Action-Adventure',false,2006,2010,40,98,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Link''s Awakening','GameBoy','Action-Adventure',true,1993,2001,20,90,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Breath of the Wild','Switch','Open World|Action-Adventure',true,2017,2020,110,99,true, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Tears of the Kingdom','Switch','Open World|Action-Adventure',false,2023,2023,110,100,true, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Ocarina of Time','N64','Action-Adventure',false,1998,2017,20,92,false, 'Japan', 'Square Enix','Square Enix'),
	 ('Red Dead Redemption 2','PS4','Open World|Action-Adventure',true,2018,2018,60,96,false, 'USA', 'Rockstar Games','Take Two Interactive'),
	 ('Marvel''s Spider-Man','PS4','Open World|Action-Adventure',true,2018,2020,30,90,false, 'USA', 'Insomniac Games', 'Sony'),
	 ('Marvel''s Spider-Man 2','PS5','Open World|Action-Adventure',true,2023,2023,30,88,false, 'USA', 'Insomniac Games', 'Sony'),
	 ('God of War','PS4','Action-Adventure|Beat''em All',true,2018,2020,75,99,false, 'USA', 'SIE Santa Monica Studio', 'Sony'),
	 ('God of War Ragnarök','PS5','Action-Adventure|Beat''em All',false,2022,2023,50,99,false, 'USA', 'SIE Santa Monica Studio', 'Sony'),
	 ('God of War III','PS4','Action-Adventure|Beat''em All',false,2015,2020,35,92,false, 'USA', 'SIE Santa Monica Studio', 'Sony');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Uncharted: Drake''s Fortune','PS4','Action-Adventure|Platformer',true,2007,2020,10,68,true, 'USA', 'Naughty Dog', 'Sony'),
	 ('Uncharted 2: Among Thieves','PS4','Action-Adventure|Platformer',true,2009,2020,10,87,true, 'USA', 'Naughty Dog', 'Sony'),
	 ('Uncharted 3: Drake''s Deception','PS4','Action-Adventure|Platformer',false,2011,2020,10,80,true, 'USA', 'Naughty Dog', 'Sony'),
	 ('Uncharted: The Nathan Drake Collection','PS4','Action-Adventure|Platformer',true,2015,2020,30,83,true, 'USA', 'Naughty Dog', 'Sony'),
	 ('Uncharted 4: A Thief''s End','PS4','Action-Adventure|Platformer',false,2016,2020,10,90,true, 'USA', 'Naughty Dog', 'Sony'),
	 ('Horizon Zero Dawn','PS4','Action-Adventure|Open World',false,2017,2019,10,91,true, 'Netherlands', 'Guerrilla Games' , 'Sony'),
	 ('Journey','PS4','Action-Adventure|Platformer',true,2012,2019,5,86,true, 'USA', 'Thatgamecompany' , 'Sony'),
	 ('Heavy Rain','PS3','Narrative',true,2010,2016,15,79,true, 'France', 'Quantic Dream' , 'Sony'),
	 ('Red Dead Redemption','PS3','Action-Adventure|Open World',true,2010,2016,30,92,false, 'USA', 'Rockstar Games','Take Two Interactive'),
	 ('The Last of Us','PS3','Action-Adventure|Survival horror',false,2011,2016,25,92,false, 'USA', 'Naughty Dog', 'Sony');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Okami','PS3','Action-Adventure',true,2006,2016,30,94,false, 'Japan', 'Clover Studio' , 'Capcom'),
	 ('God of War: Ghost of Sparta','PSP','Action|Beat''em All',true,2010,2020,6,81,false, 'USA', 'SIE Santa Monica Studio', 'Sony'),
	 ('Assassin''s Creed II','PS3','Action-Adventure|Open World',true,2012,2015,35,93,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Assassin''s Creed III','PS3','Action-Adventure|Open World',true,2014,2015,35,93,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Assassin''s Creed IV: Black Flag','PS3','Action-Adventure',true,2013,2016,35,94,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Assassin''s Creed: Unity','PC','Action-Adventure|Open World',false,2014,2018,40,93,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Assassin''s Creed Origins','PS4','RPG|Open World',true,2017,2017,70,96,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Assassin''s Creed Odyssey','PC','RPG|Open World',true,2018,2018,100,97,true, 'France', 'Ubisoft','Ubisoft'),
	 ('Watch Dogs','PS3','Open World|Action-Adventure',true,2013,2015,30,85,false, 'France', 'Ubisoft','Ubisoft'),
	 ('Watch Dogs 2','PC','Open World|Action-Adventure',true,2016,2016,50,89,false, 'France', 'Ubisoft','Ubisoft');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Sid Meier''s Civilization III','PC','STR',true,2001,2001,15,88,false, 'USA', 'Firaxis Games', 'Infogrames Interactive'),
	 ('Sid Meier''s Civilization V','PC','STR',true,2010,2014,150,97,true, 'USA', 'Firaxis Games', '2K'),
	 ('Sid Meier''s Civilization: Beyond Earth','PC','STR',true,2014,2014,15,78,false, 'USA', 'Firaxis Games', '2K'),
	 ('Sid Meier''s Civilization VI','PC','STR',true,2016,2016,300,100,true, 'USA', 'Firaxis Games', '2K'),
	 ('Sid Meier''s Civilization VII','PC','STR',false,2025,2025,20,100,false, 'USA', 'Firaxis Games', '2K'),
	 ('Command & Conquer','PC','STR',true,1996,1998,30,89,true, 'USA', 'Westwood Studios', 'Virgin Interactive'),
	 ('Command & Conquer: Tiberian Sun','PC','STR',true,1999,1999,50,92,true, 'USA', 'Westwood Studios', 'Electronic Arts'),
	 ('Command & Conquer 3: Tiberium Wars','PC','STR',true,2007,2007,60,92,true, 'USA', 'Westwood Studios', 'Electronic Arts'),
	 ('Command & Conquer: Red Alert','PC','STR',true,1996,1998,40,89,true, 'USA', 'Westwood Studios', 'Virgin Interactive'),
	 ('Command & Conquer: Red Alert 2','PC','STR',true,2000,2001,60,90,true, 'USA', 'Westwood Studios', 'Electronic Arts'),
	 ('Command & Conquer: Red Alert Yuri','PC','STR',true,2001,2001,20,91,true, 'USA', 'Westwood Studios', 'Electronic Arts');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Command & Conquer: Red Alert 3','PC','STR',true,2008,2018,10,75,true, 'USA', 'Westwood Studios', 'Electronic Arts')
	 ('Command & Conquer: Generals','PC','STR',true,2003,2005,15,77,true, 'USA', 'Westwood Studios', 'Electronic Arts')
	 ('Stronghold','PC','STR',false,2003,2003,10,73,true),
	 ('Nox','PC','RPG|Hack&Clash',true,2008,2018,10,75,true),
	 ('Diablo','PS1|PC','RPG|Hack&Clash',true,1997,1998,40,92,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('Diablo II','PC','RPG|Hack&Clash',true,2000,2005,25,89,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('Diablo III','PS3|Switch 2','RPG|Hack&Clash',true,2012,2015,35,93,true, 'USA', 'Blizzard Entertainment', 'Activision Blizzard'),
	 ('StarCraft','PC','STR',true,1998,1998,150,92,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('StarCraft Brood War','PC','STR',true,1998,1998,20,92,false, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('StarCraft II: Wings of Liberty','PC','STR',true,2010,2010,150,95,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),;
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('StarCraft II: Heart of the Swarm','PC','STR',true,2013,2013,50,94,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('StarCraft II: Legacy of the Void','PC','STR',true,2015,2015,70,96,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('Warcraft II: Tides of Darkness','PC','STR',true,1995,1996,20,85,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('Warcraft III: Reign of Chaos','PC','STR',true,2002,2002,100,95,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
	 ('Warcraft III: The Frozen Throne','PC','STR',true,2003,2003,30,93,true, 'USA', 'Blizzard Entertainment', 'Blizzard Entertainment'),
  ('Heroes of Might and Magic II: The Succession Wars','PC','STR',true,1996,1998,30,88,true, 'USA','New World Computing','The 3DO Company'),
  ('Heroes of Might and Magic III','PC','STR',true,1999,2000,60,94,true, 'USA','New World Computing','The 3DO Company'),
  ('Heroes of Might and Magic IV','PC','STR',true,2002,2002,45,94,true, 'USA','New World Computing','The 3DO Company'),
  ('Heroes of Might and Magic V','PC','STR',false,2006,2008,25,89,true, 'Russia','Nival Interactive','Ubisoft'),
  ('Heroes of Might and Magic VII','PC','STR',false,2015,2018,10,85,true, 'Germany','Limbic Entertainment','Ubisoft');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Age of Empire II','PC','STR',false,2000,2003,30,88,true, 'USA','Ensemble Studios','Microsoft'),
	 ('Life is Strange','PC','Narrative',true,2008,2018,10,79,true, 'France','Dontnod Entertainment','Square Enix'),
	 ('Worms','PC','STR|Shoot''em All',false,1995,1996,30,80,true, 'UK','Team17','Team17'),
	 ('Worms 2','PC','STR|Shoot''em All',false,1997,1997,30,82,true, 'UK','Team17','Team17'),
	 ('Worms Armageddon','PC','STR|Shoot''em All',false,1999,2000,40,87,true, 'UK','Team17','Team17'),
	 ('Worms W.M.D','PS4','STR|Shoot''em All',false,2016,2018,20,87,true, 'UK','Team17','Team17'),
	 ('Theme Hospital','PC','STR',false,1997,2000,10,80,true, 'UK','Bullfrog Productions','Electronic Arts'),
	 ('Dungeon Keeper','PC','STR',false,1997,2000,10,80,true, 'UK','Bullfrog Productions','Electronic Arts'),
	 ('The Sims','PC','STR',true,2000,2000,50,90,true, 'USA','Maxis','Electronic Arts'),
	 ('The Sims 2','PC','STR',true,2000,2005,30,88,false, 'USA','Maxis','Electronic Arts');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Baldur''s Gate','PC','Action-Adventure|RPG',true,1998,2000,40,90,false, 'Canada','BioWare','Interplay Entertainment'),
	 ('Baldur''s Gate II: Shadows of Amn','PC','Action-Adventure|RPG',true,2000,2001,50,92,false, 'Canada','BioWare','Interplay Entertainment'),
	 ('Drakan: Order of the Flame','PC','Action-Adventure',true,1999,2000,25,89,false, 'USA','Surreal Software','Psygnosis'),
	 ('Heart of Darkness','PC','Action-Adventure|Platformer',true,1998,2001,15,77,false, 'France','Amazing Studio','Infogrames'),
	 ('Heroes of the Storm','PC','MOBA',false,2016,2016,90,93,true, 'USA','Blizzard Entertainment','Blizzard Entertainment'),
	 ('Grim Fandango','PC','Point&Click',true,2008,2018,20,80,true, 'USA','LucasArts','LucasArts'),
	 ('The Curse of Monkey Island','PC','Point&Click',true,1997,2018,10,75,true, 'USA','LucasArts','LucasArts'),
	 ('Escape From Monkey Island','PC','Point&Click',true,2004,2004,30,85,true, 'USA','LucasArts','LucasArts'),
	 ('The Secret of Monkey Island','PC','Point&Click',false,1990,2018,2,87,true, 'USA','Lucasfilm Games','Lucasfilm Games'),
	 ('Myst','PC','Point&Click',true,1993,1993,25,86,true, 'USA','Cyan','Brøderbund');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Versailles','PC','Point&Click',false,1996,1996,10,73,true, 'France','Cryo Interactive','Canal+ Multimedia'),
	 ('Goblins','PC','Point&Click',false,1991,1993,10,73,true, 'France','Coktel Vision','Sierra On-Line'),
	 ('Goblins 2','PC','Point&Click',false,1992,1994,10,75,true, 'France','Coktel Vision','Sierra On-Line'),
	 ('Oddworld: Abe''s Oddysee','PC','Action-Adventure|Platformer',true,1997,1999,25,85,true, 'USA','Oddworld Inhabitants','GT Interactive'),
	 ('Oddworld: Abe''s Exoddus','PC','Action-Adventure|Platformer',true,1998,2000,10,86,true, 'USA','Oddworld Inhabitants','GT Interactive'),
	 ('Lemmings','PC','STR',false,1991,1993,15,72,true, 'UK','DMA Design','Psygnosis'),
	 ('MegaBomberMan','PC','Party Game',false,1993,1999,15,72,true, 'Japan','Hudson Soft','Sega'),
	 ('SimCity 2000','PC','STR',false,1994,1995,15,70,false, 'USA','Maxis','Maxis'),
	 ('Caesar II','PC','STR',false,1995,1998,10,80,true, 'USA','Impressions Games','Sierra On-Line'),
	 ('Pharaoh','PC','STR',false,1999,2001,20,86,true, 'USA','Impressions Games','Sierra On-Line');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Carmageddon','PC','Racing|Beat''em All',false,1997,1999,20,86,true),
	 ('Carmageddon II: Carpocalypse Now','PC','Racing|Beat''em All',false,1998,2000,10,86,true),
	 ('RollerCoaster Tycoon','PC','STR',false,1999,2000,15,70,false),
	 ('Beyond Good & Evil','PC','Action-Adventure|Platformer',false,2003,2016,5,62,false),
	 ('Star Wars: Galactic Battlegrounds','PC','STR',true,2001,2001,40,90,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: Shadows of the Empire','PC','Action-Adventure|Hack&Clash',true,1996,2002,20,85,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars Jedi Knight II: Jedi Outcast','PC','Action-Adventure|Hack&Clash',true,2002,2003,30,98,true, 'USA', 'Raven Software', 'Lucas Arts'),
	 ('Star Wars Jedi Knight: Jedi Academy','PC','Action-Adventure|Hack&Clash',true,2003,2003,30,97,true, 'USA', 'Raven Software', 'Lucas Arts'),
	 ('Star Wars: The Old Republic','PC','Action-Adventure|RPG',true,2011,2012,50,92,true, 'USA', 'BioWare', 'Lucas Arts'),
	 ('Star Wars: Knights of The Old Republic','PC|Android','Action-Adventure|RPG',true,2003,2012,25,91,false, 'USA', 'BioWare', 'Lucas Arts');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Star Wars Episode I Racer','PC','Racing',true,2001,2001,30,75,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: StarFighter','PC','Space Shooter',true,2001,2001,20,80,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: Jedi StarFighter','PS2','Space Shooter',true,2001,2001,20,80,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: Battlefront (2015)','PC','FPS|Space Shooter',true,2015,2015,20,80,true, 'Sweden', 'DICE', 'Electronic Arts'),
	 ('Star Wars: Battlefront II (2017)','PS4|PC','FPS|Space Shooter',true,2017,2017,50,90,true, 'Sweden', 'DICE', 'Electronic Arts'),
	 ('Star Wars: Bounty Hunter','PS2','Action-Adventure',true,2002,2002,30,70,true, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: The Force Unleashed','PS3','Hack&Clash',true,2008,2016,15,75,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars: The Force Unleashed II','PS3','Hack&Clash',true,2008,2016,15,75,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('LEGO Star Wars: The Complete Saga','PS3','Hack&Clash',true,2007,2016,10,75,false, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Star Wars Rogue Squadron II: Rogue Leader','GameCube','Gunfight',true,2001,2003,50,94,true, 'USA', 'Lucas Arts', 'Lucas Arts');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Star Wars: Rogue Squadron','PC','Gunfight',true,1998,2003,20,93,true, 'USA', 'Lucas Arts', 'Lucas Arts'),
	 ('Little Big Adventure','PC','Action-Adventure|Platformer',true,1994,1999,20,85,true),
	 ('Little Big Adventure 2','PC','Action-Adventure|Platformer',true,1997,2000,50,97,true),
	 ('Tomb Raider','PS1','Action|Platformer',true,1997,1997,15,85,true),
	 ('Tomb Raider II','PC','Action|Platformer',true,1997,1998,10,86,true),
	 ('Tomb Raider III: Adventures of Lara Croft','PC','Action|Platformer',true,1998,1998,10,86,true),
	 ('Tomb Raider (2013)','PS3','Action|Platformer',true,2013,2013,30,92,true),
	 ('Rise of the Tomb Raider','PS4','Action|Platformer',false,2015,2015,10,75,true),
	 ('Crash Bandicoot','PS1','Action|Platformer',false,1996,1996,10,79,true),
	 ('Crash Nitro Kart','PS2','Racing',false,2003,2003,15,72,true);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Metal Gear Solid','PS1','Action|Infiltration',false,1998,2016,5,80,false),
	 ('Splinter Cell','PS2','Action|Infiltration',false,2002,2002,15,82,false),
	 ('WipeOut 2097','PS1','Racing',false,1996,1996,15,82,true),
	 ('Driver','PC','Racing',false,1999,2000,15,72,true),
	 ('Chrono Trigger','PS1','JRPG',false,1995,2015,5,75,false),
	 ('Fighting Force','PS1','Beat''em All',true,1997,1997,20,79,true),
	 ('Tekken','PS1','Versus Fighting',false,1995,1997,20,79,true),
	 ('Resident Evil 2','PS1','Survival horror',false,1998,1998,10,80,true),
	 ('Sonic the Hedgehog','Megadrive','Platformer',true,1991,1996,40,85,true, 'Japan', 'Sega','Sega'),
	 ('Sonic the Hedgehog 2','Megadrive','Platformer',true,1992,1996,50,88,true, 'Japan', 'Sega','Sega');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Sonic the Hedgehog 3','Megadrive','Platformer',true,1994,1996,40,88,true, 'Japan', 'Sega','Sega'),
	 ('Sonic & Knuckles','Megadrive','Platformer',true,1994,1996,20,80,true, 'Japan', 'Sega','Sega'),
	 ('Sonic 3 & Knuckles','Megadrive','Platformer',true,1994,1996,60,94,true, 'Japan', 'Sega','Sega'),
	 ('ToeJam&Earl','Megadrive','Action-Adventure|Platformer',false,1991,1996,10,75,true),
	 ('Streets of Rage 3','Megadrive','Beat''em All',true,1992,1996,15,70,false),
	 ('Golden Axe','Megadrive','Beat''em All',false,1989,1993,15,70,false),
	 ('Mighty Morphin Power Rangers','Megadrive','Beat''em All',false,1994,1994,15,60,true),
	 ('Sonic 3D: Flickies'' Island','Megadrive','Platformer',true,1996,1996,30,79,false, 'Japan', 'Sega','Sega'),
	 ('Sonic Pinball','Megadrive','Platformer',true,1996,1996,30,79,true, 'Japan', 'Sega','Sega'),
	 ('Jungle Strike','Megadrive','Action-Adventure|Beat''em All',false,1993,1996,30,79,false, 'Japan', 'Sega','Sega');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('EarthWorm Jim','Megadrive','Action-Adventure|Platformer',false,1994,1995,15,78,true),
	 ('Aladdin','Megadrive','Action-Adventure|Platformer',true,1993,1994,25,89,true),
	 ('Disney''s The Lion King','Megadrive','Action-Adventure|Platformer',false,1994,1994,15,80,true),
	 ('Dr Robotnik','Megadrive','STR',true,1993,1993,30,89,true),
	 ('Micromachines','Megadrive','Racing',false,1994,1994,15,80,true),
	 ('Tintin in Tibet','Megadrive','Platformer',false,1995,1996,10,71,true),
	 ('Tales of Symphonia','GameCube','JRPG',true,2003,2008,30,85,false),
	 ('Ristar','Megadrive','Action-Adventure|Platformer',false,1995,1996,20,80,false),
	 ('AAAHH!!! Real Monsters','Megadrive','Action-Adventure|Platformer',false,1995,1996,15,68,false),
	 ('Jurassic Park','Megadrive','Action-Adventure|Platformer',false,1994,1996,5,62,true);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('The Lost World: Jurassic Park','PS1','Action-Adventure|Platformer',false,1995,1996,5,62,true),
	 ('M.U.S.H.A','Megadrive','Gunfight|Space Shooter',false,1990,1995,10,65,true),
	 ('Street Fighter 2','Megadrive','Versus Fighting',false,1991,1995,20,67,true),
	 ('Dragon Ball Z','Megadrive','Versus Fighting',false,1994,1996,10,68,true),
	 ('Mortal Kombat','Megadrive','Versus Fighting',false,1992,1994,10,67,true),
	 ('SSX','PS2','Sport',false,2000,2001,10,88,true),
	 ('SSX Tricky','PS2','Sport',true,2001,2002,30,92,true),
	 ('SSX 3','PS2','Sport',true,2003,2003,50,96,true),
	 ('SSX On Tour','PS2','Sport',true,2005,2005,50,95,true),
	 ('The Lord of the Rings: The Two Towers','PS2','Action-Adventure|Beat''em All',true,2002,2002,30,90,true);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('The Lord of the Rings: The Return of the King','PS2','Action-Adventure|Beat''em All',true,2003,2003,35,90,true),
	 ('The Lord of the Rings: The Battle for Middle-earth','PC','STR',false,2003,2003,35,85,true),
	 ('God of War','PS2','Beat''em All|Action-Adventure',true,2005,2020,10,86,false),
	 ('God of War II: Divine Retribution','PS2','Beat''em All|Action-Adventure',true,2007,2020,10,90,false),
	 ('FIFA: Road to World Cup 98','PS1','Sport',false,1998,1998,15,85,true),
	 ('FIFA 2000','PC','Sport',false,2000,2000,20,75,false),
	 ('FIFA 15','PS3','Sport',false,2014,2015,20,80,true),
	 ('FIFA 16','PS4','Sport',false,2015,2016,20,80,true),
	 ('PES5','PS2','Sport',false,2005,2005,20,75,true),
	 ('Super Mario Bros.','NES','Platformer',true,1985,1993,20,82,true, 'Japan', 'Nintendo','Nintendo');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Super Mario Bros. 2','NES','Platformer',true,1988,1995,15,83,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Super Mario Bros. 3','NES','Platformer',true,1988,1995,20,90,true, 'Japan', 'Nintendo','Nintendo'),
	 ('New Super Mario Bros. Wii','Wii','Platformer',true,2008,2010,20,90,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Super Mario Land','GameBoy','Platformer',true,1989,1993,5,65,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Kart: Double Dash','GameCube','Racing',true,2003,2003,30,90,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Super Mario Kart','SNES','Racing',false,1992,2000,5,80,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Kart Wii','Wii','Racing',false,2008,2008,30,90,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Kart Deluxe','Switch','Racing',false,2017,2020,5,90,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Kart 64','N64','Racing',false,1996,2001,10,85,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Super Mario 64','N64','Racing',false,1996,1996,15,92,true, 'Japan', 'Nintendo','Nintendo');
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Super Smash Bros. Melee','GameCube','Versus Fighting',true,2002,2002,30,92,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Party 5','GameCube','Party Game',true,2003,2003,50,89,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Party 3','N64','Party Game',true,2003,2003,50,92,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario Tennis','GameCube','Sport',false,2004,2007,15,75,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Paper Mario','GameCube','Action-Adventure|Platformer',false,2000,2009,10,80,true, 'Japan', 'Nintendo','Nintendo'),
	 ('Mario RPG','SNES','JRPG',false,1996,2000,15,82,false, 'Japan', 'Nintendo','Nintendo'),
	 ('Golden Eye','N64','FPS',false,1997,1998,40,92,true),
	 ('Perfect Dark','N64','FPS',false,2000,2000,5,80,true),
	 ('Rayman 2: The Great Escape','N64','Action-Adventure|Platformer',false,1999,2000,20,88,true),
	 ('Rayman','GBA','Action-Adventure|Platformer',true,2000,2000,25,89,true);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Rayman Origins','Wii','Action-Adventure|Platformer',false,2011,2011,20,89,true),
	 ('Batman Returns','NES','Action-Adventure|Beat''em All',false,1989,1993,10,40,true),
	 ('Pokemon Yellow: Special Pikachu Edition','GameBoy','Action-Adventure|JRPG',true,1997,1998,40,92,true),
	 ('Pokemon Gold/Pokemon Silver','GameBoy','Action-Adventure|JRPG',true,1999,1999,40,95,true),
	 ('Wii Sports','Wii','Sport',false,2006,2006,5,80,true),
	 ('Pokemon Pinball','GBA','Puzzle',false,1999,2000,10,78,true),
	 ('Monument Valley','Android','Puzzle',true,2014,2018,3,81,true),
	 ('Monument Valley 2','Android','Puzzle',true,2017,2020,3,81,true),
	 ('Polytopia','Android','STR',false,2016,2017,2,78,false),
	 ('Cyberpunk 2077','PC','RPG|Open World',true,2020,2020,120,99,false);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('Watch Dogs Legion','PC','Action-Adventure|Open World',true,2020,2020,50,95,true),
	 ('Among Us','Android','Party game',false,2018,2020,7,70,true),
	 ('Mario Galaxy','Switch','Platformer',false,2008,2020,20,94,true),
	 ('Super Mario Sunshine','Switch','Platformer',false,2003,2020,10,75,true),
	 ('Final Fantasy XII','Switch','JRPG',true,2006,2021,40,93,false),
	 ('Hades','Switch','Action-Adventure|Hack&Clash',false,2020,2021,30,93,false),
	 ('New Super Mario Bros U Deluxe','Switch','Platformer',false,2020,2021,25,90,true),
	 ('Hyrule Warriors : Age of Calamity','Switch','Action-Adventure|Hack&Clash',false,2020,2021,15,90,true),
	 ('Assassin''s Creed Valhalla','PC','RPG|Open World',false,2020,2021,50,92,false),
	 ('Demon''s Souls','PS5','JRPG|Action-Adventure',false,2020,2022,20,90,false);
INSERT INTO public.gaming_lifetime (game_name,console,game_type,finished,published_year,played_year,hours_played,perso_score,multiplayed, country_dev, studio, editor) VALUES
	 ('The Last of Us Part I','PS5','Action-Adventure|Survival horror',true,2023,2023,25,91,false),
	 ('The Last of Us Part II','PS5','Action-Adventure|Survival horror',true,2020,2023,45,93,false),
	 ('Horizon Forbidden West','PS5','RPG|Open World',true,2022,2022,50,93,false),
	 ('Hogwart''s Legacy','PS5','Open World|RPG',false,2023,2023,50,95,false),
	 ('Star Wars Jedi Fallen Order','PC','RPG|Action-Adventure',true,2019,2020,25,89,false),
	 ('Marvel''s Guardians of the Galaxy','PS5','RPG|Action-Adventure',false,2021,2023,15,89,false),
	 ('Kena: Bridge of Spirits','PS5','Action-Adventure',false,2021,2023,15,89,false),
	 ('Elden Ring','PS5','RPG|Open World',false,2022,2024,120,99,true),
	 ('Star Wars Outlaws','PS5','RPG|Open World',false,2024,2024,50,93,false),
	 ('Astro Bot','PS5','Platformer',false,2024,2024,3,88,false),
	 ('Star Wars Jedi Survivor','PS5','RPG|Action-Adventure',false,2023,2025,25,89,false),
	 ('Baldur''s Gate','PS5','RPG|Action-Adventure',true,2023,2024,25,99,false),
	 ('Outer Wilds','PS5','Open World|Action-Adventure',false,2019,2024,90,99,true),
	 ('Clair Obscur Expedition 33','PS5','RPG',false,2025,2025,90,99,true),
	 ('Pokemon Y','3DS','Action-Adventure|JRPG',false,2013,2025,1,85,false),
	 ('The Legend of Zelda: Ocarina of Time 3D','3DS','Action-Adventure',false,2011,2025,2,94,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: A Link Between Worlds','3DS','Action-Adventure',false,2013,2025,2,93,false, 'Japan', 'Nintendo','Nintendo'),
	 ('The Legend of Zelda: Majora''s Mask 3D','3DS','Action-Adventure',false,2015,2025,2,93,false, 'Japan', 'Nintendo','Nintendo'),
	 ('Tanoshiku - Omoshiroku - Kanken Shougakusei','3DS','Edutainment',false,2018,2025,2,70,false)
	 ;
	 

-- create how long to beat table
CREATE TABLE IF NOT EXISTS  public.how_long_to_beat (
    id SERIAL PRIMARY KEY,
    game_name VARCHAR(255),
    console VARCHAR(50),
    game_type VARCHAR(50),
    finished BOOLEAN,
    published_year INTEGER,
    played_year INTEGER,
    hours_played INTEGER,
    perso_score INTEGER,
    multiplayed BOOLEAN,
    comp_100 NUMERIC,
    comp_all NUMERIC,
    comp_main NUMERIC,
    comp_plus NUMERIC,
    platform VARCHAR(255),
    developer VARCHAR(255)
);

-- Populate the table with HLTB CSV data
COPY how_long_to_beat FROM '/docker-entrypoint-initdb.d/csv_file/hltb_scrap.csv' DELIMITER ',' CSV HEADER;

-- create metacritic table
CREATE TABLE IF NOT EXISTS  public.metacritic (
	id SERIAL PRIMARY KEY,
	game_name VARCHAR(255),
	platform VARCHAR(255),
	year_of_release INT,
	genre VARCHAR(255),
	publisher VARCHAR(255),
	na_sales VARCHAR(20),
	eu_sales VARCHAR(20),
	jp_sales VARCHAR(20),
	other_sales VARCHAR(20),
	global_sales VARCHAR(20),
	critic_score VARCHAR(20),
	critic_count VARCHAR(20),
	user_score VARCHAR(20),
	user_count VARCHAR(20),
	developer VARCHAR(255),
	rating VARCHAR(20)
);

-- Populate the table with metacritic CSV data
COPY metacritic FROM '/docker-entrypoint-initdb.d/csv_file/metacritic_clean.csv' DELIMITER ',' CSV HEADER;

-- create metacritic table
CREATE TABLE IF NOT EXISTS  public.metacritic_merged (
	id INT,
    game_name VARCHAR(255),
    console VARCHAR(50),
    game_type VARCHAR(50),
    finished BOOLEAN,
    published_year INT,
    played_year INT,
    hours_played INT,
    perso_score INT,
    multiplayed BOOLEAN,
    fuzz VARCHAR(255),
    game_title VARCHAR(255),
    game_platform VARCHAR(50),
    game_release_date VARCHAR(50),
    Genre VARCHAR(50),
    Publisher VARCHAR(255),
    NA_Sales DECIMAL(5,2),
    EU_Sales DECIMAL(5,2),
    JP_Sales DECIMAL(5,2),
    Other_Sales DECIMAL(5,2),
    Global_Sales DECIMAL(5,2),
    metascore INT,
    Critic_Count INT,
    user_score DECIMAL(3,1),
    User_Count INT,
    Developer VARCHAR(255),
    Rating VARCHAR(5),
    game_summary TEXT
);

-- Populate the table with metacritic merged CSV data
COPY metacritic_merged FROM '/docker-entrypoint-initdb.d/csv_file/metacritic_merged_local.csv' DELIMITER ',' CSV HEADER;
