# Udacity (Full Stack Web Developer Nanodegree) - Project P2: Tournament Results

Description:
Tournament result is a module written in Python that provide functions to deal 
with Swiss style torunaments with all data stored in a PostgreSQL database.

Functions:

Players
- registerPlayer(name): Adds a new player into the database
- deletePlayers(): Deletes all players from the database
- playerStandings(): Returns the standings from all players

Matches
- reportMatch(winner, loser): Adds a match result into the database
- deleteMatches(): Deletes all matches results from the database 

Tournament
- swissPairings(): Returns the pairs 

Limitations:
- Just works for even number of player
- It doesn't support ties
- It can't deal with multiple tournaments 

Running the program
- The program requires PostgreSQL 9.3.6 and psycopg2 installed
- A Vagrant machine with the required can be forked from the github:

git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack

- To use the module you just have to import it (import tournament) and use it

- To run the unit tests to see if everything was set correctly just run:

python tournament_test.py 

- And see if all tests passes