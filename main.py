from flask import Flask, render_template
from dbservice import get_data

# create a flask instance

app=Flask(__name__)

# create first route

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/products")
def products():
    prods=get_data("products")
    return render_template("products.html",prods=prods)

@app.route("/sales")
def sales():
    sals=get_data("sales")
    return render_template("sales.html",sals=sals)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# create a dashboard route
# create dashboard.html
# ensure all html files are bootstrap enabled


app.run(debug=True)