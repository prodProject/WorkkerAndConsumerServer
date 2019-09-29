from Database import createTableIfNotExixts
from Database.createTableIfNotExixts import CreateTableIfNotExists

ser=CreateTableIfNotExists()
ser.start()
print(ser.done())
