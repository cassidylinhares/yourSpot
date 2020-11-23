import MySQLdb
from datetime import date


class Connection:
    def __init__(self):
        self.con = MySQLdb.connect(database='project0', user='root', host='localhost', password='root')
        self.cur = self.con.cursor()

    ################# RESTAURANT INFO QUERIES ##################
    def getMenuForRestaurant(self, restaurantID):
        self.cur.execute(
            'select dish_name, description, flavour_profile, price, rating, allergies from menu where restaurant_id = %s',
            [restaurantID])
        return self.cur.fetchall()

    def getRestaurantInfo(self, restaurantID):
        self.cur.execute('select *, c.name from restaurant as r, city as c where r.id = %s and c.id = r.city_id',
                         [restaurantID])
        return self.cur.fetchall()

    def getReviewsForRestaurant(self, restaurantID):
        self.cur.execute(
            'select u.username, r.user_rating, r.review, r.date_reviewed from user_saved_restaurants as r join user as u on u.id = r.user_id where r.restaurant_id = %s',
            [restaurantID])
        return self.cur.fetchall()

    def addToFavs(self, rating, review, restaurantID, userID=1, date_reviewed=date.today()):
        self.cur.execute(
            'insert into user_saved_restaurants (user_id, restaurant_id, date_reviewed, user_rating, review) values (%s, %s, %s, %s, %s)',
            [userID, restaurantID, date_reviewed, rating, review])
        self.con.commit()

    def rmFromFavs(self, restaurantID, userID=1, date_reviewed=date.today()):
        self.cur.execute(
            'delete from user_saved_restaurants where user_id = (%s) and restaurant_id = %s and date_reviewed = %s',
            [userID, restaurantID, date_reviewed])
        self.con.commit()

    def getCurrentStatusOfFavs(self, restaurantID, userID=1, ):
        self.cur.execute(
            'select id from user_saved_restaurants where restaurant_id = %s and user_id = %s',
            [restaurantID, userID])
        return self.cur.fetchone()


