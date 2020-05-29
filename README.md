# Gaming_of_a_lifetime
**Historical Data analytics of my Gaming lifetime history**

Python Pandas, Datavisualization &amp; SQL Project - 
Having been a gamer all my life, the idea of this project is to list all the games I played, with several KPIs (score, hours played etc.), and visualize this gaming of a lifetime, to see some trends in my gaming behaviour.
- which genre did I play the most ?
- on which console ?
- for how long ?
It is a nice way to remember all of gaming experiences, and to make something professional Python training & visualization of all this leisure time I had playing on those fantastic games !

Once the database created with SQL queries, I use various Python visualization libraries (Matplotlib, Seaborn, PyPlot, Bokeh) to visualize this gaming of a lifetime.
Finally, I imported a Kaggle dataset encompassing scores of all the games I played (both from the Press & Players) to compare my scores given and theirs.

## Content
- [Project Overview](#project-overview)
- [Hypotheses / Questions](#hypotheses-questions)
- [Repo Structure](#repo-structure)
- [Workflow](#workflow)
- [Analysis](#analysis)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

## Project Overview
- Creation of a dataset of my overall gaming experience.
SQL queries to create this ad hoc dataset with the following columns :

* CREATE TABLE my_videogames(
	* id SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
    * game_name VARCHAR(255) NOT NULL,
    * console VARCHAR(20) NOT NULL,
    * game_type VARCHAR(50) NOT NULL,
    * finished BOOL NOT NULL, #have I finish the game or Not
    * published_year SMALLINT(4) NOT NULL,
    * played_year SMALLINT(4) NOT NULL, #first time I played the game
    * hours_played SMALLINT(4), #approximation of hours spent playing the game
    * perso_score SMALLINT(2) NOT NULL, #personal score on the game - rating over 100
    * multiplayed BOOL NOT NULL, #have I played it with other persons

- Datavisualization with Pandas over those gaming data
- Comparison between my personal scores given to the games, and the existing Metascore given by the Press in general to those same games

Each row for one game played, with several
cf. SQL queries for more detailed information over the dataset creation

## Hypotheses / Questions
- Finding key stats over my gaming lifetime : 
    * how many hours in average have I spent per gametype/console ?
    * which are the years I played the most ?
    * when comparing my grades given to all of those games, am I giving comparable grades to the critics (i.e. Metacritics) & in comparison to other players (i.e. playerscore) ?

## Repo Structure
1. DB_creation_SQL_queries : SQL queries for creation of the dataset
2. Notebook Pandas & Visualizations
    * Pandas visualizations of the Gaming lifetime dataset
    * Comparison of scores between this dataset and existing Metacritic dataset (TBD)

3. Plots_Charts_PNG
    * PNG plots from Visualization notebook

## Workflow
My workflow consisted on 3 steps - each detailed in the relevant notebook:
**1 - Database creation**
creating the database with SQL queries (brainstorming over the structure of the dataset, and some quality memory times to remember all those great games I played)
Each Workflow is detailed in its respective Notebooks.

**2 - Data visualization & analaysis**

**3 - Importing Metacritic dataset**
Importing & Cleaning the dataset, then doing comparison & datavisualizations over those 2 datasets

## Analysis
1. Importing & cleaning dataset
- [x] **Import & minor wrangling**

2. Visualizing gaming of a lifetime dataset
- [x] **Exploratory Data Analysis (EDA)**: Aims to appraoch the data from both a qualitative and a quantitative approach for main insights
- [x]  **Data visualizations**: plots over KPIs (seaborn & pyplot)
- [x] **Monthly churn rate and Cohort Analysis**: Aims to identify monthly churn rates and performance measurement through customer cohort analysis on retention rates

3. Comparison of Scores with complete video game dataset
- [x] **Importation & Data transformation** : import & clean 16.8K rows dataset
- [x] **Merging & EDA of two dataframes**
- [x] **Comparison plots**

## Conclusion

## Future Work
- using Bokeh