import itertools
from mysql.connector import connect

cnx = connect(
user="root",
password="coderslab",
host="localhost",
database="projekt1"
)        


query3 = """SELECT id FROM players;"""        
cursor = cnx.cursor()
cursor.execute(query3)
 
     
players_ids = cursor.fetchall()

tuple = (('aa',), ('bb',), ('cc',))

my_list = list(itertools.chain(*tuple))
my_list2 = list(itertools.chain(*players_ids))
print(my_list)
print(players_ids)
print(my_list2)

ID = 10
if ID in my_list2:
    print("Fucking AWESOME!")
else:
    print("nie ma takiego")
    
query = """SELECT team FROM players WHERE id=10;"""        
cursor = cnx.cursor()
cursor.execute(query)

team_id = int(cursor.fetchone()[0])
print(team_id)
if team_id in my_list2:
    print("Fucking AWESOME!")
else:
    print("nie ma takiego")

