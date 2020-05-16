# Gaming_of_a_lifetime
Python Pandas &amp; SQL Project - Historical Data analytics of my Gaming lifetime history

## Content
- [Project Overview](#project-overview)
- [Hypotheses / Questions](#hypotheses-questions)
- [Workflow](#workflow)
- [Repo Structure](#repo-structure)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

## Project Overview
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

## Hypotheses / Questions
- Finding key stats over my gaming lifetime : 
    * how many hours in average have I spent per gametype/console ?
    * which are the years I played the most ?
    * when comparing my grades given to all of those games, am I giving comparable grades to the critics (i.e. Metacritics) & in comparison to other players (i.e. playerscore) ?

## Workflow
My workflow consisted on 3 steps - each detailed in the relevant notebook:
**1 - Database creation**
creating the database with SQL queries (brainstorming over the structure of the dataset, and some quality memory times to remember all those great games I played)
Each Workflow is detailed in its respective Notebooks.

**2 - Data visualization & analaysis**

**3 - Importing Metacritic dataset**
Importing & Cleaning the dataset, then doing comparison & datavisualizations over those 2 datasets

## Repo Structure
1. DB_creation_SQL_queries : SQL queries for creation of the dataset
2. Notebook Pandas & Visualizations
    * Pandas visualizations of the Gaming lifetime dataset
    * Comparison of scores between this dataset and existing Metacritic dataset (TBD)

3. Plots_Charts_PNG
    * PNG plots from Visualization notebook

## Conclusion

## Future Work