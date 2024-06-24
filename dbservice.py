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

def get_products():
    query="select * from products"
    curr.execute(query)
    products=curr.fetchall()
    return products

# get_products()

# fetch sales

def get_sales():
    query="select * from sales"
    curr.execute(query)
    sales=curr.fetchall()
    return sales

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
    return data

# get_data('products') 
# get_data('sales')  

# insert data
# insert products
def insert_products():
    query="insert into products(name, buying_price,\
          selling_price, stock_quantity) values ('ginger', 100, 150, 10)"
    curr.execute(query)
    conn.commit()

# # insert_products()
# get_data("products")

# insert sales
def insert_sales():
    query="insert into sales(productid, quantity, created_at) values(22, 40, now()"
    curr.execute(query)
    conn.commit()

# insert_sales()    
# get_data("sales")  

# create a function to insert products values as parameter (placeholder)
# when calling the func you will pass values as arguments

def insert_products(values):
    query="insert into products(name, buying_price, selling_price, stock_quantity)values(%s,%s,%s,%s)"
    curr.execute(query,values)
    conn.commit()

x=("bread",65,80,4)
# insert_products(x)
# get_data("products")    

# create a function to insert sales values as parameter (placeholder)
# when calling the func you will pass values as arguments

def insert_sales(values):
    query="insert into sales(productid, quantity, created_at)values(%s,%s,now())"
    curr.execute(query,values)
    conn.commit()

# x=(22,30)
# # insert_sales(x)
# get_data("sales") 

# write a query that gets sales per product sales=selling_price(products)*quantity(sales)

# create a function give it a name sales_product
def sales_product():
    query = "select products.productid, products.name, sum(products.selling_price * sales.quantity) As total_sales from(sales INNER JOIN products on sales.productid = products.productid) GROUP BY products.productid, products.name;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# sales_product()

# write a query to get profit per product profit=(selling_price-buying_price)*quantuty

def profit():
    query ="select products.name, sum(products.selling_price - products.buying_price) As profit from(sales INNER JOIN products on sales.productid = products.productid) GROUP BY products.name;"
    curr.execute(query)
    data=curr.fetchall()
    return data
   
# profit()

# Task
# write a query that gets sales per day sales= selling_price(products) * quantity(sales) 

def sales_day():
    query = "select DATE(sales.created_at) as sales_day, sum(products.selling_price * sales.quantity) As total_sales from(sales INNER JOIN products on sales.productid = products.productid) GROUP BY sales_day;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# sales_day()    

# write a query to get profit per day profit=(selling_price-buying_price)*quantity
# hint Date fuction
# psql = dbservice

def profit_daily():
    query = "select DATE(sales.created_at) as profit_day,\
    sum((products.selling_price - products.buying_price)*sales.quantity)\
    As profit from sales JOIN products on sales.productid = products.productid\
    GROUP BY profit_day order by profit_day;"
    curr.execute(query)
    data=curr.fetchall()
    return data

# profit_daily() 
# write a query to display the total sales(psql)
# =>create a function on dbservice.py 

def total_sales():
    query= "select sum(products.selling_price * sales.quantity) As total_sales from sales  JOIN products on sales.productid = products.productid;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# total_sales()

# 2write a query to display todays sales
def today_sales():
    query= " select DATE(sales.created_at) as sales_day,sum(products.selling_price * sales.quantity) As total_sales from(sales JOIN products on sales.productid = products.productid) GROUP BY sales_day ORDER BY sales_day  DESC LIMIT 1;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# today_sales()
# =>create a function on dbservice.py  
# 3.write a query to get the total profit
def total_profit():
    query = "select sum((products.selling_price - products.buying_price)*sales.quantity)\
    As total_profit from sales JOIN products on sales.productid = products.productid;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# total_profit() 
# =>create a function on dbservice.py 
# 4.write the query to display todays profit

def today_profit():
    query = "select DATE(sales.created_at) as today_profit,\
    sum((products.selling_price - products.buying_price)*sales.quantity)\
    As profit from sales JOIN products on sales.productid = products.productid\
    GROUP BY today_profit order by today_profit DESC LIMIT 1;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# today_profit() 

# =>create a function on dbservice.py

def recent_sales():
    query="select * from sales order by created_at desc limit 10;"
    curr.execute(query)
    data=curr.fetchall()
    return data
# recent_sales()    


  
