#!/usr/bin/python3
"""
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cursor = db.cursor()
    sql = """SELECT *
            FROM states
            WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql, (argv[4],))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
