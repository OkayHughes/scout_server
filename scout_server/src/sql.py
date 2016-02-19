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
db = "../db/main.db"

performance_table_structure = """
(
P_ID int NOT NULL,
match_id int NOT NULL,
team_id int NOT NULL,
defense varchar(255),
score varchar(255),
portcull bool NOT NULL,
cheval bool NOT NULL,
moat bool NOT NULL,
ramparts bool NOT NULL,
drawbridge bool NOT NULL,
sallyport bool NOT NULL,
rockwall bool NOT NULL,
roughterr bool NOT NULL,
lowbar bool NOT NULL,
low_goals_made int NOT NULL,
low_goals_missed int NOT NULL,
high_goals_made int NOT NULL,
high_goals_missed int NOT NULL,
average_time_defenses real NOT NULL,
average_time_align real NOT NULL,
end_capture bool NOT NULL,
end_approach bool NOT NULL,
end_climb bool NOT NULL,


PRIMARY KEY (P_ID),
FOREIGN KEY (match_id) REFERENCES Matches(M_ID),
FOREIGN KEY (team_id) REFERENCES Teams(T_ID)
);
"""
team_table_structure = """
(
T_ID int NOT NULL,
name varchar(255) NOT NULL,
number int NOT NULL,

PRIMARY KEY (T_ID)
);
"""
match_table_structure = """
(
M_ID int NOT NULL,
red1 int NOT NULL,
red2 int NOT NULL,
red3 int NOT NULL,
blue1 int NOT NULL,
blue2 int NOT NULL,
blue3 int NOT NULL,
FOREIGN KEY (red1) REFERENCES Teams(T_ID),
FOREIGN KEY (red2) REFERENCES Teams(T_ID),
FOREIGN KEY (red3) REFERENCES Teams(T_ID),
FOREIGN KEY (blue1) REFERENCES Teams(T_ID),
FOREIGN KEY (blue2) REFERENCES Teams(T_ID),
FOREIGN KEY (blue3) REFERENCES Teams(T_ID)
);
"""

def create_table():
	"""WILL DESTROY EXISTING DATABASE"""
	#only run if db doesn't exist yet
	if not path.isdir("db"):
		mkdir("db")
	if path.isfile(db):
		remove(db)
	#creates default tables
	conn = connect(db)
	c = conn.cursor()
	c.execute("CREATE TABLE Performances" + performance_table_structure)
	c.execute("CREATE TABLE Matches" + match_table_structure)
	c.execute("CREATE TABLE Teams" + team_table_structure)

	conn.commit()
	conn.close()

class database:
	
	def __init__(self):
		try:
			self.connection = connect(db)
		except Error as e:
			print "{0}, {1}".format(e.errno, e.strerror)

	def add_data(self, arr_vals):
		pass
