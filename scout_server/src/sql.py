#Authored by Owen Hughes
#Creates interface for sqlite3 module for my purposes
from sqlite3 import connect
from os import path, mkdir, remove, getcwd
#EXAMPLE SESSION AND COMMANDS.
#connection = sqlite3.connect("db/example.db")
#c = connection.cursor()
#c.execute('''CREATE TABLE performance
#			     (auton_defense varchar(255), auton_score varchar(255));''')
#c.execute("INSERT INTO performance VALUES ('chival', 'high')")

#resp = c.execute("SELECT * FROM performance")
#print [x for x in resp]

#connection.commit()
#connection.close()

#Various constants
db = "db/main.db"

performance_table_structure = """
(
P_ID INTEGER PRIMARY KEY,
match_number int NOT NULL,
team_number int NOT NULL,
defense varchar(255),
score varchar(255),
portcull int NOT NULL,
cheval int NOT NULL,
moat int NOT NULL,
ramparts int NOT NULL,
drawbridge int NOT NULL,
sallyport int NOT NULL,
rockwall int NOT NULL,
roughterr int NOT NULL,
lowbar int NOT NULL,
low_goals_made int NOT NULL,
low_goals_missed int NOT NULL,
high_goals_made int NOT NULL,
high_goals_missed int NOT NULL,
average_time_defenses real NOT NULL,
average_time_align real NOT NULL,
end_capture bool NOT NULL,
end_approach bool NOT NULL,
end_climb bool NOT NULL

);
"""


def create_tables():
	
	if not path.isdir("db"):
		mkdir("db")
	conn = connect(db)
	c = conn.cursor()


	# Creates default tables
	cmd = "SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{0}';"
	num = c.execute(cmd.format("Performances")).fetchone()
	if num[0] == 0:
		c.execute("CREATE TABLE Performances" + performance_table_structure)
	conn.commit()
	conn.close()

class Database:
	
	def __init__(self, db = "db/main.db"):
		self.db = db
		self.connection = connect(db)
		self.cursor = self.connection.cursor()
	def __del__(self):
		self.connection.commit()
		self.connection.close()

	def add_performance(self, inp):
		self.validate_performance_input(inp)	
		for i,j in enumerate(inp):
			if type(j) == type(True):
				inp[i] = 1 if inp[i] else 0
		vals = str(tuple(inp))[1:]
		self.cursor.execute("INSERT INTO Performances VALUES (NULL, " + vals)
		self.connection.commit()
	def validate_performance_input(self, inp):
		if len(inp) != 22:
			raise ValueError("Performance should have 22 elements");
		sample = (1,1,"Chival", "None", 1, 1, 1,
				-1, -1, -1, -1, -1, -1,
				5, 5, 5, 5, 5.5, 5.5, True, True, True)
		
		for i,j in enumerate(inp):
			if type(j) != type(sample[i]):
				raise ValueError("Element {0} is not type {1}".format(i, type(sample[i])))

	def get_performance(self, match_number, team_number):
		return self.cursor.execute("SELECT * FROM Performances WHERE match_number={} AND team_number={}".format(match_number, team_number)).fetchone()

	def get_all(self):
		return self.cursor.execute("SELECT * FROM Performances").fetchall()
	


