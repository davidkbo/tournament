-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Creates a table to archive the players names and ids

CREATE TABLE players (
	ply_id serial NOT NULL PRIMARY KEY,
	ply_name varchar(50) NOT NULL  
);

-- Cretaes a table to archive the matches results using the ply_id 
-- from the players table

CREATE TABLE matches (
	mtc_id serial NOT NULL PRIMARY KEY,
	winner int NOT NULL REFERENCES players(ply_id),
	loser int NOT NULL REFERENCES players(ply_id)
);

-- Creates a view to show how many wins and losses each player has

CREATE VIEW players_win_loss AS
	SELECT p.ply_id, p.ply_name, COUNT(m1.winner) win, COUNT(m2.loser) loss 
	FROM players p
	LEFT JOIN matches m1 ON p.ply_id = m1.winner
	LEFT JOIN matches m2 ON p.ply_id = m2.loser
	GROUP BY p.ply_id, p.ply_name
	ORDER BY win DESC;

-- Creates a view that uses the player_win_loss view to provide the player standings 
-- as specified in the function

CREATE VIEW players_standings AS
	SELECT ply_id, ply_name, win, win + loss games 
	FROM players_win_loss
	ORDER BY win DESC;

-- Creates a view to make the pairing easier, providing the players standings in the format 
-- needed in the swissPairing() 

CREATE VIEW players_standing_id_name AS
	SELECT ply_id , ply_name FROM players_standings;