#!/usr/bin/python3
"""
Script select all cities based on name
"""
import sys
import MySQLdb as sdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    conn = sdb.connect(host="localhost",
                       user=username,
                       passwd=password,
                       db=dbname,
                       port=3306)
    cur = conn.cursor()
    name = sys.argv[4]
    query = """SELECT * FROM cities where
         cities.state_id=(select id from states
         where BINARY name=%s) ORDER BY id ASC"""
    cur.execute(query, (name,))
    result = cur.fetchall()
    if result and result[0]:
        print(result[0][2], end="")
    if result and result[1]:
        for r in result[1:]:
            print(",", r[2], end="")
    print()
