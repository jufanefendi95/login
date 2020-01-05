from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import LoginForm
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.secret_key                                  = 'D@D@#G#$V'
#app.config['SQLALCHEMY_DATABASE_URI']           = 'mysql+pymysql://root:root@localhost/challenge_app'
app.config['SQLALCHEMY_DATABASE_URI'] = \
   'sqlite:////' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False

db = SQLAlchemy(app)

class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(50))
    password    = db.Column(db.Text)


@app.route('/', methods=['GET', 'POST'])
def index():
   form = LoginForm()
   #if form.validate_on_submit:
   
   if request.method == 'POST':
      #DataUser=User.query.filter_by(username = form.namaUser1.data , password= form.kataSandi.data ).first()

      namaUser = form.namaUser1.data
      kataSandi = form.kataSandi.data
      #DataUser=User.query.filter_by(username = form.namaUser1.data , password= form.kataSandi.data ).first()
      DataUser=User.query.filter_by(username = form.namaUser1.data, password= form.kataSandi.data ).first()


      user= DataUser.username
      #pas = DataUser.password
      #user = 'aku'

      #if kataSandi == DataUser.password :
      #if namaUser == DataUser and kataSandi == DataUser.password :
         #return render_template('response.html', namaUser=namaUser)
      #if kataSandi == DataUser.password :
      if namaUser ==  {'username': DataUser.username}:
      	return 'oke benar '
      else:
        return 'salah'
        
         #pesan = 'Anda tidak berhak menggunakan aplikasi ini.'
         #return render_template('form.html', form=form, pesan=pesan)
   return render_template('form.html', form=form)

if __name__ == '__main__':
   app.run(debug=True)

