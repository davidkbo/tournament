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
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM matches")
    con.commit()
    cur.close()
    del cur
    con.close()

def deletePlayers():
    """Remove all the player records from the database."""
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM players")
    con.commit()
    cur.close()
    del cur
    con.close()

def countPlayers():
    """Returns the number of players currently registered."""
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT count(ply_name) FROM players")
    result = cur.fetchall()
    outcome = 0
    for row in result:
        outcome = row[0]
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
    con = connect()
    cur = con.cursor()
    cmd = "INSERT INTO players (ply_name) values (%s)"
    cur.execute(cmd, (name,))
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
    con = connect()
    cur = con.cursor()
    cur.execute("select * from player_standings")
    result = cur.fetchall()
    return result
    cur.close()
    del cur
    con.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    con = connect()
    cur = con.cursor()
    cmd = "INSERT INTO matches (winner,loser) values (%s,%s)"
    cur.execute(cmd, (winner, loser))
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
    con = connect()
    cur = con.cursor()
    cur.execute("select * from player_standing_id_name")
    results = cur.fetchall()
    pairings = []
    for i in range(0, len(results) - 1, 2):
        pairings.append((results[i] + results[i + 1]))
    return pairings
    con.commit()
    cur.close()
    del cur
    con.close()
