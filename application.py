from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://fahyjekubolpsb:084f71e17a72960063160b48657280549094140468ebfe534b9b91b61101a54f@ec2-52-6-143-153.compute-1.amazonaws.com:5432/dacmhgi1g82sc0"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
@app.route('/register')
def home():
    return render_template('register.html')

@app.route('/result', methods=['GET','POST'])
def result():
    full_name = request.form.get("FUll_name")
    user_name = request.form.get("user_name")
    email = request.form.get("email_name")
    password = request.form.get("password_name")
    user_obj = User(FullName = full_name, username = user_name, email = email, password = password)
    db.session.add(user_obj)
    db.session.commit()
    return render_template('result.html', Username=user_name)

@app.route('/admin')
def admin():
    data = User.query.all()
    print(data[0].username)
    return render_template('admin.html', data = data)


if __name__ == "__main__":
    app.run(debug=True)


