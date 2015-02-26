-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
	ply_id serial NOT NULL PRIMARY KEY,
	ply_name varchar(50) NOT NULL  
);

CREATE TABLE matches (
	mtc_id serial NOT NULL PRIMARY KEY,
	winner int NOT NULL REFERENCES players(ply_id),
	loser int NOT NULL REFERENCES players(ply_id)
);


create view player_win_loss as
	select p.ply_id, p.ply_name, count(m1.winner) win, count(m2.loser) loss 
	from players p
	left join matches m1 on p.ply_id = m1.winner
	left join matches m2 on p.ply_id = m2.loser
	GROUP BY p.ply_id, p.ply_name
	order by win desc;

create view player_standings as
	select ply_id, ply_name, win, win + loss games 
	from player_win_loss
	order by win desc;

create view player_standing_id_name as
	select ply_id , ply_name from player_standings;