from app import app
from flask import flash, redirect, render_template
from app.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Genuine'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "Beautiful day in Portland"
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='login', form=form)