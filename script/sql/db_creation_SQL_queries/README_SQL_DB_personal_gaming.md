# List of all the games I played (and that I could think of)
Creation of SQL base of 213 videogames

# List of all the games I played (and that I could think of)

## Table creation & criteria
9 columns (not counting id) detailed below
The idea is to measure : 
- personal score given (rating over 100)
- how many hours have I played the game (approximatively)
- have I finished it
- have I played the game with other people
- on what year have I played it

CREATE TABLE my_videogames(
    id SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
    game_name VARCHAR(255) NOT NULL,
    console VARCHAR(20) NOT NULL, #several console accepted
    game_type VARCHAR(50) NOT NULL, #several type accepted
    finished BOOL NOT NULL, #have I finish the game or Not
    published_year SMALLINT(4) NOT NULL,
    played_year SMALLINT(4) NOT NULL, #first time I played the game
    hours_played SMALLINT(4), #approximation of hours spent playing the game
    perso_score SMALLINT(2) NOT NULL, #personal score on the game - rating over 100
    multiplayed BOOL NOT NULL, #have I played it with other persons
    PRIMARY KEY(id),
    UNIQUE KEY game_name (game_name)
    )
    ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT charset=latin1;

## Limits to the method :
#- Positive preselection of games# 
high personal scores, most games having ratings greather than 75 : 
obviously all the games I played (or almost all of them), I chose them in the first place because I received positive feedbacks on them, or had very positive expectations, therefore almost all of them have very positive personal score - except few games I disliked after all, 
Therefore I really enjoyed most of the games I played (which is a good thing isn't it ?), which explains why the overal personal scores is very high 

#partial notation# 
for many games, this rating is made years (if not decades) after playing them, so my personal score relies on memories & feelings I now have when I remember playing those games back then
