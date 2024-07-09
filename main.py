from flask import Flask, render_template, request, redirect, url_for, flash
import requests as requests
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

db = SQLAlchemy()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donkzWlSihBXox7C0sKR6b'

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)
app.app_context().push()

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(30))
    address = db.Column(db.String(40))
    phone = db.Column(db.String(13))


db.create_all()


@login_manager.user_loader
def load_user(user_name):
    return Users.query.get(int(user_name))

@app.route("/")
def home():
	return render_template('index.html')


@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if not user:
            flash("Invalid Username!")
            print("Invalid User")
        elif password != user.password:
            flash("Invalid Password!")
            print("Invalid Password")
        else:
            login_user(user)
            print("Log In")
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        try:
            newUser = Users(
                username=username,
                password=password,
                name=name,
                address=address,
                phone=phone,
            )
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as register:
            flash("Something wrong!Please register with different username")
    return render_template('register.html')


@app.route("/recommend", methods=['POST', 'GET'])
@login_required
def recommend():
    if request.method=='POST':
        # Flipkart Api
        product = request.form.get('product')
        flipkart_api = requests.get(f'https://flipkart.dvishal485.workers.dev/search/{product}')
        flipkartResponse = flipkart_api.json()
        flipkart = flipkartResponse['result'][0]

        # Amazon Api
        # url = f"https://amazon-data-scraper124.p.rapidapi.com/search/{product}"
        # querystring = {"api_key": "3ba0325127417000e0b265200ab7ed34"}
        #
        # headers = {
        #     "X-RapidAPI-Key": "b6859e150fmsh54dc642c5225265p15910ejsn642549934c0e",
        #     "X-RapidAPI-Host": "amazon-data-scraper124.p.rapidapi.com"
        # }
        # Amazon_response = requests.get(url, headers=headers, params=querystring)

        # amazon = Amazon_response.json()['results'][0]

        # pricesOfAllwebsite = [float(Ebay_APIresponse.split('$')[2]), float(flipkart['current_price'])/82, float(Amazon_response['price']) ]
        # lowest_price_index = pricesOfAllwebsite.index(min(pricesOfAllwebsite))
        # lowest_price = pricesOfAllwebsite[lowest_price_index]
        # if lowest_price_index == 0:
        #     Website = "Ebay"
        #     url = Ebay_APIresponse['url']
        # elif lowest_price_index == 1:
        #     website = "FlipKart"
        #     url = flipkart['link']
        # else:
        #     website = "Amazon"
        #     url = amazon['url']
        #
        # print(amazon)

        ebayurl = f"https://ebay-search-result.p.rapidapi.com/search/{product}"

        ebayheaders = {
            "X-RapidAPI-Key": "b6859e150fmsh54dc642c5225265p15910ejsn642549934c0e",
            "X-RapidAPI-Host": "ebay-search-result.p.rapidapi.com"
        }
        Ebay_APIresponse = requests.get(ebayurl, headers=ebayheaders).json()['results']

        print(Ebay_APIresponse)
        print(flipkart)
        # time.sleep(10)
        priceInRupess = float(Ebay_APIresponse[3]['price'].split("$")[1])*82
        print(priceInRupess)

        return render_template("recommend.html", flipkarProductDetails=flipkart, Ebay_APIresponse=Ebay_APIresponse,priceInRupess=priceInRupess )
    return render_template("recommend.html", flipkarProductDetails="", Ebay_APIresponse=1)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)