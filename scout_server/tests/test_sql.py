from ..src import sql
from os import remove
from os.path import isfile
def test_sql():
	sql.db = "db/test.db"
	assert(sql.create_tables() == None)
	assert(isfile("db/test.db"))
	db = sql.Database("db/test.db")	
	a=[1, 112, "asdf", "asdf", 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 5, 2, 5.5, 5.5, True, True, True]
	db.add_performance(a)
	assert(len(db.get_all()) == 1)
	del db
	db = sql.Database()
	assert(len(db.get_all()) == 1)

	remove("db/test.db")


