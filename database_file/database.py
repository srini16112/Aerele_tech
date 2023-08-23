from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'addsales'
 
mysql = MySQL(app)
@app.route('/add_sales')
def home():
    return render_template('add_sales.html')


@app.route('/AddSale', methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        return "login via the login Form"
    
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        selectItem = request.form.get('selectItem')
        Quantity = request.form.get('Quantity')
        Rat = request.form.get('Rat')
        print((selectItem,Quantity,Rat))
        cursor.execute('insert into addsales (selectItem,Quantity,Rat) values( %s,%s,%s)',(selectItem,Quantity,Rat))
        mysql.connection.commit()
        cursor.close()
        return f"Success!@#"
    

if __name__ == "__main__":
        app.run()