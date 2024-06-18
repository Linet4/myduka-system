from flask import Flask, render_template, redirect, url_for, request
from dbservice import get_data,insert_products,insert_sales



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
    products=get_data("products")
    sals=get_data("sales")
    return render_template("sales.html",sals=sals,products=products)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add_products",methods=["POST","GET"])
def add_products():
    # check method
    if request.method == "POST":
        # get the form data
        pname = request.form["product_name"]
        bprice = request.form["buying_price"]
        sprice = request.form["selling_price"]
        squantity = request.form["stock_quantity"] 
        # insert products
        new_prod = (pname,bprice,sprice,squantity)
        insert_products(new_prod)
    return redirect(url_for("products"))

@app.route("/make_sales",methods=["POST","GET"])
def make_sales():
    # check method
    if request.method == "POST":
        # get the form data
        pid = request.form["productid"]
        quantity = request.form["quantity"]
        # insert sales
        new_sales = (pid,quantity)
        insert_sales(new_sales)
    return redirect(url_for("sales"))   

 
# create a dashboard route
# create dashboard.html
# ensure all html files are bootstrap enabled


app.run(debug=True)