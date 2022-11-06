#!/usr/bin/python3
"""
Script select states name matching argumnet given
"""
import sys
import MySQLdb as sdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]
    conn = sdb.connect(host="localhost",
                       user=username,
                       passwd=password,
                       db=dbname,
                       port=3306)
    cur = conn.cursor()
    query = """SELECT * FROM states where BINARY name='{}'
            ORDER BY id ASC""".format(name)
    cur.execute(query)
    result = cur.fetchall()
    for r in result:
        print(r)
