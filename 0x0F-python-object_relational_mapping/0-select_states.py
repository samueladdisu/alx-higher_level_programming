#!/usr/bin/python3
"""
MySQLdb demo
"""

import sys
import MySQLdb as sdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    conn = sdb.connect(host="localhost",
                       user=username, passwd=password,
                       db=dbname, port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for r in result:
        print(r)
