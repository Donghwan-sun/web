from flask import Flask, Blueprint, request, render_template, make_response , jsonify, redirect, url_for
from blog_control.user_mgmt import User
from flask_login import current_user, login_user, logout_user
from datetime import timedelta
blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        print(request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))

    elif request.method == "POST":
        # content type이 application/json인 경우 get_json() 사용 가능
        user_email = request.form['user_email']
        
        user = User.create(user_email=user_email, blog_id="A")
        login_user(user, remember=True, duration=timedelta(days=365))
        login_user(user)

        return redirect(url_for('blog.test_blog'))
    #return redirect("/blog/test_blog")
    

@blog_abtest.route('/test_blog', methods=['GET'])
def test_blog():
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        return render_template('blog_A.html')

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test_blog'))