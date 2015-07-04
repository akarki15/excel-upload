from contextlib import closing
from config import DATABASE, BASE_DIR

import sqlite3, os

# Database stuff

def connect_db():
	return sqlite3.connect(DATABASE)

def init_db():
	with closing(connect_db()) as db:
		with open(os.path.join(BASE_DIR, 'schema.sql'), mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

init_db()
print "Database set up."