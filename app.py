from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from models import User
from flask_bcrypt import Bcrypt
from forms import RegistrationForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost:3306/jo_decor'
app.config['SECRET_KEY'] = 'VUJKGVDvjhgvifdlkbc,.b d/xvfjklb'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'For {form.username.data} User account created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)