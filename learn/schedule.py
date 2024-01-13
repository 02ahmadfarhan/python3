#!/usr/bin/python3

import sys
import sqlite3 as sql

# create dataBase
dataBaseName = 'schedule.db'

def createPersonTable(conn):
    personTable = '''
                    CREATE TABLE person (
                        firstName TEXT NOT NULL,
                        lastName TEXT NOT NULL,
                        isStudent BOOLEAN
                    );
    '''
    conn.execute(personTable)
    
def createDataBase():
        sqlConn = sql.connect(dataBaseName)
        if (sqlConn == None):
            err = -1
        else:
            err = 0
            return err, sqlConn
    
def main(args):
    if len(args) !=2:
        print('Error: you need to provide exacly one parameter', file=sys.stderr)
        return -1
    
    if (args[1] == 'create'):
        err, sqlConnection = createDataBase()
        if (err == 0):
            createPersonTable(sqlConnection)
    else:
        print('Error: Invalid Parameter', file=sys.stderr)
        return -1
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))