from flask import Flask, Blueprint, request, render_template, make_response , jsonify, redirect, url_for, session
from blog_control.user_mgmt import User
from flask_login import current_user, login_user, logout_user
from datetime import timedelta

from blog_control.session_mgmt import BlogSession
blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        return redirect(url_for('blog.test_blog'))

    elif request.method == "POST":
        # content type이 application/json인 경우 get_json() 사용 가능
        user_email = request.form['user_email']
        blog_page = request.form['blog_id']

        user = User.create(user_email=user_email, blog_id=blog_page)

        login_user(user, remember=True, duration=timedelta(days=365))
        login_user(user)

        return redirect(url_for('blog.blog_fullstack'))

@blog_abtest.route('/test_blog', methods=['GET'])
def test_blog():
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        return render_template('blog_A.html')

@blog_abtest.route('/login')
def login():
    return render_template('sign_in.html')

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog_fullstack'))

@blog_abtest.route('/blog_fullstack', methods=['GET'])
def blog_fullstack():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session["client_id"], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session["client_id"], 'anonymous', webpage_name)
        return render_template(webpage_name)
