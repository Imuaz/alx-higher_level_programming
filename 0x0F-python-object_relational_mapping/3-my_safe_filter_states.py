#!/usr/bin/python3
"""script for use in getting all states from sql db
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3],
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if (args[4] == row[1]):
            print(row)
