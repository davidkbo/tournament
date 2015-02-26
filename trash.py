from tournament import *

con = connect()
cur = con.cursor()
cur.execute("select * from player_standing_id_name")
results = cur.fetchall()
pairings = []
for i in range(0, len(results) - 1, 2):
    pairings.append((results[i] + results[i + 1]))

print pairings
