from distutils import debug
from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_item')
def add_item():
    return render_template('add_item.html')

@app.route('/view_item')
def view_item():
    return render_template('view_item.html')

@app.route('/add_purchases.html')
def add_purchases():
    return render_template('add_purchases.html')


@app.route('/view_purchases.html')
def view_purchases():
    return render_template('view_purchases.html')

@app.route('/add_sales')
def add_sales():
    return render_template('add_sales.html')

@app.route('/view_sales')
def view_sales():
    return render_template('view_sales.html')

@app.route('/cash_balance')
def cash_balance():
    return render_template('cash_balance.html')
    

if __name__ =="__main__":
    app.run(debug = True)
    
