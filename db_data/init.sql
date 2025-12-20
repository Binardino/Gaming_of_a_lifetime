-- public.gaming_lifetime definition

-- Drop table

-- DROP TABLE public.gaming_lifetime;

CREATE TABLE IF NOT EXISTS public.gaming_lifetime (
	id serial4 PRIMARY KEY,
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
	editor varchar(255) NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_225486_game_name ON public.gaming_lifetime USING btree (game_name,console,published_year);
CREATE INDEX IF NOT EXISTS idx_console ON public.gaming_lifetime(console);
CREATE INDEX IF NOT EXISTS idx_game_type ON public.gaming_lifetime(game_type);
CREATE INDEX IF NOT EXISTS idx_played_year ON public.gaming_lifetime(played_year);
CREATE INDEX IF NOT EXISTS idx_finished ON public.gaming_lifetime(finished);
	 

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
CREATE INDEX IF NOT EXISTS idx_hltb_game_name ON public.how_long_to_beat(game_name);
CREATE INDEX IF NOT EXISTS idx_hltb_platform ON public.how_long_to_beat(platform);

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
CREATE INDEX IF NOT EXISTS idx_meta_game_name ON public.metacritic(game_name);
CREATE INDEX IF NOT EXISTS idx_meta_platform ON public.metacritic(platform);
CREATE INDEX IF NOT EXISTS idx_meta_genre ON public.metacritic(genre);
CREATE INDEX IF NOT EXISTS idx_meta_publisher ON public.metacritic(publisher);

-- create metacritic_merged table
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
CREATE INDEX IF NOT EXISTS idx_mm_game_name ON public.metacritic_merged(game_name);
CREATE INDEX IF NOT EXISTS idx_mm_console ON public.metacritic_merged(console);
CREATE INDEX IF NOT EXISTS idx_mm_publisher ON public.metacritic_merged(publisher);
CREATE INDEX IF NOT EXISTS idx_mm_genre ON public.metacritic_merged(genre);
