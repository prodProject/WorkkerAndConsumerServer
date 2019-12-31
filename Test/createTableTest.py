import psycopg2

from Database.databaseConnection import DatabaseConnection

query = 'TRUNCATE TABLE  "WORKER_DATA","ENTITY_DATA","LOGIN","PUSH_NOTIFICATON" RESTART IDENTITY CASCADE;'
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
postgres_insert_query = """ INSERT INTO "ENTITY_DATA" (dbid) VALUES (0)"""
record_to_insert = ('0')
cursor.execute(postgres_insert_query)
connection.commit()
count = cursor.rowcount
print(count, "Record inserted successfully into mobile table")
connection.close()
