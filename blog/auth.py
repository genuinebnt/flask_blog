import functools

from flask import Blueprint, request, render_template, url_for, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

from db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        if not password:
            error = 'Password is required'

        if error is not None:
            try:
                db.execute('INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)',
                           (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = f"Username {username} is already registered"
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM USERS WHERE USERNAME = ?',
            username
        ).fetchone()

        if user is None or check_password_hash(user['password'], password):
            error = "Incorrect username or password"

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view()
