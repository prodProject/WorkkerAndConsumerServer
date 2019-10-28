import psycopg2

from Database.databaseConnection import DatabaseConnection

query = 'SELECT * FROM "WORKER_DATA";'
'''database = DatabaseConnection()
con = database.getConnection()
cur = con.cursor()
try:
    res = cur.execute(
        'DROP TABLE "UNKNOWN";')
    print(cur.rowcount)
    print(cur.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
con.commit()  # <--- makes sure the change is shown in the database
con.close()
cur.close()'''
database = DatabaseConnection()
connection = database.getConnection()
cursor = connection.cursor()
postgres_insert_query = """ INSERT INTO "ENTITY_DATA" (dbid) VALUES (%s)"""
record_to_insert = ('0')
cursor.execute(query)
connection.commit()
count = cursor.rowcount
print(count, "Record inserted successfully into mobile table")
connection.close()
