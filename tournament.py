#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a DELETE SQL statement to clean the matches table"
    cur.execute("DELETE FROM matches")

    # Commiting all changes and deleting the cursor and closing the database
    # connection"""
    con.commit()
    cur.close()
    del cur
    con.close()

def deletePlayers():
    """Remove all the player records from the database."""

    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a DELETE SQL statement to clean the players table
    cur.execute("DELETE FROM players")

    # Commiting all changes and deleting the cursor and closing the database
    # connection
    con.commit()
    cur.close()
    del cur
    con.close()

def countPlayers():
    """Returns the number of players currently registered."""

    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a SELECT SQL statement to count the number of players and
    # fetching all results to a variable
    # The variable is iterated to return the value as a integer

    cur.execute("SELECT count(ply_name) FROM players")
    result = cur.fetchall()

    outcome = 0
    for row in result:
        outcome = row[0]

    # Commiting all changes and deleting the cursor and closing the database
    # connection and returning the fuction value
    cur.close()
    del cur
    con.close()
    return outcome

def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a INSERT SQL statement to add new players into the tournament
    cmd = "INSERT INTO players (ply_name) values (%s)"
    cur.execute(cmd, (name,))

    # Commiting all changes and deleting the cursor and closing the database
    con.commit()
    cur.close()
    del cur
    con.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a SELECT SQL statement to return players standings and
    # fetching all results to a variable
    cur.execute("select * from players_standings")
    result = cur.fetchall()

    # Deleting the cursor, closing the database and returning the function
    # result
    cur.close()
    del cur
    con.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a INSERT SQL statement to add matches results
    cmd = "INSERT INTO matches (winner,loser) values (%s,%s)"
    cur.execute(cmd, (winner, loser))

    # Commiting all changes and deleting the cursor and closing the database
    con.commit()
    cur.close()
    del cur
    con.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Connecting to the database and creating a cursor
    con = connect()
    cur = con.cursor()

    # Running a SELECT SQL statement to count the number of players and
    # fetching all results to a variable, the variable is iterated to
    # include the pairs tuples into a list
    cur.execute("select * from players_standing_id_name")
    results = cur.fetchall()

    pairings = []
    for i in range(0, len(results) - 1, 2):
        pairings.append((results[i] + results[i + 1]))

    # Deleting the cursor, closing the database and returning the function
    # result
    cur.close()
    del cur
    con.close()
    return pairings
