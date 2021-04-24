import os
import pymysql

# Get username from workspace
username = os.getenv("GitPOD_USER")

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "select * from Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
