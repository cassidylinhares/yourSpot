import MySQLdb

class Connection:
    def __init__(self):
        con = MySQLdb.connect(database='project0', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_players(self,team_id):
        self.cur.execute('select * from city', [])
        return self.cur.fetchall()

    def get_stats(self,player_id):
        self.cur.execute('select * from menu', [])
        return self.cur.fetchall()

    def get_teams(self):
        self.cur.execute('select * from city')
        return self.cur.fetchall()
