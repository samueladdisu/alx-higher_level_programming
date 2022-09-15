#!/usr/bin/python3
"""
Script select all cities
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
    query = """SELECT cities.id, cities.name, states.name
               FROM cities, states WHERE states.id = cities.state_id
               ORDER BY cities.id ASC;"""
    cur.execute(query)
    result = cur.fetchall()
    for r in result:
        print(r)
