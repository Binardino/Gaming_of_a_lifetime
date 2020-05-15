# Gaming_of_a_lifetime
Python Pandas &amp; SQL Project - Historical Data analytics of my Gaming lifetime history

##Project Overview
- Creation of a dataset of my overall gaming experience.
SQL queries to create this ad hoc dataset with the following columns :

CREATE TABLE my_videogames(
	id SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
    game_name VARCHAR(255) NOT NULL,
    console VARCHAR(20) NOT NULL,
    game_type VARCHAR(50) NOT NULL,
    finished BOOL NOT NULL, #have I finish the game or Not
    published_year SMALLINT(4) NOT NULL,
    played_year SMALLINT(4) NOT NULL, #first time I played the fame
    hours_played SMALLINT(4), #approximation of hours spent playing the game
    perso_score SMALLINT(2) NOT NULL, #personal score on the game - rating over 100
    multiplayed BOOL NOT NULL, #have I played it with other persons

- Datavisualization with Pandas over those gaming data
- Comparison between my personal scores given to the games, and the existing Metascore given by the Press in general to those same games

Each row for one game played, with several
cf. SQL queries for more detailed information over the dataset creation

##Repo Structure
- DB_creation_SQL_queries : SQL queries for creation of the dataset

##Notebook Pandas & Visualizations
- Pandas visualizations of the Gaming lifetime dataset
- Comparison of scores between this dataset and existing Metacritic dataset (TBD)

##Plots_Charts_PNG
- PNG plots from Visualization notebook