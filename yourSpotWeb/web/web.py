from flask import Flask, render_template, redirect, jsonify, url_for, request, session
from flask_restful import Api
from flask_wtf import Form, FlaskForm
from flask_wtf.csrf import CsrfProtect
<<<<<<< Updated upstream
from wtforms import SelectField
=======
from wtforms import SelectField, StringField, PasswordField, validators
>>>>>>> Stashed changes
import db.helper as connection


# initalize server
app = Flask(__name__, template_folder='views', static_folder='public')
api = Api(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CsrfProtect(app)


# create connection object and get data for teams and players
db = connection.Connection()


<<<<<<< Updated upstream
@app.route('/', methods=['GET', 'POST'])
def index():
    class SelectTeamForm(Form):
        teams = db.get_teams()
        name = SelectField(coerce=int, choices=teams, default=1610612737)
=======
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Create a form
    class Login(FlaskForm):
        username = StringField("Username: ", validators=[validators.InputRequired("Required.")])
        password = PasswordField("Password: ", validators=[validators.InputRequired("Required.")])
>>>>>>> Stashed changes

    form = Login()
    msg = ''
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.login(username, password)

        # If account exists, send them to the home screen
        if user:
            # Create session data, we can access this data in other routes
            session['logged_in'] = True
            session['id'] = int(user[0])
            session['username'] = user[3]
            session['name'] = user[1]

            return redirect('/')
        else:
            # User data could not be found
            msg = "Incorrect username or password."
    return render_template('login.html', msg=msg, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    class SignUp(FlaskForm):
        fname = StringField("First Name: ", validators=[validators.InputRequired("Required.")])
        lname = StringField("Last Name: ", validators=[validators.InputRequired("Required.")])
        username = StringField("Username: ", validators=[validators.InputRequired("Required."),
                                                         validators.Regexp('[A-Za-z0-9]+')])
        password = PasswordField("Password: ", validators=[validators.InputRequired("Required."),
                                                           validators.EqualTo('confirm', message="Does not match")])
        confirm = PasswordField("Confirm Password: ", validators=[validators.InputRequired("Required.")])
        email = StringField("Email: ", validators=[validators.InputRequired("Required."),
                                                   validators.Email(message="Must be a valid email")])

    msg = ''
    form = SignUp()

    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print(email)
        exist = db.userExist(username)
        print(exist)
        if exist is None:
            db.addUser(fname, lname, username, password, email)
            return redirect('/login')
        else:
            msg = "Username exists."
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg, form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/', methods=["GET"])
def index():
    if 'logged_in' in session:
        return render_template('home.html', username=session['username'], name=session['name'])
    return redirect(url_for('login'))


@app.route('/your_spots', methods=["GET", "POST"])
def your_spots():
    # get the restaurants to display on map
    food = db.getFavs(session['id'])

    return render_template('favourites.html', food=food, name=session['name'])


<<<<<<< Updated upstream
@app.route('/player', methods=['GET','POST'])
def player():
    class SelectPlayerForm(Form):
        team_id = session['TEAM_ID']
        players = db.get_players(team_id)
        name = SelectField(coerce=int, choices=players)
=======
@app.route('/top_spots', methods=["GET", "POST"])
def top_spots():
    # get the restaurant views
    top_rated = db.topRated()
    top_overall = db.bestOverall()
    top_avg = db.aboveAvgRating()
    food = db.allFoodAndCity()
>>>>>>> Stashed changes

    return render_template('tops.html', toprated=top_rated, topoverall=top_overall, topavg=top_avg, allspots=food,
                           name=session['name'])


@app.route('/flavour_town', methods=["GET", "POST"])
def flavour_town():
    spicy = db.numSpicyFood()
    print(spicy)
    flav_town = db.flavourTown()
    # create form class
    class SearchFlavour(FlaskForm):
        findFlav = StringField(label="Feed your Craving: ")

    form = SearchFlavour()

    results = []
    if form.validate_on_submit():
        results = db.findFlavour(form.findFlav.data)

    return render_template('flavour_town.html', form=form, spicy=spicy, flav=flav_town, results=results,
                           name=session['name'])


<<<<<<< Updated upstream
@app.route('/stats', methods=['POST', 'GET'])
def stats():
    player_id = session['PLAYER_ID']
    stats = db.get_stats(player_id)[0]

    return render_template("stats.html", name=stats[1], blocks=stats[9], drfgm=stats[11], drfga=stats[12], drfgpct=stats[13])

# create simple api that takes in id and response with stats of said player
# ex player <id> = 201960
@app.route('/api/<id>', methods=['GET','POST'])
def api(id):
    player_id = id
    stats = db.get_stats(player_id)
    return jsonify(stats)
=======
@app.route('/delete_spot/<spot>/<dt>', methods=["GET", "POST"])
def delete_spot(spot, dt):
    user_id = session['id']
    db.rmFromFavs(spot, user_id, dt)
    food = db.getFavs(user_id)
    return render_template('favourites.html', food=food, name=session['name'])


@app.route('/map_view', methods=["GET", "POST"])
def map_view():
    # get the restaurants to display on map
    food = db.getAllRestaurants()
    results = []
    for row in food:
        id = int(row[0])
        name = str(row[1]).replace("&#39;", "")
        results.append([id, name])

    return render_template('map_view.html', food=results, name=session['name'])


@app.route('/restaurant_info/<id>', methods=['GET', 'POST'])
def restaurant_info(id):
    # get data to display
    user_id = session['id']
    food_id = id
    food_info = db.getRestaurantInfo(food_id)[0]
    food_menu = db.getMenuForRestaurant(food_id)
    food_reviews = db.getReviewsForRestaurant(food_id)

    # create form class
    class AddReview(Form):
        choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
        addRating = SelectField(label="How was your experience? ", choices=choices, default=5, coerce=int)
        addReview = StringField(label="Add a review: ")

    # create form object
    form = AddReview()

    # add review to db on submit
    if form.validate_on_submit():
        db.addToFavs(form.addRating.data, form.addReview.data, restaurantID=food_id, userID=user_id)

    return render_template("restaurant_info.html", id=food_id, name=food_info[1], address=food_info[2],
                           phone=food_info[3], rating=food_info[4], menu=food_info[5], price_rating=food_info[6],
                           city=food_info[12], delivery="Yes" if (food_info[8]) else "No",
                           takeout="Yes" if (food_info[9]) else "No", flavour=food_info[10], dish=food_menu,
                           reviews=food_reviews, form=form, fname=session['name'])
>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run(debug=True, host='localhost', threaded=True)
