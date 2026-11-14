import sqlite3

connection = sqlite3.connect("instance/cms.db")

# tables = connection.execute("""
# SELECT name
# FROM sqlite_master
# WHERE type = 'table'
# ORDER BY name""").fetchall()

# print("Tables in database:", tables)

data = connection.execute(
    """
    SELECT  * FROM posts
    """
).fetchall()

print(data)

connection.close()