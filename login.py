import sys

sys.path.append('/users/meite/appdata/local/programs/python/python38/lib/site-packages')


from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

class User(UserMixin):
  def __init__(self,user_id):
    self.id = user_id

class  LoginForm(FlaskForm):
    name = StringField('名前')
    mail = StringField('メールアドレス')
    submit = SubmitField('ログイン')

@login_manager.user_loader
def load_user(user_id):
  return User(user_id)

@app.route('/')
def index():
  return render_template('top.html')

@app.route('/member')
@login_required
def member():
  return render_template('member.html')

@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.name.data == 'shimazaki' and form.mail.data == 'test@mail':
      user = User(form.name.data)
      login_user(user)
      return redirect('/member')
    else:
      return 'ログインに失敗しました'
  return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
