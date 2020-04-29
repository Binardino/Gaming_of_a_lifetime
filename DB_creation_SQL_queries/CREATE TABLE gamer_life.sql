USE gamer_lifestory ; 
DROP TABLE IF EXISTS my_videogames ;

CREATE TABLE my_videogames(
    id SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
    game_name VARCHAR(255) NOT NULL,
    console VARCHAR(20) NOT NULL, #several console accepted
    game_type VARCHAR(50) NOT NULL, #several types accepted
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
    
    