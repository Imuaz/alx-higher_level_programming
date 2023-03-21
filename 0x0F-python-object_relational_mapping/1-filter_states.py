#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
"""
cript that select all from database
"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER
                BY states.id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
