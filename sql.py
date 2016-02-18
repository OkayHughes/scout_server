#Authored by Owen Hughes
#Creates interface for sqlite3 module for my purposes
from sqlite3 import connect

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

table_structure= """
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


def create_table():
	conn = connect(db)
	c = conn.cursor()
	c.execute

class database:
	
	def __init__():
		try:
			self.connection = connect(db)
		except Error as e:
			print "{0}, {1}".format(e.errno, e.strerror)

	def add_data(arr_vals):
		
