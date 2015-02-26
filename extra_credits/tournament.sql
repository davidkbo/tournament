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
	ply_id int NOT NULL REFERENCES players(ply_id),
	match_number int NOT NULL
);

CREATE TABLE result_types (
	rst_id serial NOT NULL PRIMARY KEY,
	result_types varchar(10) NOT NULL
);

CREATE TABLE match_results (
	mrs_id serial NOT NULL PRIMARY KEY,
	ply_id int NOT NULL REFERENCES matches(mtc_id),
	rst_id int NOT NULL REFERENCES result_types(rst_id)
);
