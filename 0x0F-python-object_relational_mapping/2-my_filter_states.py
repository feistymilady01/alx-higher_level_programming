#!/usr/bin/python3
"""
Displays all values in table states where name matches the argument
"""

import MySQLdb
import sys

# arg = sys.argv[4]

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
# WHERE states.name LIKE '{}%' \
# ORDER BY states.id ASC;".format(sys.argv[4]))

    state = cur.fetchall()
    for state in state:
        print(state)
    cur.close()
    db.close()
