#!/usr/bin/python3
"""Database storage class"""

import MySQLdb


class Database:
    connection = None

    def __init__(self):
        self.connection = self.__connect()
    
    def __connect(self, host='localhost', user='root', passwd='root@sgetme', port=3306):
        return MySQLdb.connect(host=host, user=user, passwd=passwd, port=port)

    def create_connection(self, host='localhost', user='root', passwd='root@sgetme', port=3306):
        return MySQLdb.connect(host=host, user=user, passwd=passwd, port=port)


# connect to the database;
# conn = MySQLdb.connect(host='localhost', user='root', passwd="root@sgetme", port=3306)

# create databae object
db = Database()


#Create connection from database object
#   conn = db.connection
conn = db.create_connection(host='localhost', user='root', passwd='root@sgetme', port=3306)
cur = conn.cursor()


def create_db(db_name):
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    conn.commit()

def show_dbs():
    cur.execute("Show databases;")
    dbs = cur.fetchall()

    print(f"\n.......Showing List of Databases..........\n")

    for db in dbs:
        print(*db)

def drop_db(db_name):
    cur.execute(f"drop database if exists {db_name};")
    conn.commit()
    print(f"\n.......Databae <{db_name}> Dropped ..........\n")



show_dbs()
create_db("mydb")
show_dbs()

drop_db('mydb')
show_dbs()

cur.close()

