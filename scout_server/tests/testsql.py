from src import sql
from os import path, remove
def test_sql():
	sql.db = "db/test.db"
	
	print "Testing create_tables"
	assert(sql.create_table() == None)
	assert(path.isfile(sql.db))
	remove(sql.db)
	print "All tests pass"

	
	



