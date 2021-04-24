import os
import datetime
import pymysql

# Get username from workspace
username = os.getenv("GitPOD_USER")

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.executemany("delete where name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
