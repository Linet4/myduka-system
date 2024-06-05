import psycopg2

# connect to the database

conn=psycopg2.connect(
    dbname="myduka",
    user="postgres",
    host="localhost",
    password="linet123",
    port=5432
)

# innitialise the cursor to perform database operation

curr=conn.cursor()

# fetch products

# def get_products():
#     query="select * from products"
#     curr.execute(query)
#     products=curr.fetchall()
#     print(products)

# get_products()

# fetch sales

# def get_sales():
#     query="select * from sales"
#     curr.execute(query)
#     sales=curr.fetchall()
#     print(sales)

# get_sales() 

# task
# have 1 function called get data()
# its task is to get db data of any table
# it should have a parameter(tablename)


# open a repo called myduka-system
# push this code as first commit

def get_data(table_name):
    query = f"select * from {table_name}" 
    curr.execute(query)
    data=curr.fetchall()
    print(data)
get_data('products') 
get_data('sales')  

# insert data
# insert products
# def insert_products():
#     query="insert into products(name, buying_price,\
#           selling_price, stock_quantity) values ('ginger', 100, 150, 10)"
#     curr.execute(query)
#     conn.commit()

# # insert_products()
# get_data("products")

# insert sales
def insert_sales():
    query="insert into sales(productid, quantity, created_at) values(22, 40, now()"
    curr.execute(query)
    conn.commit()

# insert_sales()    
get_data("sales")  

# create a function to insert products values as parameter (placeholder)
# when calling the func you will pass values as arguments

def insert_products(values):
    query="insert into products(name, buying_price, selling_price, stock_quantity)values(%s,%s,%s,%s)"
    curr.execute(query,values)
    conn.commit()

x=("bread",65,80,4)
# insert_products(x)
get_data("products")    

# create a function to insert sales values as parameter (placeholder)
# when calling the func you will pass values as arguments

# def insert_sales(values):
#     query="insert into sales(productid, quantity, created_at)values(%s,%s,now())"
#     curr.execute(query,values)
#     conn.commit()

# x=(22,30)
# # insert_sales(x)
# get_data("sales") 

# write a query that gets sales per product sales=selling_price(products)*quantity(sales)

# create a function give it a name sales_product
# def sales_product():
#     query = "SELECT p.name, SUM(p.selling_price * s.quantity) AS totalsales FROM sales as s JOIN products as p ON s.productid = p.productid GROUP BY p.name;"
#     curr.execute(query)
#     data=curr.fetchall()
#     print(data)
# sales_product()

# write a query to get profit per product profit=(selling_price-buying_price)*quantuty

def profit():
    query = "SELECT p.name, SUM((p.selling_price - p.buying_price) * s.quantity) AS profit FROM sales as s JOIN products as p ON s.productid = p.productid GROUP BY p.name;"
    curr.execute(query)
    data=curr.fetchall()
    print(data)
   
profit()

# Task
# write a query that gets sales per day sales= selling_price(products) * quantity(sales) 
# write a query to get profit per day profit=(selling_price-buying_price)*quantity
# hint Date fuction
# psql = dbservice