import MySQLdb

class Connection:
    def __init__(self):
        con = MySQLdb.connect(database='project0', user='root', host='localhost', password='root')
        self.cur = con.cursor()

<<<<<<< Updated upstream
    def get_players(self,team_id):
        self.cur.execute('select * from city', [])
=======
    ################# RESTAURANT INFO QUERIES ##################

    def getMenuForRestaurant(self, restaurantID):
        self.cur.execute(
            'select dish_name, description, flavour_profile, price, rating, allergies from menu where restaurant_id = %s',
            [restaurantID])
>>>>>>> Stashed changes
        return self.cur.fetchall()

    def get_stats(self,player_id):
        self.cur.execute('select * from menu', [])
        return self.cur.fetchall()

<<<<<<< Updated upstream
    def get_teams(self):
        self.cur.execute('select * from city')
        return self.cur.fetchall()
=======
    def getReviewsForRestaurant(self, restaurantID): #inner join
        self.cur.execute(
            'select u.username, r.user_rating, r.review, r.date_reviewed from user_saved_restaurants as r join user as u on u.id = r.user_id where r.restaurant_id = %s',
            [restaurantID])
        return self.cur.fetchall()

    def addToFavs(self, rating, review, restaurantID, userID, date_reviewed=date.today()):
        self.cur.execute(
            'insert into user_saved_restaurants (user_id, restaurant_id, date_reviewed, user_rating, review) values (%s, %s, %s, %s, %s)',
            [userID, restaurantID, date_reviewed, rating, review])
        self.con.commit()

    def rmFromFavs(self, restaurantID, userID, date_reviewed=date.today()):
        self.cur.execute(
            'delete from user_saved_restaurants where user_id = (%s) and restaurant_id = %s and date_reviewed = %s',
            [userID, restaurantID, date_reviewed])
        self.con.commit()

    def getCurrentStatusOfFavs(self, restaurantID, userID):
        self.cur.execute(
            'select id from user_saved_restaurants where restaurant_id = %s and user_id = %s',
            [restaurantID, userID])
        return self.cur.fetchone()

    ############ MAP QUERIES ##########

    def getAllRestaurants(self):
        self.cur.execute('select id, name from restaurant', [])
        return self.cur.fetchall()

    ############ LOGIN & SIGN UP QUERIES ##########
    def login(self, username, password):
        self.cur.execute('SELECT * FROM user WHERE username = %s AND password = %s', [username, password])
        return self.cur.fetchone()

    def userExist(self, username):
        self.cur.execute('SELECT username FROM user WHERE username = %s', [username])
        return self.cur.fetchone()

    def addUser(self, f_name, l_name, username, password, email):
        self.cur.execute(
            'INSERT INTO user (first_name, last_name, username, password, email) VALUES (%s, %s, %s, %s, %s)',
            [f_name, l_name, username, password, email])
        self.con.commit()

    ############ YOUR SPOTS ##########
    def getFavs(self, userID): # triple table join; view 1
        self.cur.execute(
            '''select r.name, u.username, s.restaurant_id, s.user_rating, s.review, s.date_reviewed from 
            ((user_saved_restaurants as s join restaurant as r on s.restaurant_id  = r.id) 
            join user as u on s.user_id = u.id) 
            where u.id = %s''', [userID])
        return self.cur.fetchall()

    ############ FLAVOUR TOWN ##########
    def numSpicyFood(self): # group by and any; view 2
        string = '%spicy%'
        self.cur.execute(
            '''
            SELECT r.id, r.name, c.name, COUNT(r.id) 
            FROM Restaurant AS r, City AS c
            WHERE r.city_id = c.id AND r.id = 
            ANY (
            SELECT r2.id FROM Restaurant AS r2 WHERE r2.flavour_profile LIKE %s
            ) GROUP BY c.name
            ''', [string])
        return self.cur.fetchall()

    def findFlavour(self, flavour):
        string = "%" + flavour + "%"
        self.cur.execute(
            '''
            SELECT r.id, r.name, r.flavour_profile, c.name
            FROM restaurant as r, city as c
            where r.flavour_profile like %s and c.id = r.city_id 
            order BY r.name
            ''', [string])
        return self.cur.fetchall()

    def flavourTown(self):
        self.cur.execute(
            '''
            SELECT r.id, r.name, r.flavour_profile, c.name
            FROM restaurant as r, city c
            where c.id = r.city_id 
            order by r.name
            ''', [])
        return self.cur.fetchall()

    ############ BESTS OVERALL SPOTS ##########
    def aboveAvgRating(self): #co-related nested; view 3
        self.cur.execute(
            '''
            SELECT r.id, r.name, r.rating, c.name FROM restaurant r, city AS c
            WHERE c.id =r.city_id  AND r.rating > (
            SELECT AVG(r2.rating) FROM Restaurant r2
            WHERE city_id = r.city_id
            ) Limit 10
            ''', [])
        return self.cur.fetchall()

    def allFoodAndCity(self): #full join (note: mysql does not have a full join option); view 4 & view 5
        self.cur.execute(
            '''
            SELECT r.name as 'Restaurant', c.name as 'City' FROM restaurant r
            LEFT JOIN city c ON r.city_id = c.id
            UNION
            SELECT r.name as 'Restaurant', c.name as 'City' FROM restaurant r
            RIGHT JOIN city c ON r.city_id = c.id
            ''', [])
        return self.cur.fetchall()

    def topRated(self):
        self.cur.execute(
            '''
            SELECT id, name, rating FROM restaurant ORDER BY rating DESC LIMIT 10
            ''', [])
        return self.cur.fetchall()

    def bestOverall(self):
        self.cur.execute(
            '''
            SELECT r.id, r.name, r.rating, r.price_rating FROM Restaurant AS r
            WHERE r.rating >= 4 and r.price_rating <= (SELECT AVG(price_rating) FROM Restaurant)
            limit 10
            ''', [])
        return self.cur.fetchall()
>>>>>>> Stashed changes
