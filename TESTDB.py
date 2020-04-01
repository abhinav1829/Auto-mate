# import sqlite3

# con = sqlite3.connect('automate.db')
# cursor = con.cursor()

# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS users ('
#     'username TEXT PRIMARY KEY,'
#     'password TEXT NOT NULL,'
#     'location TEXT DEFAULT "Pune",'
#     'theme BOOLEAN DEFAULT 0,'
#     'voice BOOLEAN DEFAULT 0,'
#     'music TEXT DEFAULT "G:/Music",'
#     'video TEXT DEFAULT "G:/VDOS/Music",'
#     'movie TEXT DEFAULT "G:/Movies"'
#     ')'
# )

# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS current_user ('
#     'username TEXT PRIMARY KEY,'
#     'password TEXT NOT NULL,'
#     'location TEXT DEFAULT "Pune",'
#     'theme BOOLEAN DEFAULT 0,'
#     'voice BOOLEAN DEFAULT 0,'
#     'music TEXT DEFAULT "G:/Music",'
#     'video TEXT DEFAULT "G:/VDOS/Music",'
#     'movie TEXT DEFAULT "G:/Movies",'
#     'FOREIGN KEY (username) REFERENCES users (username)'
#     ')'
# )

# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS notes ('           ''
#     'username TEXT NOT NULL,'
#     'note TEXT NOT NULL,'
#     'note_date TEXT NOT NULL,'
#     'FOREIGN KEY (username) REFERENCES users (username))'
# )

# cursor.execute('DROP TABLE notes')

# cursor.execute(
#     'INSERT INTO users (username,password) VALUES ('
#     '"shreyash",'
#     '"shreyash"'
#     ')'
# )

# cursor.execute('UPDATE current_user SET video = "enrique"')

# username = ''
# rows = cursor.execute('select * from current_user')
# for row in rows:
#     username = row[0]
# cursor.execute('DELETE FROM current_user')
# cursor.execute('INSERT INTO current_user SELECT * FROM users WHERE username="'+username+'"')

# rows = cursor.execute("select sql from sqlite_master where type = 'table' and name = 'notes'")
# for row in rows:
#     print(row)

# rows=cursor.execute('select * from users').fetchall()
# for row in rows:
#     print(row[1])
# print(rows[0][1])

# con.commit()

# con.close()
